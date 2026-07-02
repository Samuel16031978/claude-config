---
name: notion-watch-reporter
description: Écrit un résumé de la veille GitHub sur une page Notion dédiée, en langage simple pour néophyte
allowed-tools:
  - Bash
  - Read
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-search
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-create-pages
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-update-page
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-fetch
---

# Notion Watch Reporter Skill

Publie le résumé de la veille GitHub sur une page Notion dédiée, en langage clair et concis.

## Task

Reçois le rapport de veille (chemin du fichier markdown ou données directes), et écris un bloc lisible sur la page Notion "Veille GitHub Claude Code".

## Paramètres reçus

Le contexte fournira :
- `report_date` : date de la veille (ex: 2026-05-28)
- `repos_found` : nombre de dépôts trouvés
- `repos_installed` : liste des dépôts installés avec leur score
- `repos_watching` : liste des dépôts en surveillance
- `repos_ignored` : nombre de dépôts ignorés
- `updates_available` : liste des dépôts existants qui ont du nouveau contenu (peut être vide)
- `next_watch_date` : date recommandée pour la prochaine veille (J+2)

## Instructions

### 1. Cherche la page Notion de veille

Utilise `notion-search` avec le terme "Veille GitHub Claude Code".

Si la page **existe** : récupère son ID via `notion-fetch`.

Si la page **n'existe pas** : crée-la avec `notion-create-pages` :
```
Titre : Veille GitHub Claude Code
```

### 2. Analyse les fichiers réellement installés

Pour chaque dépôt listé dans `repos_installed`, inspecte ce qui a été copié dans `.claude/` via Bash :

**Agents installés :**
```bash
# Extrait le champ description du frontmatter YAML de chaque agent
for f in .claude/agents/[préfixe-repo]-*.md; do
  grep -m1 "^description:" "$f" | sed 's/description: //'
done
```

Regroupe les descriptions par thème fonctionnel en utilisant ces catégories simples :
| Mots-clés dans la description | Catégorie lisible |
|-------------------------------|-------------------|
| code, fix, review, debug, codebase | Correction et relecture de code |
| doc, write, document | Rédaction de documentation |
| research, domain, advisor | Recherche et veille |
| plan, roadmap, executor, framework | Planification et exécution |
| audit, security, quality, verif | Contrôle qualité et sécurité |
| ui, interface, design | Interface utilisateur |
| user, profil | Analyse utilisateur |

Produit une ligne par catégorie : `N pour [catégorie]`

**Skills installés :**
```bash
# Extrait la description du frontmatter de chaque SKILL.md
grep -m1 "^description:" .claude/skills/[nom-skill]/SKILL.md | sed 's/description: //'
```

Reformule la description en une phrase simple sans jargon.

**Commandes installées :**
```bash
ls .claude/commands/[préfixe-repo]/ | wc -l
```

Indique simplement le nombre : `N raccourcis de commandes`.

### 3. Compose le résumé en langage simple

Le résumé doit être **court** (8–10 lignes max) et **compréhensible sans connaissance technique**.

Modèle de texte à adapter :

```
J'ai scanné GitHub et trouvé [N] nouveaux projets liés à Claude Code.

⬆ Mises à jour disponibles ([N ou "aucune"]) :
• [Nom projet] — du nouveau contenu a été ajouté depuis l'installation du [date]
(section absente si aucune mise à jour)

✅ Nouveaux projets installés ([N]) :
• [Nom projet] — [description détaillée par catégorie issue de l'étape 2] — Pertinence [N]/100
• [Nom projet] — [description issue du SKILL.md reformulée simplement] — Pertinence [N]/100

👁 À surveiller ([N]) :
• [Nom projet] — [raison simple]

❌ Ignorés : [N] projets (pas assez pertinents)

Prochaine veille : [DATE]
```

**Exemple de description détaillée pour un dépôt avec agents :**
> 33 assistants spécialisés (6 pour corriger/relire du code, 4 pour rédiger de la documentation, 7 pour faire de la recherche, 5 pour planifier et exécuter, 6 pour auditer la qualité et la sécurité) + 67 raccourcis de commandes

**Règles de vocabulaire :**
- "assistants" ou "outils" plutôt que "agents"
- "modèles de tâches" plutôt que "skills"
- "raccourcis de commandes" plutôt que "commands"
- "pertinence" plutôt que "score de relevance"
- Éviter les acronymes non expliqués (LLM, MCP, SDK, etc.)
- Toujours expliquer ce qu'un projet fait concrètement, catégorie par catégorie

### 4. Publie sur Notion

Utilise `notion-update-page` pour ajouter le bloc en haut de la page (les entrées récentes apparaissent en premier).

Le bloc ajouté doit contenir :
- Un séparateur horizontal avant chaque nouvelle entrée
- La date en titre de section (heading 2)
- Le contenu du résumé en texte simple

### 5. Confirme la publication

Retourne :
```
✓ Résumé publié sur Notion — page "Veille GitHub Claude Code"
  URL : [url de la page si disponible]
  Entrée du [date] ajoutée en tête de page
```

## Règles

- Toujours chercher la page avant d'en créer une nouvelle (éviter les doublons)
- Jamais de jargon technique dans le texte publié sur Notion
- Le résumé doit pouvoir être lu en moins de 30 secondes
- En cas d'erreur MCP, signaler mais ne pas bloquer la fin du workflow github-watch
