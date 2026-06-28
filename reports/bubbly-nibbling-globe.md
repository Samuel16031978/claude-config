# Plan — YouTube → GitHub Repo Scraper & Scorer (Skill)

## Context

Samuel veut un outil qui **explore les chaînes YouTube** de youtubeurs influents (IA, automatisation, entrepreneuriat, mindset) pour en **extraire les repos GitHub** mentionnés (teams, projets, vidéos), puis **noter chaque repo sur 100 points** selon une grille personnelle déjà établie dans sa routine.

Inversion clé de logique : **la vidéo est un canal de découverte ; le repo GitHub est l'objet noté.** Le livrable principal = une liste de repos GitHub classés par score /100, prêts à explorer/installer.

**La veille ne se limite pas à GitHub.** L'outil extrait aussi des transcriptions, et **note par pertinence (0-10)** : (a) les **phrases-clés/insights** sur IA, entrepreneuriat et mindset ; (b) les **outils & technos cités** (n8n, Claude, Cursor…) pour repérer les stacks tendance.

L'outil sera un **skill Claude Code** (SKILL.md) + un **script CLI Python** suivant le pattern `intervals_icu.py`. Pas d'app web — pas de clés exposées.

---

## Architecture

### Fichiers à créer

| Fichier | Rôle |
|---|---|
| `claude-global/youtube_scraper.py` | Script CLI principal (pattern intervals_icu.py) |
| `claude-global/skills/samuel/youtube-scraper/SKILL.md` | Skill Claude Code |
| `claude-global/.claude/memory/scoring-profile.md` | **Profil de scoring** (grille /100 + projets/thèmes) lu par l'agent avant d'évaluer |
| `claude-global/data/youtube-scrapes/projets-samuel.json` | Config machine AXE 4 (projets actifs + outils manquants + thèmes) |
| `claude-global/data/youtube-scrapes/` | Répertoire de données (outputs gitignored) |
| `claude-global/requirements.txt` | Dépendance `yt-dlp` |

### Profil de scoring — `.claude/memory/scoring-profile.md` (anti-drift, architecte round 3)
Décision Samuel : externaliser le profil dans `.claude/memory/scoring-profile.md`, lu par l'agent avant d'évaluer. **Le SKILL.md instruit l'agent : « Lis `.claude/memory/scoring-profile.md` avant d'évaluer la pertinence. »**

**Source unique des listes** (évite la désynchro `.md`/`.json`) : `projets-samuel.json` est l'**unique source** des projets actifs / outils manquants / thèmes surveillés. Le `.md` porte la **méthodologie** (grille des 4 axes, tables de points, ancres de verdict, plafond 65) et **référence** le JSON pour les listes vivantes — il ne les recopie pas. Ligne type dans le `.md` : *« Projets actifs et thèmes surveillés : voir `data/youtube-scrapes/projets-samuel.json` (source machine). »* Le script et l'agent lisent donc les mêmes listes depuis une seule source.

### Données persistées
- `data/youtube-scrapes/repos-scored.json` — **source de vérité unique** des repos notés (dédup par URL canonique, écriture atomique)
- `data/youtube-scrapes/<channel_slug>.json` — par scrape : vidéos + **références** vers URLs repos (pas de copie des scores) + topics + insights + tools
- `data/youtube-scrapes/tools-seen.json` — outils/technos agrégés par chaîne (stacks tendance)
- `data/youtube-scrapes/.manifest.json` — manifest dict (video IDs + repo URLs déjà vus, + ETag par repo)
- `data/youtube-scrapes/projets-samuel.json` — **commité** (repo privé, décision Samuel)

---

## Subcommandes CLI

```bash
python3 youtube_scraper.py scrape <channel_url> [--max N]
# Scrape la chaîne → extrait repos GitHub → score chaque repo /100 → maj manifest

python3 youtube_scraper.py status
# Résumé du dernier scrape (nb vidéos, nb repos trouvés, top repos par score)

python3 youtube_scraper.py repos [--min-score 60] [--axe claude|qualite|theme|perso]
# Liste les repos GitHub notés, triés par score /100, filtrables

python3 youtube_scraper.py topics [--topic ia|entrepreneuriat|mindset|dev]
# Score par topic de chaque vidéo

python3 youtube_scraper.py insights [--topic ia|entrepreneuriat|mindset] [--min-score 6]
# Phrases-clés/insights extraits des transcriptions, notés par pertinence

python3 youtube_scraper.py tools [--min-score 5]
# Outils & technos cités, classés par pertinence cumulée (stacks tendance)

python3 youtube_scraper.py new
# Vidéos ET repos ajoutés depuis le dernier scrape (comparaison manifest)

python3 youtube_scraper.py score <github_url>
# Note un repo GitHub isolé /100 (utile hors YouTube)
```

---

## Accès aux données (fallback)

1. **yt-dlp** (default, aucune clé) — extrait vidéos + transcriptions
2. **YouTube Data API v3** (fallback si `YOUTUBE_API_KEY` dans `.env.local`) — via `urllib` stdlib
3. **GitHub REST API** (via `urllib` stdlib, comme intervals_icu.py — pas de SDK) pour scorer les repos :
   - Non authentifié : 60 req/h ; authentifié si `GITHUB_TOKEN` dans `.env.local` : 5000 req/h (recommandé)
   - **`User-Agent` header obligatoire** (sinon 403 même avec token) — `urllib` ne le met pas par défaut
   - 2 appels/repo : `/repos/{owner}/{repo}` (stars, `pushed_at`, `default_branch`, description) **puis** `/git/trees/{default_branch}?recursive=1` (détection `.claude/`, `skills/`, `agents/`, `hooks/` + taille blob README)
   - Ordre imposé : repos → tree (le tree a besoin de `default_branch` du 1er appel) — **blocker B2**

### Caching (obligatoire, pas optionnel — architecte round 2)
- **ETag / `If-None-Match`** : stocker l'ETag par repo dans le manifest ; un `304` ne consomme pas le quota
- **TTL 14 jours** (décision Samuel) : repo vu il y a <14j → réutiliser le score caché ; `--refresh` force le re-score
- **Backoff** : lire `Retry-After` / `X-RateLimit-Reset`, jamais de boucle dure
- **Quota épuisé → persist-partial reprenable** (décision Samuel) : écrire les repos déjà notés, un `scrape` ultérieur reprend les manquants via le cache
- **URL canonique** (clé de dédup/cache) : `github.com/{owner}/{repo}` en minuscules, strip `.git`, strip chemins profonds/`/tree/...`

---

## Pipeline de scrape

```
1. yt-dlp extraction plate de la chaîne (IDs + titres)
2. Pour chaque vidéo (jusqu'à --max) :
   a. Récupérer description + transcription (auto-subs fr,en)
   b. Extraire repos GitHub (3 passes — voir ci-dessous)
   c. Tagger topics depuis transcription (insights IA/entrep/mindset/dev)
3. Dédupliquer les repos GitHub trouvés (par URL canonique)
4. Pour chaque repo unique : appeler GitHub API → scorer /100 (4 axes)
5. Écrire <channel_slug>.json + maj repos-scored.json + manifest
```

### Source d'analyse des insights : la transcription (pas le titre)

Les insights topic viennent de la **transcription** (auto-subs yt-dlp) — pas du titre clickbait.
`yt-dlp --write-auto-subs --sub-langs fr,en --skip-download <url>`. Fallback description.

### Extraction GitHub (orale → URL reconstruite) — 3 passes

```
Passe 1 — regex directe (description ou transcription)
  r'https?://github\.com/[\w\-\.]+/[\w\-\.]+'

Passe 2 — normalisation orale (transcription)
  "github dot com slash user slash repo" → github.com/user/repo
  "dot"→".", "slash"→"/", "tiret"/"dash"→"-", "underscore"→"_"
  puis regex sur le texte normalisé

Passe 3 — contexte de proximité
  "le repo / dépôt / code sur github" + séquence alphanumérique dans 30 mots
  → reconstruction tentative user/repo (confiance moyenne)
```

Chaque repo : `{"url": "...", "source": "oral|description", "confiance": "haute|moyenne", "found_in_video": "<id>"}`
Validation : l'API GitHub confirme l'existence (404 → confiance "non vérifiée", exclu du scoring).

---

## ⭐ Système de scoring GitHub /100 (cœur — grille de Samuel)

Chaque repo GitHub extrait est noté sur **100 points** répartis sur **4 axes** :

### AXE 1 — Contenu Claude (35 pts)
Détecté via l'arbre du repo (`git/trees/{default_branch}?recursive=1`). Match par **suffixe de chemin n'importe où** (pas seulement racine) → monorepos non sous-notés.
| Critère | Points | Règle automatisable |
|---|---|---|
| Présence dossier `.claude/` | 0–10 | présent=10, sinon 0 |
| Skills installables | 0–10 | nb fichiers `SKILL.md` : 1=4, 2-3=7, 4+=10 |
| Agents définis | 0–8 | `agents/` ou `*.agent.md` : présent=8, partiel=4 |
| Commands / hooks | 0–7 | `commands/` + `hooks/` : les deux=7, un seul=4 |

**Arbre tronqué** (`truncated: true` sur gros monorepo) : fallback `/contents/` sur les chemins AXE-1 ciblés uniquement. Si toujours indéterminable → marquer AXE 1 `unknown` (pas `0` — évite un faux négatif). 
**Plafond 65** documenté : un excellent repo non-Claude plafonne ~65 ("garder en veille") — comportement voulu pour une grille orientée contenu Claude.

### AXE 2 — Qualité (25 pts)
Détecté via `/repos/{owner}/{repo}`.
| Critère | Points | Règle |
|---|---|---|
| Stars GitHub | 0–10 | `>1000`=10, 500-1000=8, 100-500=6, 20-100=4, <20=2 |
| Activité récente (`pushed_at`) | 0–8 | <1 mois=8, <3 mois=6, <6 mois=4, <1 an=2, sinon 0 |
| Documentation / README | 0–7 | taille README via **blob du tree** (pas d'appel `/readme` séparé → reste à 2 appels/repo) : >5ko=7, >1ko=5, présent=3, absent=0 |

### AXE 3 — Thématique (20 pts)
Match des thèmes surveillés dans description/topics/README.
| Critère | Points | Règle |
|---|---|---|
| Correspond aux thèmes surveillés | 0–20 | IA, N8N, automatisation, BTP, sport — 4 pts par thème matché (max 20) |

### AXE 4 — Personnel Samuel (20 pts) — **confiance attachée (blocker B1)**
Match contre `projets-samuel.json`. **Le matching mots-clés sur/sous-déclenche** ("n8n" partout, "obat" jamais) → on attache une confiance et on **exclut les scores basse confiance du verdict** (ils sont affichés mais marqués "à valider").
| Critère | Points | Règle |
|---|---|---|
| Répond à un projet actif | 0–12 | match mot-clé projet : fort (≥2 kw)=12, partiel (1 kw)=6 |
| Comble un outil manquant | 0–8 | match liste outils manquants : oui=8, proche=4 |

Chaque repo expose `axe4_confidence: "haute|basse"` + `matched_keywords: [...]` dans `details`. Si confiance basse → AXE 4 sorti du `total_100` du verdict, signalé `⚠️ AXE4 à valider`.

### Score final
```python
score_100 = axe1 + axe2 + axe3 + axe4   # 0-100
# Verdict (ancres) :
#  85-100 → 🔥 Pépite — explorer en priorité
#  70-84  → ✅ Solide — vaut le détour
#  50-69  → 🟡 Intéressant — à garder en veille
#  <50    → ⚪ Marginal — ignorer sauf besoin précis
```

`projets-samuel.json` (config AXE 4, commité car non sensible) :
```json
{
  "projets_actifs": [
    {"nom": "WhatsApp→N8N", "keywords": ["whatsapp", "n8n", "automation", "webhook"], "poids": "fort"},
    {"nom": "SC Rénovations", "keywords": ["btp", "devis", "obat", "chantier", "renovation"], "poids": "fort"}
  ],
  "outils_manquants": [
    {"nom": "Garmin MCP", "keywords": ["garmin", "mcp", "fitness", "wearable"]},
    {"nom": "OBAT MCP", "keywords": ["obat", "devis", "facturation"]}
  ],
  "themes_surveilles": ["ia", "n8n", "automatisation", "btp", "sport"]
}
```

---

## Veille de contenu (au-delà de GitHub — décision Samuel)

En plus du scoring repo, l'outil extrait et **note par pertinence (0-10)** deux types de contenu depuis la transcription :

### A. Phrases-clés / insights (IA, entrepreneuriat, mindset)
Les transcriptions auto-générées n'ont pas de ponctuation fiable → découpage par **fenêtres glissantes** (~25-40 mots, chevauchement 50%). Chaque fenêtre reçoit :
```python
# densité thématique de la fenêtre
theme_hits = nb keywords thématiques dans la fenêtre
relevance = round(min(10, theme_hits * 2.5 + signal_bonus), 1)
# signal_bonus : +2 si tournure à valeur ("la clé c'est", "le secret", "il faut", "j'ai appris", "framework", "stratégie")
```
On garde les fenêtres `relevance ≥ 6`, dédupliquées, taguées par topic dominant. Stockées dans `insights` (top N par vidéo).

### B. Outils & technos cités
Dictionnaire nommé (extensible) : `n8n, make, zapier, claude, chatgpt, gpt, cursor, supabase, vercel, langchain, ollama, notion, airtable, python, react, docker…`
```python
# score outil = fréquence de mention × match thèmes/projets surveillés
freq = nb mentions dans la transcription
theme_match = 1 si l'outil ∈ thèmes surveillés (projets-samuel.json)
tool_relevance = round(min(10, freq * 2 + theme_match * 4), 1)
```
Agrégé au niveau chaîne dans `tools-seen.json` (quel outil revient le plus, classé par pertinence cumulée) → repère les stacks tendance.

### C. Score par topic (conservé)
```python
unique_kw = len(set(keywords_topic) & set(words_transcription))
topic_score = round(min(10, (unique_kw / len(keywords_topic)) * 25), 1)  # ~40% couverture = 10
```
Topics (FR/EN) : `ia`, `entrepreneuriat`, `mindset`, `dev` (dictionnaires bilingues).

> Tous ces scores réutilisent les listes de `projets-samuel.json` (source unique) — pas de drift.

---

## Structure JSON de sortie

### Repo noté (repos-scored.json)
```json
{
  "url": "https://github.com/user/claude-agents",
  "owner": "user", "repo": "claude-agents",
  "found_in": ["videoId1", "videoId2"],
  "source": "description", "confiance": "haute",
  "stars": 1240, "pushed_at": "2026-05-01",
  "scores": {
    "axe1_contenu_claude": 28,
    "axe2_qualite": 22,
    "axe3_thematique": 16,
    "axe4_personnel": 12,
    "total_100": 78
  },
  "verdict": "✅ Solide — vaut le détour",
  "details": {"a_dossier_claude": true, "nb_skills": 6, "themes": ["ia", "automatisation"]}
}
```

### Vidéo (channel JSON)
```json
{
  "id": "abc123", "title": "...", "url": "https://youtu.be/abc123",
  "upload_date": "20240315", "view_count": 45200,
  "analysis_source": "transcription",
  "github_repos": ["https://github.com/user/claude-agents"],
  "topics": {"ia": 8.5, "entrepreneuriat": 6.0, "mindset": 0.0, "dev": 2.5},
  "insights": [
    {"texte": "la clé en IA c'est d'automatiser le boring avant le créatif", "topic": "ia", "relevance": 8.5},
    {"texte": "un solopreneur doit valider avant de coder", "topic": "entrepreneuriat", "relevance": 7.0}
  ],
  "tools": [{"nom": "n8n", "freq": 4, "relevance": 9.0}, {"nom": "claude", "freq": 3, "relevance": 8.0}],
  "description_preview": "..."
}
```

### Outils agrégés (tools-seen.json — niveau chaîne)
```json
{
  "n8n": {"mentions_total": 12, "videos": ["abc123", "def456"], "relevance_cumulee": 9.5, "theme_surveille": true},
  "cursor": {"mentions_total": 3, "videos": ["abc123"], "relevance_cumulee": 6.0, "theme_surveille": false}
}
```

---

## SKILL.md — déclencheurs

- URL YouTube, "scrape", "chaîne youtube", "repos github d'un youtubeur"
- nom de youtubeur + IA / automatisation / mindset
- "note ce repo", "scoring github", "pépites github", "nouvelles vidéos"
- "quels repos valent le coup", "100 points"
- "insights", "phrases-clés", "quels outils il utilise", "stack", "technos citées"

---

## Manifest (dict — O(1), correction architecte)

`data/youtube-scrapes/.manifest.json` :
```json
{
  "last_scraped": "2026-06-28T10:00:00",
  "videos_seen": {"abc123": {"channel": "slug", "scraped_at": "..."}},
  "repos_seen": {"github.com/user/repo": {"score": 78, "scraped_at": "..."}}
}
```
`new` compare les clés du scrape courant aux clés du manifest.

---

## Corrections architecte (round 1 + 2, toutes intégrées)

| Problème | Sévérité | Correction |
|---|---|---|
| Gitignore manquant | Bloquant | `data/youtube-scrapes/*.json` ignoré SAUF `projets-samuel.json` (repo privé) |
| yt-dlp non documentée | Important | `requirements.txt` + guard `_check_ytdlp()` message clair |
| Manifest array | Important | dict keyed by id/url → O(1) |
| Injection URL subprocess | Mineur | regex whitelist + subprocess list-form uniquement |
| **B1** AXE 4 non validé gonfle le verdict | **Bloquant** | confiance + `matched_keywords` ; basse confiance exclue du verdict |
| **B2** branche tree hardcodée (`main`) | **Bloquant** | utiliser `default_branch` ; ordre repos→tree |
| **B3** dual-write incohérent | **Bloquant** | `repos-scored.json` source unique ; écriture atomique (temp + `os.replace`) ; channel = références seules |
| Rate-limit GitHub | Important | ETag/304 + TTL 14j + backoff `Retry-After` ; persist-partial reprenable |
| `User-Agent` manquant | Important | header obligatoire sur tous les appels GitHub |
| URL non canonique | Important | normalisation (host+owner+repo minuscule, strip `.git`/chemins) |
| README = appel séparé | Mineur | taille lue depuis le blob du tree (reste 2 appels/repo) |
| Recency non déterministe | Mineur | figer "now" par run (buckets AXE 2 stables) |
| Drift profil `.md`/`.json` | Concern | `.json` = source unique des listes ; le `.md` les référence (méthodo seule) |

---

## Ordre d'implémentation

1. **Commit 1** — `.gitignore` : `claude-global/data/youtube-scrapes/*.json` + exception `!projets-samuel.json`
2. **Commit 2** — `requirements.txt` (`yt-dlp>=2024.1.1`) + `projets-samuel.json` + `.claude/memory/scoring-profile.md`
3. **Commit 3** — `youtube_scraper.py` complet (avec contrat d'écriture atomique B3)
4. **Commit 4** — `SKILL.md` (avec instruction « Lis `.claude/memory/scoring-profile.md` avant d'évaluer »)

---

## Vérification

1. `pip install yt-dlp`
2. `python3 youtube_scraper.py scrape https://www.youtube.com/@<chaine-ia> --max 5`
3. Vérifier extraction repos GitHub + scoring /100 dans `repos-scored.json`
4. `python3 youtube_scraper.py score https://github.com/anthropics/claude-code` → score /100 cohérent
5. `repos --min-score 70` → seulement les repos solides
6. `topics --topic ia` → score topic par vidéo
7. `insights --topic entrepreneuriat --min-score 6` → phrases-clés pertinentes
8. `tools --min-score 5` → outils/technos classés (vérifier `tools-seen.json`)
9. `new` → nouveautés uniquement (manifest dict)
10. `ls claude-global/skills/samuel/youtube-scraper/`
