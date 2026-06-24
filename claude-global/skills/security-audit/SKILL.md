---
name: security-audit
description: >
  Audit de s├®curit├® complet et automatique d'un projet. D├®tecte la nature du
  projet (web, API, mobile, cloud, conteneurs, IaC, CI/CDÔÇª), s├®lectionne les
  skills cybers├®curit├® pertinents parmi les 817 disponibles, les ex├®cute dans
  l'ordre logique et produit un rapport consolid├® avec criticit├®, preuves et
  recommandations. Aucune connaissance pr├®alable des skills n'est requise.
domain: cybersecurity
subdomain: orchestration
tags:
  - audit
  - security
  - orchestration
  - devsecops
  - all-in-one
version: '1.0'
license: Apache-2.0
---

# Security Audit ÔÇö Orchestrateur automatique

> **Usage autoris├® uniquement.** Cet audit porte sur le code et les configurations
> pr├®sents dans ce d├®p├┤t. Ne jamais ex├®cuter sur des syst├¿mes tiers sans autorisation
> ├®crite explicite.

---

## Objectif

R├®aliser un audit de s├®curit├® complet sans que l'utilisateur ait ├á conna├«tre les
817 skills disponibles. L'orchestrateur :

1. **D├®tecte** automatiquement le profil du projet
2. **S├®lectionne** les skills pertinents
3. **Ex├®cute** les v├®rifications dans l'ordre logique
4. **Consolide** les r├®sultats dans un rapport unique

---

## ├ëtape 1 ÔÇö Empreinte du projet

Analyser le d├®p├┤t pour ├®tablir le profil technique :

```
├ël├®ments ├á d├®tecter                  Indicateurs ├á chercher
ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
Langage / framework                  package.json, pom.xml, go.mod, Cargo.toml,
                                     requirements.txt, Gemfile, *.csproj
API (REST / GraphQL / gRPC)          openapi.yaml, schema.graphql, *.proto,
                                     routes/, controllers/, handlers/
Application web                      templates/, views/, *.html, *.jsx/tsx,
                                     next.config.*, nuxt.config.*
Conteneurs                           Dockerfile*, docker-compose.*, .dockerignore
Kubernetes / IaC                     *.yaml dans k8s/ ou helm/, *.tf, *.bicep,
                                     cloudformation/, CDK
CI/CD                                .github/workflows/, .gitlab-ci.yml,
                                     Jenkinsfile, .circleci/, bitbucket-pipelines.yml
Cloud provider                       serverless.yml, cdk.json, terraform.tfvars,
                                     aws-exports.js, azure.json, gcp-*.json
Secrets potentiels                   .env*, *.pem, *.key, *.p12, credentials.*
D├®pendances tierces                  package-lock.json, yarn.lock, poetry.lock,
                                     Pipfile.lock, go.sum, Cargo.lock
Mobile                               AndroidManifest.xml, Info.plist, *.ipa, *.apk
```

R├®sumer le profil d├®tect├® avant de continuer.

---

## ├ëtape 2 ÔÇö S├®lection des skills

Selon le profil, activer les skills appropri├®s dans l'ordre suivant (du plus
g├®n├®rique au plus sp├®cifique). Ne pas ex├®cuter un skill qui n'est pas pertinent.

### Bloc A ÔÇö Secrets & d├®pendances (toujours effectu├®)

| Condition          | Skills ├á invoquer                                    |
|--------------------|------------------------------------------------------|
| Toujours           | `implementing-secret-scanning-with-gitleaks`         |
| Fichier lock trouv├®| `performing-sca-dependency-scanning-with-snyk`       |
| SBOM demand├®       | `generating-and-analyzing-sboms`                     |
| Supply chain ci/cd | `detecting-supply-chain-attacks-in-ci-cd`            |

### Bloc B ÔÇö Code source

| Condition              | Skills ├á invoquer                                        |
|------------------------|----------------------------------------------------------|
| Code source pr├®sent    | `integrating-sast-into-github-actions-pipeline`          |
|                        | `implementing-semgrep-for-custom-sast-rules`             |
| CI/CD d├®tect├®          | `securing-github-actions-workflows`                      |
| Signatures/artefacts   | `implementing-code-signing-for-artifacts`                |

### Bloc C ÔÇö Application web / API

| Condition          | Skills ├á invoquer                                              |
|--------------------|----------------------------------------------------------------|
| App web            | `performing-web-application-penetration-test`                  |
|                    | `performing-security-headers-audit`                            |
|                    | `testing-for-xss-vulnerabilities`                              |
|                    | `testing-for-broken-access-control`                            |
|                    | `performing-csrf-attack-simulation`                            |
| API REST           | `performing-api-security-testing-with-postman`                 |
|                    | `testing-api-security-with-owasp-top-10`                       |
|                    | `testing-api-authentication-weaknesses`                        |
|                    | `testing-for-json-web-token-vulnerabilities`                   |
| API GraphQL        | `performing-graphql-security-assessment`                       |
|                    | `performing-graphql-introspection-attack`                      |
| Auth / sessions    | `testing-oauth2-implementation-flaws`                          |
|                    | `testing-for-sensitive-data-exposure`                          |

### Bloc D ÔÇö Conteneurs & Kubernetes

| Condition          | Skills ├á invoquer                                              |
|--------------------|----------------------------------------------------------------|
| Dockerfile pr├®sent | `performing-container-image-hardening`                         |
|                    | `performing-container-security-scanning-with-trivy`            |
|                    | `hardening-docker-daemon-configuration`                        |
| docker-compose     | `scanning-docker-images-with-trivy`                            |
| Kubernetes         | `auditing-kubernetes-rbac-privilege-escalation`                |
|                    | `scanning-kubernetes-manifests-with-kubesec`                   |
|                    | `implementing-kubernetes-pod-security-standards`               |
|                    | `performing-kubernetes-cis-benchmark-with-kube-bench`          |

### Bloc E ÔÇö Infrastructure as Code & Cloud

| Condition          | Skills ├á invoquer                                              |
|--------------------|----------------------------------------------------------------|
| Terraform/CDK/CF   | `scanning-iac-and-images-with-trivy`                           |
|                    | `auditing-terraform-infrastructure-for-security`               |
| AWS                | `auditing-aws-s3-bucket-permissions`                           |
|                    | `securing-aws-iam-permissions`                                 |
| Azure              | `auditing-azure-active-directory-configuration`                |
| GCP                | `auditing-gcp-iam-permissions`                                 |
| Serverless         | `performing-serverless-function-security-review`               |
|                    | `securing-serverless-functions`                                |

### Bloc F ÔÇö Mobile

| Condition          | Skills ├á invoquer                                              |
|--------------------|----------------------------------------------------------------|
| Android            | `performing-android-app-static-analysis-with-mobsf`           |
|                    | `testing-android-intents-for-vulnerabilities`                  |
| iOS                | `performing-ios-app-security-assessment`                       |

---

## ├ëtape 3 ÔÇö Ex├®cution

Pour chaque skill s├®lectionn├® :

1. Annoncer clairement le skill en cours : `[ÔûÂ skill-name]`
2. Appliquer son analyse au code/config du projet courant (ne pas simuler ÔÇö
   lire les vrais fichiers avec Read, Grep, Glob)
3. Documenter chaque finding avec :
   - **Fichier + ligne** si applicable
   - **Preuve** (extrait de code ou config)
   - **Criticit├®** : CRITIQUE / HAUTE / MOYENNE / FAIBLE / INFO
   - **Recommandation** concr├¿te

---

## ├ëtape 4 ÔÇö Rapport consolid├®

Produire un rapport structur├® en fran├ºais (ou dans la langue de l'utilisateur) :

```
ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ
  RAPPORT D'AUDIT DE S├ëCURIT├ë
  Projet : <nom>          Date : <date>
  Profil : <web|api|conteneur|cloud|ÔÇª>
ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ

R├ëSUM├ë EX├ëCUTIF
ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  CRITIQUE  : N findings
  HAUTE     : N findings
  MOYENNE   : N findings
  FAIBLE    : N findings
  INFO      : N findings

FINDINGS D├ëTAILL├ëS
ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
[CRITIQUE] Titre court
  Fichier    : path/to/file.ext:42
  Preuve     : <extrait>
  Risque     : Explication du risque concret
  Correction : ├ëtapes pr├®cises pour corriger

[HAUTE] ÔÇª

COUVERTURE DE L'AUDIT
ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  Ô£à Secrets & d├®pendances
  Ô£à Code source (SAST)
  Ô£à API REST (OWASP Top 10)
  Ô¼£ Kubernetes (non d├®tect├®)
  ÔÇª

PROCHAINES ├ëTAPES RECOMMAND├ëES
ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  1. ÔÇª
  2. ÔÇª
```

---

## R├¿gles de comportement

- **Lire les vrais fichiers** ÔÇö ne jamais inventer de findings
- **Pas de faux positifs invent├®s** ÔÇö signaler uniquement ce qui est
  effectivement pr├®sent dans le code
- **Adapter la profondeur** ├á la taille du projet (pour un grand projet,
  ├®chantillonner par r├®pertoire)
- **Proposer** d'approfondir un bloc sp├®cifique ├á la fin si l'utilisateur
  le souhaite
- **Ne pas modifier** les fichiers du projet sans demande explicite

---

## D├®clenchement

Ce skill est invoqu├® par : `/security-audit`

L'utilisateur peut aussi cibler un sous-dossier : `/security-audit nutritrack/`
ou un type sp├®cifique : `/security-audit --focus api`
