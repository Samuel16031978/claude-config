name: Sync Intervals.icu

on:
  push:
    paths:
      - 'claude-global/data/workout_to_create.json'
      - 'claude-global/data/sync_request.json'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Create workout if requested
        env:
          INTERVALS_API_KEY: ${{ secrets.INTERVALS_API_KEY }}
          ATHLETE_ID: i171091
        run: |
          if [ -f claude-global/data/workout_to_create.json ]; then
            python3 - <<'EOF'
          import os, json, urllib.request, urllib.error, base64

          athlete_id = os.environ["ATHLETE_ID"]
          api_key = os.environ["INTERVALS_API_KEY"]
          base_url = f"https://intervals.icu/api/v1/athlete/{athlete_id}"

          with open("claude-global/data/workout_to_create.json") as f:
              workout = json.load(f)

          # Support single workout or array
          events = workout if isinstance(workout, list) else [workout]

          url = f"{base_url}/events"
          data = json.dumps(events).encode()
          req = urllib.request.Request(url, data=data, method="POST")
          creds = base64.b64encode(f"API_KEY:{api_key}".encode()).decode()
          req.add_header("Authorization", f"Basic {creds}")
          req.add_header("Content-Type", "application/json")
          req.add_header("User-Agent", "Mozilla/5.0 (compatible; intervals-icu-client/1.0)")

          try:
              with urllib.request.urlopen(req, timeout=15) as resp:
                  result = json.loads(resp.read().decode())
                  print(f"✅ Workout créé : {json.dumps(result, indent=2)}")
          except urllib.error.HTTPError as e:
              print(f"❌ HTTP {e.code}: {e.read().decode()[:300]}")
              exit(1)
          EOF
          fi

      - name: Sync wellness data
        env:
          INTERVALS_API_KEY: ${{ secrets.INTERVALS_API_KEY }}
          ATHLETE_ID: i171091
        run: |
          if [ -f claude-global/data/sync_request.json ]; then
            python3 - <<'EOF'
          import os, json, urllib.request, urllib.error, base64
          from datetime import date, timedelta

          athlete_id = os.environ["ATHLETE_ID"]
          api_key = os.environ["INTERVALS_API_KEY"]
          base_url = f"https://intervals.icu/api/v1/athlete/{athlete_id}"

          # Wellness du jour
          today = date.today().isoformat()
          url = f"{base_url}/wellness/{today}"
          req = urllib.request.Request(url)
          creds = base64.b64encode(f"API_KEY:{api_key}".encode()).decode()
          req.add_header("Authorization", f"Basic {creds}")
          req.add_header("User-Agent", "Mozilla/5.0 (compatible; intervals-icu-client/1.0)")

          with urllib.request.urlopen(req, timeout=15) as resp:
              wellness = json.loads(resp.read().decode())

          with open("claude-global/data/intervals_latest.json", "w") as f:
              json.dump(wellness, f, indent=2)

          # Historique 7 jours
          oldest = (date.today() - timedelta(days=7)).isoformat()
          url = f"{base_url}/activities?oldest={oldest}&fields=name,type,start_date_local,icu_training_load,icu_atl,icu_ctl,moving_time,average_heartrate"
          req = urllib.request.Request(url)
          req.add_header("Authorization", f"Basic {creds}")
          req.add_header("User-Agent", "Mozilla/5.0 (compatible; intervals-icu-client/1.0)")

          with urllib.request.urlopen(req, timeout=15) as resp:
              history = json.loads(resp.read().decode())

          with open("claude-global/data/intervals_history.json", "w") as f:
              json.dump(history, f, indent=2)

          print(f"✅ Wellness synced: CTL={wellness.get('ctl')}, ATL={wellness.get('atl')}")
          EOF
          fi

      - name: Commit updated data
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add claude-global/data/intervals_latest.json claude-global/data/intervals_history.json || true
          git diff --staged --quiet || git commit -m "sync: intervals.icu data $(date +%Y-%m-%d)"
          git push || true
