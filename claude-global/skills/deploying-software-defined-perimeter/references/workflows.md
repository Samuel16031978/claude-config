# SDP Deployment Workflows

## Workflow 1: SDP Connection Establishment

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé IH (Client) Ôöé     Ôöé SDP ControllerÔöé     Ôöé AH (Gateway)Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôöé                   Ôöé                     Ôöé
       Ôöé 1. Authenticate   Ôöé                     Ôöé
       ÔöéÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ>Ôöé                     Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé 2. Validate ID,   Ôöé                     Ôöé
       Ôöé    device, policy Ôöé                     Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé 3. Auth response  Ôöé                     Ôöé
       Ôöé<ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöé                     Ôöé
       Ôöé  (SPA key, AH IP) Ôöé                     Ôöé
       Ôöé                   Ôöé 4. Notify AH to     Ôöé
       Ôöé                   Ôöé    expect IH        Ôöé
       Ôöé                   ÔöéÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ>Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé 5. Send SPA packetÔöé                     Ôöé
       ÔöéÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ>Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé                   Ôöé  6. Validate SPA    Ôöé
       Ôöé                   Ôöé     Open port       Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé 7. mTLS handshake Ôöé                     Ôöé
       Ôöé<ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ>Ôöé
       Ôöé                   Ôöé                     Ôöé
       Ôöé 8. Application    Ôöé                     Ôöé
       Ôöé    traffic flows  Ôöé                     Ôöé
       Ôöé<ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ=>Ôöé
```

## Workflow 2: SDP Deployment Lifecycle

```
Phase 1: Planning (Weeks 1-2)
Ôö£ÔöÇÔöÇ Inventory protected applications
Ôö£ÔöÇÔöÇ Map user-to-application access requirements
Ôö£ÔöÇÔöÇ Design PKI infrastructure for mTLS
Ôö£ÔöÇÔöÇ Select SDP solution (open-source or commercial)
ÔööÔöÇÔöÇ Plan network architecture changes

Phase 2: Controller Setup (Weeks 3-4)
Ôö£ÔöÇÔöÇ Deploy SDP controller with HA
Ôö£ÔöÇÔöÇ Integrate with IdP (SAML/OIDC)
Ôö£ÔöÇÔöÇ Configure PKI and certificate templates
Ôö£ÔöÇÔöÇ Define application catalog and policies
ÔööÔöÇÔöÇ Test controller authentication flow

Phase 3: Gateway Deployment (Weeks 5-6)
Ôö£ÔöÇÔöÇ Deploy gateways in each app environment
Ôö£ÔöÇÔöÇ Configure default-drop firewall rules
Ôö£ÔöÇÔöÇ Enable SPA listeners
Ôö£ÔöÇÔöÇ Register applications with controller
ÔööÔöÇÔöÇ Verify gateway invisibility (port scan test)

Phase 4: Client Rollout (Weeks 7-10)
Ôö£ÔöÇÔöÇ Package SDP client with certificates
Ôö£ÔöÇÔöÇ Deploy to pilot user group
Ôö£ÔöÇÔöÇ Validate end-to-end connectivity
Ôö£ÔöÇÔöÇ Expand to all user groups
ÔööÔöÇÔöÇ Decommission legacy VPN access

Phase 5: Operations (Ongoing)
Ôö£ÔöÇÔöÇ Monitor SDP controller and gateway health
Ôö£ÔöÇÔöÇ Rotate certificates on schedule
Ôö£ÔöÇÔöÇ Review and update access policies
Ôö£ÔöÇÔöÇ Conduct quarterly penetration tests
ÔööÔöÇÔöÇ Update SDP components for security patches
```

## Workflow 3: SPA Validation

```
Incoming Packet to Gateway
    Ôöé
    v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Is it a SPA packet?  Ôöé
Ôöé (Check magic bytes)  Ôöé
ÔööÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
    Ôöé          Ôöé
   YES        NO
    Ôöé          Ôöé
    v          v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Decrypt  Ôöé  Ôöé DROP     Ôöé
Ôöé SPA data Ôöé  Ôöé silently Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
     v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Validate timestamp   Ôöé
Ôöé (within 60s window)  Ôöé
ÔööÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
   VALID    EXPIRED
    Ôöé          Ôöé
    v          v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Check    Ôöé  Ôöé DROP +   Ôöé
Ôöé HMAC     Ôöé  Ôöé Log      Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
     v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Verify replay        Ôöé
Ôöé (check sequence DB)  Ôöé
ÔööÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
   NEW      REPLAY
    Ôöé          Ôöé
    v          v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Open port Ôöé  Ôöé DROP +   Ôöé
Ôöé for src IPÔöé  Ôöé Alert    Ôöé
Ôöé (30s TTL) Ôöé  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```
