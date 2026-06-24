# Workflows - DCSync Domain Persistence

## DCSync Attack Chain

```
1. Prerequisites
   Ôö£ÔöÇÔöÇ Domain Admin or account with replication rights
   Ôö£ÔöÇÔöÇ Network access to Domain Controller (TCP/135, dynamic RPC)
   ÔööÔöÇÔöÇ Tool: Mimikatz (Windows) or secretsdump.py (Linux)

2. Credential Extraction
   Ôö£ÔöÇÔöÇ Extract KRBTGT hash (Golden Ticket capability)
   Ôö£ÔöÇÔöÇ Extract Administrator hash (immediate DA access)
   Ôö£ÔöÇÔöÇ Extract all domain hashes (comprehensive dump)
   ÔööÔöÇÔöÇ Extract service account hashes (lateral movement)

3. Golden Ticket Persistence
   Ôö£ÔöÇÔöÇ Forge Golden Ticket with KRBTGT hash
   Ôö£ÔöÇÔöÇ Set arbitrary user, SID, and group memberships
   Ôö£ÔöÇÔöÇ Import ticket into current session
   ÔööÔöÇÔöÇ Access any resource in the domain

4. DCSync Rights Persistence
   Ôö£ÔöÇÔöÇ Create low-profile account in AD
   Ôö£ÔöÇÔöÇ Grant DS-Replication-Get-Changes-All rights
   Ôö£ÔöÇÔöÇ Verify rights with ACL enumeration
   ÔööÔöÇÔöÇ Account can now perform DCSync independently
```

## Golden Ticket Lifecycle

```
Creation: KRBTGT hash + Domain SID ÔåÆ Golden Ticket (10-year validity)
Usage: Import ticket ÔåÆ Access any service in domain
Survival: Persists through password resets (except double KRBTGT reset)
Detection: Anomalous TGT lifetime, non-existent users, impossible SIDs
Cleanup: Double KRBTGT password reset (with 10+ hour gap between resets)
```
