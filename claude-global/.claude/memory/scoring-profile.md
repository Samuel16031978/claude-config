# Profil de scoring — YouTube → GitHub (Samuel)

> Lu par l'agent **avant toute évaluation de pertinence**. Décrit la méthodologie de notation.
> **Les listes vivantes (projets actifs, outils manquants, thèmes surveillés) ne sont PAS recopiées ici.**
> Source unique : [`data/youtube-scrapes/projets-samuel.json`](../../data/youtube-scrapes/projets-samuel.json) (version machine).
> Édite ce JSON pour faire évoluer le profil — le script et l'agent lisent les mêmes listes, sans risque de désynchronisation.

## Objet noté

La **vidéo** est un canal de découverte ; le **repo GitHub** est l'objet noté sur **100 points**.
On note aussi, par pertinence légère (0-10) : les **insights** (IA/entrepreneuriat/mindset) et les **outils/technos cités**.

## Grille GitHub /100 — 4 axes

### AXE 1 — Contenu Claude (35 pts)
Détecté via l'arbre du repo (match par suffixe de chemin n'importe où, pas seulement la racine).

| Critère | Points | Règle |
|---|---|---|
| Présence dossier `.claude/` | 0–10 | présent = 10, sinon 0 |
| Skills installables (`SKILL.md`) | 0–10 | 1 = 4 · 2-3 = 7 · 4+ = 10 |
| Agents définis (`agents/`, `*.agent.md`) | 0–8 | présent = 8 · partiel = 4 |
| Commands / hooks | 0–7 | les deux = 7 · un seul = 4 |

Arbre tronqué et indéterminable → AXE 1 = `unknown` (jamais `0`, qui serait un faux négatif).

### AXE 2 — Qualité (25 pts)

| Critère | Points | Règle |
|---|---|---|
| Stars | 0–10 | >1000 = 10 · 500-1000 = 8 · 100-500 = 6 · 20-100 = 4 · <20 = 2 |
| Activité récente (`pushed_at`) | 0–8 | <1 mois = 8 · <3 mois = 6 · <6 mois = 4 · <1 an = 2 · sinon 0 |
| Documentation / README | 0–7 | >5 ko = 7 · >1 ko = 5 · présent = 3 · absent = 0 |

### AXE 3 — Thématique (20 pts)
Match des **thèmes surveillés** (voir `projets-samuel.json` → `themes_surveilles`) dans description / topics / README.
**4 pts par thème matché, plafonné à 20.**

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
| 85-100 | 🔥 Pépite — explorer en priorité |
| 70-84 | ✅ Solide — vaut le détour |
| 50-69 | 🟡 Intéressant — garder en veille |
| <50 | ⚪ Marginal — ignorer sauf besoin précis |

**Plafond 65** : un excellent repo **non-Claude** plafonne vers 65 (AXE 1 ≈ 0). C'est voulu —
la grille est orientée contenu Claude. Ne pas "compenser" en gonflant les autres axes.

## Pertinence légère (insights & outils, 0-10)

- **Insight** : densité thématique d'une fenêtre de transcription + bonus tournure à valeur ("la clé c'est", "le secret", "framework"…). On garde `relevance ≥ 6`.
- **Outil** : fréquence de mention × match thèmes surveillés. Agrégé par chaîne → repère les stacks tendance.
