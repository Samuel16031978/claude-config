#!/usr/bin/env python3
"""
youtube_scraper.py — Scraper de chaînes YouTube → repos GitHub notés /100 (Samuel)

La vidéo est un canal de découverte ; le repo GitHub est l'objet noté.
On extrait aussi insights (IA/entrepreneuriat/mindset) et outils/technos cités.

Usage :
    python3 youtube_scraper.py scrape <channel_url> [--max N] [--refresh]
    python3 youtube_scraper.py status
    python3 youtube_scraper.py repos [--min-score 60] [--axe claude|qualite|theme|perso]
    python3 youtube_scraper.py topics [--topic ia|entrepreneuriat|mindset|dev]
    python3 youtube_scraper.py insights [--topic ia|entrepreneuriat|mindset] [--min-score 6]
    python3 youtube_scraper.py tools [--min-score 5]
    python3 youtube_scraper.py new
    python3 youtube_scraper.py score <github_url> [--refresh]

Dépendance optionnelle : yt-dlp (uniquement pour scrape). pip install -r requirements.txt
Clés optionnelles dans .env.local : GITHUB_TOKEN (5000 req/h), YOUTUBE_API_KEY,
YOUTUBE_COOKIES (chemin cookies.txt) ou YOUTUBE_COOKIES_FROM_BROWSER (débloque les vidéos membres).
"""

from __future__ import annotations

import os
import re
import sys
import json
import time
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "youtube-scrapes")
REPOS_FILE = os.path.join(DATA_DIR, "repos-scored.json")
TOOLS_FILE = os.path.join(DATA_DIR, "tools-seen.json")
MANIFEST_FILE = os.path.join(DATA_DIR, ".manifest.json")
PROJETS_FILE = os.path.join(DATA_DIR, "projets-samuel.json")

USER_AGENT = "Mozilla/5.0 (compatible; youtube-scraper-samuel/1.0)"
GITHUB_API = "https://api.github.com"
CACHE_TTL_DAYS = 14
MAX_HIDDEN_SCAN = 12   # borne le scan quand des vidéos non-publiques s'intercalent (évite le throttle YouTube)
DETAIL_SLEEP = 3.0     # pause entre extractions vidéo : sous ~3s YouTube throttle et availability devient null
THROTTLE_STREAK = 5    # N availability=None d'affilée → throttle probable, on bail (les vidéos publiques resettent)

YOUTUBE_URL_RE = re.compile(
    r"^https?://(www\.)?("
    r"youtube\.com/(@[\w\-.]+|channel/[\w\-]+|c/[\w\-.]+|shorts/[\w\-]+|live/[\w\-]+|watch\?v=[\w\-]+)"
    r"|youtu\.be/[\w\-]+)"
)
SINGLE_VIDEO_RE = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:shorts/|live/|watch\?v=))([\w\-]{6,})"
)
GITHUB_URL_RE = re.compile(r"https?://github\.com/[\w\-.]+/[\w\-.]+")
GITHUB_ORAL_RE = re.compile(r"github\.com/[\w\-.]+/[\w\-.]+")

# Dictionnaires de topics (FR/EN) — couverture, pas titre clickbait
TOPIC_KEYWORDS = {
    "ia": ["ia", "ai", "intelligence", "artificielle", "llm", "chatgpt", "gpt", "claude",
           "gemini", "prompt", "automation", "automatisation", "neural", "rag", "agent",
           "agents", "machine", "learning", "modele", "model", "embedding", "mistral"],
    "entrepreneuriat": ["startup", "saas", "business", "revenus", "revenue", "marketing",
                        "freelance", "solopreneur", "entrepreneur", "entrepreneuriat", "client",
                        "vente", "sales", "mrr", "product", "pmf", "scaling", "monetisation"],
    "mindset": ["mindset", "productivite", "productivity", "habits", "habitudes", "discipline",
                "deep", "work", "focus", "routine", "motivation", "developpement", "personnel",
                "objectif", "goal", "procrastination", "energie", "mental"],
    "dev": ["python", "github", "api", "open", "source", "coding", "code", "docker", "react",
            "typescript", "javascript", "backend", "frontend", "framework", "library", "git",
            "deploy", "cli", "sdk", "database"],
    "sport": ["natation", "swim", "swimming", "freestyle", "stroke", "kick", "catch", "nage",
              "crawl", "triathlon", "running", "cycling", "pace", "technique", "endurance",
              "training", "entrainement", "fitness", "garmin", "workout", "breathing", "recovery"],
}

# Outils/technos détectables (extensible)
TOOL_NAMES = ["n8n", "make", "zapier", "claude", "chatgpt", "gpt", "cursor", "copilot",
              "supabase", "vercel", "langchain", "ollama", "notion", "airtable", "python",
              "react", "docker", "nextjs", "tailwind", "stripe", "firebase", "huggingface",
              "midjourney", "perplexity", "windsurf", "replit", "lovable", "bolt"]

# Outils dont le nom est un mot courant : ne les compter qu'avec un contexte tech présent
# (sinon « make » le verbe, « notion » de…, « cursor » le curseur polluent les chaînes non-tech).
AMBIGUOUS_TOOLS = {
    "make": ["make.com", "automation", "automatis", "n8n", "zapier", "workflow", "scenario",
             "integromat", "no-code", "nocode", "webhook"],
    "notion": ["notion.so", "notion ai", "workspace", "base de données", "database", "page notion"],
    "cursor": ["cursor ai", "ide", "vscode", "vs code", "editor", "éditeur", "autocomplete", "coding"],
}

# Tournures à valeur pour booster un insight
SIGNAL_PHRASES = ["la cle c'est", "la clé c'est", "le secret", "il faut", "j'ai appris",
                  "framework", "strategie", "stratégie", "la regle", "la règle", "l'erreur",
                  "le plus important", "ce qui marche", "the key is", "the secret", "i learned"]

ORAL_REPLACEMENTS = [(" dot ", "."), (" point ", "."), (" slash ", "/"), (" barre ", "/"),
                     (" tiret ", "-"), (" dash ", "-"), (" underscore ", "_"), (" souligne ", "_")]

# Destinations d'un insight (volant d'inertie : me cultiver / process / méta auto-amélioration)
META_ERROR_CUES = ["erreur", "piège", "piege", "évite", "evite", "éviter", "ne fais pas",
                   "problème", "probleme", "fail", "mistake", "bug", "attention", "danger"]
META_BP_CUES = ["bonne pratique", "best practice", "convention", "toujours", "il faut",
                "la règle", "la regle", "discipline", "méthode", "methode", "structure"]
PROCESS_CUES = ["workflow", "process", "automatis", "pipeline", "étape", "etape", "n8n",
                "orchestr", "déléguer", "deleguer", "routine"]


# ── IO helpers ────────────────────────────────────────────────────────────────

def _load_env():
    for path in [
        os.path.join(os.path.dirname(__file__), ".env.local"),
        os.path.join(os.path.dirname(__file__), "..", ".env.local"),
        os.path.join(os.getcwd(), ".env.local"),
    ]:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        os.environ.setdefault(k.strip(), v.strip())
            return


def _read_json(path, default):
    if not os.path.isfile(path):
        return default
    with open(path) as f:
        return json.load(f)


def _write_json_atomic(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = f"{path}.tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "channel").lower()).strip("-") or "channel"


def _now():
    return datetime.now(timezone.utc)


def _compute_cutoff(args):
    """Borne basse de date (str 'YYYYMMDD') pour une fenêtre temporelle, sinon None.
    --since YYYY-MM-DD prévaut sur --months N (≈ N×30.4 jours)."""
    since = getattr(args, "since", None)
    if since:
        return since.replace("-", "")
    months = getattr(args, "months", None)
    if months:
        return (_now() - timedelta(days=round(months * 30.4))).strftime("%Y%m%d")
    return None


# ── URL normalisation ───────────────────────────────────────────────────────────

def canonical_github_url(raw):
    m = GITHUB_URL_RE.search(raw or "")
    if not m:
        return None
    parts = m.group(0).split("github.com/", 1)[1].split("/")
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    repo = repo[:-4] if repo.endswith(".git") else repo
    owner, repo = owner.lower(), repo.lower()
    if not owner or not repo or repo in ("", "tree", "blob"):
        return None
    return f"https://github.com/{owner}/{repo}"


# ── Extraction GitHub (3 passes) ────────────────────────────────────────────────

def extract_github_links(description, transcript):
    found = {}
    for url in GITHUB_URL_RE.findall(description or ""):
        canon = canonical_github_url(url)
        if canon:
            found.setdefault(canon, {"source": "description", "confiance": "haute"})
    for url in GITHUB_URL_RE.findall(transcript or ""):
        canon = canonical_github_url(url)
        if canon:
            found.setdefault(canon, {"source": "transcription", "confiance": "haute"})
    # Liens écrits mais sans protocole dans la description (ex: "github.com/user/repo")
    for match in GITHUB_ORAL_RE.findall((description or "").lower()):
        canon = canonical_github_url(f"https://{match}")
        if canon:
            found.setdefault(canon, {"source": "description", "confiance": "haute"})
    normalized = (transcript or "").lower()
    for spoken, char in ORAL_REPLACEMENTS:
        normalized = normalized.replace(spoken, char)
    for match in GITHUB_ORAL_RE.findall(normalized):
        canon = canonical_github_url(f"https://{match}")
        if canon:
            found.setdefault(canon, {"source": "oral", "confiance": "moyenne"})
    return [{"url": u, **meta} for u, meta in found.items()]


# ── Extraction insights (fenêtres glissantes) ───────────────────────────────────

def _dominant_topic(words):
    scores = {t: sum(1 for w in words if w in set(kw)) for t, kw in TOPIC_KEYWORDS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def tag_destination(text):
    # Oriente chaque insight vers une destination du volant d'inertie de connaissance.
    low = text.lower()
    if any(c in low for c in META_ERROR_CUES):
        return "meta-erreur"
    if any(c in low for c in META_BP_CUES):
        return "meta-bonne-pratique"
    if any(c in low for c in PROCESS_CUES):
        return "process"
    return "cultiver"


def extract_insights(transcript, top_n=8):
    if not transcript:
        return []
    words = transcript.split()
    window, step = 32, 16
    candidates = []
    for i in range(0, max(1, len(words) - window + 1), step):
        chunk = words[i:i + window]
        low = [w.lower().strip(".,!?;:") for w in chunk]
        theme_hits = sum(1 for w in low if any(w in set(kw) for kw in TOPIC_KEYWORDS.values()))
        text = " ".join(chunk)
        signal_bonus = 2 if any(p in text.lower() for p in SIGNAL_PHRASES) else 0
        relevance = round(min(10, theme_hits * 2.5 + signal_bonus), 1)
        if relevance >= 6:
            topic = _dominant_topic(low)
            if topic in ("ia", "entrepreneuriat", "mindset", "sport"):
                candidates.append({"texte": text, "topic": topic, "relevance": relevance,
                                   "destination": tag_destination(text)})
    candidates.sort(key=lambda c: c["relevance"], reverse=True)
    seen, unique = set(), []
    for c in candidates:
        key = c["texte"][:40].lower()
        if key not in seen:
            seen.add(key)
            unique.append(c)
    return unique[:top_n]


# ── Extraction outils ───────────────────────────────────────────────────────────

def extract_tools(transcript, themes_surveilles):
    if not transcript:
        return []
    low = transcript.lower()
    themes = set(themes_surveilles)
    out = []
    for tool in TOOL_NAMES:
        freq = len(re.findall(rf"\b{re.escape(tool)}\b", low))
        if freq == 0:
            continue
        if tool in AMBIGUOUS_TOOLS and not any(c in low for c in AMBIGUOUS_TOOLS[tool]):
            continue  # mot courant sans contexte tech → ce n'est pas l'outil
        theme_match = 1 if tool in themes else 0
        relevance = round(min(10, freq * 2 + theme_match * 4), 1)
        out.append({"nom": tool, "freq": freq, "relevance": relevance,
                    "theme_surveille": bool(theme_match)})
    out.sort(key=lambda t: t["relevance"], reverse=True)
    return out


# ── Score par topic ─────────────────────────────────────────────────────────────

def score_topics(transcript):
    words = set(w.lower().strip(".,!?;:") for w in (transcript or "").split())
    result = {}
    for topic, kw in TOPIC_KEYWORDS.items():
        matched = len(words & set(kw))
        result[topic] = round(min(10, (matched / len(kw)) * 25), 1)
    return result


# ── GitHub API (avec User-Agent, token, ETag, backoff) ──────────────────────────

class RateLimitExhausted(Exception):
    pass


def _gh_get(path, etag=None):
    url = f"{GITHUB_API}{path}"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if etag:
        req.add_header("If-None-Match", etag)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read().decode())
            return resp.status, body, resp.headers.get("ETag"), resp.headers
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return 304, None, etag, e.headers
        if e.code == 404:
            return 404, None, None, e.headers
        if e.code in (403, 429):
            _handle_rate_limit(e.headers)
            return e.code, None, None, e.headers
        raise SystemExit(f"❌ GitHub HTTP {e.code}: {e.read().decode()[:200]}")


def _handle_rate_limit(headers):
    remaining = headers.get("X-RateLimit-Remaining")
    if remaining is not None and remaining != "0":
        return
    reset = headers.get("X-RateLimit-Reset")
    retry_after = headers.get("Retry-After")
    wait = None
    if retry_after and retry_after.isdigit():
        wait = int(retry_after)
    elif reset and reset.isdigit():
        wait = max(0, int(reset) - int(time.time()))
    raise RateLimitExhausted(f"quota GitHub épuisé (reset dans ~{wait}s)" if wait else "quota GitHub épuisé")


# ── Scoring repo /100 ───────────────────────────────────────────────────────────

def _score_integrabilite(repo, tree, truncated, integrations):
    # AXE Intégrabilité = max 15 : le repo est-il branchable dans la stack de Samuel
    # (Claude / MCP / n8n / Monday) ? Généralise l'ex-axe Claude à tous ses outils.
    paths = [t.get("path", "").lower() for t in tree]
    haystack = " ".join(paths + [
        (repo.get("full_name") or "").lower(),
        (repo.get("description") or "").lower(),
        " ".join(repo.get("topics") or []).lower(),
    ])

    def _has(tokens):
        return any(tok.lower() in haystack for tok in tokens)

    has_claude = _has(integrations.get("claude", [".claude/", ".claude-plugin/"]))
    nb_skills = sum(1 for p in paths if p.endswith("skill.md"))
    has_agents = any("agents/" in p for p in paths)
    if truncated and not (has_claude or nb_skills):
        return None, {"a_dossier_claude": False, "integration": "unknown (arbre tronqué)"}

    claude_pts = min(6, (3 if has_claude else 0)
                     + (2 if nb_skills >= 2 else 1 if nb_skills == 1 else 0)
                     + (1 if has_agents else 0))
    mcp_pts = 4 if _has(integrations.get("mcp", ["mcp"])) else 0
    n8n_pts = 3 if _has(integrations.get("n8n", ["n8n"])) else 0
    monday_pts = 2 if _has(integrations.get("monday", ["monday.com"])) else 0
    total = min(15, claude_pts + mcp_pts + n8n_pts + monday_pts)
    kinds = [k for k, p in (("claude", claude_pts), ("mcp", mcp_pts),
                            ("n8n", n8n_pts), ("monday", monday_pts)) if p]
    return total, {"a_dossier_claude": has_claude, "nb_skills": nb_skills,
                   "integrations": kinds}


def _score_qualite(repo, tree):
    # AXE Qualité = max 40 (moteur universel de la veille).
    stars = repo.get("stargazers_count", 0)
    star_pts = 16 if stars > 1000 else 13 if stars >= 500 else 10 if stars >= 100 \
        else 6 if stars >= 20 else 3
    pushed = repo.get("pushed_at", "")
    act_pts = _recency_points(pushed)
    readme_size = next((t.get("size", 0) for t in tree
                        if t.get("path", "").lower() in ("readme.md", "readme.rst", "readme.txt")), 0)
    doc_pts = 9 if readme_size > 5000 else 6 if readme_size > 1000 else 3 if readme_size else 0
    return star_pts + act_pts + doc_pts, {"stars": stars, "pushed_at": pushed[:10]}


def _recency_points(pushed_at):
    if not pushed_at:
        return 0
    pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    days = (_now() - pushed).days
    return 15 if days < 31 else 11 if days < 92 else 7 if days < 183 else 3 if days < 366 else 0


_POIDS_PTS = {"fort": 10, "moyen": 7, "faible": 4}


def _kw_hits(keywords, haystack):
    # Match à frontières de mots (FR+EN) : évite "ia" ∈ "media" et capte les repos anglophones.
    return [k for k in keywords if re.search(rf"\b{re.escape(k.lower())}\b", haystack)]


def _score_pertinence(repo, tree, projets):
    # AXE Pertinence Samuel = max 45 : domaines de veille (≤25) + projets/outils perso (≤20).
    haystack = " ".join([
        repo.get("description") or "", " ".join(repo.get("topics") or []),
        repo.get("full_name") or "", " ".join(t.get("path", "") for t in tree[:80]),
    ]).lower()

    dom_pts, domaines = 0, []
    for dom in projets.get("domaines_veille", []):
        if _kw_hits(dom["keywords"], haystack):
            dom_pts += _POIDS_PTS.get(dom.get("poids", "moyen"), 7)
            domaines.append(dom["nom"])
    dom_pts = min(25, dom_pts)

    proj_pts, matched = 0, []
    for proj in projets.get("projets_actifs", []):
        hits = _kw_hits(proj["keywords"], haystack)
        if hits:
            proj_pts = max(proj_pts, 12 if len(hits) >= 2 else 6)
            matched.extend(hits)
    tool_pts = 0
    for outil in projets.get("outils_manquants", []):
        hits = _kw_hits(outil["keywords"], haystack)
        if hits:
            tool_pts = max(tool_pts, 8 if len(hits) >= 2 else 4)
            matched.extend(hits)
    perso_pts = min(20, proj_pts + tool_pts)
    confiance = "haute" if (len(set(matched)) >= 2 or proj_pts >= 12) else "basse"
    return dom_pts, perso_pts, confiance, sorted(set(matched)), domaines


def _verdict(score):
    if score >= 95:
        return "🔥 Pépite — explorer en priorité"
    if score >= 85:
        return "✅ Solide — vaut le détour"
    if score >= 70:
        return "🟡 Intéressant — garder en veille"
    return "⚪ Marginal — ignorer sauf besoin précis"


def _verdict_outil(total, stars, has_claude):
    # Verdict « outil-à-installer » : règles éprouvées de la veille GitHub de Samuel —
    # gate .claude/ (sinon n/a), plafond par étoiles, seuils 80 (installer) / 60 (surveiller).
    if not has_claude:
        return {"palier": "n/a", "score": None, "raison": "pas de contenu Claude installable"}
    capped = total
    if stars < 100:
        capped = min(capped, 70)
    elif stars < 500:
        capped = min(capped, 79)
    palier = "✅ installer" if capped >= 80 else "👁 surveiller" if capped >= 60 else "⚪ ignorer"
    return {"palier": palier, "score": capped, "raison": f"{stars}★"}


def score_repo(canon_url, projets, etag=None):
    owner, repo_name = canon_url.split("github.com/", 1)[1].split("/")[:2]
    status, repo, new_etag, _ = _gh_get(f"/repos/{owner}/{repo_name}", etag)
    if status == 304:
        return {"status": "unchanged", "etag": etag}
    if status == 404:
        return {"status": "not_found"}
    if status in (403, 429):
        raise RateLimitExhausted("quota épuisé pendant /repos")
    branch = repo.get("default_branch", "main")
    t_status, tree_data, _, _ = _gh_get(f"/repos/{owner}/{repo_name}/git/trees/{branch}?recursive=1")
    tree = (tree_data or {}).get("tree", []) if t_status == 200 else []
    truncated = (tree_data or {}).get("truncated", False) if t_status == 200 else True

    integ, d_integ = _score_integrabilite(repo, tree, truncated, projets.get("integrations_stack", {}))
    qual, d_qual = _score_qualite(repo, tree)
    dom_pts, perso_pts, conf, matched, domaines = _score_pertinence(repo, tree, projets)

    integ_val = integ if integ is not None else 0
    pertinence = dom_pts + (perso_pts if conf == "haute" else 0)
    total = qual + pertinence + integ_val
    flags = []
    if conf == "basse" and perso_pts > 0:
        flags.append("⚠️ Pertinence perso à valider")
    if integ is None:
        flags.append("⚠️ Intégrabilité inconnue (arbre tronqué)")

    stars = repo.get("stargazers_count", 0)
    return {
        "status": "scored",
        "url": canon_url, "owner": owner, "repo": repo_name,
        "stars": stars, "pushed_at": (repo.get("pushed_at") or "")[:10],
        "scores": {
            "qualite": qual, "pertinence_samuel": pertinence,
            "integrabilite": integ_val, "total_100": total,
        },
        "verdict": _verdict(total),
        "verdict_outil": _verdict_outil(total, stars, d_integ.get("a_dossier_claude")),
        "pertinence_confidence": conf, "matched_keywords": matched, "flags": flags,
        "details": {**d_integ, **d_qual, "domaines": domaines,
                    "pertinence_domaines": dom_pts, "pertinence_perso": perso_pts},
        "etag": new_etag,
        "scraped_at": _now().isoformat(),
    }


# ── yt-dlp ──────────────────────────────────────────────────────────────────────

def _check_ytdlp():
    try:
        import yt_dlp  # noqa: F401
        return yt_dlp
    except ImportError:
        raise SystemExit("❌ yt-dlp manquant — installe avec : pip install -r requirements.txt")


def _yt_auth_opts():
    """Auth yt-dlp optionnelle (.env.local) — débloque les vidéos non-publiques (membres).
    YOUTUBE_COOKIES=chemin/cookies.txt  ou  YOUTUBE_COOKIES_FROM_BROWSER=chrome|firefox|brave…
    Les cookies restent locaux (gitignorés) et ne sont jamais loggés."""
    cookie_file = os.environ.get("YOUTUBE_COOKIES", "").strip()
    if cookie_file and os.path.isfile(cookie_file):
        return {"cookiefile": cookie_file}
    browser = os.environ.get("YOUTUBE_COOKIES_FROM_BROWSER", "").strip()
    if browser:
        return {"cookiesfrombrowser": (browser,)}
    return {}


def _fetch_transcript(info):
    caps = info.get("automatic_captions") or info.get("subtitles") or {}
    for lang in ("fr", "fr-FR", "en", "en-US"):
        fmts = caps.get(lang)
        if not fmts:
            continue
        fmt = next((f for f in fmts if f.get("ext") == "json3"), fmts[0])
        try:
            req = urllib.request.Request(fmt["url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read().decode()
        except Exception:
            continue
        return _parse_caption(raw, fmt.get("ext"))
    return ""


def _parse_caption(raw, ext):
    if ext == "json3":
        try:
            events = json.loads(raw).get("events", [])
            segs = [seg.get("utf8", "") for ev in events for seg in (ev.get("segs") or [])]
            return re.sub(r"\s+", " ", "".join(segs)).strip()
        except json.JSONDecodeError:
            return ""
    text = re.sub(r"<[^>]+>", "", raw)
    text = re.sub(r"\d\d:\d\d:\d\d[.,]\d+ --> .*", "", text)
    return re.sub(r"\s+", " ", text).strip()


# ── Persistence ─────────────────────────────────────────────────────────────────

def _load_projets():
    projets = _read_json(PROJETS_FILE, None)
    if projets is None:
        raise SystemExit(f"❌ {PROJETS_FILE} introuvable — config AXE 3/4 requise")
    return projets


def _aggregate_tools(tools_index, video_id, tools):
    for t in tools:
        entry = tools_index.setdefault(t["nom"], {
            "mentions_total": 0, "videos": [], "relevance_cumulee": 0.0,
            "theme_surveille": t["theme_surveille"]})
        entry["mentions_total"] += t["freq"]
        if video_id not in entry["videos"]:
            entry["videos"].append(video_id)
        entry["relevance_cumulee"] = round(entry["relevance_cumulee"] + t["relevance"], 1)


# ── Commands ────────────────────────────────────────────────────────────────────

def _videos_tab_url(url):
    """Cible l'onglet /videos d'une chaîne (sinon yt-dlp renvoie les onglets/playlists).
    Une URL de vidéo/short/live unique est laissée intacte (pas de suffixe /videos)."""
    if "youtu.be/" in url or "/watch" in url or "/shorts/" in url or "/live/" in url:
        return url
    if re.search(r"/(videos|streams|shorts|featured)/?$", url):
        return url
    return url.rstrip("/") + "/videos"


def _extract_channel_listing(yt_dlp, flat_opts, url):
    """Liste les vidéos d'une cible. Vidéo/short unique → 1 entrée. Chaîne → essaie l'onglet
    /videos (listing propre, ordre récent), puis retombe sur l'URL brute si l'onglet manque."""
    single = SINGLE_VIDEO_RE.search(url)
    candidates = [_videos_tab_url(url)]
    if url not in candidates:
        candidates.append(url)
    for candidate in candidates:
        try:
            with yt_dlp.YoutubeDL(flat_opts) as ydl:
                chan = ydl.extract_info(candidate, download=False)
        except yt_dlp.utils.DownloadError:
            continue
        if not chan:
            continue
        # Cible = une seule vidéo/short : yt-dlp renvoie ses métadonnées sans `entries`.
        # On synthétise une liste à 1 entrée pour réutiliser le pipeline de scrape.
        if not chan.get("entries") and chan.get("id"):
            chan["entries"] = [{"id": chan["id"], "title": chan.get("title")}]
            return chan
        if chan.get("entries"):
            return chan
    if single:
        return {"title": "video", "entries": [{"id": single.group(1)}]}
    raise SystemExit(f"❌ impossible de lister les vidéos de {url} "
                     "(chaîne introuvable, supprimée, ou throttle YouTube — réessaie plus tard)")


def _flatten_entries(node):
    """Aplatit les entrées : une chaîne peut imbriquer des playlists d'entrées."""
    out = []
    for entry in (node.get("entries") or []):
        if entry is None:
            continue
        if entry.get("entries"):
            out.extend(_flatten_entries(entry))
        else:
            out.append(entry)
    return out


def _shorts_tab_url(url):
    """Onglet /shorts d'une chaîne (retire un onglet existant avant d'ajouter /shorts)."""
    base = re.sub(r"/(videos|streams|shorts|featured)/?$", "", url.rstrip("/"))
    return base + "/shorts"


def _channels_tab_url(url):
    base = re.sub(r"/(videos|streams|shorts|featured|channels)/?$", "", url.rstrip("/"))
    return base + "/channels"


# Références de chaîne YouTube en écrit : URL de chaîne + @handle nu (hors URL/email).
YT_CHANNEL_URL_RE = re.compile(
    r"youtube\.com/(@[\w.\-]{3,30}|channel/UC[\w\-]{20,30}|c/[\w.\-]{2,40}|user/[\w.\-]{2,40})", re.I)
YT_HANDLE_RE = re.compile(r"(?<![\w@/.])@([A-Za-z0-9][\w.\-]{2,29})\b")


def extract_linked_channels(texts, self_refs):
    """Détecte les chaînes liées (annexes/complémentaires) citées en écrit : URLs de chaîne +
    @handles dans les descriptions et l'onglet « en vedette ». Exclut la chaîne courante.
    Alimente une file « à scraper plus tard » (découverte par effet de réseau)."""
    self_low = {str(s).lower().lstrip("@").rstrip("/").split("/")[-1] for s in self_refs if s}
    found = {}
    for t in texts:
        if not t:
            continue
        refs = [m.group(1) for m in YT_CHANNEL_URL_RE.finditer(t)]
        refs += ["@" + m.group(1) for m in YT_HANDLE_RE.finditer(t)]
        for ref in refs:
            ref = ref.rstrip("/")
            key = ref.lower()
            ident = key.lstrip("@").split("/")[-1]
            if ident in self_low or key in found:
                continue
            found[key] = {"ref": ref, "url": f"https://youtube.com/{ref}"}
    return list(found.values())


def _featured_channel_texts(yt_dlp, flat_opts, url):
    """Best-effort : URLs des chaînes de l'onglet « en vedette » (parsées par extract_linked_channels).
    Renvoie [] sur toute erreur — ne casse jamais le scrape."""
    try:
        with yt_dlp.YoutubeDL(flat_opts) as ydl:
            node = ydl.extract_info(_channels_tab_url(url), download=False)
    except Exception:
        return []
    out = []
    for e in _flatten_entries(node or {}):
        out.append(e.get("url") or "")
        out.append(e.get("uploader_url") or "")
        uid = e.get("uploader_id")
        if uid:
            out.append(uid if str(uid).startswith("@") else f"https://youtube.com/channel/{uid}")
    return out


def _extract_channel_entries(yt_dlp, flat_opts, url, per_tab_limit):
    """Entrées {id, format} fusionnées vidéos + shorts, dédupliquées par id.
    - vidéo/short unique → 1 entrée
    - URL d'onglet explicite (/videos ou /shorts) → ce seul onglet
    - chaîne (handle/root) → tête de l'onglet vidéos + tête de l'onglet shorts.
    Retourne (entries, chan_meta) — chan_meta sert au nommage (uploader/title)."""
    if SINGLE_VIDEO_RE.search(url):
        chan = _extract_channel_listing(yt_dlp, flat_opts, url)
        fmt = "short" if "/shorts/" in url else "video"
        return [{"id": e["id"], "format": fmt}
                for e in _flatten_entries(chan) if e.get("id")], chan

    want_videos = not re.search(r"/shorts/?$", url)
    want_shorts = not re.search(r"/(videos|streams|featured)/?$", url)
    merged, seen, chan_meta = [], set(), None

    if want_videos:
        try:
            chan_meta = _extract_channel_listing(yt_dlp, flat_opts, url)
            for e in _flatten_entries(chan_meta)[:per_tab_limit]:
                if e.get("id") and e["id"] not in seen:
                    seen.add(e["id"])
                    merged.append({"id": e["id"], "format": "video"})
        except SystemExit:
            if not want_shorts:
                raise
    if want_shorts:
        try:
            with yt_dlp.YoutubeDL(flat_opts) as ydl:
                sh = ydl.extract_info(_shorts_tab_url(url), download=False)
            chan_meta = chan_meta or sh
            for e in (_flatten_entries(sh) if sh else [])[:per_tab_limit]:
                if e.get("id") and e["id"] not in seen:
                    seen.add(e["id"])
                    merged.append({"id": e["id"], "format": "short"})
        except yt_dlp.utils.DownloadError:
            pass

    if not merged:
        raise SystemExit(f"❌ impossible de lister vidéos/shorts de {url} "
                         "(chaîne introuvable, supprimée, ou throttle YouTube — réessaie plus tard)")
    return merged, (chan_meta or {"title": "channel"})


def cmd_scrape(args):
    yt_dlp = _check_ytdlp()
    url = args.channel_url
    if not YOUTUBE_URL_RE.match(url):
        raise SystemExit("❌ URL YouTube invalide (attendu youtube.com/@... ou /channel/...)")
    run_ts = _now().isoformat()
    projets = _load_projets()
    themes_surveilles = [d["nom"] for d in projets.get("domaines_veille", [])]
    manifest = _read_json(MANIFEST_FILE, {"videos_seen": {}, "repos_seen": {}})
    repos_scored = _read_json(REPOS_FILE, {})
    tools_index = _read_json(TOOLS_FILE, {})

    cutoff = _compute_cutoff(args)
    windowed = cutoff is not None
    auth = _yt_auth_opts()
    flat_opts = {"extract_flat": True, "quiet": True, "skip_download": True, **auth}
    # Fenêtre date → tête large (on s'arrête à la borne). Sinon tête = max + marge pour sauter
    # d'éventuelles non-publiques intercalées sans scanner toute la chaîne.
    per_tab = 200 if windowed else args.max + MAX_HIDDEN_SCAN
    all_entries, chan = _extract_channel_entries(yt_dlp, flat_opts, url, per_tab)
    chan_name = chan.get("uploader") or re.sub(r"\s*-\s*Videos$", "", chan.get("title") or "channel")
    slug = _slug(chan_name)

    link_texts, chaines_liees = [chan.get("description") or ""], []
    videos, repo_urls_seen, partial, non_publiques = [], set(), False, []
    none_streak = fail_streak = 0
    # ignore_no_formats_error : on ne veut que métadonnées + sous-titres ; sans ffmpeg/runtime JS
    # la résolution de format échoue ("Requested format is not available") alors qu'on ne télécharge rien.
    detail_opts = {"quiet": True, "skip_download": True, "ignoreerrors": True,
                   "ignore_no_formats_error": True, **auth}
    kept = {"video": 0, "short": 0}
    done = {"video": False, "short": False}  # format dont on a dépassé la fenêtre (mode --months/--since)
    extracted_any = False
    for entry in all_entries:
        fmt = entry.get("format", "video")
        if done[fmt]:
            continue
        # Mode fenêtre : on garde tout dans la fenêtre. Sinon : arrêt par format à `max` publiques.
        if not windowed and kept[fmt] >= args.max:
            continue
        if windowed and done["video"] and done["short"]:
            break
        if not windowed and kept["video"] >= args.max and kept["short"] >= args.max:
            break
        if len(non_publiques) >= MAX_HIDDEN_SCAN:
            break
        if none_streak >= THROTTLE_STREAK or fail_streak >= THROTTLE_STREAK:
            break  # série d'indéterminés (throttle) ou d'échecs (extraction cassée) → on arrête de marteler
        if extracted_any:
            time.sleep(DETAIL_SLEEP)
        extracted_any = True
        vid = entry.get("id")
        try:
            with yt_dlp.YoutubeDL(detail_opts) as ydl:
                info = ydl.extract_info(f"https://youtu.be/{vid}", download=False)
        except yt_dlp.utils.DownloadError:
            info = None
        if not info:
            fail_streak += 1
            continue
        fail_streak = 0
        # Onglet trié récent→ancien : la 1ʳᵉ vidéo hors fenêtre clôt le scan de ce format.
        up = info.get("upload_date")
        if windowed and up and up < cutoff:
            done[fmt] = True
            continue
        # availability != "public" → vidéo réservée aux membres / non répertoriée.
        # On ne la jette pas (potentiellement la plus intéressante) : on la signale à part,
        # et on la note pleinement seulement si --include-hidden (sous-titres rarement accessibles).
        none_streak = none_streak + 1 if info.get("availability") is None else 0
        is_public = info.get("availability") == "public"
        if not is_public and not args.include_hidden:
            non_publiques.append({
                "id": vid, "title": info.get("title"), "url": f"https://youtu.be/{vid}",
                "upload_date": info.get("upload_date"), "format": fmt,
                "availability": info.get("availability"),
                "note": "🔒 non-publique (membres/non répertoriée) — souvent le contenu le plus pointu. "
                        "Pour l'analyser à fond : ajoute YOUTUBE_COOKIES=cookies.txt dans .env.local "
                        "(session authentifiée → transcription accessible), ou relance avec --include-hidden "
                        "pour au moins le titre + la description.",
            })
            continue
        transcript = _fetch_transcript(info)
        desc = info.get("description") or ""
        link_texts.append(desc)
        analysis_source = "transcription" if transcript else "description"
        text = transcript or desc
        links = extract_github_links(desc, transcript)
        videos.append({
            "id": vid, "title": info.get("title"), "url": f"https://youtu.be/{vid}",
            "upload_date": info.get("upload_date"), "view_count": info.get("view_count"),
            "format": fmt, "acces": "public" if is_public else "non_public",
            "analysis_source": analysis_source,
            "github_repos": [link["url"] for link in links],
            "topics": score_topics(text),
            "insights": extract_insights(text),
            "tools": extract_tools(text, themes_surveilles),
            "description_preview": desc[:200],
        })
        kept[fmt] += 1

    # Tri par date décroissante. Sans fenêtre : tronquage aux N plus récents toutes catégories.
    # Avec fenêtre (--months/--since) : on garde tout l'intervalle (pas de tronquage).
    videos.sort(key=lambda v: v.get("upload_date") or "0", reverse=True)
    if not windowed:
        videos = videos[: args.max]

    # Agrégation seulement pour les vidéos retenues (sinon les tronquées pollueraient outils/repos).
    for v in videos:
        for repo_url in v["github_repos"]:
            repo_urls_seen.add(repo_url)
        _aggregate_tools(tools_index, v["id"], v["tools"])
        manifest["videos_seen"][v["id"]] = {"channel": slug, "scraped_at": run_ts}

    # Signature de throttle : aucune vidéo publique retenue alors que des vidéos ont été vues,
    # toutes avec availability indéterminé → YouTube dégrade les métadonnées (souvent : pas de
    # runtime JS + extractions trop rapprochées). La classification public/non-public n'est alors
    # pas fiable — on prévient au lieu d'affirmer un faux "tout non-public".
    throttled = not videos and non_publiques and all(v["availability"] is None for v in non_publiques)

    try:
        partial = _score_repos(repo_urls_seen, repos_scored, manifest, projets, args.refresh)
    except RateLimitExhausted as e:
        partial = True
        print(f"⚠️ {e} — résultats partiels sauvegardés, relance `scrape` pour reprendre")

    n_videos = sum(1 for v in videos if v.get("format") != "short")
    n_shorts = sum(1 for v in videos if v.get("format") == "short")
    # Sous throttle, la classification est fausse : on ne clobber pas le channel doc précédent.
    if not throttled:
        self_refs = [chan_name, chan.get("uploader_id"), chan.get("channel_id")]
        mh = re.search(r"@([\w.\-]+)", url)
        if mh:
            self_refs.append(mh.group(1))
        chaines_liees = extract_linked_channels(
            link_texts + _featured_channel_texts(yt_dlp, flat_opts, url), self_refs)
        channel_doc = {"channel": chan_name, "slug": slug, "url": url,
                       "scraped_at": run_ts, "video_count": n_videos, "short_count": n_shorts,
                       "videos": videos, "non_publiques": non_publiques,
                       "chaines_liees": chaines_liees}
        manifest["last_scraped"] = run_ts
        _write_json_atomic(os.path.join(DATA_DIR, f"{slug}.json"), channel_doc)
        _write_json_atomic(REPOS_FILE, repos_scored)
        _write_json_atomic(TOOLS_FILE, tools_index)
        _write_json_atomic(MANIFEST_FILE, manifest)

    top = sorted([r for r in repos_scored.values() if r.get("scores")],
                 key=lambda r: r["scores"]["total_100"], reverse=True)[:5]
    if throttled:
        print(json.dumps({
            "status": "throttle",
            "chaine": chan_name,
            "message": "⚠️ YouTube a dégradé les métadonnées (availability indéterminé sur toutes les vidéos) "
                       "— classification public/non-public non fiable. Réessaie plus tard (espacement plus long), "
                       "avec un runtime JS (deno) ou des cookies, ou force avec --include-hidden.",
            "videos_vues_sans_classement": [{"id": v["id"], "title": v["title"], "url": v["url"]}
                                            for v in non_publiques],
        }, indent=2, ensure_ascii=False))
        return
    print(json.dumps({
        "status": "partiel" if partial else "complet",
        "chaine": chan_name, "videos_analysees": len(videos),
        "dont_videos": n_videos, "dont_shorts": n_shorts,
        "videos_non_publiques": non_publiques,
        "repos_trouves": len(repo_urls_seen), "repos_notes": len(repos_scored),
        "top_repos": [{"url": r["url"], "score": r["scores"]["total_100"], "verdict": r["verdict"]}
                      for r in top],
        "chaines_liees": [c["ref"] for c in chaines_liees],
        "astuce": "→ `report " + slug + "` pour générer la fiche de veille",
    }, indent=2, ensure_ascii=False))


def _score_repos(repo_urls, repos_scored, manifest, projets, refresh):
    partial = False
    for canon in repo_urls:
        cached = repos_scored.get(canon)
        if cached and not refresh and _is_fresh(cached.get("scraped_at")):
            continue
        etag = manifest["repos_seen"].get(canon, {}).get("etag")
        result = score_repo(canon, projets, etag if not refresh else None)
        if result["status"] == "unchanged" and cached:
            cached["scraped_at"] = _now().isoformat()
        elif result["status"] == "scored":
            prev = repos_scored.get(canon)
            result["first_seen"] = (prev or {}).get("first_seen") or result["scraped_at"]
            repos_scored[canon] = result
        elif result["status"] == "not_found":
            continue
        manifest["repos_seen"][canon] = {
            "score": repos_scored.get(canon, {}).get("scores", {}).get("total_100"),
            "scraped_at": _now().isoformat(), "etag": result.get("etag"),
        }
    return partial


def _is_fresh(iso):
    if not iso:
        return False
    scraped = datetime.fromisoformat(iso)
    return (_now() - scraped).days < CACHE_TTL_DAYS


def cmd_score(args):
    canon = canonical_github_url(args.github_url)
    if not canon:
        raise SystemExit("❌ URL GitHub invalide (attendu github.com/owner/repo)")
    projets = _load_projets()
    repos_scored = _read_json(REPOS_FILE, {})
    manifest = _read_json(MANIFEST_FILE, {"videos_seen": {}, "repos_seen": {}})
    etag = None if args.refresh else manifest["repos_seen"].get(canon, {}).get("etag")
    result = score_repo(canon, projets, etag)
    if result["status"] == "scored":
        repos_scored[canon] = result
        manifest["repos_seen"][canon] = {"score": result["scores"]["total_100"],
                                         "scraped_at": _now().isoformat(), "etag": result.get("etag")}
        _write_json_atomic(REPOS_FILE, repos_scored)
        _write_json_atomic(MANIFEST_FILE, manifest)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_status(_):
    repos = _read_json(REPOS_FILE, {})
    manifest = _read_json(MANIFEST_FILE, {"videos_seen": {}, "repos_seen": {}})
    scored = [r for r in repos.values() if r.get("scores")]
    top = sorted(scored, key=lambda r: r["scores"]["total_100"], reverse=True)[:5]
    print(json.dumps({
        "dernier_scrape": manifest.get("last_scraped"),
        "videos_vues": len(manifest.get("videos_seen", {})),
        "repos_notes": len(scored),
        "top_repos": [{"url": r["url"], "score": r["scores"]["total_100"], "verdict": r["verdict"]}
                      for r in top],
    }, indent=2, ensure_ascii=False))


def cmd_repos(args):
    repos = _read_json(REPOS_FILE, {})
    axe_key = {"qualite": "qualite", "pertinence": "pertinence_samuel",
               "integrabilite": "integrabilite"}.get(args.axe)
    out = []
    for r in repos.values():
        if not r.get("scores"):
            continue
        if r["scores"]["total_100"] < args.min_score:
            continue
        sort_val = r["scores"][axe_key] if axe_key else r["scores"]["total_100"]
        out.append((sort_val, r))
    out.sort(key=lambda x: (x[0] or 0), reverse=True)
    print(json.dumps([r for _, r in out], indent=2, ensure_ascii=False))


def cmd_topics(args):
    out = []
    for path in _channel_files():
        doc = _read_json(path, {})
        for v in doc.get("videos", []):
            topics = v.get("topics", {})
            if args.topic and topics.get(args.topic, 0) < 5:
                continue
            out.append({"video": v["title"], "url": v["url"], "topics": topics})
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_insights(args):
    seen: set[tuple] = set()
    out = []
    for path in _channel_files():
        doc = _read_json(path, {})
        for v in doc.get("videos", []):
            for ins in v.get("insights", []):
                if args.topic and ins["topic"] != args.topic:
                    continue
                if ins["relevance"] < args.min_score:
                    continue
                key = (ins["texte"], v.get("id", v["url"]))
                if key in seen:
                    continue
                seen.add(key)
                out.append({**ins, "video": v["title"], "url": v["url"]})
    out.sort(key=lambda i: i["relevance"], reverse=True)
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_tools(args):
    tools = _read_json(TOOLS_FILE, {})
    out = [{"nom": k, **v} for k, v in tools.items() if v["relevance_cumulee"] >= args.min_score]
    out.sort(key=lambda t: t["relevance_cumulee"], reverse=True)
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_new(_):
    manifest = _read_json(MANIFEST_FILE, {"videos_seen": {}, "repos_seen": {}})
    last = manifest.get("last_scraped")
    if not last:
        raise SystemExit("❌ aucun scrape enregistré — lance d'abord `scrape`")
    new_videos = [{"id": vid, **meta} for vid, meta in manifest["videos_seen"].items()
                  if meta.get("scraped_at") == last]
    repos = _read_json(REPOS_FILE, {})
    new_repos = [{"url": u, "score": r.get("scores", {}).get("total_100")}
                 for u, r in repos.items() if r.get("scraped_at", "")[:19] >= last[:19]]
    print(json.dumps({"depuis": last, "nouvelles_videos": new_videos,
                      "nouveaux_repos": new_repos}, indent=2, ensure_ascii=False))


def _channel_files():
    if not os.path.isdir(DATA_DIR):
        return []
    return [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
            if f.endswith(".json") and f not in
            ("repos-scored.json", "tools-seen.json", "projets-samuel.json")]


# ── Rapport / fiche de veille ────────────────────────────────────────────────────

def _fmt_date(yyyymmdd):
    if not yyyymmdd or len(yyyymmdd) != 8:
        return yyyymmdd or "?"
    return f"{yyyymmdd[6:8]}/{yyyymmdd[4:6]}/{yyyymmdd[0:4]}"


# Topics vidéo (TOPIC_KEYWORDS) → thèmes d'apprentissage de Samuel (Boîte à Idées).
TOPIC_TO_THEME = {"ia": "ia", "entrepreneuriat": "business", "mindset": "divers",
                  "dev": "dev", "sport": "sport"}


def _verdict_idee(repo_result, citing_videos, scan_iso):
    # Verdict « idée-à-approfondir » : pilote la Boîte à Idées. DÉCENTRÉ — pas de gate .claude/
    # ni de plafond étoiles : la curation d'un vidéaste (sujet central) prime.
    if not citing_videos:
        return None
    curation, best_topic = 0, None
    for v in citing_videos:
        topics = v.get("topics") or {}
        dom_topic = max(topics, key=topics.get) if topics else None
        strength = topics.get(dom_topic, 0) if dom_topic else 0
        sole = len(v.get("github_repos", [])) == 1   # repo seul cité = sujet central probable
        c = (45 if sole else 18) * min(1.0, strength / 4.0)
        if c >= curation:
            curation, best_topic = c, dom_topic
    nouveaute = 12
    first_seen = repo_result.get("first_seen") if repo_result else None
    if first_seen and scan_iso:
        try:
            days = (datetime.fromisoformat(scan_iso) - datetime.fromisoformat(first_seen)).days
            nouveaute = 30 if days < 1 else 20 if days < 14 else 10 if days < 60 else 5
        except ValueError:
            pass
    theme = TOPIC_TO_THEME.get(best_topic, "divers")
    theme_pts = 25 if best_topic in TOPIC_TO_THEME else 10
    score = round(min(100, curation + nouveaute + theme_pts))
    potentiel = "🔥" if score >= 75 else "⚡" if score >= 50 else "💡"
    return {"score": score, "potentiel": potentiel, "theme": theme,
            "raison": f"curation {round(curation)} · nouveauté {nouveaute} · thème {theme}"}


def _build_report(slug, doc, repos_scored, tools_seen):
    videos = doc.get("videos", [])
    vid_ids = {v["id"] for v in videos}

    # Repos cités dans la chaîne, joints aux scores (un repo cité mais non noté reste listé).
    repo_urls = []
    for v in videos:
        for u in v.get("github_repos", []):
            if u not in repo_urls:
                repo_urls.append(u)
    scan_iso = doc.get("scraped_at")
    repos = []
    for u in repo_urls:
        r = repos_scored.get(u)
        citing = [v for v in videos if u in v.get("github_repos", [])]
        found_in = [v["title"] for v in citing]
        idee = _verdict_idee(r, citing, scan_iso)
        if r and r.get("scores"):
            s = r["scores"]
            repos.append({
                "url": u, "score": s["total_100"], "verdict": r["verdict"],
                "axes": f'{s.get("qualite", "?")}/{s.get("pertinence_samuel", "?")}/'
                        f'{s.get("integrabilite", "?")}',
                "verdict_outil": r.get("verdict_outil"), "verdict_idee": idee,
                "flags": r.get("flags", []), "found_in": found_in,
            })
        else:
            repos.append({"url": u, "score": None, "verdict": "— non noté", "axes": "—",
                          "verdict_outil": None, "verdict_idee": idee,
                          "flags": [], "found_in": found_in})
    repos.sort(key=lambda x: x["score"] if x["score"] is not None else -1, reverse=True)

    theme_sum = {}
    for v in videos:
        for t, sc in (v.get("topics") or {}).items():
            theme_sum[t] = theme_sum.get(t, 0) + sc
    themes = [t for t in sorted(theme_sum, key=theme_sum.get, reverse=True) if theme_sum[t] >= 5]

    outils = [{"nom": k, "relevance": m["relevance_cumulee"], "mentions": m["mentions_total"]}
              for k, m in tools_seen.items() if set(m.get("videos", [])) & vid_ids]
    outils.sort(key=lambda x: x["relevance"], reverse=True)

    seen, insights = set(), []
    for v in videos:
        for it in v.get("insights", []):
            key = (it["texte"], v["id"])
            if key in seen:
                continue
            seen.add(key)
            insights.append({**it, "video": v["title"]})
    insights.sort(key=lambda x: x["relevance"], reverse=True)

    dates = sorted(v.get("upload_date") for v in videos if v.get("upload_date"))
    periode = f"{_fmt_date(dates[-1])} → {_fmt_date(dates[0])}" if dates else "?"
    top = repos[0] if repos and repos[0]["score"] is not None else None

    idees = sorted(({"url": r["url"], **r["verdict_idee"]} for r in repos if r.get("verdict_idee")),
                   key=lambda x: x["score"], reverse=True)
    dest_tally = {}
    for it in insights:
        d = it.get("destination", "cultiver")
        dest_tally[d] = dest_tally.get(d, 0) + 1

    return {
        "chaine": doc.get("channel"), "url": doc.get("url"), "slug": slug,
        "date_scan": (doc.get("scraped_at") or "")[:10], "periode": periode,
        "nb_videos": doc.get("video_count", 0), "nb_shorts": doc.get("short_count", 0),
        "repos_trouves": len(repos),
        "top_repo": top["url"] if top else None,
        "top_score": top["score"] if top else None,
        "verdict_top": top["verdict"].split()[0] if top else None,
        "themes": themes, "top_outils": [o["nom"] for o in outils[:8]],
        "nb_insights": len(insights),
        "repos": repos, "insights": insights[:10], "outils": outils[:12],
        "idees": idees[:10], "destinations": dest_tally,
        "non_publiques": doc.get("non_publiques", []),
        "chaines_liees": doc.get("chaines_liees", []),
    }


def _fiche_markdown(rep):
    L = [f"**{rep['chaine']}** · {rep['periode']} · {rep['nb_videos']} vidéos / "
         f"{rep['nb_shorts']} shorts · scan {rep['date_scan']}", ""]

    L.append("## 🏆 Repos notés — 2 verdicts (Outil / Idée)")
    if rep["repos"]:
        L += ["| Repo | /100 | Q/P/I | 🔧 Outil | 💡 Idée | Cité dans |",
              "|---|---|---|---|---|---|"]
        for r in rep["repos"]:
            score = f"{r['score']}" if r["score"] is not None else "—"
            axes = r["axes"] + (" ⚠️" if r.get("flags") else "")
            vo = r.get("verdict_outil") or {}
            outil = vo.get("palier", "—") if r["score"] is not None else "—"
            vi = r.get("verdict_idee") or {}
            idee = f"{vi.get('potentiel', '')} {vi.get('score', '')}".strip() or "—"
            cite = "; ".join(r["found_in"][:2])
            L.append(f"| {r['url']} | {score} | {axes} | {outil} | {idee} | {cite} |")
    else:
        L.append("_Aucun repo GitHub cité dans les vidéos analysées._")
    L.append("")

    L.append("## 💡 Idées à approfondir (→ Boîte à Idées)")
    idees = sorted((r for r in rep["repos"] if r.get("verdict_idee")),
                   key=lambda r: r["verdict_idee"]["score"], reverse=True)
    if idees:
        for r in idees[:8]:
            vi = r["verdict_idee"]
            cite = "; ".join(r["found_in"][:1])
            L.append(f"- {vi['potentiel']} **{vi['score']}/100** · `{vi['theme']}` · {r['url']} — _{cite}_")
    else:
        L.append("_Aucune idée déclenchée._")
    L.append("")

    L.append("## 📚 Insights clés (taggés par destination)")
    if rep["insights"]:
        if rep.get("destinations"):
            tally = " · ".join(f"{k}: {v}" for k, v in sorted(rep["destinations"].items()))
            L.append(f"_Répartition : {tally}_")
        for it in rep["insights"]:
            dest = it.get("destination", "cultiver")
            L.append(f"- **[{it['topic']} {it['relevance']} · {dest}]** {it['texte']} — _{it['video']}_")
    else:
        L.append("_Aucun insight au-dessus du seuil._")
    L.append("")

    L.append("## 🛠️ Stack & outils cités")
    if rep["outils"]:
        L.append(" · ".join(f"{o['nom']} (×{o['mentions']})" for o in rep["outils"]))
    else:
        L.append("_Aucun outil détecté._")
    L.append("")

    L.append("## 📡 Chaînes liées (à scraper plus tard)")
    if rep.get("chaines_liees"):
        for c in rep["chaines_liees"]:
            L.append(f"- {c['ref']} — {c['url']}")
    else:
        L.append("_Aucune détectée._")
    L.append("")

    L.append("## 🔒 Vidéos non-publiques à creuser")
    if rep["non_publiques"]:
        for v in rep["non_publiques"]:
            L.append(f"- {v['title']} ({_fmt_date(v.get('upload_date'))}) — {v['url']}")
    else:
        L.append("_Aucune._")
    L.append("")

    L.append("## 📋 Annexe — par vidéo")
    return "\n".join(L)


def _annex_lines(doc):
    out = []
    for v in sorted(doc.get("videos", []), key=lambda v: v.get("upload_date") or "0", reverse=True):
        repos = ", ".join(v.get("github_repos", [])) or "—"
        outils = ", ".join(t["nom"] for t in v.get("tools", [])) or "—"
        top_ins = max(v.get("insights", []), key=lambda i: i["relevance"], default=None)
        ins = f" · 💡 {top_ins['texte'][:80]}" if top_ins else ""
        out.append(f"- `[{_fmt_date(v.get('upload_date'))}]` `{v.get('format','video')}` "
                   f"**{v['title']}** · {v.get('analysis_source')} · repos: {repos} · "
                   f"outils: {outils}{ins}")
    return "\n".join(out)


def cmd_report(args):
    slug = args.channel if os.path.isfile(os.path.join(DATA_DIR, f"{args.channel}.json")) \
        else _slug(args.channel)
    path = os.path.join(DATA_DIR, f"{slug}.json")
    doc = _read_json(path, None)
    if doc is None:
        raise SystemExit(f"❌ aucun scan pour '{args.channel}' ({path} introuvable) — lance `scrape` d'abord")
    rep = _build_report(slug, doc, _read_json(REPOS_FILE, {}), _read_json(TOOLS_FILE, {}))
    markdown = _fiche_markdown(rep) + "\n" + _annex_lines(doc)
    if args.format == "md":
        print(markdown)
    elif args.format == "json":
        print(json.dumps({k: v for k, v in rep.items()}, indent=2, ensure_ascii=False))
    else:  # both
        print(json.dumps({**rep, "markdown": markdown}, indent=2, ensure_ascii=False))


def main():
    _load_env()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")

    p_scrape = sub.add_parser("scrape")
    p_scrape.add_argument("channel_url")
    p_scrape.add_argument("--max", type=int, default=20)
    p_scrape.add_argument("--months", type=int, help="fenêtre : N derniers mois (ignore --max)")
    p_scrape.add_argument("--since", help="fenêtre : depuis cette date YYYY-MM-DD (ignore --max)")
    p_scrape.add_argument("--refresh", action="store_true")
    p_scrape.add_argument("--include-hidden", action="store_true", dest="include_hidden",
                          help="inclure les vidéos non publiques (membres/non répertoriées)")

    sub.add_parser("status")

    p_repos = sub.add_parser("repos")
    p_repos.add_argument("--min-score", type=int, default=0, dest="min_score")
    p_repos.add_argument("--axe", choices=["qualite", "pertinence", "integrabilite"])

    p_topics = sub.add_parser("topics")
    p_topics.add_argument("--topic", choices=["ia", "entrepreneuriat", "mindset", "dev", "sport"])

    p_insights = sub.add_parser("insights")
    p_insights.add_argument("--topic", choices=["ia", "entrepreneuriat", "mindset", "sport"])
    p_insights.add_argument("--min-score", type=float, default=6, dest="min_score")

    p_tools = sub.add_parser("tools")
    p_tools.add_argument("--min-score", type=float, default=5, dest="min_score")

    sub.add_parser("new")

    p_score = sub.add_parser("score")
    p_score.add_argument("github_url")
    p_score.add_argument("--refresh", action="store_true")

    p_report = sub.add_parser("report")
    p_report.add_argument("channel", help="slug ou nom de chaîne déjà scannée")
    p_report.add_argument("--format", choices=["md", "json", "both"], default="both")

    args = parser.parse_args()
    cmds = {"scrape": cmd_scrape, "status": cmd_status, "repos": cmd_repos,
            "topics": cmd_topics, "insights": cmd_insights, "tools": cmd_tools,
            "new": cmd_new, "score": cmd_score, "report": cmd_report}
    if args.cmd not in cmds:
        parser.print_help()
        sys.exit(1)
    cmds[args.cmd](args)


if __name__ == "__main__":
    main()
