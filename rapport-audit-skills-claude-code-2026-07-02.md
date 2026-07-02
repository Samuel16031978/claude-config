[← README](README.md)

# Rapport d'audit — Skills Claude Code (hors claude.ai)

> Date : **2026-07-02** · Périmètre : skills **Claude Code only** du dépôt `claude-config`
> (lots claude-flow v3, agentdb, swarm, github-\*, openspec, flow-nexus + perso). Les **23 skills
> claude.ai** (nommage FR) sont **hors audit** (source de vérité = `/mnt/skills/user/` sur claude.ai,
> synchronisés 02/07/2026) : seuls leurs **deltas Notion→repo** sont traités (§4).

## Résumé exécutif

- **Corrigés (commits) :** 3 — `intervals-icu-samuel`, `notion-watch-reporter` (mojibake UTF-8),
  `rodin` (delta Notion appliqué).
- **Secrets en dur :** **0** détecté sur tout le périmètre (scan élargi : `sk-`, `ntn_`, `ghp_`,
  `xoxb-`, `AKIA`, clés PEM, `Bearer`, `api_key=…`). Rien à purger.
- **Sains :** les 30 skills des lots génériques (contenu éditeur tiers : claude-flow, AgentDB,
  flow-nexus…), + 5 perso (`ask-panel`, `notion-protocol`, `import-devis-monday`,
  `rh-cv-apprenti-ia`, `first-principles-business`).
- **Doublon à trancher :** `protocole-panel` ×2 sur Notion (§3).
- **Candidats archivage :** `weather-fetcher`, `weather-svg-creator`, `time-skill` (skills démo).

## 1. Table d'audit

### 1a. Skills perso (les seuls réellement rédigés par Samuel)

| Skill | Verdict | Corrections | Hypothèses / non vérifiés |
|---|---|---|---|
| `intervals-icu-samuel` | **corrigé** | Réécrit en UTF-8 propre (mojibake + BOM supprimés). Réfs obsolètes corrigées : `training-adaptatif`→`training-ironman-2026`, `planning-expert`→`planificateur` (validé par le référentiel Notion). | Athlete ID `i171091`, FC max 191, facteurs TRIMP : non re-vérifiés (données perso, plausibles). |
| `notion-watch-reporter` | **corrigé** | Réécrit en UTF-8 propre (mojibake + BOM sur tout le fichier, y compris frontmatter et emojis). | — |
| `rodin` | **corrigé** | Ajout de la section « Rôle dans le Panel 4 IA » présente sur la source Notion (02/07), absente du repo depuis le sync 27/06. Frontmatter préservé. | Skill claude.ai → traité en §4 (delta), pas réécrit. |
| `ask-panel` | **sain** | — | Réfère la page Notion `…8175…` comme autoritaire → cohérent avec le choix du doublon (§3). 4 fichiers `references/` présents. Migration `ask_panel.py`→pont Notion correcte (script bien absent). |
| `notion-protocol` | **sain** | — | — |
| `import-devis-monday` | **sain** (gap auto-documenté) | — | Réfère `scripts/parse_obat_pdf.py` + `build_monday_mutations.py` **absents du dépôt** — le skill le signale lui-même. Board Monday `2134855206` et IDs de colonnes : [NON VÉRIFIÉ] (API Monday non appelée). |
| `first-principles-business` | **sain** | — | Raccourcis `/fp`, `/vision`… = conventions internes, pas des slash-commands Claude Code réelles (conforme au design). |
| `rh-cv-apprenti-ia` | **sain** | — | Titre interne EN « HR-AI Strategy Expert » cohabite avec `name` FR — acceptable (prompt de rôle). |

### 1b. Lots génériques (contenu éditeur tiers — importés 06/06, jamais déployés sur claude.ai)

| Lot | Skills | Verdict | Note |
|---|---|---|---|
| claude-flow v3 | `v3-*` (9) | **sain** | Version cible `v3.0.0` : cohérente en interne (docs vendeur). Aucun secret, aucune réf FR cassée. |
| AgentDB | `agentdb-*` (5) | **sain** | Épingle `AgentDB v1.0.7+` / `agentic-flow v1.5.11+` = minimums vendeur, dates d'exemple. [NON VÉRIFIÉ] via web (faible enjeu). |
| Swarm | `swarm-advanced`, `swarm-orchestration` | **sain** | `claude-flow@alpha`, `Last Updated 2025-10-19` (métadonnées vendeur). |
| GitHub | `github-*` (6) | **sain** | Volumineux (jusqu'à 1262 l.) mais cohérents ; pas de fait Samuel-spécifique périmé. |
| OpenSpec | `openspec-*` (4) | **sain** | Concis, pas d'anomalie. |
| Flow Nexus | `flow-nexus-*` (3) | **sain** | Dates/timestamps = exemples de payloads. `v1.0.0 (2025-10-19)`. |

> **Pourquoi « sain » sans réécriture des lots :** ce sont des skills d'éditeurs tiers (non rédigés
> par Samuel). Les densifier « −30-40 % » reviendrait à réécrire de la doc vendeur qu'il ne maintient
> pas. Le contrôle utile a été fait : **0 secret**, **0 référence FR cassée**, **0 fait perso périmé**.
> Une densification n'apporterait pas de valeur et risquerait d'introduire des erreurs.

### 1c. Candidats archivage (skills démo, à ne pas supprimer — juste taggés)

| Skill | Emplacement | Raison |
|---|---|---|
| `weather-fetcher` | `claude-code-best-practice/.claude/skills/` | Skill jouet (démo météo). |
| `weather-svg-creator` | idem | Skill jouet (démo SVG). |
| `time-skill` | idem | Skill jouet (démo heure). |

## 2. Secrets purgés

**Aucun.** Le scan élargi (patterns `sk-…`, `ntn_…`, `ghp_/gho_`, `xoxb-`, `AKIA…`, blocs PEM,
`Bearer …`, `api_key=/token=`) sur les 30 lots + 8 skills perso n'a **rien remonté**. Bonne hygiène :
les clés passent par `.env.local` (intervals) et par le MCP Notion (aucune clé dans le code).

## 3. Doublon à trancher (Notion — pas de suppression sans validation)

`protocole-panel` existe en **2 pages Notion, au contenu identique** :

| Page | Icône | ID | Décision proposée |
|---|---|---|---|
| ⚖️ protocole-panel | ⚖️ | `37d34dfd-cd3b-8175-b952-d837fd01271b` | **GARDER** — page citée comme autoritaire par `ask-panel/SKILL.md` ; bloc de code mieux formaté. |
| 🤝 protocole-panel | 🤝 | `37d34dfd-cd3b-816e-9831-c1ed00e6faa3` | **SUPPRIMER** — copie redondante, aucune perte de contenu. |

> Anomalie connexe signalée par le référentiel : la page **« Session 24/06/2026 »**
> (`38934dfd-cd3b-8143-83f4-cd29797adb10`) est rangée sous le référentiel des skills au lieu du Work
> Log → à déplacer (housekeeping Notion, hors dépôt).

## 4. Deltas Notion → repo pour les 23 skills claude.ai

**Contexte :** source de vérité = `/mnt/skills/user/` sur claude.ai (audit « 5 vagues » terminé
02/07/2026), miroir Notion synchronisé le 02/07. Le repo a été reverse-syncé pour la dernière fois le
**27/06** (commit `631a467`) → fenêtre de delta de 5 jours.

**Delta appliqué (1) :**
- `rodin` — section « Rôle dans le Panel 4 IA » (présente Notion 02/07, absente repo) → **ajoutée**,
  frontmatter préservé. Commit `sync(rodin): …`.

**Limite pour les 22 autres — [HYPOTHÈSE de méthode] :** un pull massif Notion→repo est **risqué et
non fait** ici, pour deux raisons :
1. **Les pages Notion ne contiennent pas le frontmatter YAML** (`name` + `description`/déclencheurs
   vivent dans les propriétés de page, pas dans le corps). Une copie naïve **écraserait les
   déclencheurs** et casserait le skill. Toute reprise doit être un **merge additif préservant le
   frontmatter** (méthode appliquée à `rodin`).
2. La **vraie** source est `/mnt/skills/user/` sur claude.ai, **non atteignable** depuis cet
   environnement ; Notion n'en est qu'un miroir documentaire.

→ **Recommandation :** réconcilier les 22 restants via la routine dédiée `skill-sync-notion`
(claude.ai↔GitHub, consciente du frontmatter) plutôt qu'à la main. Le repérage de delta est faisable
page par page (comme démontré sur `rodin` et `intervals`), mais l'application en masse doit passer par
l'outil de sync pour ne pas dégrader les 23 skills exclus de l'audit.

## Annexe — orphelins constatés

- `~/.claude/skills/Samuel/` (casse **majuscule**) contient encore 4 dossiers hérités
  (`first-principles-business`, `marketing-samuel`, `skill-sync-notion`, `training-adaptatif`) : restes
  d'installation avant l'unification en `samuel/` minuscule. Côté **install** (pas le dépôt) → à nettoyer
  via `sync_skills.py install`, sans impact sur GitHub.
- `NutriTrack` (`add-query`, `add-screen`) : listés « Claude Code only » au référentiel mais **absents
  de ce dépôt** (projet séparé). Orphelins vis-à-vis de `claude-config`.
