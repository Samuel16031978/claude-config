---
name: skill-sync-notion
description: "Sync Notion ↔ GitHub après création/MAJ de skill : mise à jour page Notion + déclenchement routine Claude Code via API."
---

# Skill Sync Notion

## Rôle

Après création ou mise à jour d'un skill dans Notion, synchroniser automatiquement vers GitHub et maintenir la cohérence du référentiel.

## Configuration

- **Token Notion** : à lire depuis variable d'environnement `NOTION_TOKEN` — ne jamais stocker ici
- **Repo GitHub** : `samuel16031978/Projet-Test`
- **Branche cible** : `main`
- **Chemin** : `claude-global/skills/Samuel/<nom-skill>/SKILL.md`

## Protocole d'exécution (4 étapes)

1. **Lire** la page Notion du skill via `mcp__Notion__notion-fetch` (ID de la page)
2. **Vérifier** l'existence du fichier GitHub via `mcp__github__get_file_contents`
3. **Comparer** le contenu — si identique, skip ; si différent ou absent, pousser
4. **Pousser** via `mcp__github__push_files` avec message `sync: update <skill> from Notion [date]`

## Correspondance skill ↔ Notion

| Skill | Page Notion ID | Chemin GitHub |
|-------|---------------|---------------|
| rodin | (ID page Notion) | claude-global/skills/Samuel/rodin/SKILL.md |
| rh-sc-renovations | (ID page Notion) | claude-global/skills/Samuel/rh-sc-renovations/SKILL.md |
| session-notion-samuel | (ID page Notion) | claude-global/skills/Samuel/session-notion-samuel/SKILL.md |
| ... | ... | ... |

*Compléter la table au fur et à mesure des créations.*

## Routine Claude Code

Pour déclencher la sync depuis Claude Code CLI :

```bash
# Depuis le repo local
claude --skill skill-sync-notion "Sync skill <nom-skill> depuis Notion page ID <page-id>"
```

## Règles

- Ne jamais committer de token ou secret dans les fichiers
- En cas d'erreur sur un skill : continuer les autres, lister les erreurs à la fin
- Commit message format : `sync: update skills from Notion [YYYY-MM-DD]`
- Si plusieurs skills en même temps : batch dans un seul commit via `push_files`
