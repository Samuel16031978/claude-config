---
name: notion-watch-reporter
description: ├ëcrit un r├®sum├® de la veille GitHub sur une page Notion d├®di├®e, en langage simple pour n├®ophyte
allowed-tools:
  - Bash
  - Read
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-search
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-create-pages
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-update-page
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-fetch
---

# Notion Watch Reporter Skill

Publie le r├®sum├® de la veille GitHub sur une page Notion d├®di├®e, en langage clair et concis.

## Task

Re├ºois le rapport de veille (chemin du fichier markdown ou donn├®es directes), et ├®crit un bloc lisible sur la page Notion "Veille GitHub Claude Code".

## Param├¿tres re├ºus

Le contexte fournira :
- `report_date` : date de la veille (ex: 2026-05-28)
- `repos_found` : nombre de d├®p├┤ts trouv├®s
- `repos_installed` : liste des d├®p├┤ts install├®s avec leur score
- `repos_watching` : liste des d├®p├┤ts en surveillance
- `repos_ignored` : nombre de d├®p├┤ts ignor├®s
- `updates_available` : liste des d├®p├┤ts existants qui ont du nouveau contenu (peut ├¬tre vide)
- `next_watch_date` : date recommand├®e pour la prochaine veille (J+2)

## Instructions

### 1. Cherche la page Notion de veille

Utilise `notion-search` avec le terme "Veille GitHub Claude Code".

Si la page **existe** : r├®cup├¿re son ID via `notion-fetch`.

Si la page **n'existe pas** : cr├®e-la avec `notion-create-pages` :
```
Titre : Veille GitHub Claude Code
```

### 2. Analyse les fichiers r├®ellement install├®s

Pour chaque d├®p├┤t list├® dans `repos_installed`, inspecte ce qui a ├®t├® copi├® dans `.claude/` via Bash :

**Agents install├®s :**
```bash
# Extrait le champ description du frontmatter YAML de chaque agent
for f in .claude/agents/[pr├®fixe-repo]-*.md; do
  grep -m1 "^description:" "$f" | sed 's/description: //'
done
```

Regroupe les descriptions par th├¿me fonctionnel en utilisant ces cat├®gories simples :
| Mots-cl├®s dans la description | Cat├®gorie lisible |
|-------------------------------|-------------------|
| code, fix, review, debug, codebase | Correction et relecture de code |
| doc, write, document | R├®daction de documentation |
| research, domain, advisor | Recherche et veille |
| plan, roadmap, executor, framework | Planification et ex├®cution |
| audit, security, quality, verif | Contr├┤le qualit├® et s├®curit├® |
| ui, interface, design | Interface utilisateur |
| user, profil | Analyse utilisateur |

Produit une ligne par cat├®gorie : `N pour [cat├®gorie]`

**Skills install├®s :**
```bash
# Extrait la description du frontmatter de chaque SKILL.md
grep -m1 "^description:" .claude/skills/[nom-skill]/SKILL.md | sed 's/description: //'
```

Reformule la description en une phrase simple sans jargon.

**Commandes install├®es :**
```bash
ls .claude/commands/[pr├®fixe-repo]/ | wc -l
```

Indique simplement le nombre : `N raccourcis de commandes`.

### 3. Compose le r├®sum├® en langage simple

Le r├®sum├® doit ├¬tre **court** (8ÔÇô10 lignes max) et **compr├®hensible sans connaissance technique**.

Mod├¿le de texte ├á adapter :

```
J'ai scann├® GitHub et trouv├® [N] nouveaux projets li├®s ├á Claude Code.

Ô¼å Mises ├á jour disponibles ([N ou "aucune"]) :
ÔÇó [Nom projet] ÔÇö du nouveau contenu a ├®t├® ajout├® depuis l'installation du [date]
(section absente si aucune mise ├á jour)

Ô£à Nouveaux projets install├®s ([N]) :
ÔÇó [Nom projet] ÔÇö [description d├®taill├®e par cat├®gorie issue de l'├®tape 2] ÔÇö Pertinence [N]/100
ÔÇó [Nom projet] ÔÇö [description issue du SKILL.md reformul├®e simplement] ÔÇö Pertinence [N]/100

­ƒæü ├Ç surveiller ([N]) :
ÔÇó [Nom projet] ÔÇö [raison simple]

ÔØî Ignor├®s : [N] projets (pas assez pertinents)

Prochaine veille : [DATE]
```

**Exemple de description d├®taill├®e pour un d├®p├┤t avec agents :**
> 33 assistants sp├®cialis├®s (6 pour corriger/relire du code, 4 pour r├®diger de la documentation, 7 pour faire de la recherche, 5 pour planifier et ex├®cuter, 6 pour auditer la qualit├® et la s├®curit├®) + 67 raccourcis de commandes

**R├¿gles de vocabulaire :**
- "assistants" ou "outils" plut├┤t que "agents"
- "mod├¿les de t├óches" plut├┤t que "skills"
- "raccourcis de commandes" plut├┤t que "commands"
- "pertinence" plut├┤t que "score de relevance"
- ├ëviter les acronymes non expliqu├®s (LLM, MCP, SDK, etc.)
- Toujours expliquer ce qu'un projet fait concr├¿tement, cat├®gorie par cat├®gorie

### 4. Publie sur Notion

Utilise `notion-update-page` pour ajouter le bloc en haut de la page (les entr├®es r├®centes apparaissent en premier).

Le bloc ajout├® doit contenir :
- Un s├®parateur horizontal avant chaque nouvelle entr├®e
- La date en titre de section (heading 2)
- Le contenu du r├®sum├® en texte simple

### 5. Confirme la publication

Retourne :
```
Ô£ô R├®sum├® publi├® sur Notion ÔÇö page "Veille GitHub Claude Code"
  URL : [url de la page si disponible]
  Entr├®e du [date] ajout├®e en t├¬te de page
```

## R├¿gles

- Toujours chercher la page avant d'en cr├®er une nouvelle (├®viter les doublons)
- Jamais de jargon technique dans le texte publi├® sur Notion
- Le r├®sum├® doit pouvoir ├¬tre lu en moins de 30 secondes
- En cas d'erreur MCP, signaler mais ne pas bloquer la fin du workflow github-watch
