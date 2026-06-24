---
description: Veille technologique GitHub ÔÇö d├®tecte et installe automatiquement les nouvelles ressources Claude Code (cadence 48h)
model: sonnet
allowed-tools:
  - AskUserQuestion
  - Agent
  - Skill
  - WebFetch
  - Read
  - Write
  - Bash
---

# GitHub Watch ÔÇö Veille Technologique

Surveille GitHub pour d├®tecter les nouveaux d├®p├┤ts Claude Code pertinents et les installe automatiquement si le score d├®passe le seuil. Cadence : **toutes les 48h**.

Pour lancer en boucle : `/loop 48h /github-watch`

## Constantes

```
REPO_CIBLE      : Samuel16031978/Projet-Test
BRANCHE         : claude/code-best-practice-8X6zg
NOTION_PAGE_ID  : 36e34dfd-cd3b-817d-b4f1-ead30d95c86a
REGISTRE        : .claude/installed-repos.json
SEUIL_INSTALL   : 80
SEUIL_SURVEILLER: 60
```

## Execution Contract (non-negotiable)

Tu DOIS suivre les ├®tapes dans l'ordre. Interdit de :
- Sauter la v├®rification des mises ├á jour
- Installer sans scoring pr├®alable
- ├ëcraser un fichier existant dans .claude/
- Pousser sur une autre branche que `claude/code-best-practice-8X6zg`
- Installer un d├®p├┤t avec score < 80/100
- **Reconstruire ou r├®├®crire un fichier source depuis un r├®sum├® WebFetch ÔÇö INTERDIT**

### R├¿gle absolue : contenu original uniquement

Lors de l'installation de tout fichier (SKILL.md, AGENT.md, commande, plugin) :
1. Toujours r├®cup├®rer le contenu original avec `curl` ou `Bash` :
   ```bash
   curl -fsSL https://raw.githubusercontent.com/[owner]/[repo]/main/[chemin]
   ```
2. Si `curl` retourne une erreur, ne PAS reconstruire depuis un r├®sum├® WebFetch.
3. Si WebFetch r├®sume le contenu au lieu de le retourner verbatim, utiliser `Bash curl` ├á la place.
4. Un fichier non r├®cup├®rable verbatim doit ├¬tre marqu├® `pending` dans le registre ÔÇö jamais r├®├®crit de m├®moire.

## Vocabulaire impos├®

- "assistants" (jamais "agents")
- "outils" (jamais "skills")
- "raccourcis" (jamais "commands")

---

## ├ëtape 1 ÔÇö Mises ├á jour des outils install├®s

Lis le registre via GitHub MCP :
```
mcp__github__get_file_contents
  owner: Samuel16031978
  repo: Projet-Test
  path: .claude/installed-repos.json
  ref: refs/heads/claude/code-best-practice-8X6zg
```

Pour chaque d├®p├┤t list├®, appelle via WebFetch :
```
https://api.github.com/repos/[owner]/[repo]
```
Prompt : "Retourne pushed_at et stargazers_count"

Compare `pushed_at` avec `last_checked` :
- Si `pushed_at > last_checked` ÔåÆ **mise ├á jour disponible**
- Sinon ÔåÆ ├á jour

Met ├á jour `last_checked` (date du jour) pour tous les d├®p├┤ts et pousse via GitHub MCP.

---

## ├ëtape 2 ÔÇö Recherche (48 derni├¿res heures)

Adapte [DATE] ├á aujourd'hui - 2 jours. Lance ces 3 recherches en parall├¿le via WebFetch :

```
https://api.github.com/search/repositories?q=claude-code+created:>[DATE]&sort=stars&order=desc&per_page=15
https://api.github.com/search/repositories?q=topic:ai-agents+claude+created:>[DATE]&sort=stars&order=desc&per_page=10
https://api.github.com/search/repositories?q=mcp-server+claude+created:>[DATE]&sort=stars&order=desc&per_page=10
```

Prompt commun : "Retourne une liste JSON avec : full_name, description, stargazers_count, pushed_at, topics, html_url"

D├®doublonne les r├®sultats (certains d├®p├┤ts apparaissent dans plusieurs recherches).

---

## ├ëtape 3 ÔÇö Score de pertinence (sur 100 = 4 axes)

### Axe 1 ÔÇö Contenu Claude Code (35 pts max)

V├®rifie la structure du d├®p├┤t via WebFetch :
```
https://api.github.com/repos/[owner]/[repo]/contents/.claude
```

Points attribu├®s :
- Dossier `.claude/skills/` pr├®sent : **+20**
- Dossier `.claude/agents/` pr├®sent : **+10**
- Dossier `.claude/commands/` pr├®sent : **+5**
- Dossier `.claude-plugin/` pr├®sent (format marketplace officiel Anthropic) : **+20** *(non cumulable avec .claude/skills/)*

> ÔÜá´©Å Le format `.claude-plugin/` est le format natif du marketplace officiel Claude Code (ex: obra/superpowers). Il remplace `.claude/skills/` et doit recevoir le m├¬me score.

Si l'API retourne 403 (rate limit), d├®duis le score depuis la description et les topics.

### Axe 2 ÔÇö Qualit├® (25 pts max)

- Plus de 500 ├®toiles : **+15**
- Entre 100 et 500 ├®toiles : **+10**
- Moins de 100 ├®toiles : **+5**
- Dernier commit < 7 jours : **+10**

### Axe 3 ÔÇö Pertinence th├®matique (20 pts max)

- Topics incluent `claude-code` ou `claude` : **+10**
- Topics incluent `ai-agents`, `mcp` ou `mcp-server` : **+10**

### Axe 4 ÔÇö Pertinence personnelle Samuel (20 pts max)

**+20 pts** si le d├®p├┤t touche ├á (pertinence primaire) :
```
whatsapp, n8n, monday, webhook, automation, workflow,
btp, construction, chantier, renovation, devis, gantt, planning,
garmin, intervals, triathlon, running, cycling, swim,
training, ironman, marathon, endurance, linkedin, prospection, crm
```

**+10 pts** si pertinence secondaire :
```
email, calendar, pdf, signature, social-media, make, zapier,
api, accounting, invoice, scheduling
```

*(Maximum 20 pts au total pour cet axe ÔÇö pas de cumul primaire + secondaire)*

### Seuils de d├®cision

| Score | Action |
|---|---|
| ÔëÑ 80 | Ô£à Installer automatiquement |
| 60ÔÇô79 | ­ƒæü Surveiller (noter dans Notion) |
| < 60 | ÔØî Ignorer |

> **Note de calibrage** : Avec moins de 100 ├®toiles, le score max th├®orique est 70/100 (qualit├® = +15 au lieu de +25). Les seuils sont donc atteignables uniquement pour des d├®p├┤ts avec 100+ ├®toiles ET contenu Claude Code confirm├® ET pertinence personnelle.

> ­ƒÜ¿ **Priorit├® haute** : Si un MCP whatsapp, n8n, garmin ou intervals.icu est d├®tect├®, le signaler explicitement m├¬me si le score < 60.

---

## ├ëtape 4 ÔÇö Installation automatique (repos avec score ÔëÑ 80)

Pour chaque d├®p├┤t ├á installer :

**4a. Lister r├®cursivement TOUS les fichiers `.claude/`**

> ÔÜá´©Å Ne pas lister uniquement le niveau racine ÔÇö les agents et commands sont souvent dans des sous-dossiers.

Pour chaque sous-dossier connu (agents, commands, skills), lister r├®cursivement via WebFetch :
```
https://api.github.com/repos/[owner]/[repo]/git/trees/HEAD?recursive=1
```
Prompt : "Retourne tous les chemins commen├ºant par `.claude/` ÔÇö y compris les sous-dossiers (agents/analysis/, commands/workflows/, etc.)"

Si le d├®p├┤t utilise `.claude-plugin/`, m├¬me approche avec le pr├®fixe `.claude-plugin/`.

Construis la liste exhaustive de tous les fichiers `.md` ├á installer, class├®s par cat├®gorie :
- `.claude/agents/**/*.md` (tous niveaux)
- `.claude/commands/**/*.md` (tous niveaux)
- `.claude/skills/*/SKILL.md`
- `.claude/rules/*.md`

**4b. Pour chaque fichier de la liste exhaustive :**
1. V├®rifier qu'il n'existe PAS d├®j├á dans Samuel16031978/Projet-Test via GitHub MCP `get_file_contents`
2. Si absent : r├®cup├®rer le contenu **original** via Bash curl (JAMAIS via WebFetch r├®sum├®) :
   ```bash
   curl -fsSL https://raw.githubusercontent.com/[owner]/[repo]/main/.claude/[chemin]
   ```
3. Pousser via GitHub MCP `push_files` vers `claude/code-best-practice-8X6zg`
4. **Ne jamais ├®craser un fichier existant**
5. **Ne jamais reconstruire un fichier depuis un r├®sum├®** ÔÇö si curl ├®choue, marquer `pending`

**4c. V├®rification d'exhaustivit├® apr├¿s installation :**

Compte les fichiers install├®s vs la liste construite en 4a :
```
Attendus  : [N] fichiers (.md r├®cursif)
Install├®s : [N] fichiers
Conflits  : [N] fichiers existants ignor├®s
Manquants : [N] fichiers ni install├®s ni en conflit ÔåÆ signaler explicitement
```

Si des fichiers sont manquants (non couverts par un conflit d├®clar├®), les lister et proposer une action corrective.

**4d. Mettre ├á jour le registre** `.claude/installed-repos.json` :
Ajouter l'entr├®e avec : `name`, `url`, `installed_at`, `last_checked`, `stars_current`, `files_installed`, `conflicts`, `update_available: false`.
Pousser sur `claude/code-best-practice-8X6zg`.

---

## ├ëtape 5 ÔÇö Publication Notion

Ouvre la page Notion ID `36e34dfd-cd3b-817d-b4f1-ead30d95c86a`.
Ajoute en **t├¬te de page** (`position: start`) un bloc dat├® avec ce format exact :

```
## [DATE DU JOUR]

Ô¼å Mises ├á jour sur outils install├®s :
ÔÇó [nom] ÔÇö nouveau contenu depuis le [date]
(section absente si aucune)

Ô£à Install├®s automatiquement :
ÔÇó [nom] ÔÇö [ce qu'il fait concr├¿tement] ÔÇö Score [N]/100
  ÔåÆ Pourquoi utile pour toi : [raison personnelle si applicable]
(ou : Aucun ÔÇö seuil de 80 pts non atteint)

­ƒæü ├Ç surveiller (score 60ÔÇô79) :
ÔÇó [nom] ÔÇö [raison simple]
(ou : Aucun ce cycle)

ÔØî Ignor├®s : [N] projets

­ƒöì [MCP whatsapp/n8n/garmin/intervals.icu si trouv├® ÔÇö PRIORIT├ë HAUTE]

Prochaine veille : [DATE + 2 jours]

---
```

Etape non-bloquante : si Notion est inaccessible, signale l'erreur mais termine le workflow.

---

## Output Summary

Affiche en fin de session :
- Mises ├á jour d├®tect├®es sur les outils install├®s
- Nombre de d├®p├┤ts trouv├®s / analys├®s / install├®s
- Liste des installations avec score
- Liste des d├®p├┤ts ├á surveiller
- Confirmation de publication Notion (ou erreur non-bloquante)
- Prochaine veille recommand├®e
