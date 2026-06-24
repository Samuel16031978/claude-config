# Google Workspace SSO - Workflows

## SSO Configuration Workflow

```
1. PREPARE IDP
   Ôö£ÔöÇÔöÇ Create Google Workspace SAML application in IdP
   Ôö£ÔöÇÔöÇ Configure ACS URL: https://www.google.com/a/{domain}/acs
   Ôö£ÔöÇÔöÇ Configure Entity ID: google.com/a/{domain}
   Ôö£ÔöÇÔöÇ Set NameID to user email address
   Ôö£ÔöÇÔöÇ Map required attributes (firstName, lastName)
   ÔööÔöÇÔöÇ Download IdP metadata (SSO URL, certificate, entity ID)

2. CONFIGURE GOOGLE ADMIN CONSOLE
   Ôö£ÔöÇÔöÇ Navigate to Security > Authentication > SSO with third-party IdP
   Ôö£ÔöÇÔöÇ Enable third-party SSO
   Ôö£ÔöÇÔöÇ Enter Sign-in page URL from IdP
   Ôö£ÔöÇÔöÇ Enter Sign-out page URL from IdP
   Ôö£ÔöÇÔöÇ Upload IdP verification certificate
   Ôö£ÔöÇÔöÇ Enable domain-specific issuer
   ÔööÔöÇÔöÇ Save configuration

3. ASSIGN SSO PROFILE
   Ôö£ÔöÇÔöÇ Apply to entire organization OR
   Ôö£ÔöÇÔöÇ Apply to specific organizational units OR
   ÔööÔöÇÔöÇ Apply to specific groups

4. TEST
   Ôö£ÔöÇÔöÇ Test IdP-initiated SSO (login from IdP portal)
   Ôö£ÔöÇÔöÇ Test SP-initiated SSO (login from Google page)
   Ôö£ÔöÇÔöÇ Test sign-out flow
   Ôö£ÔöÇÔöÇ Test with user not in IdP (should fail)
   ÔööÔöÇÔöÇ Test break-glass Super Admin access (should bypass SSO)

5. ROLLOUT
   Ôö£ÔöÇÔöÇ Communicate changes to users
   Ôö£ÔöÇÔöÇ Apply to all organizational units
   Ôö£ÔöÇÔöÇ Monitor for authentication failures
   ÔööÔöÇÔöÇ Update help desk with troubleshooting guide
```

## User Authentication Flow (SP-Initiated)

```
User navigates to mail.google.com/a/{domain}
    Ôöé
    Ôö£ÔöÇÔöÇ Google identifies federated domain
    Ôöé
    Ôö£ÔöÇÔöÇ Redirect to IdP with SAML AuthnRequest
    Ôöé   URL: {IdP SSO URL}?SAMLRequest={base64encoded}
    Ôöé
    Ôö£ÔöÇÔöÇ User authenticates at IdP:
    Ôöé   Ôö£ÔöÇÔöÇ Enter credentials
    Ôöé   Ôö£ÔöÇÔöÇ Complete MFA challenge
    Ôöé   ÔööÔöÇÔöÇ IdP validates against directory
    Ôöé
    Ôö£ÔöÇÔöÇ IdP generates SAML Response:
    Ôöé   Ôö£ÔöÇÔöÇ Assertion with NameID (email)
    Ôöé   Ôö£ÔöÇÔöÇ Authentication context (MFA)
    Ôöé   Ôö£ÔöÇÔöÇ Digitally signed with IdP certificate
    Ôöé   ÔööÔöÇÔöÇ Optionally encrypted
    Ôöé
    Ôö£ÔöÇÔöÇ Browser POSTs Response to Google ACS URL
    Ôöé
    Ôö£ÔöÇÔöÇ Google validates:
    Ôöé   Ôö£ÔöÇÔöÇ Signature against uploaded certificate
    Ôöé   Ôö£ÔöÇÔöÇ Assertion not expired
    Ôöé   Ôö£ÔöÇÔöÇ Audience matches entity ID
    Ôöé   Ôö£ÔöÇÔöÇ NameID matches a Google Workspace user
    Ôöé   ÔööÔöÇÔöÇ InResponseTo matches original request
    Ôöé
    ÔööÔöÇÔöÇ User logged in to Google Workspace
```

## Certificate Renewal Workflow

```
IdP signing certificate approaching expiration (30 days before)
    Ôöé
    Ôö£ÔöÇÔöÇ Generate new signing certificate in IdP
    Ôöé
    Ôö£ÔöÇÔöÇ Upload new certificate to Google Admin Console
    Ôöé   (Google supports multiple verification certificates)
    Ôöé
    Ôö£ÔöÇÔöÇ Promote new certificate as primary in IdP
    Ôöé
    Ôö£ÔöÇÔöÇ Verify SSO still works with new certificate
    Ôöé
    ÔööÔöÇÔöÇ Remove old certificate from Google Admin Console after confirmation
```

## Troubleshooting Workflow

```
User reports SSO failure
    Ôöé
    Ôö£ÔöÇÔöÇ Check 1: Is user assigned to the Google Workspace app in IdP?
    Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Assign user in IdP
    Ôöé
    Ôö£ÔöÇÔöÇ Check 2: Does NameID match user's Google email exactly?
    Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Fix attribute mapping in IdP
    Ôöé
    Ôö£ÔöÇÔöÇ Check 3: Is the IdP certificate expired?
    Ôöé   ÔööÔöÇÔöÇ YES ÔåÆ Upload renewed certificate
    Ôöé
    Ôö£ÔöÇÔöÇ Check 4: Is there clock skew between IdP and Google?
    Ôöé   ÔööÔöÇÔöÇ YES ÔåÆ Sync NTP on IdP server (max 5 min skew allowed)
    Ôöé
    Ôö£ÔöÇÔöÇ Check 5: Is the SAML assertion properly signed?
    Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Verify IdP signing algorithm matches uploaded cert
    Ôöé
    ÔööÔöÇÔöÇ Check 6: Check IdP SAML debug logs for detailed error
```
