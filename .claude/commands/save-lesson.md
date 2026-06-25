---
description: Enregistrer une leçon apprise dans CLAUDE.md après une erreur ou correction
allowed-tools: Read, Edit, Bash
---

## Contexte

!`date +%Y-%m-%d`
!`grep -n "Leçons apprises" CLAUDE.md 2>/dev/null || echo "section absente"`

## Instructions

Ajoute une entrée dans la section **"Leçons apprises"** de `CLAUDE.md` :

```
- [DATE] sujet : leçon précise
```

Exemples :
```
- 2026-05-29 Drizzle JSON fields : toujours JSON.parse() sur allergies et dietary_prefs
- 2026-05-29 Expo Router tabs : mettre à jour _layout.tsx quand on ajoute un onglet
```

Si la section "Leçons apprises" n'existe pas dans `CLAUDE.md`, la créer avant la première section existante.

Après modification, committe `CLAUDE.md` pour que la leçon persiste entre sessions et appareils.
