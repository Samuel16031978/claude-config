# Service Account Credential Rotation - Workflows

## Automated Rotation Workflow

```
Rotation Scheduler (cron/secrets manager)
    Ôöé
    Ôö£ÔöÇÔöÇ Pre-Rotation Checks:
    Ôöé   Ôö£ÔöÇÔöÇ Verify service account exists and is active
    Ôöé   Ôö£ÔöÇÔöÇ Verify all dependent services are healthy
    Ôöé   Ôö£ÔöÇÔöÇ Confirm change window (maintenance window)
    Ôöé   ÔööÔöÇÔöÇ Notify operations team of pending rotation
    Ôöé
    Ôö£ÔöÇÔöÇ Generate New Credential:
    Ôöé   Ôö£ÔöÇÔöÇ Create new password/key with required complexity
    Ôöé   Ôö£ÔöÇÔöÇ Store new credential in secrets vault
    Ôöé   ÔööÔöÇÔöÇ Maintain old credential as backup
    Ôöé
    Ôö£ÔöÇÔöÇ Update Source System:
    Ôöé   Ôö£ÔöÇÔöÇ AD: Set-ADAccountPassword
    Ôöé   Ôö£ÔöÇÔöÇ AWS: CreateAccessKey
    Ôöé   Ôö£ÔöÇÔöÇ Azure: Add client secret to service principal
    Ôöé   Ôö£ÔöÇÔöÇ GCP: Create new service account key
    Ôöé   ÔööÔöÇÔöÇ DB: ALTER USER ... PASSWORD ...
    Ôöé
    Ôö£ÔöÇÔöÇ Propagate to Consumers:
    Ôöé   Ôö£ÔöÇÔöÇ Update application config (env vars, config files)
    Ôöé   Ôö£ÔöÇÔöÇ Update Kubernetes secrets
    Ôöé   Ôö£ÔöÇÔöÇ Update CI/CD pipeline secrets
    Ôöé   Ôö£ÔöÇÔöÇ Restart dependent services if required
    Ôöé   ÔööÔöÇÔöÇ Wait for propagation
    Ôöé
    Ôö£ÔöÇÔöÇ Post-Rotation Verification:
    Ôöé   Ôö£ÔöÇÔöÇ Health check all dependent services
    Ôöé   Ôö£ÔöÇÔöÇ Test authentication with new credentials
    Ôöé   Ôö£ÔöÇÔöÇ Verify old credential no longer works
    Ôöé   ÔööÔöÇÔöÇ Log rotation success/failure
    Ôöé
    ÔööÔöÇÔöÇ Cleanup:
        Ôö£ÔöÇÔöÇ Deactivate old credential after grace period
        Ôö£ÔöÇÔöÇ Delete old credential after confirmation
        ÔööÔöÇÔöÇ Update rotation audit log
```

## Emergency Rotation Workflow (Credential Compromise)

```
Credential compromise detected
    Ôöé
    Ôö£ÔöÇÔöÇ IMMEDIATE (within 15 minutes):
    Ôöé   Ôö£ÔöÇÔöÇ Disable compromised credential
    Ôöé   Ôö£ÔöÇÔöÇ Generate new credential
    Ôöé   Ôö£ÔöÇÔöÇ Update source system
    Ôöé   ÔööÔöÇÔöÇ Notify incident response team
    Ôöé
    Ôö£ÔöÇÔöÇ SHORT-TERM (within 1 hour):
    Ôöé   Ôö£ÔöÇÔöÇ Propagate new credential to all consumers
    Ôöé   Ôö£ÔöÇÔöÇ Verify service health
    Ôöé   Ôö£ÔöÇÔöÇ Review audit logs for unauthorized use
    Ôöé   ÔööÔöÇÔöÇ Assess blast radius of compromise
    Ôöé
    ÔööÔöÇÔöÇ FOLLOW-UP (within 24 hours):
        Ôö£ÔöÇÔöÇ Complete incident report
        Ôö£ÔöÇÔöÇ Review rotation procedures
        Ôö£ÔöÇÔöÇ Update dependent service configurations
        ÔööÔöÇÔöÇ Rotate any related credentials
```

## gMSA Migration Workflow

```
Identify service accounts eligible for gMSA migration
    Ôöé
    Ôö£ÔöÇÔöÇ For each eligible service account:
    Ôöé   Ôö£ÔöÇÔöÇ Create gMSA in Active Directory
    Ôöé   Ôö£ÔöÇÔöÇ Add target servers to PrincipalsAllowedToRetrieve
    Ôöé   Ôö£ÔöÇÔöÇ Install gMSA on each target server
    Ôöé   Ôö£ÔöÇÔöÇ Test gMSA retrieval (Test-ADServiceAccount)
    Ôöé   Ôöé
    Ôöé   Ôö£ÔöÇÔöÇ During maintenance window:
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Stop the service
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Change service logon account to gMSA
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Update file/folder permissions if needed
    Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Start the service
    Ôöé   Ôöé   ÔööÔöÇÔöÇ Verify service functionality
    Ôöé   Ôöé
    Ôöé   ÔööÔöÇÔöÇ Post-migration:
    Ôöé       Ôö£ÔöÇÔöÇ Disable old service account
    Ôöé       Ôö£ÔöÇÔöÇ Monitor service for 2 weeks
    Ôöé       ÔööÔöÇÔöÇ Delete old account after confirmation
    Ôöé
    ÔööÔöÇÔöÇ Update service account inventory
```
