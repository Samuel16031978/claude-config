# claude-config

Configuration Claude Code de Samuel Chembah et **source de vérité unique** de ses skills perso.
Ces skills sont maintenus identiques entre **Claude Code** et **Claude AI** (claude.ai) via la
routine [`skill-sync`](claude-global/skills/samuel/skill-sync/SKILL.md), avec GitHub au centre.

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

## Skills perso (25)

Source de vérité : `claude-global/skills/samuel/`. Synchronisés vers Claude Code et claude.ai par `skill-sync`.

### Stratégie & business
| Skill | Rôle |
|-------|------|
| `rodin` | Contradicteur intellectuel d'élite — déconstruction d'idées business |
| `c-level-samuel` | Conseiller stratégique multi-projets (scaling, structuration, fiscalité…) |
| `first-principles-business` | Raisonnement par premiers principes |
| `saas-financial-samuel` | Modèles financiers, projections, valorisation |
| `pitch-deck-samuel` | Pitch decks par objectif (investisseur, banque, client) |
| `landing-page-samuel` | Landing pages haute conversion (11 sections) |
| `lead-research-samuel` | Qualification & outreach de prospects |
| `marketing-samuel` | Frameworks marketing (PAS/AIDA/BAB, channel matrix) |
| `ai-transformation-samuel` | Diagnostic & déploiement IA (interne + offre conseil) |
| `social-media-samuel` | Stratégie contenu (LinkedIn, YouTube, newsletter) |
| `avis-google` | Avis Google optimisés (points Local Guide) |

### RH & juridique
| Skill | Rôle |
|-------|------|
| `rh-sc-renovations` | Expert RH BTP — droit du travail, procédures disciplinaires |
| `rh-cv-apprenti-ia` | Analyse de CV pour recrutement profil IA/Tech |
| `maitre-horizon` | Droit de la famille — divorce, régime matrimonial |
| `aide-reponse-avocat` | Courriers de réponse à avocat (dossier de litige) |

### Sport & santé
| Skill | Rôle |
|-------|------|
| `training-adaptatif` | Plans d'entraînement adaptatifs (triathlon, running, cycling) |
| `coach-mental-sport-samuel` | Coach mental profil tout-ou-rien |
| `planning-expert` | Cohérence chronologique, tapers, récupérations, ACWR |
| `intervals-icu-samuel` | Charge d'entraînement via intervals.icu |

### Productivité & outils
| Skill | Rôle |
|-------|------|
| `ask-panel` | Panel des 4 IA via pont Notion, sans API |
| `balanced-samuel` | 5 modes d'analyse rapide (TLDR/STEELMAN/DECISION/AUDIT/SOCRATIC) |
| `import-devis-monday` | Import devis PDF OBAT → board Monday Chantiers |
| `notion-protocol` | Conventions d'écriture Notion (SNAPSHOT/LOG, texte brut) |
| `skill-sync` | La routine de parité Claude Code ↔ Claude AI |
| `session-notion-samuel` | _(déprécié → voir `skill-sync`)_ |

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
