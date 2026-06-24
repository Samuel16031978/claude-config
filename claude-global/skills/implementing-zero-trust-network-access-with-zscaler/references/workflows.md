# ZTNA Implementation Workflows

## Workflow 1: Initial ZPA Deployment

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Pre-Assessment   Ôöé
Ôöé - Inventory apps Ôöé
Ôöé - Map user groupsÔöé
Ôöé - Classify data  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé IdP Integration      Ôöé
Ôöé - SAML/OIDC config   Ôöé
Ôöé - SCIM provisioning  Ôöé
Ôöé - MFA enrollment     Ôöé
Ôöé - Test SSO flow      Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé App Connector Deploy Ôöé
Ôöé - Provision VMs      Ôöé
Ôöé - Generate enroll keyÔöé
Ôöé - Install + enroll   Ôöé
Ôöé - Health validation  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Application Segments Ôöé
Ôöé - Define apps by     Ôöé
Ôöé   FQDN/IP + ports   Ôöé
Ôöé - Create seg groups  Ôöé
Ôöé - Map to server grps Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Access Policies      Ôöé
Ôöé - User->App mapping  Ôöé
Ôöé - Posture conditions Ôöé
Ôöé - Deny rules         Ôöé
Ôöé - Priority ordering  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Client Deployment    Ôöé
Ôöé - Package connector  Ôöé
Ôöé - MDM distribution   Ôöé
Ôöé - Forwarding profile Ôöé
Ôöé - User acceptance    Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Validation & Monitor Ôöé
Ôöé - Access testing     Ôöé
Ôöé - SIEM integration   Ôöé
Ôöé - Dashboard setup    Ôöé
Ôöé - Incident playbooks Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Workflow 2: Access Request Evaluation (Runtime)

```
User Request
    Ôöé
    v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Client Connector  ÔöéÔöÇÔöÇÔöÇ>Ôöé ZPA Service Edge  Ôöé
Ôöé - Capture request Ôöé    Ôöé - Receive tunnel  Ôöé
Ôöé - Forward to edge Ôöé    Ôöé - Identify user   Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                 Ôöé
                    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇvÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                    Ôöé Authentication          Ôöé
                    Ôöé - Redirect to IdP       Ôöé
                    Ôöé - Validate SAML/OIDC    Ôöé
                    Ôöé - Check MFA completion  Ôöé
                    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                 Ôöé
                    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇvÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                    Ôöé Authorization            Ôöé
                    Ôöé - Match access policies  Ôöé
                    Ôöé - Evaluate posture       Ôöé
                    Ôöé - Check context signals  Ôöé
                    Ôöé - Apply least privilege  Ôöé
                    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                 Ôöé
                    ÔöîÔöÇÔöÇÔöÇÔöÇYESÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇNOÔöÇÔöÇÔöÇÔöÇÔöÉ
                    v                         v
           ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ         ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
           Ôöé Grant Access  Ôöé         Ôöé Deny Access   Ôöé
           Ôöé - Select App  Ôöé         Ôöé - Log denial  Ôöé
           Ôöé   Connector   Ôöé         Ôöé - Alert SIEM  Ôöé
           Ôöé - Stitch tunnelÔöé        Ôöé - User notify Ôöé
           Ôöé - Monitor     Ôöé         ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
           ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Workflow 3: VPN-to-ZTNA Migration

```
Phase 1: Assessment (Weeks 1-2)
Ôö£ÔöÇÔöÇ Catalog all VPN-accessed applications
Ôö£ÔöÇÔöÇ Map user groups to applications
Ôö£ÔöÇÔöÇ Identify application dependencies
Ôö£ÔöÇÔöÇ Baseline VPN performance metrics
ÔööÔöÇÔöÇ Document compliance requirements

Phase 2: Parallel Deployment (Weeks 3-6)
Ôö£ÔöÇÔöÇ Deploy ZPA alongside existing VPN
Ôö£ÔöÇÔöÇ Configure App Connectors for pilot apps
Ôö£ÔöÇÔöÇ Create policies mirroring VPN ACLs
Ôö£ÔöÇÔöÇ Deploy Client Connector to pilot users
ÔööÔöÇÔöÇ Validate access and performance

Phase 3: Migration Waves (Weeks 7-16)
Ôö£ÔöÇÔöÇ Wave 1: Low-risk web applications
Ôö£ÔöÇÔöÇ Wave 2: Business-critical web apps
Ôö£ÔöÇÔöÇ Wave 3: Non-web TCP/UDP applications
Ôö£ÔöÇÔöÇ Wave 4: Legacy applications
ÔööÔöÇÔöÇ Each wave: test ÔåÆ validate ÔåÆ migrate ÔåÆ monitor

Phase 4: VPN Decommission (Weeks 17-20)
Ôö£ÔöÇÔöÇ Verify all applications accessible via ZPA
Ôö£ÔöÇÔöÇ Disable VPN for migrated user groups
Ôö£ÔöÇÔöÇ Monitor for access issues (2-week soak)
Ôö£ÔöÇÔöÇ Decommission VPN concentrators
ÔööÔöÇÔöÇ Update disaster recovery documentation
```

## Workflow 4: Device Posture Enforcement

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Device Connects    Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Posture Assessment Ôöé
Ôöé - OS version       Ôöé
Ôöé - Patch level      Ôöé
Ôöé - Disk encryption  Ôöé
Ôöé - AV/EDR status    Ôöé
Ôöé - Firewall enabled Ôöé
Ôöé - Domain joined    Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Posture Evaluation Ôöé
Ôöé Compare against    Ôöé
Ôöé posture profiles   Ôöé
ÔööÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÿ
    Ôöé          Ôöé
  PASS       FAIL
    Ôöé          Ôöé
    v          v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Full   Ôöé Ôöé Restricted Access Ôöé
Ôöé Access Ôöé Ôöé - Browser only    Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ Ôöé - Limited apps    Ôöé
           Ôöé - Remediation msg Ôöé
           ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Workflow 5: Incident Response with ZPA

```
Alert Triggered (SIEM/SOAR)
    Ôöé
    v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé 1. Triage         Ôöé
Ôöé - Review ZPA logs Ôöé
Ôöé - Identify user   Ôöé
Ôöé - Identify app    Ôöé
Ôöé - Classify event  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé 2. Containment    Ôöé
Ôöé - Revoke user     Ôöé
Ôöé   access in ZPA   Ôöé
Ôöé - Isolate app     Ôöé
Ôöé   segment         Ôöé
Ôöé - Block device    Ôöé
Ôöé   via posture     Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé 3. Investigation  Ôöé
Ôöé - Pull session    Ôöé
Ôöé   logs from ZPA   Ôöé
Ôöé - Correlate with  Ôöé
Ôöé   IdP/EDR/SIEM    Ôöé
Ôöé - Map lateral     Ôöé
Ôöé   movement        Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé 4. Recovery       Ôöé
Ôöé - Update policies Ôöé
Ôöé - Re-enable accessÔöé
Ôöé - Post-incident   Ôöé
Ôöé   review          Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```
