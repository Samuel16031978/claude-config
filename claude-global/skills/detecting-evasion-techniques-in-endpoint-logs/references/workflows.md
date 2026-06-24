# Workflows - Detecting Evasion Techniques in Endpoint Logs

## Workflow 1: Evasion Technique Threat Hunt

```
[Select evasion technique to hunt]
    Ôöé
    Ôö£ÔöÇÔöÇ T1055 Process Injection
    Ôö£ÔöÇÔöÇ T1070 Log Tampering
    Ôö£ÔöÇÔöÇ T1036 Masquerading
    Ôö£ÔöÇÔöÇ T1562 Security Tool Disabling
    Ôöé
    Ôû╝
[Craft detection query (Splunk/KQL/Elastic)]
    Ôöé
    Ôû╝
[Execute across 30-90 days of endpoint telemetry]
    Ôöé
    Ôû╝
[Triage results]
    Ôöé
    Ôö£ÔöÇÔöÇ Known-good (allowlist) ÔöÇÔöÇÔû║ [Add to baseline, refine query]
    Ôö£ÔöÇÔöÇ Suspicious ÔöÇÔöÇÔû║ [Deep investigation]
    Ôöé                       Ôöé
    Ôöé                       Ôö£ÔöÇÔöÇ Correlate with other telemetry
    Ôöé                       Ôö£ÔöÇÔöÇ Check process tree
    Ôöé                       Ôö£ÔöÇÔöÇ Review network connections
    Ôöé                       Ôöé
    Ôöé                       Ôö£ÔöÇÔöÇ True positive ÔöÇÔöÇÔû║ [Escalate to IR]
    Ôöé                       ÔööÔöÇÔöÇ False positive ÔöÇÔöÇÔû║ [Tune detection]
    Ôöé
    ÔööÔöÇÔöÇ No results ÔöÇÔöÇÔû║ [Validate logging covers technique]
```

## Workflow 2: Detection Rule Deployment

```
[Create Sigma/SIEM detection rule]
    Ôöé
    Ôû╝
[Test against historical data]
    Ôöé
    Ôö£ÔöÇÔöÇ High false positive rate ÔöÇÔöÇÔû║ [Refine exclusions]
    Ôöé
    ÔööÔöÇÔöÇ Acceptable FP rate ÔöÇÔöÇÔû║ [Deploy in alert mode]
                                     Ôöé
                                     Ôû╝
                                [Monitor for 2 weeks]
                                     Ôöé
                                     Ôû╝
                                [Review alert quality]
                                     Ôöé
                                     Ôû╝
                                [Promote to production detection]
```

## Workflow 3: Evasion Incident Response

```
[Evasion technique detected]
    Ôöé
    Ôû╝
[Assess scope: Which endpoints affected?]
    Ôöé
    Ôû╝
[Correlate with initial access and persistence]
    Ôöé
    Ôû╝
[Determine if adversary achieved objectives]
    Ôöé
    Ôö£ÔöÇÔöÇ Active intrusion ÔöÇÔöÇÔû║ [Full incident response]
    Ôöé
    ÔööÔöÇÔöÇ Isolated event ÔöÇÔöÇÔû║ [Remediate endpoint, enhance detection]
```
