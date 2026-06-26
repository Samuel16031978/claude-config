---
name: saas-financial-samuel
description: "Modélisation financière et projections pour Samuel. 5 modèles : SaaS metrics, service & formation, service BTP (SC Réno), valorisation/exit, ROI investissement. Benchmarks complets (Quick Ratio, Magic Number, Rule of 40, multiples sectoriels). Déclencheurs : projections financières, MRR, ARR, churn, LTV, CAC, valorisation, point mort, ROI, modèle financier."
---

# SaaS & Financial Projections Samuel

## Contexte opérateur
Samuel est entrepreneur multi-projets avec culture ROI forte. Priorité : modèles simples actionnables sur hypothèses réalistes. Signaler systématiquement les hypothèses et les paramètres critiques.

## Routing

| Demande | Section |
|---------|---------|
| SaaS / abonnement | §A — SaaS Metrics |
| Service / Formation | §B — Service & Formation |
| Entreprise B2B (SC Réno) | §C — Service BTP |
| Valorisation / Exit | §D — Valorisation |
| Investissement / capex | §E — ROI investissement |

---

## §A — SaaS Metrics

| Métrique | Formule | Benchmark sain |
|----------|---------|----------------|
| MRR | nb clients × ARPU | — |
| ARR | MRR × 12 | — |
| Churn mensuel | clients perdus / clients début mois | <3% |
| LTV | ARPU / churn mensuel | — |
| CAC | budget acquisition / nb nouveaux clients | — |
| LTV/CAC | LTV ÷ CAC | >3 excellent, >5 exceptionnel |
| Payback period | CAC ÷ marge mensuelle par client | <12 mois idéal |
| NRR | (MRR début + expansion - churn) / MRR début | >100% = croissance organique |
| Quick Ratio | (new MRR + expansion MRR) / (churned + contraction MRR) | >4 = sain |
| Magic Number | (ARR Δ × marge brute) / S&M trimestre précédent | >0.75 = efficace |
| Rule of 40 | croissance ARR% + marge EBITDA% | >40 = sain |

**P&L SaaS simplifié :**
```
ARR
- Coût serveurs / infra (COGS)
= Marge brute (viser >70%)
- S&M (Sales & Marketing)
- R&D
- G&A (admin)
= EBITDA
```

**Scénarios à modéliser systématiquement :**
- Bear : croissance MRR +5%/mois
- Base : +10%/mois
- Bull : +20%/mois

---

## §B — Service & Formation en ligne
**Modèle de projection formation :**
```
Trafic mensuel
× taux opt-in (benchmark : 20–40%)
× taux conversion (cold 1–3%, warm 5–15%)
× prix
= CA brut
- Coût acquisition (paid ads, contenu)
- Frais plateforme (3–5%)
- Frais paiement (2–3%)
= Marge nette
```
**Point mort :** Charges fixes mensuelles ÷ marge sur coût variable = volume minimum

---

## §C — Service BTP (SC Rénovations)

| Métrique | Calcul | Cible SC Réno |
|----------|--------|---------------|
| Panier moyen | CA / nb chantiers | Optimiser mix |
| Taux de closing | devis signés / devis envoyés | 55–65% |
| Marge brute chantier | (CA - coût direct) / CA | 30–35% |
| BFR | créances + stocks - dettes fournisseurs | Minimiser |
| Délai moyen encaissement | — | <45 jours |

**Projection CA :**
```
Nb chantiers/mois × panier moyen × taux closing = CA mensuel
Objectif 4M€ = ~333K€/mois à atteindre progressivement
```
**Levier BFR :** Réduire délai encaissement (acomptes), allonger délai fournisseurs, facturer à l'avancement.

---

## §D — Valorisation & Exit

| Secteur | Multiple EBE | Multiple CA |
|---------|--------------|-------------|
| SaaS B2B | 8–15× | 3–8× |
| Formation en ligne | 3–6× | 1–3× |
| Service BTP | 3–5× | 0.5–1× |
| Consulting | 4–8× | 1–2× |

**DCF simplifié :**
1. Projeter cash-flows libres sur 5 ans
2. Taux d'actualisation : 15–25% (startup/PME)
3. Valeur terminale = CF année 5 × multiple sectoriel

**Déclencheurs de revalorisation :** récurrence vs transactionnel, dépendance réduite au fondateur, croissance documentée.

---

## §E — ROI Investissement / Capex
1. Coût total (acquisition + déploiement + formation)
2. Gain attendu (revenu supplémentaire ou coût évité)
3. Délai de retour : coût total ÷ gain mensuel
4. Analyse de sensibilité : -30% sur le gain, que se passe-t-il ?
5. Coût de l'inaction (ne pas investir)

---

## Workflow de modélisation Samuel
1. **Qualifier** : type de projet, données disponibles
2. **Hypothèses critiques** : identifier les 3 paramètres qui font tout bouger
3. **Modèle base** avec chiffres conservateurs réalistes
4. **3 scénarios** : bear / base / bull sur les hypothèses critiques
5. **Point mort** : à quel volume Samuel est rentable
6. **Cash-flow** : quand a-t-il besoin de financement externe
7. **Tableau synthèse** : 1 page max, lisible en 30 secondes

**Règles :** Partir des hypothèses les plus pessimistes réalistes. Séparer charges fixes vs variables. Signaler si un paramètre est "trop beau pour être vrai". Travailler avec données partielles en indiquant clairement les hypothèses.
