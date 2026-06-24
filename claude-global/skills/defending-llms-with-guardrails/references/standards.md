# Standards and Framework Mapping

## NIST AI Risk Management Framework (AI RMF 1.0 / GenAI Profile NIST AI 600-1)

| ID | Name | Rationale |
|----|------|-----------|
| MANAGE-2.1 | Resources required to manage AI risks are documented and put into action | Deploying Llama Guard / NeMo / LLM Guard is the operational control that manages identified LLM safety risks at runtime. |

## MITRE ATLAS

| ID | Name | Rationale |
|----|------|-----------|
| AML.T0054 | LLM Jailbreak | The guardrail layer is the primary mitigation that detects and blocks jailbreak attempts before/after model inference. |
| AML.T0051 | LLM Prompt Injection | Input rails and the PromptInjection scanner block direct injection attempts. |
| AML.T0051.001 | LLM Prompt Injection: Indirect | Retrieval/input scanning blocks injection embedded in retrieved or tool-returned content. |
| AML.T0057 | LLM Data Leakage | Output scanners (Sensitive, Secrets, Deanonymize) prevent leakage of PII, secrets, and instructions. |

## OWASP Top 10 for LLM Applications (2025)

| ID | Name | Rationale |
|----|------|-----------|
| LLM01 | Prompt Injection | Guardrails are the recommended runtime mitigation for direct and indirect injection. |
| LLM02 | Sensitive Information Disclosure | Output PII/secrets scanners prevent disclosure. |
| LLM07 | System Prompt Leakage | Input/output rails detect attempts to extract and leak the system prompt. |

## MLCommons Hazard Taxonomy (Llama Guard 3 categories)

S1 Violent Crimes ┬À S2 Non-Violent Crimes ┬À S3 Sex-Related Crimes ┬À S4 Child Sexual Exploitation ┬À S5 Defamation ┬À S6 Specialized Advice ┬À S7 Privacy ┬À S8 Intellectual Property ┬À S9 Indiscriminate Weapons ┬À S10 Hate ┬À S11 Suicide & Self-Harm ┬À S12 Sexual Content ┬À S13 Elections ┬À S14 Code Interpreter Abuse.
