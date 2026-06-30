---
name: youtube-scraper
description: >
  Explore les chaînes YouTube de youtubeurs (IA, automatisation, entrepreneuriat, mindset) pour en
  extraire les repos GitHub cités — même à l'oral — et les noter sur 100 points selon la grille de Samuel.
  Extrait aussi des insights (IA/entrepreneuriat/mindset) et les outils/technos cités, notés par pertinence.
  DÉCLENCHE ce skill dès que Samuel : donne une URL YouTube ou un nom de youtubeur à analyser ;
  demande "les repos github d'un youtubeur", "quels repos valent le coup", "pépites github", "scoring github",
  "note ce repo", "100 points" ; demande les "insights", "phrases-clés", "quels outils il utilise", "sa stack",
  "technos citées" ; demande "les nouvelles vidéos" d'une chaîne déjà scannée.
---

# YouTube Scraper → GitHub /100 — Skill Samuel

## Rôle

La **vidéo est un canal de découverte ; le repo GitHub est l'objet noté.** Le livrable principal = une liste
de repos GitHub classés sur **100 points** (4 axes), prêts à explorer/installer. En second, l'outil extrait
et note par pertinence les **insights** (IA/entrepreneuriat/mindset) et les **outils/technos** cités.

Toutes les opérations passent par `youtube_scraper.py` (lancé depuis `claude-global/`).

## ⚠️ Avant toute évaluation de pertinence

**Lis `claude-global/.claude/memory/scoring-profile.md`** — il décrit le **moteur /100 (3 axes)**, les **2
verdicts** (Outil-à-installer / Idée-à-approfondir), les **4 destinations** et la règle de confiance. Les listes
vivantes (domaines de veille, projets actifs, outils manquants) sont dans
`data/youtube-scrapes/projets-samuel.json` (source unique, éditable).

## Configuration

```
Script   : claude-global/youtube_scraper.py
Profil   : claude-global/.claude/memory/scoring-profile.md  (méthodologie)
Listes   : claude-global/data/youtube-scrapes/projets-samuel.json  (source unique AXE 3/4)
Optionnel: .env.local → GITHUB_TOKEN (5000 req/h vs 60), YOUTUBE_API_KEY
Membres  : .env.local → YOUTUBE_COOKIES=cookies.txt (ou YOUTUBE_COOKIES_FROM_BROWSER=chrome)
           → débloque la transcription des vidéos non-publiques (membres / non répertoriées)
Dépendance: yt-dlp (pip install -r requirements.txt) — requis pour `scrape` uniquement
```

### Vidéos publiques vs non-publiques

`--max N` compte les vidéos **publiques** retenues, dans l'ordre « plus récentes d'abord ». Les vidéos
**non-publiques** (membres / non répertoriées, `availability ≠ public`) ne volent pas de slot et ne décalent
pas le classement : elles sont listées à part sous `videos_non_publiques` — **souvent le contenu le plus
pointu**. Pour les analyser : cookies authentifiés (transcription complète) ou `--include-hidden`
(titre + description seulement). Si YouTube renvoie `status: throttle` (métadonnées dégradées,
fréquent sans runtime JS), réessaie plus tard, plus espacé, ou avec des cookies.

## Opérations disponibles

### 1. Scraper une chaîne (découverte + scoring)
```bash
python3 youtube_scraper.py scrape <url> [--max N | --months N | --since YYYY-MM-DD] [--refresh] [--include-hidden]
```
Extrait les vidéos → repos GitHub → score chaque repo /100 → maj manifest. `--refresh` ignore le cache.
`--include-hidden` analyse aussi les vidéos non-publiques (sinon listées à part).
**Fenêtre temporelle** : `--months N` (N derniers mois) ou `--since YYYY-MM-DD` garde **tout** l'intervalle
(vidéos + shorts) et ignore `--max`. Sans fenêtre, `--max N` garde les N plus récents toutes catégories.

`<url>` accepte : chaîne (`@handle`, `/channel/…`), onglet `/videos` ou `/shorts`, **lien direct** d'une
vidéo (`youtu.be/…`, `watch?v=…`) ou d'un **short** (`/shorts/<id>`). Scraper une chaîne par `@handle`
**fusionne vidéos + shorts** (dédupliqués, triés par date → les N plus récents toutes catégories) ; pour
restreindre, passe `…/videos` ou `…/shorts`. Le même pipeline traite tout, avec ou sans lien GitHub
(insights + outils sont extraits dans tous les cas). Chaque vidéo porte un champ `format` (video|short).

### 2. Résumé du dernier scrape
```bash
python3 youtube_scraper.py status
```

### 3. Repos notés, filtrables
```bash
python3 youtube_scraper.py repos [--min-score 60] [--axe qualite|pertinence|integrabilite]
```
Triés par score /100 (ou par axe si `--axe`).

### 4. Score par topic des vidéos
```bash
python3 youtube_scraper.py topics [--topic ia|entrepreneuriat|mindset|dev]
```

### 5. Insights extraits (phrases-clés notées)
```bash
python3 youtube_scraper.py insights [--topic ia|entrepreneuriat|mindset] [--min-score 6]
```

### 6. Outils & technos cités (stacks tendance)
```bash
python3 youtube_scraper.py tools [--min-score 5]
```

### 7. Nouveautés depuis le dernier scan
```bash
python3 youtube_scraper.py new
```

### 8. Noter un repo GitHub isolé (hors YouTube)
```bash
python3 youtube_scraper.py score <github_url> [--refresh]
```

### 9. Générer la fiche de veille (livrable)
```bash
python3 youtube_scraper.py report <slug> [--format md|json|both]
```
`md` = fiche Markdown lisible ; `json` = payload de propriétés (mapping Notion) ; `both` (défaut) = JSON
incluant la fiche sous la clé `markdown`. La fiche = repos /100 (2 verdicts) · idées à approfondir · insights
taggés · **chaînes liées (à scraper plus tard)** · vidéos non-publiques · annexe par vidéo.

**Découverte de chaînes liées** : au `scrape`, l'outil détecte les chaînes annexes/complémentaires du
youtubeur (URLs de chaîne + `@handles` dans les descriptions + onglet « en vedette »), hors chaîne courante,
exposées dans `chaines_liees` → une file « à scraper plus tard » (la veille s'auto-alimente par effet de réseau).

## Livrable : fiche de veille → Notion

**Quand Samuel donne une chaîne**, le livrable est une **fiche de veille dans Notion**, dans la base récap
de la page racine `📺 Veille YouTube (Scraper)`. En Notion, *une ligne de base EST une page* → la base
récap liste les chaînes (1 ligne = 1 chaîne) et **le contenu de chaque ligne-page = la fiche complète**.

**Flux exécuté par l'agent (via le serveur MCP Notion, pas par le script — aucune clé dans le code) :**

1. **Bootstrap (1×)** — créer la page racine `📺 Veille YouTube (Scraper)` puis la base **Chaînes scannées** :
   ```sql
   CREATE TABLE (
     "Chaîne" TITLE, "URL chaîne" URL, "Date scan" DATE, "Période" RICH_TEXT,
     "Vidéos" NUMBER, "Shorts" NUMBER, "Repos trouvés" NUMBER,
     "Top repo" URL, "Top score" NUMBER,
     "Verdict top" SELECT('🔥':red,'✅':green,'🟡':yellow,'⚪':gray),
     "Thèmes" MULTI_SELECT('ia':blue,'entrepreneuriat':orange,'mindset':purple,'dev':gray),
     "Top outils" RICH_TEXT )
   ```
   Mémoriser `{root_page_id, database_id, data_source_id}` dans `data/youtube-scrapes/.notion.json` (gitignoré).
2. **Par scan** — `scrape <url> --max N` puis `report <slug> --format both`. **Upsert** : chercher la
   chaîne (par titre) dans la base ; créer la ligne sinon mettre à jour ses propriétés depuis le payload ;
   poser le contenu de la page = la clé `markdown` (`notion-update-page replace_content`). Idempotent.
3. Rendre l'URL de la page Notion à Samuel + un récap court en chat.

Mapping payload → colonnes : `chaine→Chaîne`, `url→URL chaîne`, `date_scan→Date scan`, `periode→Période`,
`nb_videos→Vidéos`, `nb_shorts→Shorts`, `repos_trouves→Repos trouvés`, `top_repo→Top repo`,
`top_score→Top score`, `verdict_top→Verdict top`, `themes→Thèmes`, `top_outils→Top outils`.

## Phase 2 — auto-routage **conscient du thème** (après chaque scrape)

Le routage dépend de la **nature du thème** (ids + listes dans `data/youtube-scrapes/.notion.json`) :
- **Thèmes PROJET** (`themes_projet` : ia, automatisation, dev, business, btp, trading-finance) = à *construire*.
- **Thèmes SAVOIR** (`themes_savoir` : sport, mindset, developpement-personnel, divers) = à *apprendre*.

> ⚠️ La `💡 Boîte à Idées - Projets` est une boîte **business/projets** — n'y router QUE les thèmes projet.
> Un savoir (sport/santé/dev-perso) va dans la base **Apprentissage**, jamais dans la Boîte à Idées.

### A. Idées-à-approfondir (repos 🔥/⚡) → Boîte à Idées *(thèmes projet uniquement)*
1. `report <slug> --format json` → clé `idees` (`{url, score, potentiel, theme}`).
2. Garder `potentiel ∈ {🔥, ⚡}` **ET `theme ∈ themes_projet`** (un repo-idée de thème savoir → étape B).
3. **Dédup par URL** : `notion-query-data-sources` SQL sur `boite_idees_data_source_id`,
   `WHERE "userDefined:URL" LIKE '%<repo>%'` → si présent, **skip**.
4. Sinon `notion-create-pages` (parent `boite_idees_data_source_id`) : `Nom du Projet`, `userDefined:URL`,
   `Potentiel` (`🔥 Élevé`/`⚡ Moyen`), **`Décision` = `À évaluer`**, `Description`, `date:Date d'ajout:start`.

### B. Insights → base Apprentissage *(tous thèmes, routés par thème)*
1. Clé `insights` (`{texte, topic, relevance, destination}`).
2. `notion-create-pages` (parent `apprentissage_data_source_id`) : `Insight` = texte · `Thème` = topic ·
   `Type` = destination (cultiver/process/meta-erreur/meta-bonne-pratique) · `Chaîne` · `Vidéo` · `Pertinence` · `Date`.
3. Filtrer par `Thème` dans Notion pour réviser un domaine (KPI PRD : retrouver un insight en <30 s).

### C. Rendre à Samuel le récap : idées ajoutées · insights routés par thème · idées ignorées (déjà présentes).

> Idempotent par URL côté Boîte à Idées. Destinations restantes (sous-étapes) : log Veille GitHub (outils-à-installer),
> Chaînes-à-explorer (`chaines_liees`), et la boucle méta Phase 3 (insights `Type = meta-*`).

## Scoring : 1 moteur, 2 verdicts (résumé — détail dans scoring-profile.md)

**Moteur /100** (sobre, video-agnostique) :

| Axe | Points | Mesure |
|---|---|---|
| Qualité | 40 | stars, activité récente, README |
| Pertinence Samuel | 45 | domaines (FR+EN, frontières de mots) + projets/outils (confiance) |
| Intégrabilité | 15 | branchable stack : Claude / MCP / n8n / Monday |

**2 verdicts dérivés** :
- 🔧 **Outil-à-installer** (règles éprouvées) : gate `.claude/`, plafond étoiles (<100★→70, <500★→79),
  seuils `≥80 installer · 60-79 surveiller · <60 ignorer`.
- 💡 **Idée-à-approfondir** (décentré, calculé au `report`) : curation vidéo + nouveauté + thème →
  potentiel 🔥/⚡/💡 → alimente la Boîte à Idées.

Un repo modeste mais **sujet central d'une vidéo on-theme** = **idée 🔥** sans gonfler la note repo (découplage
qui évite le biais clickbait). Chaque insight porte un `destination` (cultiver/process/meta-erreur/meta-bonne-pratique).

## Règles d'utilisation

- Lire `scoring-profile.md` avant d'évaluer/commenter un score (sinon interprétation hors-grille)
- Un AXE 4 `basse confiance` est **exclu du verdict** et marqué `⚠️ AXE4 à valider` — ne jamais l'affirmer
- Recommander un `GITHUB_TOKEN` dans `.env.local` avant un gros scrape (quota 60 → 5000 req/h)
- Sur quota épuisé : le scrape sauvegarde le partiel ; relancer `scrape` reprend via le cache (TTL 14j)
- Éditer les listes (projets/outils/thèmes) uniquement dans `projets-samuel.json` — jamais dans le `.md`
- Ne jamais committer les outputs (`repos-scored.json`, `*.json` de chaîne) — gitignorés par design
