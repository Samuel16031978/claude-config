# Workflow Reference: Secret Scanning with Gitleaks

## Secret Detection Pipeline

```
Developer Workstation          CI/CD Pipeline              Security Response
     Ôöé                              Ôöé                           Ôöé
     Ôû╝                              Ôöé                           Ôöé
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ                    Ôöé                           Ôöé
Ôöé Pre-commit   Ôöé                    Ôöé                           Ôöé
Ôöé Hook (local) Ôöé                    Ôöé                           Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ                    Ôöé                           Ôöé
       Ôöé                            Ôöé                           Ôöé
  ÔöîÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÉ                       Ôöé                           Ôöé
  Ôöé         Ôöé                       Ôöé                           Ôöé
PASS      FAIL                      Ôöé                           Ôöé
  Ôöé     (blocked)                   Ôöé                           Ôöé
  Ôû╝                                 Ôöé                           Ôöé
Push to                             Ôöé                           Ôöé
Remote                              Ôöé                           Ôöé
  Ôöé                                 Ôû╝                           Ôöé
  Ôöé                        ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ                     Ôöé
  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ>Ôöé Gitleaks CI  Ôöé                     Ôöé
                           Ôöé Scan (PR)    Ôöé                     Ôöé
                           ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ                     Ôöé
                                  Ôöé                             Ôöé
                            ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ                      Ôöé
                            Ôöé           Ôöé                       Ôöé
                          PASS        FAIL                      Ôöé
                            Ôöé     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ               Ôöé
                            Ôöé     Ôöé Block PR   Ôöé               Ôöé
                            Ôöé     Ôöé + Alert    ÔöéÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ>Ôöé
                            Ôöé     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                            Ôöé                       Ôöé Rotate Secret   Ôöé
                            Ôöé                       Ôöé Update Baseline Ôöé
                            Ôöé                       Ôöé Clean History   Ôöé
                            Ôöé                       ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                            Ôû╝
                    Merge Permitted
```

## Gitleaks Rule Configuration Deep Dive

### Rule Anatomy
```toml
[[rules]]
id = "rule-unique-identifier"          # Unique rule ID
description = "Human-readable desc"     # What this rule detects
regex = '''pattern'''                   # Detection regex
entropy = 3.5                           # Minimum entropy threshold (optional)
secretGroup = 1                         # Regex capture group containing secret
keywords = ["key1", "key2"]             # Fast pre-filter keywords
tags = ["aws", "credential"]            # Categorization tags
path = '''\.env$'''                     # Path filter regex (optional)
```

### Built-in Rule Categories
| Category | Example Rules | Count |
|----------|--------------|-------|
| Cloud Provider Keys | aws-access-key-id, gcp-service-account | 15+ |
| API Tokens | github-pat, gitlab-pat, slack-token | 20+ |
| Private Keys | private-key, rsa-private-key | 5+ |
| Database Credentials | generic-password, connection-string | 10+ |
| Service Tokens | stripe-api-key, sendgrid-api-key | 30+ |

### Entropy Scoring
- Entropy measures string randomness (Shannon entropy)
- Random-looking strings (API keys) have entropy > 3.5
- Regular English text has entropy around 2.0-3.0
- Setting entropy threshold reduces false positives on non-random strings
- Combine entropy with regex for highest accuracy

## Remediation Process

### Secret Rotation Checklist
1. Identify the exposed secret type and associated service
2. Log into the service provider and revoke the exposed credential
3. Generate a new credential with the same permissions
4. Store the new credential in a secrets manager (Vault, AWS SM, etc.)
5. Update all consuming services to use the new credential
6. Verify service functionality with the new credential
7. Update the Gitleaks baseline to remove the resolved finding
8. Optionally clean git history with git-filter-repo

### History Cleanup Decision Matrix
| Factor | Clean History | Keep History |
|--------|--------------|--------------|
| Secret is rotated | Optional | Acceptable |
| Repo is public | Required | Never |
| Compliance mandate | Required | Not compliant |
| Active contributor count | < 10 preferred | > 10 difficult |
| Secret exposure duration | Long (high risk) | Short (lower risk) |
