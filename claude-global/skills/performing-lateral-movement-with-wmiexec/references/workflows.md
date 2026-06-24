# Workflows - WMIExec Lateral Movement

## Lateral Movement Chain

```
1. Initial Compromise ÔåÆ Credential Harvesting ÔåÆ WMIExec to target
2. On each new host:
   Ôö£ÔöÇÔöÇ Enumerate local users and groups
   Ôö£ÔöÇÔöÇ Harvest credentials (LaZagne, Mimikatz, SAM dump)
   Ôö£ÔöÇÔöÇ Check for domain admin sessions
   ÔööÔöÇÔöÇ Pivot to next target using recovered credentials
```

## Multi-Method Fallback

```
Primary:   wmiexec.py (semi-interactive, output capture)
Fallback1: dcomexec.py (different DCOM object, avoids WMI-specific detection)
Fallback2: Native PowerShell CIM (blends with admin activity)
Fallback3: smbexec.py (uses SMB service, noisier but reliable)
```
