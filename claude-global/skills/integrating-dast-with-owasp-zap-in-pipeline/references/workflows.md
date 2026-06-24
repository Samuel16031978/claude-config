# Workflow Reference: DAST with OWASP ZAP

## DAST Pipeline Integration

```
Build & Deploy to Staging
       Ôöé
       Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Health Check      Ôöé
Ôöé (wait for ready)  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôöé
       Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
       Ôû╝              Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé ZAP       Ôöé  Ôöé ZAP API   Ôöé
Ôöé Baseline  Ôöé  Ôöé Scan      Ôöé
Ôöé Scan      Ôöé  Ôöé (OpenAPI) Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
      Ôöé               Ôöé
      ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
              Ôû╝
       ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
       Ôöé Report Gen   Ôöé
       Ôöé + Upload     Ôöé
       ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
              Ôöé
       ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
       Ôû╝             Ôû╝
     PASS          FAIL
     Deploy to     Block +
     Production    Alert
```

## ZAP Scan Types Comparison

| Scan Type | Duration | Coverage | CI/CD Suitable | Active Attacks |
|-----------|----------|----------|----------------|----------------|
| Baseline | 2-5 min | Passive only | Yes | No |
| Full Scan | 30-120 min | Comprehensive | Scheduled | Yes |
| API Scan | 5-15 min | API endpoints | Yes | Yes |

## ZAP Docker Commands

```bash
# Baseline scan (passive)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-baseline.py -t http://target:8080 \
  -r report.html -J report.json -c rules.tsv

# Full scan (active)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-full-scan.py -t http://target:8080 \
  -r report.html -J report.json -c rules.tsv -T 60

# API scan (OpenAPI)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-api-scan.py -t http://target:8080/openapi.json \
  -f openapi -r report.html -J report.json
```

## Authenticated Scanning Configuration

```yaml
# zap-auth-config.yaml
authentication:
  method: form
  loginUrl: http://target:8080/login
  parameters:
    username: testuser
    password: testpass123
  loggedInIndicator: "\\QWelcome\\E"
  loggedOutIndicator: "\\QSign In\\E"

context:
  name: "auth-context"
  include:
    - "http://target:8080/.*"
  exclude:
    - "http://target:8080/logout"
    - "http://target:8080/static/.*"
```
