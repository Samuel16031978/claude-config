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

**Lis `claude-global/.claude/memory/scoring-profile.md`** — il décrit la grille des 4 axes, les ancres de
verdict, le plafond 65 et la règle de confiance AXE 4. Les listes vivantes (projets actifs, outils manquants,
thèmes surveillés) sont dans `data/youtube-scrapes/projets-samuel.json` (source unique, éditable).

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
python3 youtube_scraper.py scrape <url> [--max N] [--refresh] [--include-hidden]
```
Extrait les vidéos → repos GitHub → score chaque repo /100 → maj manifest. `--refresh` ignore le cache.
`--include-hidden` analyse aussi les vidéos non-publiques (sinon listées à part).

`<url>` accepte : chaîne (`@handle`, `/channel/…`), onglet `/shorts`, **lien direct** d'une vidéo
(`youtu.be/…`, `watch?v=…`) ou d'un **short** (`/shorts/<id>`). Le même pipeline traite vidéos et
shorts, avec ou sans lien GitHub (insights + outils sont extraits dans tous les cas). Note : scraper
une chaîne par `@handle` vise l'onglet `/videos` (long-format) ; pour ses shorts, passe l'URL `…/shorts`.

### 2. Résumé du dernier scrape
```bash
python3 youtube_scraper.py status
```

### 3. Repos notés, filtrables
```bash
python3 youtube_scraper.py repos [--min-score 60] [--axe claude|qualite|theme|perso]
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

## Grille de scoring /100 (résumé — détail dans scoring-profile.md)

| Axe | Points | Mesure |
|---|---|---|
| AXE 1 — Contenu Claude | 35 | `.claude/`, skills, agents, commands/hooks |
| AXE 2 — Qualité | 25 | stars, activité récente, README |
| AXE 3 — Thématique | 20 | thèmes surveillés (`projets-samuel.json`) |
| AXE 4 — Personnel | 20 | projet actif / outil manquant (avec confiance) |

**Verdict :** 🔥 ≥85 · ✅ 70-84 · 🟡 50-69 · ⚪ <50. Plafond ~65 pour un repo non-Claude (voulu).

## Règles d'utilisation

- Lire `scoring-profile.md` avant d'évaluer/commenter un score (sinon interprétation hors-grille)
- Un AXE 4 `basse confiance` est **exclu du verdict** et marqué `⚠️ AXE4 à valider` — ne jamais l'affirmer
- Recommander un `GITHUB_TOKEN` dans `.env.local` avant un gros scrape (quota 60 → 5000 req/h)
- Sur quota épuisé : le scrape sauvegarde le partiel ; relancer `scrape` reprend via le cache (TTL 14j)
- Éditer les listes (projets/outils/thèmes) uniquement dans `projets-samuel.json` — jamais dans le `.md`
- Ne jamais committer les outputs (`repos-scored.json`, `*.json` de chaîne) — gitignorés par design
