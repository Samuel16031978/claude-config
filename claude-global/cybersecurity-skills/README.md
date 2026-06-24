<p align="center">
  <img src="assets/banner.png" alt="Anthropic Cybersecurity Skills" width="100%">
</p>

<div align="center">

#  Anthropic Cybersecurity Skills

### The largest open-source cybersecurity skills library for AI agents

[![GARS-2026 Survey](https://img.shields.io/badge/GARS--2026-Take%20the%20Survey-E8B84B?style=for-the-badge&logo=googleforms&logoColor=black)](https://mahipal.engineer/survey?utm_source=github_badge&utm_medium=readme&utm_campaign=gars2026)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-817-brightgreen?style=flat-square)](#whats-inside--29-security-domains)
[![Frameworks](https://img.shields.io/badge/frameworks-6-orange?style=flat-square)](#six-frameworks-one-skill-library)
[![MITRE F3](https://img.shields.io/badge/MITRE-F3_v1.1-blue?style=flat-square)](https://ctid.mitre.org/fraud/)
[![Domains](https://img.shields.io/badge/domains-29-9cf?style=flat-square)](#whats-inside--29-security-domains)
[![Platforms](https://img.shields.io/badge/platforms-26%2B-blueviolet?style=flat-square)](#compatible-platforms)
[![GitHub stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/commits/main)
[![agentskills.io](https://img.shields.io/badge/standard-agentskills.io-ff6600?style=flat-square)](https://agentskills.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Playground](https://img.shields.io/badge/Playground-Casky.ai-blue)](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-compatible-blueviolet?style=flat)](https://github.com/NousResearch/hermes-agent)


**817 production-grade cybersecurity skills ┬À 29 security domains ┬À 6 framework mappings ┬À 26+ AI platforms**

[Get Started](#quick-start) ┬À [What's Inside](#whats-inside--29-security-domains) ┬À [Frameworks](#five-frameworks-one-skill-library) ┬À [Platforms](#compatible-platforms) ┬À [Contributing](#contributing)

</div>

---

> ÔÜá´©Å **Community Project** ÔÇö This is an independent, community-created project. Not affiliated with Anthropic PBC. 

## Give any AI agent the security skills of a senior analyst

A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't ÔÇö unless you give it these skills.**

This repo contains **817 structured cybersecurity skills** spanning **29 security domains**, each following the [agentskills.io](https://agentskills.io) open standard.  Every skill is mapped to **six industry frameworks** ÔÇö MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework (F3) ÔÇö making this the only open-source skills library with unified cross-framework coverage.  Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.

## Six frameworks, one skill library

No other open-source skills library maps every skill to all of these frameworks.  One skill, six compliance checkboxes. 

| Framework | Version | Scope in this repo | What it maps |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org) | v19.1 | 15 tactics ┬À 286 techniques | Adversary behaviors and TTPs |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions ┬À 22 categories | Organizational security posture |
| [MITRE ATLAS](https://atlas.mitre.org) | v5.4 | 16 tactics ┬À 84 techniques | AI/ML adversarial threats |
| [MITRE D3FEND](https://d3fend.mitre.org) | v1.3 | 7 categories ┬À 267 techniques | Defensive countermeasures |
| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions ┬À 72 subcategories | AI risk management |
| [MITRE F3 (Fight Fraud Framework)](https://ctid.mitre.org/fraud/) | v1.1 (2026-04-09) | 8 tactics ┬À 123 techniques ┬À 94 fraud-relevant skills | Cyber-enabled financial fraud TTPs |

**Example ÔÇö a single skill maps across all six:**

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF | F3 |
|---|---|---|---|---|---|---|
| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 | ÔÇö |
| `detecting-business-email-compromise` | T1566 | DE.AE | ÔÇö | ÔÇö | ÔÇö | F1005.006 ┬À monetization |

### ­ƒåò MITRE Fight Fraud Framework (F3) ÔÇö 94 fraud-relevant skills

[![MITRE F3](https://img.shields.io/badge/MITRE-F3_v1.1-blue?style=flat-square)](https://ctid.mitre.org/fraud/)

The **[MITRE Fight Fraud Framework (F3)](https://ctid.mitre.org/fraud/)** was released **April 9, 2026** by MITRE's Center for Threat-Informed Defense (CTID), co-developed with JPMorganChase, Citigroup, Lloyds Banking Group, Standard Chartered, CrowdStrike, Verizon Business, FS-ISAC, and others. It is an ATT&CK-compatible TTP catalog for **cyber-enabled financial fraud** ÔÇö filling the gap ATT&CK leaves after initial compromise.

F3 v1.1 adds **two fraud-specific tactics** that ATT&CK does not enumerate:
- **Positioning** (`FA0001`) ÔÇö actions taken after access to collect/manipulate data and prepare the fraud (synthetic-identity seeding, account warming, beneficiary setup, SIM-swap pre-positioning, banking-session hijack).
- **Monetization** (`FA0002`) ÔÇö converting stolen assets into usable funds (money-mule layering, APP fraud, crypto off-ramping, card cash-out, refund/chargeback abuse).

Fraud-specific techniques use `F1XXX` IDs (e.g. `F1005.003` Add Beneficiary, `F1025.003` Wire Transfer, `F1007` Adversary-in-the-Browser); reused ATT&CK techniques keep their `T1XXX` IDs. Mappings live in each skill's `mitre_f3:` frontmatter block ÔÇö all 123 F3 v1.1 technique IDs were verified against the upstream STIX bundle. See [`docs/mitre-f3-mapping.md`](docs/mitre-f3-mapping.md) for the schema.

### MITRE ATT&CK v19.1 ÔÇö 754/754 skills mapped

Every skill carries a `mitre_attack` frontmatter list validated against **MITRE ATT&CK v19.1** (the latest release) using the official `mitreattack-python` library ÔÇö 286 distinct techniques across all 15 Enterprise tactics, plus ICS and Mobile techniques where relevant. Zero revoked or deprecated IDs. v19.1's restructured Defense Evasion (now split into **Stealth** and **Defense Impairment**) is reflected below.

| Tactic | ID | Skills |
|--------|----|--------|
| Reconnaissance | TA0043 | 103 |
| Resource Development | TA0042 | 22 |
| Initial Access | TA0001 | 467 |
| Execution | TA0002 | 350 |
| Persistence | TA0003 | 444 |
| Privilege Escalation | TA0004 | 464 |
| Stealth | TA0005 | 442 |
| Defense Impairment | TA0112 | 92 |
| Credential Access | TA0006 | 202 |
| Discovery | TA0007 | 237 |
| Lateral Movement | TA0008 | 68 |
| Collection | TA0009 | 172 |
| Command and Control | TA0011 | 123 |
| Exfiltration | TA0010 | 82 |
| Impact | TA0040 | 50 |

## Quick start

```bash
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Works immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any [agentskills.io](https://agentskills.io)-compatible platform. 

## ­ƒîì GARS-2026 ÔÇö Global Agentic AI Readiness Survey

I'm running a global academic study measuring how ready security professionals,
developers, and enterprise teams actually are for agentic AI ÔÇö MCP servers,
tool calling, governance, and human-in-the-loop workflows.

**If you use this repo, your response would be a genuinely valuable data point.**

­ƒôï **Take the survey (10 min):**
[Survey Link](https://mahipal.engineer/survey?utm_source=github_repo&utm_medium=readme&utm_campaign=gars2026)

- 60 questions ┬À Anonymous ┬À Supervised by SRH Berlin
- You get **50 Casky Tokens** for early access to [casky.ai](https://casky.ai)
- Results published open access under CC-BY 4.0

## ­ƒÜÇ Try it on the Playground

Experience Casky.ai hands-on ÔÇö no setup required.

**[ÔåÆ Launch Playground on Casky.ai](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)**

The playground lets you:
- Run live cybersecurity skill exercises against real targets
- See AI agents execute structured skills in real time
- Explore MITRE ATT&CK mapped workflows interactively
- Test threat hunting, DFIR, and penetration testing scenarios

No installation. No configuration. Just open and start.
## Why this exists

The cybersecurity workforce gap hit **4.8 million unfilled roles** globally in 2024 (ISC2). AI agents can help close that gap ÔÇö but only if they have structured domain knowledge to work from. Today's agents can write code and search the web, but they lack the practitioner playbooks that turn a generic LLM into a capable security analyst.

Existing security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows: when to use each technique, what prerequisites to check, how to execute step-by-step, and how to verify results. That is the gap this project fills.

**Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** built from the ground up for the agentskills.io standard  ÔÇö YAML frontmatter for sub-second discovery, structured Markdown for step-by-step execution, and reference files for deep technical context.  Every skill encodes real practitioner workflows, not generated summaries. 

## What's inside ÔÇö 29 security domains

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 66 | AWS, Azure, GCP hardening ┬À CSPM ┬À cloud attack emulation ┬À cloud forensics |
| Threat Hunting | 58 | Hypothesis-driven hunts ┬À LOTL detection ┬À EVTX hunting ┬À fleet hunting |
| Threat Intelligence | 52 | STIX/TAXII ┬À MISP ┬À OpenCTI ┬À feed integration ┬À actor profiling |
| Network Security | 43 | IDS/IPS ┬À firewall rules ┬À VLAN segmentation ┬À traffic analysis |
| Web Application Security | 42 | OWASP Top 10 ┬À SQLi ┬À XSS ┬À SSRF ┬À deserialization |
| Digital Forensics | 41 | Disk imaging ┬À memory forensics ┬À Hayabusa/KAPE/Plaso timelines |
| Malware Analysis | 39 | Static/dynamic analysis ┬À reverse engineering ┬À sandboxing |
| Identity & Access Management | 37 | Entra ID/ROADtools ┬À device-code phishing ┬À PAM ┬À zero trust identity |
| SOC Operations | 35 | Playbooks ┬À escalation workflows ┬À Graph-log detection ┬À tabletop exercises |
| Red Teaming | 33 | ADCS/Certipy ┬À BloodHound CE ┬À Sliver/Havoc C2 ┬À NTLM relay |
| Container Security | 33 | K8s RBAC ┬À image scanning ┬À Falco ┬À container escape |
| Security Operations | 28 | SIEM correlation ┬À log analysis ┬À alert triage |
| OT/ICS Security | 28 | Modbus ┬À DNP3 ┬À IEC 62443 ┬À historian defense ┬À SCADA |
| API Security | 28 | GraphQL ┬À REST ┬À OWASP API Top 10 ┬À WAF bypass |
| Incident Response | 26 | Breach containment ┬À ransomware response ┬À IR playbooks |
| Vulnerability Management | 25 | Nessus ┬À scanning workflows ┬À patch prioritization ┬À CVSS |
| Penetration Testing | 21 | Network ┬À web ┬À cloud ┬À mobile ┬À NetExec lateral movement |
| DevSecOps | 18 | CI/CD security ┬À Trivy IaC/image scanning ┬À code signing |
| Zero Trust Architecture | 17 | BeyondCorp ┬À CISA maturity model ┬À microsegmentation |
| Endpoint Security | 17 | EDR ┬À LOTL detection ┬À fileless malware ┬À persistence hunting |
| Cryptography | 16 | TLS ┬À Ed25519 ┬À post-quantum migration ┬À key management |
| Phishing Defense | 15 | Email authentication ┬À BEC detection ┬À phishing IR |
| AI Security | 14 | LLM red-teaming (garak/PyRIT) ┬À prompt injection ┬À MCP/agentic security ┬À guardrails |
| Mobile Security | 13 | Android/iOS analysis ┬À mobile pentesting ┬À MDM forensics |
| Ransomware Defense | 13 | Precursor detection ┬À response ┬À recovery ┬À encryption analysis |
| Compliance & Governance | 9 | NIST 800-30/RMF ┬À CMMC ┬À HIPAA ┬À TPRM ┬À CIS benchmarks |
| Supply Chain Security | 8 | SBOMs ┬À dependency confusion ┬À malicious-package triage ┬À SLSA/Sigstore |
| Deception Technology | 6 | Honeytokens ┬À canarytokens ┬À breach detection |
| Hardware & Firmware Security | 4 | CHIPSEC/UEFI audit ┬À Secure Boot bypass ┬À TPM attestation ┬À bootkit hunting |

## How AI agents use these skills

Each skill costs **~30 tokens to scan** (frontmatter only)  and **500ÔÇô2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 817 skills in a single pass without blowing context windows. 

```
User prompt: "Analyze this memory dump for signs of credential theft"

Agent's internal process:

  1. Scans 817 skill frontmatters (~30 tokens each)
     ÔåÆ identifies 12 relevant skills by matching tags, description, domain

  2. Loads top 3 matches:
     ÔÇó performing-memory-forensics-with-volatility3
     ÔÇó hunting-for-credential-dumping-lsass
     ÔÇó analyzing-windows-event-logs-for-credential-access

  3. Executes the structured Workflow section step-by-step
     ÔåÆ runs Volatility3 plugins, checks LSASS access patterns,
        correlates with event log evidence

  4. Validates results using the Verification section
     ÔåÆ confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)
```

**Without these skills**, the agent guesses at tool commands and misses critical steps. **With them**, it follows the same playbook a senior DFIR analyst would use. 

## Skill anatomy

Every skill follows a consistent directory structure:

```
skills/performing-memory-forensics-with-volatility3/
Ôö£ÔöÇÔöÇ SKILL.md              ÔåÉ Skill definition (YAML frontmatter + Markdown body)
Ôö£ÔöÇÔöÇ references/
Ôöé   Ôö£ÔöÇÔöÇ standards.md      ÔåÉ MITRE ATT&CK, ATLAS, D3FEND, NIST mappings
Ôöé   ÔööÔöÇÔöÇ workflows.md      ÔåÉ Deep technical procedure reference
Ôö£ÔöÇÔöÇ scripts/
Ôöé   ÔööÔöÇÔöÇ process.py        ÔåÉ Working helper scripts
ÔööÔöÇÔöÇ assets/
    ÔööÔöÇÔöÇ template.md       ÔåÉ Filled-in checklists and report templates
```


### YAML frontmatter (real example)

```yaml
---
name: performing-memory-forensics-with-volatility3
description: >-
  Analyze memory dumps to extract running processes, network connections,
  injected code, and malware artifacts using the Volatility3 framework.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response, dfir]
atlas_techniques: [AML.T0047]
d3fend_techniques: [D3-MA, D3-PSMD]
nist_ai_rmf: [MEASURE-2.6]
nist_csf: [DE.CM-01, RS.AN-03]
version: "1.2"
author: mukul975
license: Apache-2.0
---
```


### Markdown body sections

```markdown
## When to Use
Trigger conditions ÔÇö when should an AI agent activate this skill?

## Prerequisites
Required tools, access levels, and environment setup.

## Workflow
Step-by-step execution guide with specific commands and decision points.

## Verification
How to confirm the skill was executed successfully.
```

Frontmatter fields: `name` (kebab-case, 1ÔÇô64 chars), `description` (keyword-rich for agent discovery), `domain`, `subdomain`, `tags`,  `atlas_techniques` (MITRE ATLAS IDs), `d3fend_techniques` (MITRE D3FEND IDs), `nist_ai_rmf` (NIST AI RMF references), `nist_csf` (NIST CSF 2.0 categories).  MITRE ATT&CK technique mappings are documented in each skill's `references/standards.md` file and in the ATT&CK Navigator layer included with releases. 

<details>
<summary><strong>­ƒôè MITRE ATT&CK Enterprise coverage ÔÇö all 14 tactics</strong></summary>

&nbsp;

| Tactic | ID | Coverage | Key skills |
|---|---|---|---|
| Reconnaissance | TA0043 | Strong | OSINT, subdomain enumeration, DNS recon |
| Resource Development | TA0042 | Moderate | Phishing infrastructure, C2 setup detection |
| Initial Access | TA0001 | Strong | Phishing simulation, exploit detection, forced browsing |
| Execution | TA0002 | Strong | PowerShell analysis, fileless malware, script block logging |
| Persistence | TA0003 | Strong | Scheduled tasks, registry, service accounts, LOTL |
| Privilege Escalation | TA0004 | Strong | Kerberoasting, AD attacks, cloud privilege escalation |
| Defense Evasion | TA0005 | Strong | Obfuscation, rootkit analysis, evasion detection |
| Credential Access | TA0006 | Strong | Mimikatz detection, pass-the-hash, credential dumping |
| Discovery | TA0007 | Moderate | BloodHound, AD enumeration, network scanning |
| Lateral Movement | TA0008 | Strong | SMB exploits, lateral movement detection with Splunk |
| Collection | TA0009 | Moderate | Email forensics, data staging detection |
| Command and Control | TA0011 | Strong | C2 beaconing, DNS tunneling, Cobalt Strike analysis |
| Exfiltration | TA0010 | Strong | DNS exfiltration, DLP controls, data loss detection |
| Impact | TA0040 | Strong | Ransomware defense, encryption analysis, recovery |

An **ATT&CK Navigator layer file** is included in the [v1.0.0 release assets](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) for visual coverage mapping. 

> **Note:** ATT&CK v19 lands April 28, 2026 ÔÇö splitting Defense Evasion (TA0005) into two new tactics: *Stealth* and *Impair Defenses*.  Skill mappings will be updated in a forthcoming release.

</details>

<details>
<summary><strong>­ƒôè NIST CSF 2.0 alignment ÔÇö all 6 functions</strong></summary>

&nbsp;

| Function | Skills | Examples |
|---|---|---|
| **Govern (GV)** | 30+ | Risk strategy, policy frameworks, roles & responsibilities |
| **Identify (ID)** | 120+ | Asset discovery, threat landscape assessment, risk analysis |
| **Protect (PR)** | 150+ | IAM hardening, WAF rules, zero trust, encryption |
| **Detect (DE)** | 200+ | Threat hunting, SIEM correlation, anomaly detection |
| **Respond (RS)** | 160+ | Incident response, forensics, breach containment |
| **Recover (RC)** | 40+ | Ransomware recovery, BCP, disaster recovery |

NIST CSF 2.0 (February 2024) added the **Govern** function  and expanded scope from critical infrastructure to all organizations.  Skill mappings align to all 22 categories and reference 106 subcategories. 

</details>

<details>
<summary><strong>­ƒôè Framework deep dive ÔÇö ATLAS, D3FEND, AI RMF</strong></summary>

&nbsp;

### MITRE ATLAS v5.4 ÔÇö AI/ML adversarial threats
ATLAS maps adversarial tactics, techniques, and case studies specific to AI and machine learning systems. Version 5.4 covers **16 tactics and 84 techniques** including agentic AI attack vectors added in late 2025: AI agent context poisoning, tool invocation abuse, MCP server compromises, and malicious agent deployment.  Skills mapped to ATLAS help agents identify and defend against threats to ML pipelines, model weights, inference APIs, and autonomous workflows. 

### MITRE D3FEND v1.3 ÔÇö Defensive countermeasures
D3FEND is an NSA-funded knowledge graph of **267 defensive techniques** organized across 7 tactical categories: Model, Harden, Detect, Isolate, Deceive, Evict, and Restore.  Built on OWL 2 ontology, it uses a shared Digital Artifact layer to bidirectionally map defensive countermeasures to ATT&CK offensive techniques.  Skills tagged with D3FEND identifiers let agents recommend specific countermeasures for detected threats.

### NIST AI RMF 1.0 + GenAI Profile (AI 600-1)
The AI Risk Management Framework defines 4 core functions ÔÇö Govern, Map, Measure, Manage ÔÇö with **72 subcategories** for trustworthy AI development.  The GenAI Profile (AI 600-1, July 2024) adds **12 risk categories** specific to generative AI, from confabulation and data privacy to prompt injection and supply chain risks.  Colorado's AI Act (effective February 2026) provides a **legal safe harbor** for organizations complying with NIST AI RMF, making these mappings directly relevant to regulatory compliance.

</details>

## Compatible platforms

**AI code assistants**
Claude Code (Anthropic) ┬À GitHub Copilot (Microsoft) ┬À Cursor ┬À Windsurf ┬À Cline ┬À Aider ┬À Continue ┬À Roo Code ┬À Amazon Q Developer ┬À Tabnine ┬À Sourcegraph Cody ┬À JetBrains AI 

**CLI agents**
OpenAI Codex CLI ┬À Gemini CLI (Google) 

**Autonomous agents**
Devin ┬À Replit Agent ┬À SWE-agent ┬À OpenHands 

**Agent frameworks & SDKs**
LangChain ┬À CrewAI ┬À AutoGen ┬À Semantic Kernel ┬À Haystack ┬À Vercel AI SDK ┬À Any MCP-compatible agent 

All platforms that support the [agentskills.io](https://agentskills.io) standard can load these skills with zero configuration. 

## What people are saying

> *"A database of real, organized security skills that any AI agent can plug into and use. Not tutorials. Not blog posts."* 
> ÔÇö **[Hasan Toor (@hasantoxr)](https://x.com/hasantoxr/status/2033193922349179249)**, AI/tech creator

> *"This is not a random collection of security scripts. It's a structured operational knowledge base designed for AI-driven security workflows."* 
> ÔÇö **[fazal-sec](https://fazal-sec.medium.com/claude-skills-ai-powered-cybersecurity-the-complete-guide-to-building-intelligent-security-7bb7e9d14c8e)**,  Medium

## Featured in

| Where | Type | Link |
|---|---|---|
| **awesome-agent-skills** | Awesome List (1,000+ skills index) | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |
| **awesome-ai-security** | Awesome List (AI security tools) | [ottosulin/awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) |
| **awesome-codex-cli** | Awesome List (Codex CLI resources) | [RoggeOhta/awesome-codex-cli](https://github.com/RoggeOhta/awesome-codex-cli) |
| **SkillsLLM** | Skills directory & marketplace | [skillsllm.com/skill/anthropic-cybersecurity-skills](https://skillsllm.com/skill/anthropic-cybersecurity-skills) |
| **Openflows** | Signal analysis & tracking | [openflows.org](https://openflows.org/currency/currents/anthropic-cybersecurity-skills/) |
| **NeverSight skills_feed** | Automated skills index | [NeverSight/skills_feed](https://github.com/NeverSight/skills_feed) |

## Star history

<a href="https://star-history.com/#mukul975/Anthropic-Cybersecurity-Skills&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" width="100%" />
 </picture>
</a>

## Releases

| Version | Date | Highlights |
|---|---|---|
| [v1.0.0](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) | March 11, 2026 | 734 skills ┬À 26 domains ┬À MITRE ATT&CK + NIST CSF 2.0 mapping ┬À ATT&CK Navigator layer |

Skills have continued to grow on `main` since v1.0.0 ÔÇö the library now contains **817 skills** with **6-framework mapping**  (MITRE ATLAS, D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework added post-release).  Check [Releases](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases) for the latest tagged version.

## Contributing

This project grows through community contributions. Here is how to get involved:

**Add a new skill** ÔÇö Domains like Deception Technology (2 skills) and Compliance & Governance (5 skills) need the most help. Follow the template in [CONTRIBUTING.md](CONTRIBUTING.md) and submit a PR with the title `Add skill: your-skill-name`.

**Improve existing skills** ÔÇö Add framework mappings, fix workflows, update tool references, or contribute scripts and templates.

**Report issues** ÔÇö Found an inaccurate procedure or broken script? [Open an issue](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues).

Every PR is reviewed for technical accuracy and agentskills.io standard compliance within 48 hours.  Check [good first issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) for a starting point.

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you agree to uphold this code. 

## Community

­ƒÆ¼ [Discussions](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) ÔÇö Questions, ideas, and roadmap conversations
­ƒÉø [Issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues) ÔÇö Bug reports and feature requests
­ƒöÆ [Security Policy](SECURITY.md) ÔÇö Responsible disclosure process (48-hour acknowledgment) 

## Citation

If you use this project in research or publications:

```bibtex
@software{anthropic_cybersecurity_skills,
  author       = {Jangra, Mahipal},
  title        = {Anthropic Cybersecurity Skills},
  year         = {2026},
  url          = {https://github.com/mukul975/Anthropic-Cybersecurity-Skills},
  license      = {Apache-2.0},
  note         = {817 structured cybersecurity skills for AI agents,
                  mapped to MITRE ATT\&CK, NIST CSF 2.0, MITRE ATLAS,
                  MITRE D3FEND, and NIST AI RMF}
}
```

## License

This project is licensed under the [Apache License 2.0](LICENSE). You are free to use, modify, and distribute these skills in both personal and commercial projects. 

---

<div align="center">

**If this project helps your security work, consider giving it a Ô¡É**

[Ô¡É Star](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers) ┬À [­ƒì┤ Fork](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/fork) ┬À [­ƒÆ¼ Discuss](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) ┬À [­ƒôØ Contribute](CONTRIBUTING.md)

Community project by [@mukul975](https://github.com/mukul975). Not affiliated with Anthropic PBC.

</div>
