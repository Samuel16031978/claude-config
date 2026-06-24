# Access Recertification with Saviynt - Workflows

## Campaign Execution Workflow

```
WEEK 1: PREPARATION
    Ôö£ÔöÇÔöÇ Review and update certifier assignments
    Ôö£ÔöÇÔöÇ Verify identity data freshness (HR sync)
    Ôö£ÔöÇÔöÇ Validate entitlement data accuracy
    Ôö£ÔöÇÔöÇ Configure campaign template
    ÔööÔöÇÔöÇ Schedule campaign launch

WEEK 2: LAUNCH AND REVIEW
    Ôö£ÔöÇÔöÇ Launch campaign (auto-notifications sent)
    Ôö£ÔöÇÔöÇ Certifiers receive email with review link
    Ôö£ÔöÇÔöÇ Certifiers review each line item:
    Ôöé   Ôö£ÔöÇÔöÇ Check user's current role
    Ôöé   Ôö£ÔöÇÔöÇ Review risk score
    Ôöé   Ôö£ÔöÇÔöÇ Check last access date
    Ôöé   Ôö£ÔöÇÔöÇ Compare with peer group
    Ôöé   ÔööÔöÇÔöÇ Make certify/revoke decision
    ÔööÔöÇÔöÇ Day 7: First reminder sent

WEEK 3: FOLLOW-UP
    Ôö£ÔöÇÔöÇ Day 10: Second reminder sent
    Ôö£ÔöÇÔöÇ Day 13: Final reminder (escalation warning)
    Ôö£ÔöÇÔöÇ Security team contacts non-responsive certifiers
    ÔööÔöÇÔöÇ Campaign manager reviews progress dashboard

WEEK 4: CLOSE AND REMEDIATE
    Ôö£ÔöÇÔöÇ Day 14: Campaign due date
    Ôö£ÔöÇÔöÇ Day 15: Auto-revoke for non-certified items (if configured)
    Ôö£ÔöÇÔöÇ Revocation tasks created automatically
    Ôö£ÔöÇÔöÇ Remediation tickets sent to provisioning team
    Ôö£ÔöÇÔöÇ Access removed from target systems
    ÔööÔöÇÔöÇ Campaign report generated for compliance
```

## Certifier Decision Workflow

```
Certifier opens Saviynt certification inbox
    Ôöé
    Ôö£ÔöÇÔöÇ For each user-entitlement pair:
    Ôöé
    Ôöé   Ôö£ÔöÇÔöÇ Review Context:
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ User's name, title, department
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Entitlement name and application
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Risk score (1-10)
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Last access: 3 days ago / 180 days ago / Never
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Peer analysis: 85% of peers have this access
    Ôöé   Ôöé   ÔööÔöÇÔöÇ SoD violation: None / Conflict detected
    Ôöé   Ôöé
    Ôöé   Ôö£ÔöÇÔöÇ Decision Logic:
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Active user + Used recently + Peers have it ÔåÆ CERTIFY
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Active user + Not used in 90+ days ÔåÆ INVESTIGATE
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ User changed department ÔåÆ LIKELY REVOKE
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ SoD violation detected ÔåÆ REVOKE or ESCALATE
    Ôöé   Ôöé   ÔööÔöÇÔöÇ Cannot determine ÔåÆ DELEGATE to app owner
    Ôöé   Ôöé
    Ôöé   ÔööÔöÇÔöÇ Record decision with justification
    Ôöé
    ÔööÔöÇÔöÇ Submit all decisions
```

## Event-Based Certification Workflow

```
User attribute changes in HR system (e.g., department transfer)
    Ôöé
    Ôö£ÔöÇÔöÇ Saviynt detects change via HR connector sync
    Ôöé
    Ôö£ÔöÇÔöÇ User update rule triggers micro-certification:
    Ôöé   Ôö£ÔöÇÔöÇ Scope: All entitlements for this user
    Ôöé   Ôö£ÔöÇÔöÇ Certifier: New manager
    Ôöé   ÔööÔöÇÔöÇ Due date: 7 days
    Ôöé
    Ôö£ÔöÇÔöÇ New manager reviews all access:
    Ôöé   Ôö£ÔöÇÔöÇ Certify access relevant to new role
    Ôöé   Ôö£ÔöÇÔöÇ Revoke access specific to old role
    Ôöé   ÔööÔöÇÔöÇ Request new access if needed
    Ôöé
    ÔööÔöÇÔöÇ Remediation executes for revoked items
```

## Remediation Tracking Workflow

```
Campaign completes with revoked items
    Ôöé
    Ôö£ÔöÇÔöÇ Saviynt creates provisioning tasks for each revocation
    Ôöé
    Ôö£ÔöÇÔöÇ For each revoked entitlement:
    Ôöé   Ôö£ÔöÇÔöÇ Create deprovisioning request
    Ôöé   Ôö£ÔöÇÔöÇ Route to target system connector
    Ôöé   Ôö£ÔöÇÔöÇ Execute removal (API/connector)
    Ôöé   Ôö£ÔöÇÔöÇ Verify removal succeeded
    Ôöé   ÔööÔöÇÔöÇ Update audit log
    Ôöé
    Ôö£ÔöÇÔöÇ If automated removal fails:
    Ôöé   Ôö£ÔöÇÔöÇ Create manual remediation ticket (ServiceNow)
    Ôöé   Ôö£ÔöÇÔöÇ Assign to application admin
    Ôöé   Ôö£ÔöÇÔöÇ Track SLA compliance
    Ôöé   ÔööÔöÇÔöÇ Escalate if overdue
    Ôöé
    ÔööÔöÇÔöÇ Post-remediation verification:
        Ôö£ÔöÇÔöÇ Re-scan target systems
        Ôö£ÔöÇÔöÇ Confirm revoked access no longer present
        ÔööÔöÇÔöÇ Archive compliance evidence
```
