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

## Skills perso

| Skill | Rôle |
|-------|------|
| [`ask-panel`](claude-global/skills/samuel/ask-panel/SKILL.md) | Panel des 4 IA (ChatGPT/Gemini/DeepSeek) via pont Notion, sans API |
| [`balanced-samuel`](claude-global/skills/samuel/balanced-samuel/SKILL.md) | 5 modes d'analyse rapide (TLDR/STEELMAN/DECISION/AUDIT/SOCRATIC) |
| [`first-principles-business`](claude-global/skills/samuel/first-principles-business/SKILL.md) | Raisonnement par premiers principes pour décisions business |
| [`intervals-icu-samuel`](claude-global/skills/samuel/intervals-icu-samuel/SKILL.md) | Charge d'entraînement et séances via intervals.icu |
| [`marketing-samuel`](claude-global/skills/samuel/marketing-samuel/SKILL.md) | Cadres marketing personnels |
| [`skill-sync`](claude-global/skills/samuel/skill-sync/SKILL.md) | La routine de parité Claude Code ↔ Claude AI |
| [`training-adaptatif`](claude-global/skills/samuel/training-adaptatif/SKILL.md) | Plans d'entraînement adaptatifs |

## Synchroniser les skills

```bash
cd claude-global
python3 sync_skills.py status   # quels skills ont changé depuis le dernier sync ?
python3 sync_skills.py bundle   # zippe les skills modifiés -> dist/skills/ (import claude.ai)
python3 sync_skills.py commit-manifest   # fige l'état après un sync réussi
python3 sync_skills.py install   # lie les skills (à plat) dans ~/.claude/skills pour Claude Code
```

- **Claude Code** : `install` une fois (symlink par skill), puis `git pull` suffit pour mettre à jour le contenu.
- **claude.ai** : import manuel du `.zip` par skill modifié (Settings → Skills).

Détails et prompt de routine : [`skill-sync/SKILL.md`](claude-global/skills/samuel/skill-sync/SKILL.md).
