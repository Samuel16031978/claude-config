# Privileged Account Access Review - Workflows

## Quarterly Review Cycle

```
Week 1: PREPARATION
    Ôö£ÔöÇÔöÇ Extract privileged account inventory from PAM/AD/Cloud
    Ôö£ÔöÇÔöÇ Identify new accounts since last review
    Ôö£ÔöÇÔöÇ Assign reviewers based on account ownership
    ÔööÔöÇÔöÇ Send review campaign notifications

Week 2-3: REVIEW EXECUTION
    Ôö£ÔöÇÔöÇ Reviewers evaluate each account against criteria
    Ôö£ÔöÇÔöÇ Approve, revoke, or flag for investigation
    Ôö£ÔöÇÔöÇ Escalate unresponsive reviewers after 7 days
    ÔööÔöÇÔöÇ Security team reviews flagged accounts

Week 4: REMEDIATION
    Ôö£ÔöÇÔöÇ Disable/remove revoked accounts
    Ôö£ÔöÇÔöÇ Rotate credentials for all reviewed accounts
    Ôö£ÔöÇÔöÇ Create tickets for privilege reduction
    ÔööÔöÇÔöÇ Generate review completion report
```

## Account Discovery Workflow

```
1. Active Directory Enumeration
   Ôö£ÔöÇÔöÇ Query AdminCount=1 accounts
   Ôö£ÔöÇÔöÇ Enumerate privileged group memberships
   Ôö£ÔöÇÔöÇ Identify accounts with SPN (service accounts)
   ÔööÔöÇÔöÇ Check for accounts with delegation rights

2. Cloud Platform Enumeration
   Ôö£ÔöÇÔöÇ AWS: List IAM users/roles with admin policies
   Ôö£ÔöÇÔöÇ Azure: Export Entra ID directory role assignments
   Ôö£ÔöÇÔöÇ GCP: List IAM bindings with Owner/Editor roles
   ÔööÔöÇÔöÇ Cross-reference with known approved accounts

3. Database and Application Enumeration
   Ôö£ÔöÇÔöÇ Query database system role memberships
   Ôö£ÔöÇÔöÇ Export application admin role assignments
   ÔööÔöÇÔöÇ Identify shared/generic admin accounts

4. Consolidation
   Ôö£ÔöÇÔöÇ Merge all discovered accounts into single inventory
   Ôö£ÔöÇÔöÇ Deduplicate accounts across platforms
   Ôö£ÔöÇÔöÇ Assign risk classification
   ÔööÔöÇÔöÇ Identify accounts missing from PAM vault
```

## Reviewer Decision Workflow

```
Reviewer receives account for certification
    Ôöé
    Ôö£ÔöÇÔöÇ Is the account owner still employed?
    Ôöé   Ôö£ÔöÇÔöÇ NO ÔåÆ Revoke immediately, disable account
    Ôöé   ÔööÔöÇÔöÇ YES ÔåÆ Continue
    Ôöé
    Ôö£ÔöÇÔöÇ Has the account been used in last 90 days?
    Ôöé   Ôö£ÔöÇÔöÇ NO ÔåÆ Recommend disable, notify owner
    Ôöé   ÔööÔöÇÔöÇ YES ÔåÆ Continue
    Ôöé
    Ôö£ÔöÇÔöÇ Does the user's current role require this privilege?
    Ôöé   Ôö£ÔöÇÔöÇ NO ÔåÆ Revoke, provide lower-privilege alternative
    Ôöé   ÔööÔöÇÔöÇ YES ÔåÆ Continue
    Ôöé
    Ôö£ÔöÇÔöÇ Can the privilege be reduced (least privilege)?
    Ôöé   Ôö£ÔöÇÔöÇ YES ÔåÆ Approve with remediation to reduce
    Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Continue
    Ôöé
    Ôö£ÔöÇÔöÇ Are there SoD conflicts?
    Ôöé   Ôö£ÔöÇÔöÇ YES ÔåÆ Flag for risk acceptance or remediation
    Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Continue
    Ôöé
    ÔööÔöÇÔöÇ CERTIFY the access with documented justification
```

## Emergency Account Review Workflow

```
Break-glass account used
    Ôöé
    Ôö£ÔöÇÔöÇ Alert generated to security team
    Ôöé
    Ôö£ÔöÇÔöÇ Within 24 hours:
    Ôöé   Ôö£ÔöÇÔöÇ Verify incident ticket exists for the usage
    Ôöé   Ôö£ÔöÇÔöÇ Confirm authorized personnel used the account
    Ôöé   Ôö£ÔöÇÔöÇ Review session recording (if available)
    Ôöé   ÔööÔöÇÔöÇ Validate actions taken were appropriate
    Ôöé
    Ôö£ÔöÇÔöÇ Within 48 hours:
    Ôöé   Ôö£ÔöÇÔöÇ Reset break-glass account credentials
    Ôöé   Ôö£ÔöÇÔöÇ Store new credentials in sealed envelope/vault
    Ôöé   ÔööÔöÇÔöÇ Document usage in access review log
    Ôöé
    ÔööÔöÇÔöÇ Monthly: Verify break-glass accounts have not been used
        without corresponding incident documentation
```
