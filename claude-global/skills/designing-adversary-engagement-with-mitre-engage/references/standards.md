# MITRE Engage ÔÇö Standards & Framework Reference

## Primary framework
### MITRE EngageÔäó v1.0
- **Publisher**: The MITRE Corporation
- **Version**: 1.0, last updated 2022-02-28
- **Home**: https://engage.mitre.org
- **Live Matrix**: https://engage.mitre.org/matrix/ (authoritative source for all Goal/Approach/Activity names and IDs)
- **Starter Kit**: https://engage.mitre.org/starter-kit/ (10-Step Process, planning worksheets, whitepapers)
- **Predecessor**: MITRE Shield (Engage supersedes and restructures Shield).
- **Note**: Engage is a framework for *planning and discussing* denial, deception, and adversary engagement. It is not a tool; it provides a shared language across defenders, vendors, and decision-makers.

## Engage Matrix structure
Five columns (Goals): **Prepare ┬À Expose ┬À Affect ┬À Elicit ┬À Understand**
- **Prepare** and **Understand** are *strategic* bookends (operation inputs and outputs).
- **Expose**, **Affect**, **Elicit** are the three *Engagement* goals; together they form the default **Operate** view and are mapped to MITRE ATT&CK.

### ID prefixes (verified from engage.mitre.org)
| Component | Strategic prefix | Engagement prefix |
|---|---|---|
| Goals | SGO | EGO |
| Approaches | SAP | EAP |
| Activities | SAC | EAC |

Always resolve specific numeric IDs (e.g., the EAC for "Decoy Credentials") against the live matrix rather than from memory.

### Engagement Approaches (EAP) by Goal
- **Expose** ÔåÆ Collection, Detection
- **Affect** ÔåÆ Prevention, Direction, Disruption
- **Elicit** ÔåÆ Reassurance, Motivation

### Representative Engagement Activities (EAC), by name
Decoy Credentials ┬À Decoy Content ┬À Decoy Account ┬À Decoy Diversity ┬À Lures ┬À Pocket Litter ┬À
Persona Creation ┬À Artifact Diversity ┬À Network Diversity ┬À Application Diversity ┬À
Email Manipulation ┬À Network Manipulation ┬À Software Manipulation ┬À Hardware Manipulation ┬À
Security Controls ┬À Isolation ┬À Attack Vector Migration ┬À Peripheral Management ┬À Baseline ┬À
Network Monitoring ┬À System Activity Monitoring ┬À API Monitoring ┬À Malware Detonation ┬À
Burn-In ┬À Introduced Vulnerabilities.

> The matrix maps each Activity to the ATT&CK techniques whose execution exposes an adversary weakness. Use the Navigator overlay to confirm current mappings.

## Operating principle: Affect is defender-network-only
All Affect Activities are constrained to infrastructure the defender owns and controls. Acting on adversary or third-party infrastructure is out of scope and creates legal exposure.

## Complementary frameworks

### MITRE ATT&CK
- https://attack.mitre.org ÔÇö the technique catalog used to model the target adversary. Engagement Activities exist to exploit the weaknesses adversary techniques create.

### MITRE D3FEND ÔÇö `Deceive` tactic
D3FEND (https://d3fend.mitre.org) provides defensive-technique naming that pairs with Engage. The `Deceive` tactic includes:
- **Decoy Environment**: Connected Honeynet, Integrated Honeynet, Standalone Honeynet
- **Decoy Object**: Decoy File, Decoy Network Resource, Decoy Persona, Decoy Public Release, Decoy Session Token, Decoy User Credential

Use D3FEND honeynet types when documenting environment isolation in the operation plan:
- **Standalone Honeynet** ÔÇö fully isolated; safest; least realistic to a sophisticated adversary.
- **Connected Honeynet** ÔÇö bridged to production paths to appear reachable; moderate risk.
- **Integrated Honeynet** ÔÇö decoys interleaved with production assets; most realistic; highest operational risk and tightest gating required.

## NIST CSF 2.0 alignment
| CSF 2.0 ID | Relevance to adversary engagement |
|---|---|
| GV.RM-01 | Risk management objectives established ÔÇö anchors the strategic Prepare goal |
| ID.RA-01 | Vulnerabilities identified ÔÇö informs which weaknesses to expose |
| ID.IM-02 | Security testing / improvement ÔÇö engagement operations validate detections |
| DE.CM-01 | Networks monitored to find adverse events ÔÇö Expose Activities feed monitoring |
| DE.AE-02 | Potentially adverse events analyzed ÔÇö triage of decoy alerts |

## Legal & ethical references
- Engagement operations interact with live adversaries; obtain written legal review before deployment.
- Preserve evidence per the organization's incident-response and forensics procedures (chain of custody).
- Coordinate with law enforcement engagement policy where applicable.
- Document rules of engagement and gating criteria before any Activity is deployed.
