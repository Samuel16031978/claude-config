# Rapport de Veille GitHub ÔÇö 28 mai 2026

## Param├¿tres

| Param├¿tre | Valeur |
|-----------|--------|
| Date | 2026-05-28 |
| Th├¿mes surveill├®s | `claude-code`, `ai-agents` |
| P├®riode | Cette semaine (2026-05-21 ÔåÆ 2026-05-28) |
| Seuil auto-install | ÔëÑ 90/100 |
| Mode 70ÔÇô89 | Confirmation manuelle |
| Agent de recherche | github-watch-agent (haiku) |
| Agents de scoring | github-relevance-agent ├ù 10 (haiku, parall├¿le) |

---

## R├®sum├®

| M├®trique | Valeur |
|----------|--------|
| D├®p├┤ts trouv├®s | 18 |
| D├®p├┤ts scor├®s | 10 |
| Install├®s automatiquement (ÔëÑ 90) | 3 |
| Mis en surveillance (70ÔÇô89) | 1 |
| Ignor├®s (< 70) | 7 |

---

## D├®p├┤ts install├®s

### Ô£à open-gsd/get-shit-done-redux ÔÇö Score 100/100

- **URL** : https://github.com/open-gsd/get-shit-done-redux
- **├ëtoiles** : 1 383 Ô¡É
- **Cr├®├®** : 2026-05-22
- **Raison** : Score parfait ÔÇö skills, agents, commands Claude Code, 1383 ├®toiles, context engineering & meta-prompting
- **Install├®** :
  - 33 agents (`gsd-*`) ÔåÆ `.claude/agents/`
  - 67 commandes ÔåÆ `.claude/commands/gsd/`

### Ô£à UditAkhourii/adhd ÔÇö Score 90/100

- **URL** : https://github.com/UditAkhourii/adhd
- **├ëtoiles** : 378 Ô¡É
- **Cr├®├®** : 2026-05-25
- **Raison** : Skill tree-of-thought pruning avec divergence cognitive, topics `claude`, `claude-agent-sdk`
- **Install├®** :
  - 1 skill `adhd` ÔåÆ `.claude/skills/adhd/`

### Ô£à VILA-Lab/FigMirror ÔÇö Score 90/100

- **URL** : https://github.com/VILA-Lab/FigMirror
- **├ëtoiles** : 335 Ô¡É
- **Cr├®├®** : 2026-05-22
- **Raison** : 5 skills Claude Code natifs, outil de visualisation donn├®es style papers
- **Install├®** :
  - 5 skills ÔåÆ `.claude/skills/figmirror/`, `openspec-explore/`, `openspec-propose/`, `openspec-apply-change/`, `openspec-archive-change/`

---

## D├®p├┤ts en surveillance

### ­ƒæü op7418/guizang-social-card-skill ÔÇö Score 75/100

- **URL** : https://github.com/op7418/guizang-social-card-skill
- **├ëtoiles** : 315 Ô¡É
- **Cr├®├®** : 2026-05-27
- **D├®cision utilisateur** : Surveiller (pas encore install├®)
- **Raison** : Skill social media carousels niche (28 layouts, 10 th├¿mes)

---

## D├®p├┤ts ignor├®s

| D├®p├┤t | Ô¡É | Score | Raison |
|-------|-----|-------|--------|
| `cclank/lanshu-awesome-ai-video-kit` | 163 | 55 | Pas de structure .claude/ compl├¿te |
| `aref-vc/tufte-claude-skill` | 204 | 50 | Topics vides, skill sp├®cialis├®e |
| `OpenBMB/PilotDeck` | 517 | 40 | Pas de contenu Claude Code natif |
| `bryanyzhu/agentic-ai-system-course` | 273 | 30 | Ressource p├®dagogique g├®n├®rique |
| `study8677/awesome-architecture` | 591 | 25 | Aucun contenu Claude Code |
| `jianshuo/ccglass` | 317 | 15 | Proxy r├®seau, non installable |
| `XingYu-Zhong/DeepSeek-GUI` | 446 | ÔÇö | Filtr├® (hors th├¿me) |

---

## Nouvelles ressources disponibles

Apr├¿s cette veille, votre projet dispose de :

| Type | Nouvelles | Total estim├® |
|------|-----------|-------------|
| Agents | +33 (gsd-*) | ~50 |
| Commandes | +67 (gsd/*) | ~80 |
| Skills | +6 (adhd, figmirror, openspec├ù4) | ~20 |

---

## Prochaine veille recommand├®e

- **Date** : 2026-06-04 (dans 7 jours)
- **Th├¿mes ├á ajouter** : `mcp-server`, `openspec`
- **D├®p├┤ts ├á re-scorer** : `guizang-social-card-skill` (surveiller ├®volution)
- **Commande** : `/github-watch` ou `/loop 7d /github-watch`
