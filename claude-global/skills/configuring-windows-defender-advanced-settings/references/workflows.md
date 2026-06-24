# Workflows - Configuring Windows Defender Advanced Settings

## Workflow 1: ASR Rule Deployment

```
[Identify ASR rules to deploy]
    Ôöé
    Ôû╝
[Deploy all rules in Audit mode via Intune/GPO]
    Ôöé
    Ôû╝
[Monitor ASR audit events for 2-4 weeks]
    Ôöé
    Ôö£ÔöÇÔöÇ Review events in M365 Defender portal
    Ôö£ÔöÇÔöÇ Identify false positives per rule
    Ôöé
    Ôû╝
[Create exclusions for legitimate applications]
    Ôöé
    Ôû╝
[Switch low-risk rules to Block mode]
    Ôöé  (Office rules, email content, USB)
    Ôöé
    Ôû╝
[Monitor for 1 week]
    Ôöé
    Ôö£ÔöÇÔöÇ No issues ÔöÇÔöÇÔû║ [Switch remaining rules to Block mode]
    Ôöé
    ÔööÔöÇÔöÇ Issues found ÔöÇÔöÇÔû║ [Add exclusions, maintain Audit mode for affected rules]
                              Ôöé
                              Ôû╝
                         [Re-evaluate after 2 weeks]
```

## Workflow 2: Controlled Folder Access Deployment

```
[Enable Controlled Folder Access in Audit mode]
    Ôöé
    Ôû╝
[Monitor Event ID 1124 for blocked write attempts]
    Ôöé
    Ôû╝
[Categorize blocked applications]
    Ôöé
    Ôö£ÔöÇÔöÇ Legitimate business app ÔöÇÔöÇÔû║ [Add to allowed applications list]
    Ôöé
    Ôö£ÔöÇÔöÇ Backup/sync software ÔöÇÔöÇÔû║ [Add to allowed applications list]
    Ôöé
    ÔööÔöÇÔöÇ Unknown/suspicious ÔöÇÔöÇÔû║ [Investigate, potentially malicious]
    Ôöé
    Ôû╝
[Switch to Enabled (Block) mode]
    Ôöé
    Ôû╝
[Add custom protected folders beyond defaults]
    Ôöé
    Ôû╝
[Ongoing monitoring via M365 Defender dashboard]
```

## Workflow 3: Defender Configuration Audit

```
[Quarterly Defender Configuration Review]
    Ôöé
    Ôû╝
[Export current Defender settings from all endpoints]
    Ôöé
    Ôö£ÔöÇÔöÇ PowerShell: Get-MpPreference | Export-Clixml
    Ôö£ÔöÇÔöÇ Intune: Endpoint security reports
    Ôöé
    Ôû╝
[Compare against security baseline]
    Ôöé
    Ôö£ÔöÇÔöÇ All settings match baseline ÔöÇÔöÇÔû║ [Document compliance, next review]
    Ôöé
    ÔööÔöÇÔöÇ Drift detected ÔöÇÔöÇÔû║ [Investigate cause]
                                Ôöé
                                Ôö£ÔöÇÔöÇ Unauthorized change ÔöÇÔöÇÔû║ [Security incident, restore settings]
                                Ôöé
                                ÔööÔöÇÔöÇ Authorized exception ÔöÇÔöÇÔû║ [Document, update baseline]
```

## Workflow 4: False Positive Handling

```
[User reports blocked application]
    Ôöé
    Ôû╝
[Identify which Defender feature blocked it]
    Ôöé
    Ôö£ÔöÇÔöÇ ASR rule ÔöÇÔöÇÔû║ [Check ASR event log for specific rule GUID]
    Ôöé                     Ôöé
    Ôöé                     Ôû╝
    Ôöé                [Create ASR exclusion for file/folder/process]
    Ôöé
    Ôö£ÔöÇÔöÇ Controlled Folder ÔöÇÔöÇÔû║ [Add application to allowed list]
    Ôöé
    Ôö£ÔöÇÔöÇ Network Protection ÔöÇÔöÇÔû║ [Review URL/domain, submit false positive to Microsoft]
    Ôöé
    ÔööÔöÇÔöÇ Real-time AV ÔöÇÔöÇÔû║ [Submit file for analysis, create AV exclusion if clean]
    Ôöé
    Ôû╝
[Deploy exclusion via Intune/GPO]
    Ôöé
    Ôû╝
[Verify application works, document exclusion]
```
