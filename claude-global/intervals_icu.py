#!/usr/bin/env python3
"""
intervals_icu.py ÔÇö Client API intervals.icu pour Samuel Chembah (i171091)

Usage :
    python3 intervals_icu.py wellness
    python3 intervals_icu.py zones [run|ride|swim]
    python3 intervals_icu.py calc_charge --ctl_target 27
    python3 intervals_icu.py session --charge 120 --sport run --zone 2
    python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2"
    python3 intervals_icu.py history --days 7
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import date, timedelta

ATHLETE_ID = "i171091"
BASE_URL = f"https://intervals.icu/api/v1/athlete/{ATHLETE_ID}"

# Facteurs TRIMP par zone FC (profil Samuel, FCmax 191)
TRIMP_FACTORS = {
    "run":  {1: 0.9, 2: 1.5, 3: 2.2, 4: 3.1, 5: 4.0},
    "ride": {1: 0.7, 2: 1.1, 3: 1.6, 4: 2.3, 5: 3.0},
    "swim": {1: 0.8, 2: 1.3, 3: 1.9, 4: 2.6, 5: 3.4},
}

# Zones FC Samuel par sport (valeurs par d├®faut ÔÇö remplac├®es par l'API)
DEFAULT_ZONES = {
    "run":  [0, 114, 142, 158, 172, 191],
    "ride": [0, 109, 137, 153, 167, 191],
    "swim": [0, 114, 142, 158, 172, 191],
}


def _load_env():
    for path in [
        os.path.join(os.path.dirname(__file__), ".env.local"),
        os.path.join(os.path.dirname(__file__), "..", ".env.local"),
        os.path.join(os.getcwd(), ".env.local"),
    ]:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        os.environ.setdefault(k.strip(), v.strip())
            return
    raise SystemExit("ÔØî .env.local introuvable ÔÇö ajoute INTERVALS_API_KEY=ta_cle")


def _get(path, params=""):
    key = os.environ.get("INTERVALS_API_KEY", "")
    if not key:
        raise SystemExit("ÔØî INTERVALS_API_KEY manquante dans .env.local")
    url = f"{BASE_URL}{path}{'?' + params if params else ''}"
    req = urllib.request.Request(url)
    import base64
    creds = base64.b64encode(f"API_KEY:{key}".encode()).decode()
    req.add_header("Authorization", f"Basic {creds}")
    req.add_header("User-Agent", "Mozilla/5.0 (compatible; intervals-icu-client/1.0)")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ÔØî HTTP {e.code}: {e.read().decode()[:200]}")
    except Exception as e:
        raise SystemExit(f"ÔØî {type(e).__name__}: {e}")


def _post(path, payload):
    key = os.environ.get("INTERVALS_API_KEY", "")
    url = f"{BASE_URL}{path}"
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    import base64
    creds = base64.b64encode(f"API_KEY:{key}".encode()).decode()
    req.add_header("Authorization", f"Basic {creds}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "Mozilla/5.0 (compatible; intervals-icu-client/1.0)")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ÔØî HTTP {e.code}: {e.read().decode()[:200]}")


def cmd_wellness(_):
    today = date.today().isoformat()
    data = _get(f"/wellness/{today}")
    result = {
        "date": today,
        "CTL": data.get("ctl"),
        "ATL": data.get("atl"),
        "TSB": round((data.get("ctl") or 0) - (data.get("atl") or 0), 1),
        "resting_hr": data.get("restingHR"),
        "hrv": data.get("hrv"),
        "ctl_load": data.get("ctlLoad"),
        "atl_load": data.get("atlLoad"),
        "ramp_rate": data.get("rampRate"),
    }
    print(json.dumps(result, indent=2))


def cmd_zones(args):
    sport = getattr(args, "sport", "run") or "run"
    data = _get("/sport-settings")
    sport_map = {"run": "Run", "ride": "Ride", "swim": "Swim"}
    label = sport_map.get(sport.lower(), "Run")
    zones_out = None
    for s in data:
        if s.get("type") == label:
            zones_out = s.get("hrZones") or s.get("zones")
            break
    if not zones_out:
        zones_out = DEFAULT_ZONES.get(sport.lower(), DEFAULT_ZONES["run"])
        print(f"ÔÜá´©Å Zones {label} non trouv├®es dans l'API ÔÇö utilisation des valeurs par d├®faut")
    result = {"sport": label, "hr_zones": zones_out}
    print(json.dumps(result, indent=2))


def cmd_calc_charge(args):
    today = date.today().isoformat()
    data = _get(f"/wellness/{today}")
    ctl_actuel = data.get("ctl") or 0
    ctl_target = args.ctl_target
    # Formule EWMA : charge = CTL_cible + (CTL_cible - CTL_actuel) ├ù 41
    charge = ctl_target + (ctl_target - ctl_actuel) * 41
    charge = max(0, round(charge))
    result = {
        "CTL_actuel": ctl_actuel,
        "CTL_cible": ctl_target,
        "charge_necessaire": charge,
        "note": "Charge TRIMP ├á produire aujourd'hui pour atteindre le CTL cible"
    }
    print(json.dumps(result, indent=2))


def cmd_session(args):
    sport = (args.sport or "run").lower()
    zone = int(args.zone or 2)
    charge = float(args.charge)
    factor = TRIMP_FACTORS.get(sport, TRIMP_FACTORS["run"]).get(zone, 1.5)
    duree_min = round(charge / factor)
    zones = DEFAULT_ZONES.get(sport, DEFAULT_ZONES["run"])
    fc_min = zones[zone - 1] if zone - 1 < len(zones) else "?"
    fc_max = zones[zone] if zone < len(zones) else "?"
    # Allure estim├®e run Z2 (profil Samuel ~8 km/h en Z2)
    allure = None
    if sport == "run":
        vitesses = {1: 6.5, 2: 8.0, 3: 9.5, 4: 11.0, 5: 13.0}
        v = vitesses.get(zone, 8.0)
        dist = round(v * duree_min / 60, 1)
        allure = f"~{round(60/v, 1)} min/km ÔÇö ~{dist} km"
    result = {
        "sport": sport,
        "zone": zone,
        "charge_cible": charge,
        "duree_minutes": duree_min,
        "fc_cible": f"{fc_min}ÔÇô{fc_max} bpm",
        "allure": allure,
        "facteur_trimp": factor,
    }
    print(json.dumps(result, indent=2))


def cmd_push_event(args):
    payload = {
        "category": "WORKOUT",
        "start_date_local": f"{args.date}T08:00:00",
        "name": args.name,
        "description": args.description or "",
    }
    result = _post("/events", [payload])
    print(json.dumps({"status": "Ô£à S├®ance ajout├®e au calendrier", "event": result}, indent=2))


def cmd_history(args):
    days = int(args.days or 7)
    oldest = (date.today() - timedelta(days=days)).isoformat()
    data = _get(
        "/activities",
        f"oldest={oldest}&fields=name,type,start_date_local,icu_training_load,icu_atl,icu_ctl,moving_time,average_heartrate"
    )
    result = []
    for a in data:
        result.append({
            "date": a.get("start_date_local", "")[:10],
            "name": a.get("name"),
            "type": a.get("type"),
            "charge": a.get("icu_training_load"),
            "CTL": a.get("icu_ctl"),
            "ATL": a.get("icu_atl"),
            "duree_min": round((a.get("moving_time") or 0) / 60),
            "fc_moy": a.get("average_heartrate"),
        })
    print(json.dumps(result, indent=2))


def main():
    _load_env()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("wellness")

    p_zones = sub.add_parser("zones")
    p_zones.add_argument("sport", nargs="?", default="run")

    p_charge = sub.add_parser("calc_charge")
    p_charge.add_argument("--ctl_target", type=float, required=True)

    p_session = sub.add_parser("session")
    p_session.add_argument("--charge", type=float, required=True)
    p_session.add_argument("--sport", default="run")
    p_session.add_argument("--zone", type=int, default=2)

    p_push = sub.add_parser("push_event")
    p_push.add_argument("--date", required=True)
    p_push.add_argument("--name", required=True)
    p_push.add_argument("--description", default="")

    p_hist = sub.add_parser("history")
    p_hist.add_argument("--days", type=int, default=7)

    args = parser.parse_args()
    cmds = {
        "wellness": cmd_wellness,
        "zones": cmd_zones,
        "calc_charge": cmd_calc_charge,
        "session": cmd_session,
        "push_event": cmd_push_event,
        "history": cmd_history,
    }
    if args.cmd not in cmds:
        parser.print_help()
        sys.exit(1)
    cmds[args.cmd](args)


if __name__ == "__main__":
    main()
