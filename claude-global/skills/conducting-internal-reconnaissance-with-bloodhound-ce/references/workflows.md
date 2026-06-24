# Workflows - BloodHound CE Reconnaissance

## Complete Reconnaissance Workflow

```
1. Deployment
   Ôö£ÔöÇÔöÇ Pull BloodHound CE Docker images
   Ôö£ÔöÇÔöÇ Start services with docker compose up -d
   Ôö£ÔöÇÔöÇ Access web UI and set admin password
   ÔööÔöÇÔöÇ Verify API connectivity

2. Data Collection
   Ôö£ÔöÇÔöÇ Choose collector: SharpHound v2 (Windows) or BloodHound.py (Linux)
   Ôö£ÔöÇÔöÇ Run All collection method for comprehensive data
   Ôö£ÔöÇÔöÇ Run Session collection in loop for user mapping
   Ôö£ÔöÇÔöÇ Collect from all reachable domains
   ÔööÔöÇÔöÇ Exfiltrate ZIP data to analysis workstation

3. Import and Setup
   Ôö£ÔöÇÔöÇ Upload ZIP files via BloodHound CE web interface
   Ôö£ÔöÇÔöÇ Wait for data processing to complete
   Ôö£ÔöÇÔöÇ Mark owned/compromised principals
   ÔööÔöÇÔöÇ Set high-value targets

4. Analysis
   Ôö£ÔöÇÔöÇ Run built-in attack path queries
   Ôö£ÔöÇÔöÇ Execute custom Cypher queries
   Ôö£ÔöÇÔöÇ Identify ACL abuse opportunities
   Ôö£ÔöÇÔöÇ Map delegation configurations
   Ôö£ÔöÇÔöÇ Find Kerberoastable / AS-REP roastable accounts
   ÔööÔöÇÔöÇ Discover GPO modification paths

5. Attack Planning
   Ôö£ÔöÇÔöÇ Prioritize paths by hop count and stealth
   Ôö£ÔöÇÔöÇ Identify tools needed per hop
   Ôö£ÔöÇÔöÇ Plan OPSEC for each technique
   ÔööÔöÇÔöÇ Document execution plan

6. Reporting
   Ôö£ÔöÇÔöÇ Export graph visualizations
   Ôö£ÔöÇÔöÇ Generate path summaries
   Ôö£ÔöÇÔöÇ Document all findings with evidence
   ÔööÔöÇÔöÇ Provide remediation recommendations
```

## Stealthy Collection Workflow

```
Low-Noise Collection:
  1. DCOnly mode: Only queries domain controllers via LDAP
     SharpHound.exe -c DCOnly

  2. Targeted collection: Specific container/OU
     SharpHound.exe -c All --searchbase "OU=Servers,DC=domain,DC=local"

  3. Session loop: Passive session enumeration over time
     SharpHound.exe -c Session --loop --loopduration 04:00:00 --loopinterval 00:05:00
```
