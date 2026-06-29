# Profil de scoring — YouTube → GitHub (Samuel)

> Lu par l'agent **avant toute évaluation de pertinence**. Décrit la méthodologie de notation.
> **Les listes vivantes (projets actifs, outils manquants, thèmes surveillés) ne sont PAS recopiées ici.**
> Source unique : [`data/youtube-scrapes/projets-samuel.json`](../../data/youtube-scrapes/projets-samuel.json) (version machine).
> Édite ce JSON pour faire évoluer le profil — le script et l'agent lisent les mêmes listes, sans risque de désynchronisation.

## Objet noté

La **vidéo** est un canal de découverte ; le **repo GitHub** est l'objet noté sur **100 points**.
On note aussi, par pertinence légère (0-10) : les **insights** (IA/entrepreneuriat/mindset) et les **outils/technos cités**.

## Grille GitHub /100 — 4 axes

> **Grille v2 — décentrée des repos Claude (décision Samuel).** La veille n'est plus pilotée par le
> contenu Claude : Qualité + Thématique en sont le moteur, le contenu Claude n'est qu'un **bonus / 2ᵉ filtre**.

### AXE 1 — Contenu Claude (10 pts — bonus)
Détecté via l'arbre du repo (match par suffixe de chemin n'importe où, pas seulement la racine).

| Critère | Points | Règle |
|---|---|---|
| Présence dossier `.claude/` | 0–3 | présent = 3, sinon 0 |
| Skills installables (`SKILL.md`) | 0–3 | 1 = 1 · 2-3 = 2 · 4+ = 3 |
| Agents définis (`agents/`, `*.agent.md`) | 0–2 | présent = 2 |
| Commands / hooks | 0–2 | les deux = 2 · un seul = 1 |

Arbre tronqué et indéterminable → AXE 1 = `unknown` (jamais `0`, qui serait un faux négatif).

### AXE 2 — Qualité (40 pts — moteur principal)

| Critère | Points | Règle |
|---|---|---|
| Stars | 0–16 | >1000 = 16 · 500-1000 = 13 · 100-500 = 10 · 20-100 = 6 · <20 = 3 |
| Activité récente (`pushed_at`) | 0–15 | <1 mois = 15 · <3 mois = 11 · <6 mois = 7 · <1 an = 3 · sinon 0 |
| Documentation / README | 0–9 | >5 ko = 9 · >1 ko = 6 · présent = 3 · absent = 0 |

### AXE 3 — Thématique (30 pts)
Match des **thèmes surveillés** (voir `projets-samuel.json` → `themes_surveilles`) dans description / topics / README.
**6 pts par thème matché, plafonné à 30.**

### AXE 4 — Personnel Samuel (20 pts)
Match contre `projets-samuel.json` (`projets_actifs`, `outils_manquants`).

| Critère | Points | Règle |
|---|---|---|
| Répond à un projet actif | 0–12 | fort (≥2 keywords) = 12 · partiel (1 keyword) = 6 |
| Comble un outil manquant | 0–8 | oui = 8 · proche = 4 |

**Confiance obligatoire** : le matching mots-clés sur/sous-déclenche. Chaque repo expose
`axe4_confidence` + `matched_keywords`. Si confiance **basse**, l'AXE 4 est **exclu du verdict**
et signalé `⚠️ AXE4 à valider` — ne jamais affirmer un score AXE 4 basse confiance.

## Verdict (ancres)

| Score /100 | Verdict |
|---|---|
| 95-100 | 🔥 Pépite — explorer en priorité |
| 85-94 | ✅ Solide — vaut le détour |
| 70-84 | 🟡 Intéressant — garder en veille |
| <70 | ⚪ Marginal — ignorer sauf besoin précis |

**Décentré Claude** : un repo **non-Claude** atteint **90** au maximum (AXE 1 = 0) → la veille (70) et le
solide (85) lui sont accessibles. Qualité + Thématique = 70 = **plancher de veille sans aucun contenu Claude**.
La **pépite (95+)** exige en plus le bonus AXE 1 (contenu Claude) — c'est le seul rôle de Claude désormais.

## Pertinence légère (insights & outils, 0-10)

- **Insight** : densité thématique d'une fenêtre de transcription + bonus tournure à valeur ("la clé c'est", "le secret", "framework"…). On garde `relevance ≥ 6`.
- **Outil** : fréquence de mention × match thèmes surveillés. Agrégé par chaîne → repère les stacks tendance.
