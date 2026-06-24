# Workflows ÔÇö Active Directory Penetration Testing

## AD Attack Flow

```
Domain User Credentials
    Ôöé
    Ôö£ÔöÇÔöÇ Enumeration
    Ôöé   Ôö£ÔöÇÔöÇ BloodHound (attack paths)
    Ôöé   Ôö£ÔöÇÔöÇ LDAP queries (users, groups, GPOs)
    Ôöé   ÔööÔöÇÔöÇ Service account discovery (SPNs)
    Ôöé
    Ôö£ÔöÇÔöÇ Kerberos Attacks
    Ôöé   Ôö£ÔöÇÔöÇ Kerberoasting ÔåÆ Hash cracking
    Ôöé   Ôö£ÔöÇÔöÇ AS-REP Roasting ÔåÆ Hash cracking
    Ôöé   ÔööÔöÇÔöÇ Delegation abuse (unconstrained/constrained/RBCD)
    Ôöé
    Ôö£ÔöÇÔöÇ ADCS Attacks
    Ôöé   Ôö£ÔöÇÔöÇ ESC1-ESC8 template exploitation
    Ôöé   ÔööÔöÇÔöÇ Certificate-based auth to DA
    Ôöé
    Ôö£ÔöÇÔöÇ Credential Harvesting
    Ôöé   Ôö£ÔöÇÔöÇ LSASS dump (Mimikatz)
    Ôöé   Ôö£ÔöÇÔöÇ SAM/SYSTEM extraction
    Ôöé   ÔööÔöÇÔöÇ DPAPI credential decryption
    Ôöé
    Ôö£ÔöÇÔöÇ Domain Escalation
    Ôöé   Ôö£ÔöÇÔöÇ DCSync (krbtgt + all hashes)
    Ôöé   Ôö£ÔöÇÔöÇ Golden Ticket
    Ôöé   ÔööÔöÇÔöÇ AdminSDHolder persistence
    Ôöé
    ÔööÔöÇÔöÇ Impact Demonstration
        Ôö£ÔöÇÔöÇ Full domain hash extraction
        Ôö£ÔöÇÔöÇ Access to sensitive resources
        ÔööÔöÇÔöÇ Cross-forest trust abuse
```
