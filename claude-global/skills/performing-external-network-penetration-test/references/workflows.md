# Workflows ÔÇö External Network Penetration Testing

## End-to-End Workflow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Pre-Engagement   ÔöéÔöÇÔöÇÔöÇ>Ôöé  Reconnaissance   ÔöéÔöÇÔöÇÔöÇ>Ôöé Vulnerability        Ôöé
Ôöé - Scoping        Ôöé    Ôöé  - Passive OSINT  Ôöé    Ôöé Analysis             Ôöé
Ôöé - RoE signing    Ôöé    Ôöé  - Active scanningÔöé    Ôöé - Automated scans    Ôöé
Ôöé - Legal docs     Ôöé    Ôöé  - Enum subdomainsÔöé    Ôöé - Manual validation  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                                          Ôöé
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé   Reporting      Ôöé<ÔöÇÔöÇÔöÇÔöé Post-Exploitation Ôöé<ÔöÇÔöÇÔöÇÔöé   Exploitation       Ôöé
Ôöé - Findings doc   Ôöé    Ôöé  - Priv escalationÔöé    Ôöé - Service exploits   Ôöé
Ôöé - CVSS scoring   Ôöé    Ôöé  - Persistence    Ôöé    Ôöé - Web app attacks    Ôöé
Ôöé - Remediation    Ôöé    Ôöé  - Pivoting proof  Ôöé    Ôöé - Password attacks   Ôöé
Ôöé - Executive briefÔöé    Ôöé  - Evidence gather Ôöé    Ôöé - Credential spray   Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Daily Testing Workflow

```
Morning:
  1. Review previous day's findings
  2. Update target list with new discoveries
  3. Run updated scans on newly discovered hosts
  4. Verify scan results and triage

Afternoon:
  5. Manual exploitation of high-value targets
  6. Attempt lateral movement from compromised hosts
  7. Document all successful and failed exploitation attempts

Evening:
  8. Compile evidence and screenshots
  9. Update findings tracker
  10. Plan next day's attack vectors
  11. Communicate critical findings to client immediately
```

## Reconnaissance Sub-Workflow

```
Domain Target
    Ôöé
    Ôö£ÔöÇÔöÇ DNS Enumeration ÔöÇÔöÇ> Subdomain Discovery ÔöÇÔöÇ> IP Resolution
    Ôöé                                                    Ôöé
    Ôö£ÔöÇÔöÇ WHOIS/ASN Lookup ÔöÇÔöÇ> IP Range Identification ÔöÇÔöÇÔöÇÔöÇÔöñ
    Ôöé                                                    Ôöé
    Ôö£ÔöÇÔöÇ Certificate Transparency ÔöÇÔöÇ> Hidden Subdomains ÔöÇÔöÇÔöñ
    Ôöé                                                    Ôöé
    Ôö£ÔöÇÔöÇ Shodan/Censys ÔöÇÔöÇ> Service Fingerprinting ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ
    Ôöé                                                    Ôöé
    ÔööÔöÇÔöÇ OSINT (GitHub, Pastebin) ÔöÇÔöÇ> Credential Leaks    Ôöé
                                                         Ôû╝
                                              Master Target List
                                           (IPs, Ports, Services)
```

## Vulnerability Triage Workflow

```
Scan Results
    Ôöé
    Ôö£ÔöÇÔöÇ Critical (CVSS >= 9.0) ÔöÇÔöÇ> Immediate exploitation attempt
    Ôöé                               ÔöÇÔöÇ> Notify client if RCE confirmed
    Ôöé
    Ôö£ÔöÇÔöÇ High (CVSS 7.0-8.9) ÔöÇÔöÇ> Validate and exploit within 24h
    Ôöé
    Ôö£ÔöÇÔöÇ Medium (CVSS 4.0-6.9) ÔöÇÔöÇ> Validate, exploit if time permits
    Ôöé
    ÔööÔöÇÔöÇ Low/Info (CVSS < 4.0) ÔöÇÔöÇ> Document, include in final report
```

## Evidence Collection Workflow

```
For each successful exploitation:
  1. Screenshot the exploit execution
  2. Record terminal output (script command or asciinema)
  3. Capture network traffic (tcpdump/Wireshark)
  4. Document exact commands/payloads used
  5. Note timestamps (UTC)
  6. Hash any files extracted (SHA-256)
  7. Store evidence in organized folder structure:
     evidence/
     Ôö£ÔöÇÔöÇ {date}/
     Ôöé   Ôö£ÔöÇÔöÇ {target-ip}/
     Ôöé   Ôöé   Ôö£ÔöÇÔöÇ screenshots/
     Ôöé   Ôöé   Ôö£ÔöÇÔöÇ terminal_logs/
     Ôöé   Ôöé   Ôö£ÔöÇÔöÇ pcaps/
     Ôöé   Ôöé   ÔööÔöÇÔöÇ notes.md
```
