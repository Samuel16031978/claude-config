# Plan — Livrable « Fiche de veille chaîne » → Notion

## Context

Le scraper `youtube_scraper.py` est **déjà construit et validé** (extraction repos GitHub oral+écrit, notation /100 sur 4 axes, insights, outils, support vidéos **et** shorts, cookies auth, anti-throttle/anti-runaway — branche `claude/youtube-scraper-github-26iaoq`, PR #6). Ce qui manque : **définir ce que Samuel reçoit** quand il donne une chaîne. Aujourd'hui `scrape` ne renvoie qu'un statut technique brut ; la richesse dort dans les JSON.

**Décisions Samuel (ce tour) :**
- **Livrable = Notion** : une **base de données récap « Chaînes scannées »** (1 ligne = 1 chaîne), chaque ligne portant un résumé (score top, nb repos…) et **son contenu de page = la fiche complète**. En Notion, *une ligne de base EST une page* → le « lien vers une sous-page par chaîne » est natif (la ligne ouvre la fiche).
- **Emplacement** : une **nouvelle page racine dédiée** `📺 Veille YouTube (Scraper)` contenant la base + un mode d'emploi.
- **Périmètre** : **vidéos + shorts fusionnés** (triés par date, dédupliqués).
- **Profondeur** : **synthèse + annexe par vidéo**.

**Résultat visé** : Samuel donne une URL de chaîne → une fiche structurée apparaît dans Notion (et un récap en chat), réutilisable et archivée, sans friction.

## Répartition des responsabilités (clé)

- **Python (`youtube_scraper.py`)** = données + scoring + **génération de la fiche** (Markdown) et d'un **payload JSON** de propriétés. Aucune clé externe, stdlib only (cohérent avec `intervals_icu.py`).
- **Agent (skill) via Notion MCP** = **livraison Notion** (créer la page racine + la base une fois, puis upsert d'une ligne + contenu par scan). Pas de clé Notion dans le code. Respecte la règle sécurité et la leçon CLAUDE.md sur les connecteurs.

## Changements de code

### 1. Fusion vidéos + shorts — `youtube_scraper.py`
- Nouveau helper `_extract_channel_entries(yt_dlp, flat_opts, url)` qui réutilise `_extract_channel_listing` (déjà robuste : `/videos` → fallback URL brute) **et** liste aussi l'onglet `…/shorts`, fusionne via `_flatten_entries`, **déduplique par id** (certaines chaînes ex. @ia_irl recouvrent les deux onglets).
- Marquer la provenance : `format = "short"` si l'entrée vient de `/shorts` (ou durée ≤ 180s), sinon `"video"`.
- Dans `cmd_scrape` : remplacer l'appel unique par ce helper ; conserver la sélection « N plus récents » en **triant les vidéos analysées par `upload_date` décroissant** avant de couper à `--max` (l'ordre inter-onglets n'est fiable qu'après extraction détaillée). Garder le garde-fou `fail_streak`/`none_streak`.
- Stocker `format` dans chaque enregistrement vidéo du channel JSON ; exposer `video_count`/`short_count`.

### 2. Nouvelle commande `report <channel|slug>` — `youtube_scraper.py`
- `cmd_report(args)` lit le channel JSON + `repos-scored.json` + `tools-seen.json` et produit, selon `--format md|json|both` (défaut `both`) :
  - **JSON de propriétés** (pour mapper aux colonnes Notion) : `chaine, url, date_scan, periode (max→min upload_date), nb_videos, nb_shorts, repos[{url,score,verdict,axes,found_in}], top_repo, top_score, verdict_top, themes_dominants[], top_outils[], nb_insights`.
  - **Fiche Markdown** (sections, dans l'ordre des priorités d'origine) :
    1. En-tête (chaîne · période · N vidéos / M shorts)
    2. `🏆 Repos GitHub notés /100` — table triée (repo · score · verdict · axes C/Q/T/P · vidéo source). Repos = union des `github_repos` des vidéos de la chaîne, jointe à `repos-scored.json`.
    3. `💡 Insights clés` — top par `relevance`, groupés par thème (ia/entrepreneuriat/mindset).
    4. `🛠️ Stack & outils cités` — agrégé (depuis `tools-seen.json`, filtré sur les vidéos de la chaîne).
    5. `🔒 Vidéos non-publiques à creuser` — depuis le bucket `videos_non_publiques`.
    6. `📋 Annexe — par vidéo` — ligne compacte : `[date] [format] Titre · source · repos · outils · top insight`.
- Ajouter le sous-parseur `report` (arg positionnel chaîne/slug + `--format`). Réutilise `_slug`, `_read_json`, `_verdict`.

### 3. Doc — `skills/samuel/youtube-scraper/SKILL.md`
- Nouvelle section **« Livrable : fiche de veille → Notion »** décrivant le flux que l'agent exécute :
  1. **Bootstrap (1×)** : créer la page racine `📺 Veille YouTube (Scraper)` puis la base récap (schéma ci-dessous) ; mémoriser les ids dans `data/youtube-scrapes/.notion.json` (gitignoré).
  2. **Par scan** : `scrape <url>` (vidéos+shorts) → `report --format both` → **upsert** d'une ligne (rechercher la chaîne par titre ; créer sinon mettre à jour) avec les propriétés, puis **contenu de la page = la fiche Markdown** (`notion-update-page replace_content`). Idempotent : re-scan = mise à jour, pas de doublon.
  3. Rendre l'URL de la page Notion à Samuel + un récap en chat.

### 4. Persistance ids Notion — `data/youtube-scrapes/.notion.json` (gitignoré)
- `{root_page_id, database_id, data_source_id}` pour réutiliser la même base d'un scan à l'autre. Couvert par la règle gitignore existante `data/youtube-scrapes/*.json` (exception seulement pour `projets-samuel.json`).

## Schéma de la base récap (Notion, via `notion-create-database`)

```sql
CREATE TABLE (
  "Chaîne" TITLE,
  "URL chaîne" URL,
  "Date scan" DATE,
  "Période" RICH_TEXT,
  "Vidéos" NUMBER,
  "Shorts" NUMBER,
  "Repos trouvés" NUMBER,
  "Top repo" URL,
  "Top score" NUMBER,
  "Verdict top" SELECT('🔥':red,'✅':green,'🟡':yellow,'⚪':gray),
  "Thèmes" MULTI_SELECT('ia':blue,'entrepreneuriat':orange,'mindset':purple,'dev':gray),
  "Top outils" RICH_TEXT
)
```
Le **contenu** de chaque ligne-page = la fiche Markdown (synthèse + annexe). Vue par défaut triée par `Date scan` desc ; vue secondaire triée par `Top score` desc.

## Fichiers touchés

| Fichier | Action |
|---|---|
| `claude-global/youtube_scraper.py` | `_extract_channel_entries` (videos+shorts), tri par date dans `cmd_scrape`, `cmd_report` + sous-parseur, champ `format` |
| `claude-global/skills/samuel/youtube-scraper/SKILL.md` | section livrable + flux Notion |
| `claude-global/data/youtube-scrapes/.notion.json` | (gitignoré) ids Notion persistés par l'agent |
| Notion (via MCP, pas de fichier) | page racine `📺 Veille YouTube (Scraper)` + base récap |

## Exécution Notion — page racine fournie par Samuel

Le bootstrap auto a été bloqué (écritures MCP `requires approval`). Samuel a créé manuellement la page
racine et fourni son URL : **`38e34dfdcd3b80759e17f8e93e91d979`** (page vide « Nouvelle page »).

Étapes restantes (écritures MCP Notion) :
1. **Renommer/poser** la page racine en `📺 Veille YouTube (Scraper)` + intro (`notion-update-page`).
2. **Créer la base** « Chaînes scannées » sous cette page (`notion-create-database`, parent `page_id` =
   `38e34dfdcd3b80759e17f8e93e91d979`, schéma de la section précédente). Récupérer `data_source_id`.
3. **Upsert @ia_irl** : `report ia-irl --format both` → créer la ligne (propriétés mappées) + contenu de
   page = `markdown` (déjà validé : Ponytail 50/100, gpt ×23, 8 vidéos). Idempotent.
4. Persister `{root_page_id, database_id, data_source_id}` dans `data/youtube-scrapes/.notion.json` (gitignoré).
5. Rendre l'URL de la base + de la fiche à Samuel.

Si les écritures restent bloquées, repli : commiter la fiche dans `reports/veille-youtube/<slug>.md`.

## Vérification (bout en bout)

1. `python3 youtube_scraper.py scrape https://youtube.com/@ia_irl --max 5` → vérifier vidéos **et** shorts fusionnés, triés par date, champ `format` présent.
2. `python3 youtube_scraper.py report ia-irl --format md` → fiche Markdown complète (6 sections) ; `--format json` → payload de propriétés cohérent.
3. Bootstrap Notion : créer la page racine + base ; vérifier le schéma via `notion-fetch`.
4. Upsert ligne @ia_irl (propriétés + contenu fiche) ; ouvrir la page → table repos + sections rendues.
5. Re-scan @ia_irl → la **même ligne** est mise à jour (pas de doublon) ; contenu rafraîchi.
6. Scénario sans repo (ex. `@kagoa_camp`) → fiche correcte avec « Repos : aucun », outils/insights vides, pas de faux positif.
7. `.notion.json` bien gitignoré (`git check-ignore`).
