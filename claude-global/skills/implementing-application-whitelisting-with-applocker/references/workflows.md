# Workflows - Implementing Application Whitelisting with AppLocker

## Workflow 1: Initial AppLocker Deployment

```
[Application Inventory]
    Ôöé
    Ôö£ÔöÇÔöÇ Scan reference endpoints for installed applications
    Ôö£ÔöÇÔöÇ Catalog all approved software by publisher/path/hash
    Ôö£ÔöÇÔöÇ Identify admin tools vs. standard user applications
    Ôöé
    Ôû╝
[Policy Design]
    Ôöé
    Ôö£ÔöÇÔöÇ Create default allow rules (Program Files, Windows)
    Ôö£ÔöÇÔöÇ Create publisher rules for third-party vendors
    Ôö£ÔöÇÔöÇ Create deny rules for LOLBins (standard users only)
    Ôö£ÔöÇÔöÇ Create script control rules
    Ôöé
    Ôû╝
[Audit Mode Deployment]
    Ôöé
    Ôö£ÔöÇÔöÇ Deploy via GPO to pilot OU (Audit Only)
    Ôö£ÔöÇÔöÇ Enable Application Identity service
    Ôö£ÔöÇÔöÇ Monitor for 2-4 weeks
    Ôöé
    Ôû╝
[Audit Log Analysis]
    Ôöé
    Ôö£ÔöÇÔöÇ Export blocked events (8003, 8006)
    Ôö£ÔöÇÔöÇ Identify legitimate applications being blocked
    Ôöé
    Ôö£ÔöÇÔöÇ Blocked app is legitimate ÔöÇÔöÇÔû║ [Create allow rule]
    Ôöé                                       Ôöé
    Ôöé                                       Ôû╝
    Ôöé                                  [Re-audit 1 week]
    Ôöé
    ÔööÔöÇÔöÇ All blocked apps are unauthorized ÔöÇÔöÇÔû║ [Proceed to enforcement]
                                                    Ôöé
                                                    Ôû╝
                                               [Switch to Enforce mode (phased)]
                                                    Ôöé
                                                    Ôö£ÔöÇÔöÇ Week 1: EXE rules
                                                    Ôö£ÔöÇÔöÇ Week 2: Script rules
                                                    Ôö£ÔöÇÔöÇ Week 3: MSI rules
                                                    ÔööÔöÇÔöÇ Week 4: DLL rules (optional)
```

## Workflow 2: New Application Approval

```
[User requests new application]
    Ôöé
    Ôû╝
[Security review of application]
    Ôöé
    Ôö£ÔöÇÔöÇ Is it signed by trusted publisher? ÔöÇÔöÇÔû║ [Create publisher rule]
    Ôöé
    Ôö£ÔöÇÔöÇ Unsigned but necessary? ÔöÇÔöÇÔû║ [Create hash rule + document exception]
    Ôöé
    ÔööÔöÇÔöÇ Fails security review ÔöÇÔöÇÔû║ [Deny request, document reason]
    Ôöé
    Ôû╝
[Add rule to AppLocker GPO]
    Ôöé
    Ôû╝
[Deploy to pilot OU, verify no conflicts]
    Ôöé
    Ôû╝
[Deploy to production OU]
    Ôöé
    Ôû╝
[Update application inventory]
```

## Workflow 3: AppLocker Bypass Incident Response

```
[Detection: Unauthorized execution despite AppLocker]
    Ôöé
    Ôû╝
[Identify bypass technique]
    Ôöé
    Ôö£ÔöÇÔöÇ LOLBin not blocked ÔöÇÔöÇÔû║ [Add deny rule for specific binary]
    Ôöé
    Ôö£ÔöÇÔöÇ Execution from allowed path ÔöÇÔöÇÔû║ [Restrict path rule scope]
    Ôöé
    Ôö£ÔöÇÔöÇ Admin user bypass ÔöÇÔöÇÔû║ [Evaluate WDAC migration for admin enforcement]
    Ôöé
    ÔööÔöÇÔöÇ DLL side-loading ÔöÇÔöÇÔû║ [Enable DLL rules or deploy WDAC]
    Ôöé
    Ôû╝
[Update AppLocker policy with fix]
    Ôöé
    Ôû╝
[Verify fix in audit mode on test endpoint]
    Ôöé
    Ôû╝
[Deploy fix to production]
    Ôöé
    Ôû╝
[Update threat model and rule documentation]
```

## Workflow 4: AppLocker to WDAC Migration

```
[Decision: Migrate from AppLocker to WDAC]
    Ôöé
    Ôû╝
[Audit current AppLocker policy]
    Ôöé
    Ôö£ÔöÇÔöÇ Export AppLocker rules as XML
    Ôö£ÔöÇÔöÇ Identify rules that need WDAC equivalents
    Ôöé
    Ôû╝
[Create WDAC policy using WDAC Wizard]
    Ôöé
    Ôö£ÔöÇÔöÇ Convert publisher rules to WDAC signer rules
    Ôö£ÔöÇÔöÇ Convert path rules to WDAC filepath rules
    Ôö£ÔöÇÔöÇ Add Microsoft recommended block rules
    Ôöé
    Ôû╝
[Deploy WDAC in Audit mode alongside AppLocker]
    Ôöé
    Ôû╝
[Monitor WDAC audit events for 4 weeks]
    Ôöé
    Ôû╝
[Resolve WDAC audit findings]
    Ôöé
    Ôû╝
[Switch WDAC to Enforce mode]
    Ôöé
    Ôû╝
[Disable AppLocker policy]
```
