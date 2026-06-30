# claude-config

Configuration Claude Code de Samuel Chembah et **miroir versionné** de ses skills perso.
Samuel édite ses skills dans **claude.ai** (source canonique) ; GitHub les versionne et alimente
**Claude Code**. Sens de synchro réel : **claude.ai → GitHub → Claude Code** (voir
[`skill-sync`](claude-global/skills/samuel/skill-sync/SKILL.md)).

## Structure

```
claude-config/
└── claude-global/
    ├── intervals_icu.py        # Client API intervals.icu
    ├── sync_skills.py          # Routine de sync des skills (status / bundle / commit-manifest)
    └── skills/samuel/          # Skills perso (source de vérité)
        ├── .sync-manifest.json # Empreintes sha256 du dernier sync
        └── <skill>/SKILL.md
```

## Skills perso (29)

Source canonique : **claude.ai** (Samuel y travaille et y refactore ses skills). GitHub en est le
miroir versionné, qui alimente Claude Code. Noms majoritairement refactorés en français (juin 2026).

### Stratégie & business
| Skill | Rôle |
|-------|------|
| `rodin` | Contradicteur épistémique — autopsie profonde, décisions à fort enjeu |
| `contradicteur` | Contradicteur rapide multi-modes, faible enjeu (complément de Rodin) |
| `stratege` | Conseiller stratégique multi-projets (scaling, structuration, fiscalité…) |
| `first-principles-business` | Raisonnement par premiers principes |
| `modelisation-financiere` | Modèles financiers, projections, valorisation |
| `presentation-investisseur` | Pitch decks par objectif (investisseur, banque, client) |
| `page-de-vente` | Landing pages haute conversion |
| `recherche-leads` | Qualification & outreach de prospects |
| `marketing` | Frameworks marketing (PAS/AIDA/BAB, channel matrix) |
| `expert-automatisation` | Diagnostic & déploiement IA (interne + offre conseil) |
| `reseaux-sociaux` | Stratégie contenu (LinkedIn, YouTube, newsletter) |
| `avis-google` | Avis Google optimisés (points Local Guide) |

### RH & juridique
| Skill | Rôle |
|-------|------|
| `ressources-humaines` | Expert RH BTP — droit du travail, procédures disciplinaires |
| `rh-cv-apprenti-ia` | Analyse de CV pour recrutement profil IA/Tech |
| `divorce-patrimoine` | Droit de la famille — divorce, régime matrimonial |
| `aide-reponse-avocat` | Contentieux commercial & chantier (réponses à avocat adverse) |

### Sport & santé
| Skill | Rôle |
|-------|------|
| `training-ironman-2026` | Plans d'entraînement adaptatifs (triathlon, running, cycling) |
| `coach-mental-sport` | Coach mental profil tout-ou-rien |
| `coach-premier-marathon` | Coach course à pied, grande débutante (run/walk) |
| `planificateur` | Cohérence chronologique, tapers, récupérations, ACWR |
| `intervals-icu-samuel` | Charge d'entraînement via intervals.icu |

### Productivité & outils
| Skill | Rôle |
|-------|------|
| `ask-panel` | Panel des 4 IA via pont Notion, sans API |
| `checkpoint` | Génère un fichier de reprise de session |
| `import-devis-monday` | Import devis PDF OBAT → board Monday Chantiers |
| `notion-protocol` | Conventions d'écriture Notion (SNAPSHOT/LOG, texte brut) |
| `session-notion` | Work log automatique des sessions vers Notion |
| `skill-sync` | Routine de parité des skills via GitHub |
| `skill-sync-notion` | Sync Notion ↔ GitHub après MAJ d'un skill (tokens en env, jamais en dur) |
| `youtube-scraper` | Scrape chaînes YouTube → repos GitHub notés /100 + insights/outils |

## Synchroniser les skills

```bash
cd claude-global
python3 sync_skills.py status   # quels skills ont changé depuis le dernier sync ?
python3 sync_skills.py bundle   # zippe les skills modifiés -> dist/skills/ (import claude.ai)
python3 sync_skills.py commit-manifest   # fige l'état après un sync réussi
python3 sync_skills.py install   # lie les skills (à plat) dans ~/.claude/skills pour Claude Code
```

- **Claude Code (macOS/Linux)** : `install` une fois (symlink par skill), puis `git pull` suffit.
- **Claude Code (Windows)** : lancer `.\install_skills.ps1` (git pull + copie, sans Python ni admin). `sync_skills.py install` bascule aussi automatiquement en mode copie sous Windows.
- **claude.ai** : import manuel du `.zip` par skill modifié (Settings → Skills).

Détails et prompt de routine : [`skill-sync/SKILL.md`](claude-global/skills/samuel/skill-sync/SKILL.md).
