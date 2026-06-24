# Workflows: Full-Scope Red Team Engagement

## Engagement Lifecycle Workflow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé                    RED TEAM ENGAGEMENT LIFECYCLE                  Ôöé
Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ
Ôöé                                                                  Ôöé
Ôöé  1. SCOPING & PLANNING                                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Define Rules of Engagement (RoE)                         Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Identify threat actors to emulate                        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Define objectives and success criteria                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Establish communication channels and emergency stops     Ôöé
Ôöé     ÔööÔöÇÔöÇ Legal authorization and sign-off                         Ôöé
Ôöé                                                                  Ôöé
Ôöé  2. RECONNAISSANCE (2-4 weeks)                                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Passive OSINT collection                                 Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ DNS enumeration (Amass, subfinder)                   Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Email harvesting (theHarvester)                      Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Social media profiling (LinkedIn, Twitter)           Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Credential breach searches (DeHashed)                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Active scanning (if in scope)                            Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Port/service scanning (Nmap)                         Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Web application discovery (Aquatone)                 Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Vulnerability scanning (Nuclei)                      Ôöé
Ôöé     ÔööÔöÇÔöÇ Target prioritization matrix                             Ôöé
Ôöé                                                                  Ôöé
Ôöé  3. WEAPONIZATION (1-2 weeks)                                    Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Develop custom payloads                                  Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Shellcode generation and encryption                  Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Loader development (C/C++, Rust, Nim)                Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Sandbox evasion techniques                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Configure C2 infrastructure                              Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Deploy team server (Havoc/Cobalt Strike)             Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Set up HTTPS redirectors                             Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Configure domain fronting or CDN                     Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Test beacon callbacks                                Ôöé
Ôöé     ÔööÔöÇÔöÇ Prepare phishing infrastructure                          Ôöé
Ôöé         Ôö£ÔöÇÔöÇ Register look-alike domains                          Ôöé
Ôöé         Ôö£ÔöÇÔöÇ Configure SPF/DKIM/DMARC                             Ôöé
Ôöé         ÔööÔöÇÔöÇ Design email templates                               Ôöé
Ôöé                                                                  Ôöé
Ôöé  4. INITIAL ACCESS (1-2 weeks)                                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Execute phishing campaign (T1566)                        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Exploit external services (T1190)                        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Credential stuffing/spraying (T1110)                     Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Supply chain vectors (T1195)                             Ôöé
Ôöé     ÔööÔöÇÔöÇ Physical access attempts (if in scope)                   Ôöé
Ôöé                                                                  Ôöé
Ôöé  5. POST-EXPLOITATION (2-4 weeks)                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Establish persistence (T1053, T1547)                     Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Privilege escalation                                     Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Local priv esc (T1068, T1548)                        Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Domain priv esc (Kerberoasting, DCSync)              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Credential harvesting                                    Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ LSASS dump (T1003.001)                               Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ SAM database (T1003.002)                             Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Kerberos tickets (T1558)                             Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Lateral movement                                         Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ SMB (T1021.002)                                      Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ WMI (T1047)                                          Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ WinRM (T1021.006)                                    Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ RDP (T1021.001)                                      Ôöé
Ôöé     ÔööÔöÇÔöÇ Objective pursuit                                        Ôöé
Ôöé         Ôö£ÔöÇÔöÇ Crown jewel identification                           Ôöé
Ôöé         Ôö£ÔöÇÔöÇ Data staging (T1074)                                 Ôöé
Ôöé         ÔööÔöÇÔöÇ Exfiltration demonstration (T1041)                   Ôöé
Ôöé                                                                  Ôöé
Ôöé  6. REPORTING & DEBRIEF (1-2 weeks)                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Attack narrative with timeline                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ MITRE ATT&CK heat map                                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Detection gap analysis                                   Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Remediation recommendations                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Executive debrief presentation                           Ôöé
Ôöé     ÔööÔöÇÔöÇ Purple team follow-up sessions                           Ôöé
Ôöé                                                                  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Decision Tree: Initial Access Vector Selection

```
START: Select Initial Access Vector
Ôöé
Ôö£ÔöÇÔöÇ Is phishing in scope?
Ôöé   Ôö£ÔöÇÔöÇ YES ÔåÆ Target high-value employees
Ôöé   Ôöé         Ôö£ÔöÇÔöÇ C-suite ÔåÆ CEO fraud / whale phishing
Ôöé   Ôöé         Ôö£ÔöÇÔöÇ IT Staff ÔåÆ Credential harvesting
Ôöé   Ôöé         ÔööÔöÇÔöÇ HR/Finance ÔåÆ Malicious attachment
Ôöé   ÔööÔöÇÔöÇ NO ÔåÆ Proceed to external attack surface
Ôöé
Ôö£ÔöÇÔöÇ External-facing services found?
Ôöé   Ôö£ÔöÇÔöÇ VPN ÔåÆ Check for CVEs (Fortinet, Pulse Secure, Citrix)
Ôöé   Ôö£ÔöÇÔöÇ Exchange ÔåÆ ProxyShell/ProxyLogon
Ôöé   Ôö£ÔöÇÔöÇ Web Apps ÔåÆ OWASP Top 10, file upload, RCE
Ôöé   ÔööÔöÇÔöÇ RDP ÔåÆ Brute force / credential stuffing
Ôöé
ÔööÔöÇÔöÇ Physical access in scope?
    Ôö£ÔöÇÔöÇ Badge cloning (Proxmark3)
    Ôö£ÔöÇÔöÇ Tailgating
    ÔööÔöÇÔöÇ Rogue device deployment (LAN Turtle)
```

## Operational Security (OPSEC) Checklist

1. **Infrastructure Separation**: Separate attack infrastructure from assessment infrastructure
2. **Redirectors**: Use HTTPS redirectors between C2 and targets
3. **Domain Aging**: Register domains 30+ days before engagement
4. **Categorization**: Categorize phishing domains before use (Bluecoat, Fortiguard)
5. **Payload Testing**: Test payloads against VirusTotal alternatives (antiscan.me)
6. **Log Rotation**: Rotate and encrypt operational logs
7. **Clean-up**: Remove all implants and artifacts post-engagement
8. **Communication**: Use encrypted channels for team coordination (Signal, Keybase)

## TTPs Execution Checklist

| Phase | TTP | Tool | Status |
|---|---|---|---|
| Recon | T1593 - Open Website Search | Amass, Recon-ng | [ ] |
| Recon | T1589 - Victim Identity Info | theHarvester, LinkedIn | [ ] |
| Initial Access | T1566.001 - Spearphishing | GoPhish, custom | [ ] |
| Execution | T1059.001 - PowerShell | Custom stager | [ ] |
| Persistence | T1053.005 - Scheduled Task | schtasks.exe | [ ] |
| Priv Esc | T1558.003 - Kerberoasting | Rubeus | [ ] |
| Defense Evasion | T1055 - Process Injection | Custom loader | [ ] |
| Credential Access | T1003.001 - LSASS Memory | Mimikatz/SafetyKatz | [ ] |
| Discovery | T1087.002 - Domain Account Discovery | BloodHound/SharpHound | [ ] |
| Lateral Movement | T1021.002 - SMB/Admin Shares | PsExec, wmiexec | [ ] |
| Collection | T1560 - Archive Data | 7-Zip, tar | [ ] |
| Exfiltration | T1041 - Exfil Over C2 | Havoc/CS download | [ ] |
