---
name: session-notion-samuel
description: "[DÉPRÉCIÉ] Ancienne routine de sync via pont Notion + déclencheur d'API. Remplacée par skill-sync (GitHub source de vérité). Conservée pour mémoire du workflow de mise à jour des skills."
---

# session-notion-samuel — DÉPRÉCIÉ

> ⚠️ **Ce skill est déprécié.** Sa mécanique d'origine (synchronisation via une page Notion
> relais + déclenchement d'une routine Claude Code par endpoint d'API avec token) a été
> remplacée par **`skill-sync`**, qui fait de **GitHub la source de vérité unique**.
>
> → Voir `../skill-sync/SKILL.md`.

## Pourquoi le remplacement

| Ancien design (ce skill) | Nouveau design (`skill-sync`) |
|--------------------------|-------------------------------|
| Notion = relais central | GitHub = source de vérité |
| Déclencheur d'API + token (401 récurrent) | `git pull` + helper `sync_skills.py`, sans secret |
| Écrasement direct de `/mnt/skills/user/` | `install` (symlink) côté Claude Code |

## Ce qui reste utile (mémoire de workflow)

Le **workflow de mise à jour d'un skill sport** reste valable et s'appuie désormais sur `ask-panel` :

1. Confronter les 4 voix IA via `ask-panel` (pont Notion, sans API) → consensus ≥ 3/4
2. Réécrire le `SKILL.md` concerné dans `claude-global/skills/samuel/<skill>/`
3. Commit + push sur GitHub (source de vérité)
4. `skill-sync` propage : `git pull` côté Claude Code, bundle `.zip` à ré-importer côté claude.ai

## Action recommandée

Ne plus invoquer ce skill. Utiliser `skill-sync` pour la synchronisation et `ask-panel` pour
la boucle de confrontation/notation.
