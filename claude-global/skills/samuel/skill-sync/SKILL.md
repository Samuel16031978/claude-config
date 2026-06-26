---
name: skill-sync
description: "Maintient la parité des skills perso de Samuel entre Claude Code et Claude AI (claude.ai), avec GitHub comme source de vérité unique. Détecte les skills modifiés, construit les bundles .zip à importer dans claude.ai, et écrit un rapport de sync. Déclencheurs : sync skills, synchroniser skills, parité Claude AI / Claude Code, routine sync, skill-sync."
user-invocable: true
allowed-tools:
  - Read
  - Bash
  - mcp__github__get_file_contents
  - mcp__github__push_files
---

# Skill Sync — parité des skills via GitHub

## Rôle

Garder **les mêmes skills perso entre Claude Code et Claude AI** (claude.ai / appli desktop).
GitHub (`samuel16031978/claude-config`) est la **source de vérité unique** : toute modif de skill
y est commitée, puis propagée vers les deux surfaces.

```
                ┌─────────────────────────────┐
                │   GitHub  claude-config      │  ← SOURCE DE VÉRITÉ
                │ claude-global/skills/samuel/ │
                └──────────────┬──────────────┘
                   git pull    │   bundle .zip
              ┌────────────────┴────────────────┐
              ▼                                  ▼
   ┌────────────────────┐            ┌────────────────────────┐
   │   Claude Code      │            │   Claude AI (claude.ai)│
   │ ~/.claude/skills/  │            │  Settings → Skills     │
   │  (auto: git pull)  │            │  (import .zip manuel)  │
   └────────────────────┘            └────────────────────────┘
```

**Asymétrie clé :** Claude Code peut tirer automatiquement depuis GitHub (`git pull`).
claude.ai **ne tire pas tout seul** depuis un repo : l'import d'un skill modifié reste un geste
manuel (1 zip à déposer dans Settings → Skills). La routine automatise tout *sauf* ce dépôt,
et produit la liste exacte des skills à ré-importer pour éviter de tout refaire à chaque fois.

## Configuration

| Clé | Valeur |
|-----|--------|
| Repo | `samuel16031978/claude-config` |
| Branche | `main` |
| Source des skills | `claude-global/skills/samuel/<skill>/` |
| Manifeste de dérive | `claude-global/skills/samuel/.sync-manifest.json` |
| Bundles générés | `claude-global/dist/skills/<skill>.zip` (gitignoré) |
| Helper | `claude-global/sync_skills.py` |

> Aucun token, aucune clé API n'est nécessaire ni stocké ici. Le push GitHub passe par le MCP
> GitHub (ou `git push` si exécuté en local).

## Helper `sync_skills.py`

```bash
cd claude-global
python3 sync_skills.py status           # liste les skills + détecte les modifs (hash vs manifeste)
python3 sync_skills.py bundle           # zippe uniquement les skills modifiés -> dist/skills/
python3 sync_skills.py bundle --all     # zippe les 6 skills
python3 sync_skills.py commit-manifest  # fige l'état courant dans le manifeste (après un sync réussi)
```

La détection repose sur un **sha256 du contenu** de chaque dossier skill (pas les dates, qui
mentent après un clone). Le manifeste versionné mémorise le dernier état synchronisé.

## Protocole de la routine (exécution autonome)

1. **Sync** — `git pull origin main` (récupère les dernières modifs de skills).
2. **Détecter** — `python3 claude-global/sync_skills.py status`. Si « synchro » → étape 6 (rien à faire).
3. **Empaqueter** — `python3 claude-global/sync_skills.py bundle` (zippe les skills modifiés).
4. **Rapport** — écrire `reports/skills-sync-<YYYY-MM-DD>.md` listant :
   - les skills modifiés depuis le dernier sync,
   - pour chacun, l'action : « ré-importer `dist/skills/<skill>.zip` dans claude.ai → Settings → Skills »,
   - les skills supprimés (à retirer aussi de claude.ai).
5. **Figer + pousser** — `commit-manifest`, puis commit `sync: skills <date> (<N> modifiés)` avec
   le manifeste à jour + le rapport. Pousser sur `main`.
6. **Confirmer** — afficher le résumé (skills à jour, ou liste des zips à ré-importer côté claude.ai).

> Côté **Claude Code** : aucune action manuelle. Le `git pull` de l'étape 1 suffit si
> `~/.claude/skills/samuel` pointe vers (ou est un checkout de) ce dossier du repo. Voir
> « Installation locale » plus bas.

## Prompt de la routine (à coller dans Claude Code → Routines)

```
Synchronise mes skills perso. Étapes :
1. git pull origin main
2. cd claude-global && python3 sync_skills.py status
3. Si des skills sont modifiés : python3 sync_skills.py bundle, puis écris
   reports/skills-sync-<date>.md avec la liste des .zip à ré-importer dans claude.ai.
4. python3 sync_skills.py commit-manifest
5. Commit (manifeste + rapport) et push sur main.
6. Dis-moi quels zip ré-importer dans claude.ai (Settings → Skills), ou « tout est synchro ».
Ne committe jamais dist/ (gitignoré) ni aucun secret.
```

## Installation locale (Claude Code de Samuel, une seule fois)

Pour que `git pull` suffise côté Claude Code, lier les skills perso au dossier Claude Code :

```bash
# Depuis le repo cloné en local
ln -s "$(pwd)/claude-global/skills/samuel" ~/.claude/skills/samuel
# ou, sans symlink : copier après chaque pull
# cp -r claude-global/skills/samuel/* ~/.claude/skills/
```

## Règles

- **GitHub est la seule source de vérité** : on ne modifie un skill que dans le repo, jamais
  directement dans claude.ai (sinon la modif est perdue au prochain sync).
- Ne jamais committer `dist/`, `.env.local`, ni aucun token/secret.
- Un skill modifié = un seul geste manuel : ré-importer son zip dans claude.ai.
- En cas d'erreur sur un skill : continuer les autres, lister les échecs dans le rapport.
- Format du commit : `sync: skills <YYYY-MM-DD> (<N> modifiés)`.
