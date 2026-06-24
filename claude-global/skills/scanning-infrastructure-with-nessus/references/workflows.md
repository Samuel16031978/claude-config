# Workflows - Scanning Infrastructure with Nessus

## Workflow 1: Initial Infrastructure Assessment

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé  Asset Discovery ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé  Policy Creation ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé  Credential Config Ôöé
Ôöé  (Host Enum)     Ôöé     Ôöé  (Custom/Default)Ôöé     Ôöé  (SSH/WinRM/SNMP)  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                                          Ôöé
        ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé   Launch Scan    ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé  Monitor Status  ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé   Export Results   Ôöé
Ôöé   (On-Demand)    Ôöé     Ôöé  (API Polling)   Ôöé     Ôöé   (CSV/HTML/PDF)   Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                                          Ôöé
        ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
        v
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Analyze Findings ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé Prioritize Vulns ÔöéÔöÇÔöÇÔöÇÔöÇ>Ôöé  Create Tickets    Ôöé
Ôöé (Severity/CVSS)  Ôöé     Ôöé (Risk-Based)     Ôöé     Ôöé  (Jira/ServiceNow) Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Workflow 2: Recurring Scheduled Scanning

1. **Weekly**: Scan DMZ and internet-facing assets
2. **Bi-weekly**: Scan internal production servers
3. **Monthly**: Full infrastructure scan including workstations
4. **Quarterly**: Comprehensive scan with compliance audits
5. **Ad-hoc**: Post-patch verification scans

## Workflow 3: Scan Result Processing Pipeline

```
Nessus Export (.nessus XML)
    Ôöé
    Ôö£ÔöÇÔöÇ> Parse with Python (xml.etree / defusedxml)
    Ôöé        Ôöé
    Ôöé        Ôö£ÔöÇÔöÇ> Filter by severity (Critical/High)
    Ôöé        Ôö£ÔöÇÔöÇ> Deduplicate findings across hosts
    Ôöé        Ôö£ÔöÇÔöÇ> Enrich with EPSS scores
    Ôöé        ÔööÔöÇÔöÇ> Map to MITRE ATT&CK techniques
    Ôöé
    Ôö£ÔöÇÔöÇ> Import to Vulnerability Management Platform
    Ôöé        Ôöé
    Ôöé        Ôö£ÔöÇÔöÇ> Tenable.sc / Tenable.io
    Ôöé        Ôö£ÔöÇÔöÇ> DefectDojo
    Ôöé        ÔööÔöÇÔöÇ> Faraday
    Ôöé
    ÔööÔöÇÔöÇ> Generate Executive Report
             Ôöé
             Ôö£ÔöÇÔöÇ> Vulnerability count by severity
             Ôö£ÔöÇÔöÇ> Top 10 most critical findings
             Ôö£ÔöÇÔöÇ> Remediation progress trending
             ÔööÔöÇÔöÇ> Risk score by business unit
```

## Workflow 4: API Automation Flow

```python
# Nessus API Workflow Steps:
# 1. POST /session -> Get auth token
# 2. GET /editor/scan/templates -> List available templates
# 3. POST /scans -> Create scan with template UUID
# 4. POST /scans/{id}/launch -> Start the scan
# 5. GET /scans/{id} -> Poll until status == "completed"
# 6. POST /scans/{id}/export -> Request export (format: nessus/csv/html)
# 7. GET /scans/{id}/export/{file_id}/status -> Poll export status
# 8. GET /scans/{id}/export/{file_id}/download -> Download results
# 9. DELETE /session -> Logout
```

## Workflow 5: Multi-Scanner Coordination

For large enterprises with multiple Nessus scanners:

1. **Central Management**: Use Tenable.sc to manage multiple scanners
2. **Zone Assignment**: Assign scanners to specific network zones
3. **Scan Windowing**: Stagger scans to prevent network saturation
4. **Result Aggregation**: Consolidate results in central repository
5. **Deduplication**: Merge findings from overlapping scan ranges
