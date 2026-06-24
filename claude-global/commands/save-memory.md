---
name: save-memory
description: Sauvegarde le contexte de la session dans .claude/memory/ et commite dans git
model: sonnet
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Save Memory ÔÇö Fin de session

Met ├á jour les fichiers de m├®moire avec ce qui s'est pass├® dans cette session, puis commite.

## ├ëtape 1 ÔÇö R├®sume la session

Analyse la conversation courante et identifie :
- Ce qui a ├®t├® **construit ou modifi├®** (fichiers, configs, workflows)
- Les **d├®cisions** prises (nouvelles r├¿gles, choix techniques, seuils)
- L'**avancement** des projets actifs
- Les **prochains pas** concrets identifi├®s
- Les **blocages** rencontr├®s

## ├ëtape 2 ÔÇö Met ├á jour context.md

Lis `.claude/memory/context.md`, puis mets ├á jour :
- La date "Derni├¿re mise ├á jour"
- L'├®tat de chaque projet impact├® par cette session
- La section "Notes de session en cours" avec un r├®sum├® de 3ÔÇô5 lignes

```bash
# Date du jour
date +%Y-%m-%d
```

## ├ëtape 3 ÔÇö Ajoute dans decisions.md

Si de nouvelles d├®cisions importantes ont ├®t├® prises, ajoute une entr├®e dat├®e en t├¬te de `.claude/memory/decisions.md` :

```markdown
## [DATE]

- **[D├®cision]** ÔÇö [explication courte]
```

## ├ëtape 4 ÔÇö Met ├á jour le fichier projet concern├®

Si un projet sp├®cifique a avanc├®, mets ├á jour le fichier correspondant dans `.claude/memory/projects/` :
- Coche les t├óches accomplies
- Ajoute les blocages d├®couverts
- Met ├á jour les prochains pas

## ├ëtape 5 ÔÇö Commite et pousse

```bash
git add .claude/memory/
git commit -m "memory: session [DATE] ÔÇö [r├®sum├® 1 ligne]"
git push -u origin claude/code-best-practice-8X6zg
```

## Output

```
Ô£ô context.md mis ├á jour
Ô£ô decisions.md mis ├á jour (N nouvelles d├®cisions)
Ô£ô projects/[nom].md mis ├á jour
Ô£ô Commit├® et pouss├® : "memory: session [DATE] ÔÇö [r├®sum├®]"

Session r├®sum├®e en 3 lignes :
[ligne 1]
[ligne 2]
[ligne 3]
```
