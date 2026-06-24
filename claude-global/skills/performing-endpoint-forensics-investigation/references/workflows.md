# Workflows

## Workflow 1: Endpoint Forensic Investigation

```
[Incident Detected / Investigation Authorized]
    Ôöé
    Ôû╝
[Preserve Evidence (Order of Volatility)]
    Ôöé
    Ôö£ÔöÇÔöÇ 1. Capture memory (WinPMEM/FTK Imager)
    Ôö£ÔöÇÔöÇ 2. Capture volatile data (processes, network, users)
    Ôö£ÔöÇÔöÇ 3. Create forensic disk image (E01/dd)
    Ôö£ÔöÇÔöÇ 4. Hash all evidence, document chain of custody
    Ôöé
    Ôû╝
[Analysis Phase]
    Ôöé
    Ôö£ÔöÇÔöÇ Memory analysis (Volatility 3)
    Ôö£ÔöÇÔöÇ Artifact parsing (KAPE + EZ tools)
    Ôö£ÔöÇÔöÇ Timeline reconstruction (plaso)
    Ôö£ÔöÇÔöÇ Malware analysis (if samples found)
    Ôöé
    Ôû╝
[Correlate Findings]
    Ôöé
    Ôö£ÔöÇÔöÇ Initial access vector identified
    Ôö£ÔöÇÔöÇ Persistence mechanisms documented
    Ôö£ÔöÇÔöÇ Scope of compromise determined
    Ôöé
    Ôû╝
[Generate IOCs and Report]
    Ôöé
    Ôû╝
[Handoff to Remediation Team]
```

## Workflow 2: Memory Analysis

```
[Memory dump acquired]
    Ôöé
    Ôû╝
[Identify OS profile: vol windows.info]
    Ôöé
    Ôû╝
[Process analysis: pslist ÔåÆ pstree ÔåÆ psscan]
    Ôöé
    Ôö£ÔöÇÔöÇ Hidden processes found ÔöÇÔöÇÔû║ [Analyze with malfind, dlllist]
    Ôöé
    Ôû╝
[Network analysis: netscan]
    Ôöé
    Ôö£ÔöÇÔöÇ Suspicious connections ÔöÇÔöÇÔû║ [Extract IOCs (IPs, domains)]
    Ôöé
    Ôû╝
[Injection detection: malfind]
    Ôöé
    Ôö£ÔöÇÔöÇ Injected code found ÔöÇÔöÇÔû║ [Dump and analyze with YARA]
    Ôöé
    Ôû╝
[Credential analysis: hashdump, lsadump]
    Ôöé
    Ôû╝
[Document all findings with screenshots and hashes]
```
