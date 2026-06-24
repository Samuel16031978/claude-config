---
name: load-memory
description: Charge le contexte persistant au d├®but d'une nouvelle session
model: sonnet
allowed-tools:
  - Read
  - Bash
---

# Load Memory ÔÇö D├®but de session

Charge et pr├®sente le contexte persistant pour reprendre l├á o├╣ on s'├®tait arr├¬t├®.

## ├ëtape 1 ÔÇö Lis tous les fichiers de m├®moire

```bash
# Contexte g├®n├®ral
cat .claude/memory/context.md

# D├®cisions r├®centes (10 derni├¿res)
head -50 .claude/memory/decisions.md

# Projets actifs
ls .claude/memory/projects/
```

Lis ensuite chaque fichier de projet dans `.claude/memory/projects/`.

## ├ëtape 2 ÔÇö Pr├®sente un briefing de session

Affiche un r├®sum├® structur├® et actionnable :

```
ÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöü
Bonjour Samuel ÔÇö Contexte charg├®
Derni├¿re session : [date]
ÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöü

ÔÜí PRIORITAIRE
[projet prioritaire + ├®tat + prochain pas]

­ƒôï EN COURS
ÔÇó [projet 2] ÔÇö [├®tat court]
ÔÇó [projet 3] ÔÇö [├®tat court]

­ƒÅâ SPORT
[├®tat entra├«nement + prochain objectif]

­ƒöº Outils install├®s depuis derni├¿re session
[si nouvelles installations]

­ƒÆ¼ Par o├╣ veux-tu commencer ?
ÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöüÔöü
```

## R├¿gle

- Toujours terminer avec "Par o├╣ veux-tu commencer ?" pour orienter la session
- Si les fichiers m├®moire sont vides ou absents, signaler et proposer `/save-memory` pour initialiser
