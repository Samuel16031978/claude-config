# Workflows - Configuring Host-Based Intrusion Detection

## Workflow 1: Wazuh HIDS Deployment

```
[Deploy Wazuh Manager]
    Ôöé
    Ôû╝
[Configure FIM, rootcheck, and log analysis modules]
    Ôöé
    Ôû╝
[Deploy agents to pilot endpoints]
    Ôöé
    Ôû╝
[Establish baseline (48 hours)]
    Ôöé
    Ôû╝
[Tune rules: suppress false positives, add exclusions]
    Ôöé
    Ôû╝
[Deploy agents to production fleet]
    Ôöé
    Ôû╝
[Integrate with SIEM]
    Ôöé
    Ôû╝
[Create dashboards and alert workflows]
```

## Workflow 2: FIM Alert Investigation

```
[FIM alert: File modified]
    Ôöé
    Ôû╝
[Check file path and change details]
    Ôöé
    Ôö£ÔöÇÔöÇ Known system update ÔöÇÔöÇÔû║ [Correlate with patch window, close alert]
    Ôö£ÔöÇÔöÇ Authorized config change ÔöÇÔöÇÔû║ [Verify change ticket, close alert]
    ÔööÔöÇÔöÇ Unauthorized change ÔöÇÔöÇÔû║ [Investigate]
                                     Ôöé
                                     Ôö£ÔöÇÔöÇ Determine who/what changed the file
                                     Ôö£ÔöÇÔöÇ Review process tree and timeline
                                     Ôöé
                                     Ôö£ÔöÇÔöÇ Malicious ÔöÇÔöÇÔû║ [Escalate to IR]
                                     ÔööÔöÇÔöÇ Operational ÔöÇÔöÇÔû║ [Update change process]
```
