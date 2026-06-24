# Workflows - EvilGinx3 Initial Access

## End-to-End AiTM Phishing Workflow

```
1. Reconnaissance
   Ôö£ÔöÇÔöÇ Identify target authentication service (M365, Google, Okta)
   Ôö£ÔöÇÔöÇ Analyze target MFA implementation (SMS, Authenticator, FIDO2)
   Ôö£ÔöÇÔöÇ Register lookalike domain with appropriate TLD
   ÔööÔöÇÔöÇ Categorize domain to avoid URL filtering

2. Infrastructure Setup
   Ôö£ÔöÇÔöÇ Deploy VPS and configure DNS records
   Ôö£ÔöÇÔöÇ Install and configure EvilGinx3
   Ôö£ÔöÇÔöÇ Enable phishlet for target service
   Ôö£ÔöÇÔöÇ Verify SSL certificate provisioning
   ÔööÔöÇÔöÇ Create and test lure URLs

3. Phishing Delivery
   Ôö£ÔöÇÔöÇ Craft pretext email with social engineering
   Ôö£ÔöÇÔöÇ Configure GoPhish or SMTP relay for delivery
   Ôö£ÔöÇÔöÇ Send phishing emails to authorized targets
   ÔööÔöÇÔöÇ Monitor delivery and open rates

4. Credential and Session Capture
   Ôö£ÔöÇÔöÇ Monitor EvilGinx3 session dashboard
   Ôö£ÔöÇÔöÇ Capture credentials as victims authenticate
   Ôö£ÔöÇÔöÇ Capture session cookies (MFA bypass tokens)
   ÔööÔöÇÔöÇ Export session data for exploitation

5. Session Hijacking
   Ôö£ÔöÇÔöÇ Import session cookies into attacker browser
   Ôö£ÔöÇÔöÇ Navigate to target service with hijacked session
   Ôö£ÔöÇÔöÇ Validate access to victim's account
   ÔööÔöÇÔöÇ Enumerate accessible resources

6. Persistence and Escalation
   Ôö£ÔöÇÔöÇ Create application-specific passwords
   Ôö£ÔöÇÔöÇ Register attacker device in Azure AD / Entra ID
   Ôö£ÔöÇÔöÇ Add OAuth application consents
   ÔööÔöÇÔöÇ Establish email forwarding rules for persistence

7. Reporting
   Ôö£ÔöÇÔöÇ Document attack chain with evidence
   Ôö£ÔöÇÔöÇ Record number of successful captures
   Ôö£ÔöÇÔöÇ Identify defensive gaps exploited
   ÔööÔöÇÔöÇ Provide remediation recommendations
```

## Cookie Import Workflow

```
1. From EvilGinx3 session output, copy cookie data
2. Open browser with Cookie-Editor extension
3. Navigate to target service login page
4. Clear existing cookies for the domain
5. Import captured cookies via Cookie-Editor
6. Refresh the page to obtain authenticated session
7. Verify access to victim's account
```
