# Workflows - LaZagne Credential Access

## Credential Harvesting Workflow

```
1. Pre-Execution
   Ôö£ÔöÇÔöÇ Verify access level (standard user vs. admin/SYSTEM)
   Ôö£ÔöÇÔöÇ Check AV/EDR status on target
   Ôö£ÔöÇÔöÇ Prepare output directory for results
   ÔööÔöÇÔöÇ Plan exfiltration method for credential data

2. Execution
   Ôö£ÔöÇÔöÇ Run lazagne.exe all -oJ for full extraction
   Ôö£ÔöÇÔöÇ Run specific modules if full scan is too noisy
   Ôö£ÔöÇÔöÇ Elevate to SYSTEM if needed for DPAPI/LSA
   ÔööÔöÇÔöÇ Collect output files

3. Analysis
   Ôö£ÔöÇÔöÇ Parse JSON output
   Ôö£ÔöÇÔöÇ Deduplicate credentials
   Ôö£ÔöÇÔöÇ Categorize by source (browser, email, system, etc.)
   ÔööÔöÇÔöÇ Prioritize by value (domain creds > local > web)

4. Validation
   Ôö£ÔöÇÔöÇ Test domain credentials with CrackMapExec
   Ôö£ÔöÇÔöÇ Verify cloud credentials (AWS CLI, Azure CLI)
   Ôö£ÔöÇÔöÇ Check VPN/remote access credentials
   ÔööÔöÇÔöÇ Map credentials to BloodHound attack paths

5. Lateral Movement
   Ôö£ÔöÇÔöÇ Use validated credentials for next hop
   Ôö£ÔöÇÔöÇ Repeat credential harvesting on new targets
   ÔööÔöÇÔöÇ Document credential chain for report
```

## Module Execution Priority

```
High Priority (run first):
  browsers    ÔåÆ Web application credentials, SSO tokens
  windows     ÔåÆ Domain cached credentials, DPAPI
  sysadmin    ÔåÆ SSH keys, RDP credentials, PuTTY

Medium Priority:
  databases   ÔåÆ Database connection strings
  mails       ÔåÆ Email credentials for BEC
  git         ÔåÆ Source code repository access

Low Priority:
  wifi        ÔåÆ Network access but limited value
  chat        ÔåÆ Communication platform access
  svn         ÔåÆ Legacy source control
```
