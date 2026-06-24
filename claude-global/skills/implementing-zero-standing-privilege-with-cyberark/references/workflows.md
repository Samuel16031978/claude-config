# Zero Standing Privilege with CyberArk - Workflows

## JIT Access Request Workflow

```
Developer needs to access AWS production environment
    Ôöé
    Ôö£ÔöÇÔöÇ Opens CyberArk Secure Cloud Access portal
    Ôöé
    Ôö£ÔöÇÔöÇ Selects target: AWS Account "Production" (123456789012)
    Ôöé
    Ôö£ÔöÇÔöÇ Selects policy: "Developer Production Read Access"
    Ôöé
    Ôö£ÔöÇÔöÇ Specifies duration: 2 hours
    Ôöé
    Ôö£ÔöÇÔöÇ Provides justification: "Investigating PROD-1234 latency issue"
    Ôöé
    Ôö£ÔöÇÔöÇ Submits request
    Ôöé
    Ôö£ÔöÇÔöÇ CyberArk evaluates TEA policy:
    Ôöé   Ôö£ÔöÇÔöÇ Time: 2 hours within allowed range
    Ôöé   Ôö£ÔöÇÔöÇ Entitlements: Read-only production access
    Ôöé   ÔööÔöÇÔöÇ Approval: Manager approval required
    Ôöé
    Ôö£ÔöÇÔöÇ Approval request sent to manager (Slack/email)
    Ôöé
    Ôö£ÔöÇÔöÇ Manager approves
    Ôöé
    Ôö£ÔöÇÔöÇ CyberArk provisions ephemeral IAM role:
    Ôöé   Ôö£ÔöÇÔöÇ Creates role with ReadOnlyAccess + resource restrictions
    Ôöé   Ôö£ÔöÇÔöÇ Sets session duration to 2 hours
    Ôöé   ÔööÔöÇÔöÇ Generates temporary STS credentials
    Ôöé
    Ôö£ÔöÇÔöÇ Developer accesses AWS console/CLI with temp credentials
    Ôöé   ÔööÔöÇÔöÇ All actions recorded in session log
    Ôöé
    ÔööÔöÇÔöÇ After 2 hours: role deleted, credentials revoked
```

## Standing Privilege Migration Workflow

```
Phase 1: DISCOVERY AND ANALYSIS
    Ôö£ÔöÇÔöÇ Export all IAM users/roles with standing admin access
    Ôö£ÔöÇÔöÇ Analyze CloudTrail logs for actual permission usage
    Ôö£ÔöÇÔöÇ Identify which permissions are actually used vs. assigned
    Ôö£ÔöÇÔöÇ Calculate right-sized policy for each use case
    ÔööÔöÇÔöÇ Map standing privileges to CyberArk ZSP policies

Phase 2: POLICY CREATION
    Ôö£ÔöÇÔöÇ Create CyberArk SCA policies for each access pattern
    Ôö£ÔöÇÔöÇ Define TEA parameters:
    Ôöé   Ôö£ÔöÇÔöÇ Maximum session duration per policy
    Ôöé   Ôö£ÔöÇÔöÇ Entitlement scope (AWS managed policies + custom)
    Ôöé   ÔööÔöÇÔöÇ Approval requirements (auto vs. manual)
    Ôö£ÔöÇÔöÇ Configure approval workflows
    ÔööÔöÇÔöÇ Test policies with pilot group

Phase 3: PILOT MIGRATION (2-4 weeks)
    Ôö£ÔöÇÔöÇ Assign ZSP policies to pilot users
    Ôö£ÔöÇÔöÇ Remove standing privileges from pilot users
    Ôö£ÔöÇÔöÇ Monitor for access denied errors
    Ôö£ÔöÇÔöÇ Adjust policies based on feedback
    ÔööÔöÇÔöÇ Measure: request volume, approval time, session duration

Phase 4: FULL MIGRATION (4-8 weeks)
    Ôö£ÔöÇÔöÇ Migrate teams in waves (1 team per week)
    Ôö£ÔöÇÔöÇ Remove standing privileges after ZSP confirmed working
    Ôö£ÔöÇÔöÇ Configure auto-detect for new standing privilege creation
    ÔööÔöÇÔöÇ Report metrics to security leadership

Phase 5: CONTINUOUS GOVERNANCE
    Ôö£ÔöÇÔöÇ Weekly: Review and right-size ZSP policies
    Ôö£ÔöÇÔöÇ Monthly: Audit for any standing privilege re-creation
    Ôö£ÔöÇÔöÇ Quarterly: Entitlement optimization report
    ÔööÔöÇÔöÇ Alert on: New standing admin roles created outside CyberArk
```

## Emergency Break-Glass Workflow

```
CyberArk SCA unavailable or network issue
    Ôöé
    Ôö£ÔöÇÔöÇ Retrieve break-glass credentials from:
    Ôöé   Ôö£ÔöÇÔöÇ Physical safe (sealed envelope)
    Ôöé   Ôö£ÔöÇÔöÇ Or secondary vault (Azure Key Vault / AWS Secrets Manager)
    Ôöé
    Ôö£ÔöÇÔöÇ Authenticate with break-glass credentials
    Ôöé
    Ôö£ÔöÇÔöÇ Perform emergency actions
    Ôöé
    Ôö£ÔöÇÔöÇ Document all actions taken
    Ôöé
    ÔööÔöÇÔöÇ Post-incident:
        Ôö£ÔöÇÔöÇ Rotate break-glass credentials
        Ôö£ÔöÇÔöÇ Review session logs for the emergency access
        Ôö£ÔöÇÔöÇ File incident report
        ÔööÔöÇÔöÇ Verify no unauthorized changes made
```
