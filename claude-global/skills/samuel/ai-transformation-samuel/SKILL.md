---
name: ai-transformation-samuel
description: "Double usage : interne (automatiser SC Réno) + externe (offre conseil IA PME). Matrice effort/impact, stack IA par niveaux, questionnaire d'audit, pricing, recrutement profil IA. Déclencheurs : automatiser, transformation IA, audit IA, offre conseil IA, quick wins, stack IA, ROI automatisation."
---

# AI Transformation Samuel — Diagnostic & Déploiement IA

## Contexte opérateur

Samuel est à la fois utilisateur IA avancé (SC Rénovations) et potentiel prestataire de conseil IA pour PME. Ce skill couvre deux usages : (1) transformer ses propres opérations, (2) diagnostiquer et pitcher une offre de transformation IA à des clients externes.

---

## Routing

| Demande | Mode | Section |
|---------|------|---------|
| Automatiser mes propres process | Interne | §A |
| Pitcher/vendre une offre IA à un client | Externe | §B |
| Auditer une entreprise | Audit | §C |
| Recruter un profil IA | RH | §D |

---

## §A — Transformation IA interne (SC Rénovations & projets Samuel)

### Matrice effort/impact

| Process | Outil recommandé | Impact | Effort | Priorité |
|---------|------------------|--------|--------|----------|
| Relance devis non signés | Monday.com • email auto | Haut | Faible | 🔴 |
| Génération rapports chantier | Claude + template | Haut | Faible | 🔴 |
| Qualification leads entrants | n8n + Claude | Haut | Moyen | 🟡 |
| Suivi facturation / BFR | Monday.com • Zapier | Moyen | Faible | 🟡 |
| Réponses emails répétitifs | Claude + Gmail MCP | Moyen | Faible | 🟡 |
| Planification chantiers | Monday.com automatisé | Haut | Moyen | 🟡 |
| Création contenus formation | Claude + workflow | Haut | Moyen | 🟡 |

### Stack IA recommandé Samuel

**Niveau 1 — Déjà disponible (activer maintenant) :**
- Claude + Monday.com MCP → gestion projets en langage naturel
- Claude + Gmail MCP → traitement emails, rédaction
- Claude + Google Drive MCP → gestion docs

**Niveau 2 — À déployer (ROI rapide) :**
- n8n (self-hosted ou cloud) → orchestration workflows complexes
- Make (Integromat) → automatisations no-code simples
- Zapier → connecteurs rapides si budget disponible

**Niveau 3 — Horizon 3–6 mois :**
- Agents IA autonomes (sous-traitants virtuels)
- RAG sur base de connaissances SC Rénovations
- Dashboard BI automatisé (CA, marges, BFR en temps réel)

---

## §B — Offre de conseil IA externe (clients PME)

**Structure offre type :**
1. Diagnostic IA (demi-journée) → livrable : cartographie des 5 quick wins
2. Déploiement guidé (1–3 jours) → livrable : premiers workflows opérationnels
3. Formation équipe (1 jour) → livrable : autonomie sur les outils déployés
4. Suivi mensuel (optionnel) → livrable : optimisation et nouveaux cas d'usage

**Pricing indicatif PME :**
- Diagnostic : 500–1500€ (demi-journée)
- Déploiement : 2000–5000€ (projet)
- Formation : 800–2000€ (journée)
- Retainer mensuel : 500–2000€/mois

---

## §C — Audit IA d'une entreprise

### Mode Express (30 min)
1. **Activité** : Décris ton activité principale et tes 3 principaux process répétitifs
2. **Douleurs** : Qu'est-ce qui te prend le plus de temps sans valeur ajoutée ?
3. **Tech stack** : Quels outils utilises-tu actuellement (CRM, ERP, email, etc.) ?
4. **Équipe** : Combien de personnes, quelles compétences digitales ?
5. **Budget** : Quel investissement est envisageable (outils + accompagnement) ?
6. **Objectif** : Gagner du temps / réduire des coûts / augmenter le CA / les 3 ?

### Mode Deep Dive (2h)
Ajouter : cartographie complète des process, identification des données disponibles, analyse des intégrations existantes, évaluation maturité digitale équipe (0–5), identification des résistances au changement, définition des KPIs de succès (mesurables à 3 et 6 mois).

### Livrable audit
```
# Rapport Diagnostic IA — [Entreprise]

## Résumé exécutif
[3 lignes : potentiel identifié, priorité recommandée, ROI estimé]

## Top 5 Quick Wins
| # | Process | Outil | Gain estimé | Délai déploiement |

## Roadmap recommandée
Phase 1 (J0–J30) : [actions immédiates]
Phase 2 (J30–J90) : [consolidation]
Phase 3 (J90+) : [scaling]

## Investissement estimé
[Coût outils + accompagnement vs gain annuel estimé]
```

---

## §D — Recrutement profil IA (stagiaire / alternant / freelance)

**Profil idéal pour PME phase de croissance :**
- Compétences : Python ou no-code, LLM API, n8n/Make, prompt engineering
- Output attendu : workflows déployés, pas du code théorique
- Structure contrat : via SC Holding (facturation à l'output, pas de masse salariale fixe)

**Grille évaluation candidat :**
- A-t-il déjà déployé un agent ou un workflow en production ? (pas juste du ChatGPT)
- Peut-il expliquer une automatisation qu'il a construite de A à Z ?
- Connaît-il les limites des LLMs (hallucinations, contexte, coût) ?
- Score final : /10 sur capacité à produire des résultats concrets en < 30 jours

---

## Règles de réponse
- Toujours partir de l'objectif business (gain temps/argent) avant l'outil
- Proposer la solution la plus simple qui résout le problème
- Signaler le coût réel (outils + temps de déploiement) avant de recommander
- Alerter si une automatisation risque de créer plus de maintenance que de gain
