# Workflows - Deploying EDR Agent with CrowdStrike

## Workflow 1: Enterprise Sensor Rollout

```
[Plan Deployment]
    Ôöé
    Ôö£ÔöÇÔöÇ Obtain Falcon Console access and CID
    Ôö£ÔöÇÔöÇ Download sensor installer for each OS
    Ôö£ÔöÇÔöÇ Create deployment groups (Workstations, Servers, VDI)
    Ôöé
    Ôû╝
[Configure Policies Before Deployment]
    Ôöé
    Ôö£ÔöÇÔöÇ Create prevention policies per group
    Ôö£ÔöÇÔöÇ Configure sensor update policies (pinned vs. auto-update)
    Ôö£ÔöÇÔöÇ Set sensor grouping tags for auto-assignment
    Ôöé
    Ôû╝
[Pilot Deployment (5% of endpoints)]
    Ôöé
    Ôö£ÔöÇÔöÇ Deploy via SCCM/Intune to pilot group
    Ôö£ÔöÇÔöÇ Monitor for 1 week: performance impact, false positives
    Ôö£ÔöÇÔöÇ Tune exclusions for LOB applications
    Ôöé
    Ôû╝
[Validation]
    Ôöé
    Ôö£ÔöÇÔöÇ All pilot hosts show "Online" in Falcon Console
    Ôö£ÔöÇÔöÇ Test detection with CsTestDetect
    Ôö£ÔöÇÔöÇ No critical application breakage
    Ôöé
    Ôû╝
[Production Rollout (phased)]
    Ôöé
    Ôö£ÔöÇÔöÇ Phase 1: Workstations (2 weeks)
    Ôö£ÔöÇÔöÇ Phase 2: Standard servers (2 weeks)
    Ôö£ÔöÇÔöÇ Phase 3: Critical servers (1 week, change window)
    Ôöé
    Ôû╝
[Post-Deployment]
    Ôöé
    Ôö£ÔöÇÔöÇ Enable SIEM integration
    Ôö£ÔöÇÔöÇ Configure automated response policies
    Ôö£ÔöÇÔöÇ Establish exclusion review cadence (monthly)
    ÔööÔöÇÔöÇ Train SOC on Falcon Console workflows
```

## Workflow 2: Detection Triage in Falcon Console

```
[New Detection Alert]
    Ôöé
    Ôû╝
[Review Detection in Falcon Console]
    Ôöé
    Ôö£ÔöÇÔöÇ Severity: Critical/High/Medium/Low/Informational
    Ôö£ÔöÇÔöÇ Tactic & Technique (ATT&CK mapping)
    Ôö£ÔöÇÔöÇ Process tree visualization
    Ôö£ÔöÇÔöÇ Network connections
    Ôöé
    Ôû╝
[Assess: True Positive or False Positive?]
    Ôöé
    Ôö£ÔöÇÔöÇ True Positive ÔöÇÔöÇÔû║ [Contain Host via Network Containment]
    Ôöé                          Ôöé
    Ôöé                          Ôû╝
    Ôöé                     [Launch RTR session for investigation]
    Ôöé                          Ôöé
    Ôöé                          Ôû╝
    Ôöé                     [Collect artifacts, kill malicious processes]
    Ôöé                          Ôöé
    Ôöé                          Ôû╝
    Ôöé                     [Remediate and release from containment]
    Ôöé
    ÔööÔöÇÔöÇ False Positive ÔöÇÔöÇÔû║ [Create exclusion rule]
                                Ôöé
                                Ôû╝
                           [Document exclusion with justification]
                                Ôöé
                                Ôû╝
                           [Mark detection as false positive]
```

## Workflow 3: Sensor Troubleshooting

```
[Sensor Issue Reported]
    Ôöé
    Ôû╝
[Check Falcon Console Host Status]
    Ôöé
    Ôö£ÔöÇÔöÇ Online ÔöÇÔöÇÔû║ [Issue is not connectivity; check policy assignment]
    Ôöé
    ÔööÔöÇÔöÇ Offline / RFM ÔöÇÔöÇÔû║ [Check network connectivity]
                               Ôöé
                               Ôö£ÔöÇÔöÇ Can reach ts01-b.cloudsink.net:443?
                               Ôöé     Ôöé
                               Ôöé     Ôö£ÔöÇÔöÇ Yes ÔöÇÔöÇÔû║ [Check proxy settings]
                               Ôöé     Ôöé              Ôû╝
                               Ôöé     Ôöé          [Reconfigure: falconctl -s --apd=false --aph=proxy --app=8080]
                               Ôöé     Ôöé
                               Ôöé     ÔööÔöÇÔöÇ No ÔöÇÔöÇÔû║ [Firewall blocking; add CrowdStrike domains to allowlist]
                               Ôöé
                               Ôû╝
                          [Check sensor service status]
                               Ôöé
                               Ôö£ÔöÇÔöÇ Service running ÔöÇÔöÇÔû║ [Review sensor logs in C:\Windows\System32\drivers\CrowdStrike\]
                               Ôöé
                               ÔööÔöÇÔöÇ Service stopped ÔöÇÔöÇÔû║ [Restart: sc start csagent (Windows) or systemctl start falcon-sensor (Linux)]
```

## Workflow 4: Sensor Version Upgrade

```
[New Sensor Version Available]
    Ôöé
    Ôû╝
[Review Release Notes in Falcon Console]
    Ôöé
    Ôû╝
[Test on pilot group (N-1 update policy)]
    Ôöé
    Ôö£ÔöÇÔöÇ No issues after 1 week ÔöÇÔöÇÔû║ [Move production to N update policy]
    Ôöé
    ÔööÔöÇÔöÇ Issues found ÔöÇÔöÇÔû║ [Hold on current version, file support ticket]
                              Ôöé
                              Ôû╝
                         [Pin current version in sensor update policy]
```
