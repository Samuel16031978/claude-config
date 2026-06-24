# Workflows: BloodHound AD Analysis

## BloodHound Analysis Workflow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé              BLOODHOUND ANALYSIS WORKFLOW                         Ôöé
Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ
Ôöé                                                                  Ôöé
Ôöé  1. DATA COLLECTION                                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Select collector (SharpHound/AzureHound)                 Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Choose collection method                                 Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ All (comprehensive, noisy)                           Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ DCOnly (LDAP only, stealthier)                       Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Session (user sessions on computers)                 Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ ACL (permission relationships)                       Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Execute collection                                       Ôöé
Ôöé     ÔööÔöÇÔöÇ Exfiltrate ZIP to analysis workstation                   Ôöé
Ôöé                                                                  Ôöé
Ôöé  2. DATA IMPORT                                                  Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Start BloodHound CE/Neo4j                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Upload collection ZIP                                    Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Verify node counts (Users, Computers, Groups)            Ôöé
Ôöé     ÔööÔöÇÔöÇ Mark owned principals and high-value targets             Ôöé
Ôöé                                                                  Ôöé
Ôöé  3. INITIAL ANALYSIS                                             Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Run pre-built analytics                                  Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Find all Domain Admins                               Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Find Kerberoastable accounts                         Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Find AS-REP Roastable accounts                       Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Find unconstrained delegation                        Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Find shortest paths to DA                            Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Identify high-value targets                              Ôöé
Ôöé     ÔööÔöÇÔöÇ Document initial findings                                Ôöé
Ôöé                                                                  Ôöé
Ôöé  4. ATTACK PATH IDENTIFICATION                                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Mark owned nodes                                         Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Shortest path from owned to DA                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Analyze ACL abuse paths                                  Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ GenericAll / GenericWrite                             Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ WriteDACL / WriteOwner                               Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ ForceChangePassword                                  Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ AddMember                                            Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Analyze delegation abuse                                 Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Analyze GPO abuse paths                                  Ôöé
Ôöé     ÔööÔöÇÔöÇ Prioritize attack paths by feasibility                   Ôöé
Ôöé                                                                  Ôöé
Ôöé  5. EXPLOITATION                                                 Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Execute selected attack path                             Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Kerberoast service accounts                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Abuse ACL misconfigurations                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Leverage delegation settings                             Ôöé
Ôöé     ÔööÔöÇÔöÇ Mark newly owned principals                              Ôöé
Ôöé                                                                  Ôöé
Ôöé  6. REPORTING                                                    Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Export attack path screenshots                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Document each hop in attack chain                        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Map to MITRE ATT&CK techniques                          Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Provide remediation for each finding                     Ôöé
Ôöé     ÔööÔöÇÔöÇ Generate AD hardening recommendations                    Ôöé
Ôöé                                                                  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## SharpHound Collection Method Selection

```
Collection Method Decision
Ôöé
Ôö£ÔöÇÔöÇ Need comprehensive data?
Ôöé   ÔööÔöÇÔöÇ Use -c All (Collects everything)
Ôöé       Warning: Noisy, generates LDAP and SMB traffic
Ôöé
Ôö£ÔöÇÔöÇ Need stealth?
Ôöé   ÔööÔöÇÔöÇ Use -c DCOnly (Queries only DCs via LDAP)
Ôöé       Limitation: No session or local group data
Ôöé
Ôö£ÔöÇÔöÇ Need session data over time?
Ôöé   ÔööÔöÇÔöÇ Use -c Session --loop
Ôöé       Best for: Finding where admins are logged in
Ôöé
Ôö£ÔöÇÔöÇ Azure AD environment?
Ôöé   ÔööÔöÇÔöÇ Use AzureHound
Ôöé       Collects: Roles, App Registrations, Service Principals
Ôöé
ÔööÔöÇÔöÇ Minimal footprint needed?
    ÔööÔöÇÔöÇ Use -c Group,ACL
        Collects: Group memberships and ACL relationships only
```

## Attack Path Exploitation Decision Tree

```
BloodHound Shows Path to DA
Ôöé
Ôö£ÔöÇÔöÇ Path via Kerberoastable account?
Ôöé   Ôö£ÔöÇÔöÇ Request TGS ticket (Rubeus/GetUserSPNs)
Ôöé   Ôö£ÔöÇÔöÇ Crack with hashcat (-m 13100)
Ôöé   ÔööÔöÇÔöÇ Use cracked credential to continue path
Ôöé
Ôö£ÔöÇÔöÇ Path via ACL abuse?
Ôöé   Ôö£ÔöÇÔöÇ GenericAll on user? ÔåÆ ForceChangePassword
Ôöé   Ôö£ÔöÇÔöÇ GenericAll on group? ÔåÆ Add self to group
Ôöé   Ôö£ÔöÇÔöÇ WriteDACL? ÔåÆ Grant self GenericAll, then abuse
Ôöé   Ôö£ÔöÇÔöÇ WriteOwner? ÔåÆ Change owner, then modify DACL
Ôöé   ÔööÔöÇÔöÇ AddMember? ÔåÆ Add self to privileged group
Ôöé
Ôö£ÔöÇÔöÇ Path via delegation?
Ôöé   Ôö£ÔöÇÔöÇ Unconstrained? ÔåÆ Coerce DC auth + capture TGT
Ôöé   Ôö£ÔöÇÔöÇ Constrained? ÔåÆ S4U2Self + S4U2Proxy abuse
Ôöé   ÔööÔöÇÔöÇ RBCD? ÔåÆ Configure msDS-AllowedToActOnBehalf
Ôöé
Ôö£ÔöÇÔöÇ Path via GPO?
Ôöé   Ôö£ÔöÇÔöÇ GenericWrite on GPO? ÔåÆ Add scheduled task
Ôöé   ÔööÔöÇÔöÇ GpLink control? ÔåÆ Link malicious GPO to OU
Ôöé
ÔööÔöÇÔöÇ Path via session?
    Ôö£ÔöÇÔöÇ Admin on computer with DA session?
    Ôö£ÔöÇÔöÇ Dump LSASS for DA credentials
    ÔööÔöÇÔöÇ Or steal token/ticket
```

## BloodHound Edge Reference

| Edge Type | Meaning | Abuse Method |
|---|---|---|
| MemberOf | Group membership | Inherit group permissions |
| AdminTo | Local admin rights | PsExec, WMI, WinRM |
| HasSession | User logged in | Credential theft |
| GenericAll | Full control | Reset password, modify object |
| GenericWrite | Write properties | Set SPN, modify attributes |
| WriteDacl | Modify permissions | Grant self full control |
| WriteOwner | Change owner | Take ownership then WriteDacl |
| ForceChangePassword | Reset password | Change user password |
| AddMember | Add to group | Add self to privileged group |
| AllowedToDelegate | Constrained delegation | S4U2Proxy abuse |
| AllowedToAct | RBCD | Resource-based constrained delegation |
| CanRDP | RDP access | Remote desktop connection |
| CanPSRemote | WinRM access | PowerShell remoting |
| ExecuteDCOM | DCOM execution | Remote code execution |
| GPLink | GPO linked to OU | Modify GPO for code execution |
