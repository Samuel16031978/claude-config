# Workflows - Hardening Windows Endpoint with CIS Benchmark

## Workflow 1: Initial Baseline Deployment

```
[Select Windows Version & CIS Benchmark]
    Ôöé
    Ôû╝
[Choose Profile Level (L1 or L2)]
    Ôöé
    Ôû╝
[Download CIS Build Kit GPOs from CIS WorkBench]
    Ôöé
    Ôû╝
[Import GPOs into Active Directory via GPMC]
    Ôöé
    Ôû╝
[Link GPO to Pilot OU with 5-10 test endpoints]
    Ôöé
    Ôû╝
[Run CIS-CAT assessment on pilot endpoints]
    Ôöé
    Ôö£ÔöÇÔöÇ Score >= 95% ÔöÇÔöÇÔû║ [Test application compatibility for 2 weeks]
    Ôöé                         Ôöé
    Ôöé                         Ôö£ÔöÇÔöÇ No issues ÔöÇÔöÇÔû║ [Deploy GPO to production OUs]
    Ôöé                         Ôöé
    Ôöé                         ÔööÔöÇÔöÇ Issues found ÔöÇÔöÇÔû║ [Document exceptions, add compensating controls]
    Ôöé                                                  Ôöé
    Ôöé                                                  Ôû╝
    Ôöé                                              [Redeploy with exceptions]
    Ôöé
    ÔööÔöÇÔöÇ Score < 95% ÔöÇÔöÇÔû║ [Investigate GPO application failures]
                              Ôöé
                              Ôû╝
                         [Fix WMI filters, security filtering, or GPO precedence]
                              Ôöé
                              Ôû╝
                         [Re-run CIS-CAT assessment]
```

## Workflow 2: Continuous Compliance Monitoring

```
[Weekly CIS-CAT Scheduled Scan]
    Ôöé
    Ôû╝
[Parse XML results ÔåÆ ingest into SIEM]
    Ôöé
    Ôû╝
[Compare against baseline score]
    Ôöé
    Ôö£ÔöÇÔöÇ Score drift > 2% ÔöÇÔöÇÔû║ [Generate compliance drift alert]
    Ôöé                              Ôöé
    Ôöé                              Ôû╝
    Ôöé                         [Identify changed settings via GPResult /H]
    Ôöé                              Ôöé
    Ôöé                              Ôû╝
    Ôöé                         [Determine if change was authorized]
    Ôöé                              Ôöé
    Ôöé                              Ôö£ÔöÇÔöÇ Authorized ÔöÇÔöÇÔû║ [Update baseline, document exception]
    Ôöé                              Ôöé
    Ôöé                              ÔööÔöÇÔöÇ Unauthorized ÔöÇÔöÇÔû║ [Revert change, investigate as security incident]
    Ôöé
    ÔööÔöÇÔöÇ Score stable ÔöÇÔöÇÔû║ [Log compliance status, update dashboard]
```

## Workflow 3: New CIS Benchmark Version Upgrade

```
[CIS releases new benchmark version]
    Ôöé
    Ôû╝
[Download updated benchmark and Build Kit]
    Ôöé
    Ôû╝
[Diff new vs. current benchmark recommendations]
    Ôöé
    Ôû╝
[Identify new/changed/removed recommendations]
    Ôöé
    Ôû╝
[Impact assessment: Will new settings break applications?]
    Ôöé
    Ôö£ÔöÇÔöÇ Yes ÔöÇÔöÇÔû║ [Lab test, document new exceptions]
    Ôöé
    ÔööÔöÇÔöÇ No ÔöÇÔöÇÔû║ [Update GPO with new Build Kit]
                    Ôöé
                    Ôû╝
               [Deploy to pilot OU first]
                    Ôöé
                    Ôû╝
               [Run CIS-CAT with new benchmark profile]
                    Ôöé
                    Ôû╝
               [Production rollout after 2-week pilot]
```

## Workflow 4: Standalone Endpoint Hardening (Non-Domain)

```
[Identify standalone Windows endpoint]
    Ôöé
    Ôû╝
[Download LGPO.exe from Microsoft SCT]
    Ôöé
    Ôû╝
[Export CIS Build Kit GPO to local policy format]
    Ôöé
    Ôû╝
[Apply via LGPO.exe: LGPO.exe /g C:\CIS-Policy]
    Ôöé
    Ôû╝
[Run CIS-CAT Lite assessment]
    Ôöé
    Ôû╝
[Document results and exceptions]
    Ôöé
    Ôû╝
[Schedule quarterly manual reassessment]
```
