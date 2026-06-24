#!/usr/bin/env python3
"""
Remplit un company.json paperasse ├á partir d'un SIREN, via l'API publique
Annuaire des Entreprises (recherche-entreprises.api.gouv.fr).

├Ç lancer sur une machine o├╣ l'API est joignable (l'environnement Claude Code
distant la bloque par politique r├®seau).

Usage :
    python3 paperasse-config/fill-from-siren.py <cle_societe> <SIREN>

    cle_societe Ôêê {sc-renovations-sarl, holding-sasu, sci}

Exemple :
    python3 paperasse-config/fill-from-siren.py sc-renovations-sarl 123456789

Met ├á jour ├á la fois :
  - ~/.claude/paperasse/companies/<cle>/company.json   (config live)
  - paperasse-config/companies/<cle>.json              (config versionn├®e)

Les champs absents de l'API (capital social, nom du dirigeant) restent en
A_COMPLETER : ├á renseigner ├á la main, puis recommiter.
"""
import json
import os
import sys
import urllib.request
import urllib.error

KEYS = {"sc-renovations-sarl", "holding-sasu", "sci"}
HOME = os.path.expanduser("~")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fetch(siren: str) -> dict:
    siren = siren.replace(" ", "")[:9]
    url = f"https://recherche-entreprises.api.gouv.fr/search?q={siren}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            data = json.loads(r.read().decode())
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        sys.exit(
            f"ÔØî API injoignable ({e}).\n"
            "   L'environnement Claude Code distant bloque cette API : "
            "lancez ce script sur votre machine locale."
        )
    results = data.get("results") or []
    if not results:
        sys.exit(f"ÔØî Aucune entreprise trouv├®e pour le SIREN {siren}")
    return results[0]


def patch(path: str, fields: dict) -> None:
    if not os.path.exists(path):
        print(f"   (ignor├®, absent : {path})")
        return
    with open(path, encoding="utf-8") as f:
        company = json.load(f)
    company.update(fields)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(company, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"   Ô£ô {path}")


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in KEYS:
        sys.exit(__doc__)
    key, siren = sys.argv[1], sys.argv[2]

    c = fetch(siren)
    siege = c.get("siege", {})
    cp = siege.get("code_postal", "") or ""
    ville = siege.get("libelle_commune", "") or ""
    adresse = siege.get("adresse", "") or ""

    fields = {
        "name": c.get("nom_complet") or "A_COMPLETER",
        "siren": c.get("siren") or "A_COMPLETER",
        "siret": siege.get("siret") or "A_COMPLETER",
        "address": adresse,
        "city": ville,
        "naf": c.get("activite_principale") or "A_COMPLETER",
    }

    print(f"\n{fields['name']}  (SIREN {fields['siren']}, SIRET {fields['siret']})")
    print(f"  {adresse} ÔÇö {cp} {ville}\n")

    patch(os.path.join(HOME, ".claude/paperasse/companies", key, "company.json"), fields)
    patch(os.path.join(REPO_ROOT, "paperasse-config/companies", f"{key}.json"), fields)

    print("\nÔÜá´©Å  ├Ç compl├®ter ├á la main : capital social, RCS, nom du dirigeant, exercice fiscal.")


if __name__ == "__main__":
    main()
