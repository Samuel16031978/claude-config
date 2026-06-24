# Workflows ÔÇö Internal Network Penetration Testing

## Attack Flow

```
Network Access (Ethernet/VPN)
    Ôöé
    Ôö£ÔöÇÔöÇ Network Discovery (Nmap, ARP scan)
    Ôöé
    Ôö£ÔöÇÔöÇ Credential Capture (Responder, mitm6)
    Ôöé       Ôöé
    Ôöé       ÔööÔöÇÔöÇ Hash Cracking (Hashcat)
    Ôöé
    Ôö£ÔöÇÔöÇ AD Enumeration (BloodHound, LDAP)
    Ôöé       Ôöé
    Ôöé       Ôö£ÔöÇÔöÇ Kerberoasting
    Ôöé       Ôö£ÔöÇÔöÇ AS-REP Roasting
    Ôöé       ÔööÔöÇÔöÇ GPP Password Extraction
    Ôöé
    Ôö£ÔöÇÔöÇ Lateral Movement (PsExec, WMI, WinRM)
    Ôöé       Ôöé
    Ôöé       ÔööÔöÇÔöÇ Credential Harvesting (Mimikatz, LSASS dump)
    Ôöé
    Ôö£ÔöÇÔöÇ Privilege Escalation
    Ôöé       Ôöé
    Ôöé       Ôö£ÔöÇÔöÇ Local (unquoted paths, token impersonation)
    Ôöé       ÔööÔöÇÔöÇ Domain (DCSync, Golden Ticket, ADCS)
    Ôöé
    ÔööÔöÇÔöÇ Impact Demonstration
            Ôö£ÔöÇÔöÇ Sensitive data access
            Ôö£ÔöÇÔöÇ Domain compromise proof
            ÔööÔöÇÔöÇ Attack path documentation
```

## Evidence Collection Workflow

```
evidence/
Ôö£ÔöÇÔöÇ credentials/
Ôöé   Ôö£ÔöÇÔöÇ responder_captures/
Ôöé   Ôö£ÔöÇÔöÇ cracked_hashes/
Ôöé   ÔööÔöÇÔöÇ dumped_creds/
Ôö£ÔöÇÔöÇ screenshots/
Ôö£ÔöÇÔöÇ bloodhound/
Ôöé   ÔööÔöÇÔöÇ domain_data.json
Ôö£ÔöÇÔöÇ scan_results/
Ôöé   Ôö£ÔöÇÔöÇ nmap/
Ôöé   ÔööÔöÇÔöÇ shares/
ÔööÔöÇÔöÇ attack_paths/
    ÔööÔöÇÔöÇ path_documentation.md
```
