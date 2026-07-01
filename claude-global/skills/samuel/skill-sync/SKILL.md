---
name: skill-sync
description: >
  Maintient la parité des skills perso de Samuel entre claude.ai (source de vérité), Notion (relais)
  et Claude Code (consommateur), avec GitHub comme hub de distribution et d'historique.
  Exécute la migration one-time au premier run si le manifeste n'a pas de clé "migration_2026".
  Déclencheurs : sync skills, synchroniser skills, parité Claude AI / Claude Code, routine sync, skill-sync.
user-invocable: true
allowed-tools:
  - Read
  - Bash
  - mcp__github__get_file_contents
  - mcp__github__push_files
  - mcp__Notion__notion-fetch
---

# Skill Sync — parité des skills via GitHub

## Architecture canonique (alignée avec `skill-sync-notion`)

```
claude.ai  /mnt/skills/user/<skill>/     ← ÉDITION = SOURCE DE VÉRITÉ
    │  skill-sync-notion (MCP, immédiat)
    ▼
Notion "🧠 Skills Claude — Référentiel Samuel" (35734dfdcd3b8179b160fe16b555081a)  ← RELAIS
    │  routine Claude Code nocturne (Notion → commit)
    ▼
GitHub samuel16031978/claude-config · claude-global/skills/samuel/<skill>/  ← HUB distribution + historique
    │  git pull + symlinks
    ▼
Claude Code  ~/.claude/skills/<skill>/  ← CONSOMMATEUR
```

**Règle d'or : on n'édite JAMAIS un skill directement dans GitHub ou Claude Code.** Toute modif passe
par claude.ai (ou à défaut : modif locale → zip → ré-import claude.ai → MCP Notion, pour réaligner
immédiatement). En cas de divergence de contenu, **la version claude.ai/Notion prime toujours**.

**Asymétrie résiduelle :** claude.ai ne tire pas depuis GitHub. Le seul flux GitHub → claude.ai est
le ré-import manuel d'un zip (Settings → Skills) — nécessaire uniquement si un skill a été modifié
hors claude.ai (exception).

---

## Configuration

| Clé | Valeur |
|---|---|
| Repo | `samuel16031978/claude-config` · branche `main` |
| Source skills | `claude-global/skills/samuel/<skill>/` |
| Nommage canon | **noms FRANÇAIS** (`stratege`, `contradicteur`…) — jamais les anciens noms anglais |
| Manifeste | `claude-global/skills/samuel/.sync-manifest.json` (sha256 par skill) |
| Bundles | `claude-global/dist/skills/<skill>.zip` (gitignoré) |
| Helper | `claude-global/sync_skills.py` |
| Archive orphelins | `claude-global/skills/archive/` |

Aucun token ni secret dans ce skill. Push via MCP GitHub ou `git push` local.

---

## Helper `sync_skills.py`

```bash
cd claude-global
python3 sync_skills.py status           # inventaire DYNAMIQUE + détection modifs (hash vs manifeste)
python3 sync_skills.py bundle           # zippe les skills modifiés → dist/skills/
python3 sync_skills.py bundle --all     # zippe TOUS les skills présents (jamais de nombre codé en dur)
python3 sync_skills.py commit-manifest  # fige l'état après sync réussi
python3 sync_skills.py install          # symlinks ~/.claude/skills/<skill> → repo
```

---

## MIGRATION ONE-TIME — résorption du drift (à exécuter en premier, une seule fois)

État constaté (audit 06/2026) : 15 paires de renommage EN→FR, contenus divergents, skills présents d'un seul côté.

### M1 — Renommages (git mv, conserve l'historique)

| Ancien nom GitHub | Nouveau nom (canon) |
|---|---|
| balanced-samuel | contradicteur |
| c-level-samuel | stratege |
| rh-sc-renovations | ressources-humaines |
| maitre-horizon | divorce-patrimoine |
| social-media-samuel | reseaux-sociaux |
| session-notion-samuel | session-notion |
| ai-transformation-samuel | expert-automatisation |
| marketing-samuel | marketing |
| landing-page-samuel | page-de-vente |
| pitch-deck-samuel | presentation-investisseur |
| saas-financial-samuel | modelisation-financiere |
| lead-research-samuel | recherche-leads |
| coach-mental-sport-samuel | coach-mental-sport |
| planning-expert | planificateur |
| training-adaptatif | training-ironman-2026 |

### M2 — Contenus divergents

Pour chaque skill dont le hash diffère entre GitHub et Notion : **écraser le fichier GitHub avec la
version Notion** (reflet de claude.ai). Jamais l'inverse.

### M3 — Présents uniquement côté claude.ai/Notion

Créer le dossier + SKILL.md dans GitHub depuis le contenu Notion (frontmatter reconstruit depuis la description).

### M4 — Présents uniquement côté GitHub

Deux cas, à trier au cas par cas :
- **Skills Claude-Code-only assumés** (ex. outils dev/routines locales) → conserver, les tagger `code-only: true` dans le manifeste (exclus des rapports de parité claude.ai)
- **Vrais orphelins** (anciens skills abandonnés) → déplacer vers `claude-global/skills/archive/`

### M5 — Clore

`commit-manifest` + commit `sync: migration reverse claude.ai→GitHub <date>` + push. Renommer les
titres des pages Notion vers les noms FR. Marquer `"migration_2026": true` dans le manifeste — ne
jamais rejouer M1-M4.

---

## Protocole routine (régime permanent, exécution autonome)

1. **Pull** — `git pull origin main`
2. **Inventaire** — `sync_skills.py status` (liste dynamique ; signaler tout skill hors nommage FR)
3. **Parité** — comparer GitHub vs Notion (relais de claude.ai) :
   - Notion plus récent/divergent → écraser GitHub (M2)
   - GitHub modifié hors flux (exception) → `bundle` + rapport « ré-importer `dist/skills/<skill>.zip` dans claude.ai » + réaligner Notion
   - Skill supprimé côté Notion → archiver côté GitHub + signaler suppression claude.ai
4. **Install** — `sync_skills.py install` (symlinks ; requis seulement pour un NOUVEAU skill, les modifs passent par le pull)
5. **Figer + pousser** — `commit-manifest`, commit `sync: skills <YYYY-MM-DD> (<N> modifiés)`, push
6. **Rapport** — `reports/skills-sync-<YYYY-MM-DD>.md` : skills traités / mis à jour / créés / archivés / zips à ré-importer / erreurs

---

## Prompt de la routine (Claude Code → Routines)

```
Synchronise mes skills perso (skill claude-global/skills/samuel — architecture : claude.ai source de vérité, Notion relais, GitHub hub).
1. Si manifeste sans "migration_2026": exécute d'abord la MIGRATION ONE-TIME (M1→M5) du SKILL.md skill-sync.
2. git pull origin main
3. cd claude-global && python3 sync_skills.py status
4. Pour chaque skill : Notion divergent → écraser GitHub avec la version Notion. GitHub modifié hors flux → bundle + à ré-importer dans claude.ai.
5. python3 sync_skills.py install (si nouveau skill)
6. commit-manifest, commit "sync: skills <date> (<N> modifiés)", push.
7. Rapport reports/skills-sync-<date>.md + résumé (ou « tout est synchro »).
Ne committe jamais dist/ ni aucun secret. En cas d'erreur sur un skill : continuer les autres, lister en fin de rapport.
```

---

## Règles

- **claude.ai/Notion prime** sur GitHub en cas de conflit — GitHub est un hub, pas une source d'édition
- Nommage FR canon partout ; tout nom anglais résiduel = drift à corriger
- Jamais de nombre de skills codé en dur — inventaire toujours dynamique
- Ne jamais committer `dist/`, `.env.local`, ni token/secret
- Un skill modifié hors claude.ai = un seul geste manuel : ré-importer son zip
- Erreur sur un skill → continuer les autres, lister les échecs
