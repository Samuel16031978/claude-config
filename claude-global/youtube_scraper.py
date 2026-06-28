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
Clés optionnelles dans .env.local : GITHUB_TOKEN (5000 req/h), YOUTUBE_API_KEY.
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
from datetime import datetime, timezone

DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "youtube-scrapes")
REPOS_FILE = os.path.join(DATA_DIR, "repos-scored.json")
TOOLS_FILE = os.path.join(DATA_DIR, "tools-seen.json")
MANIFEST_FILE = os.path.join(DATA_DIR, ".manifest.json")
PROJETS_FILE = os.path.join(DATA_DIR, "projets-samuel.json")

USER_AGENT = "Mozilla/5.0 (compatible; youtube-scraper-samuel/1.0)"
GITHUB_API = "https://api.github.com"
CACHE_TTL_DAYS = 14

YOUTUBE_URL_RE = re.compile(
    r"^https?://(www\.)?(youtube\.com/(@[\w\-.]+|channel/[\w\-]+|c/[\w\-.]+)|youtu\.be/[\w\-]+)"
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
}

# Outils/technos détectables (extensible)
TOOL_NAMES = ["n8n", "make", "zapier", "claude", "chatgpt", "gpt", "cursor", "copilot",
              "supabase", "vercel", "langchain", "ollama", "notion", "airtable", "python",
              "react", "docker", "nextjs", "tailwind", "stripe", "firebase", "huggingface",
              "midjourney", "perplexity", "windsurf", "replit", "lovable", "bolt"]

# Tournures à valeur pour booster un insight
SIGNAL_PHRASES = ["la cle c'est", "la clé c'est", "le secret", "il faut", "j'ai appris",
                  "framework", "strategie", "stratégie", "la regle", "la règle", "l'erreur",
                  "le plus important", "ce qui marche", "the key is", "the secret", "i learned"]

ORAL_REPLACEMENTS = [(" dot ", "."), (" point ", "."), (" slash ", "/"), (" barre ", "/"),
                     (" tiret ", "-"), (" dash ", "-"), (" underscore ", "_"), (" souligne ", "_")]


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
            if topic in ("ia", "entrepreneuriat", "mindset"):
                candidates.append({"texte": text, "topic": topic, "relevance": relevance})
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

def _score_axe1_claude(tree, truncated):
    paths = [t.get("path", "") for t in tree]
    has_claude = any(".claude/" in p or p == ".claude" for p in paths)
    nb_skills = sum(1 for p in paths if p.endswith("SKILL.md"))
    has_agents = any("agents/" in p for p in paths) or any(p.endswith(".agent.md") for p in paths)
    has_commands = any("commands/" in p for p in paths)
    has_hooks = any("hooks/" in p for p in paths)
    if truncated and not (has_claude or nb_skills):
        return None, {"axe1": "unknown (arbre tronqué)"}
    skills_pts = 10 if nb_skills >= 4 else 7 if nb_skills >= 2 else 4 if nb_skills == 1 else 0
    agents_pts = 8 if has_agents else 0
    ch_pts = 7 if (has_commands and has_hooks) else 4 if (has_commands or has_hooks) else 0
    total = (10 if has_claude else 0) + skills_pts + agents_pts + ch_pts
    details = {"a_dossier_claude": has_claude, "nb_skills": nb_skills,
               "agents": has_agents, "commands": has_commands, "hooks": has_hooks}
    return total, details


def _score_axe2_qualite(repo, tree):
    stars = repo.get("stargazers_count", 0)
    star_pts = 10 if stars > 1000 else 8 if stars >= 500 else 6 if stars >= 100 \
        else 4 if stars >= 20 else 2
    pushed = repo.get("pushed_at", "")
    act_pts = _recency_points(pushed)
    readme_size = next((t.get("size", 0) for t in tree
                        if t.get("path", "").lower() in ("readme.md", "readme.rst", "readme.txt")), 0)
    doc_pts = 7 if readme_size > 5000 else 5 if readme_size > 1000 else 3 if readme_size else 0
    return star_pts + act_pts + doc_pts, {"stars": stars, "pushed_at": pushed[:10]}


def _recency_points(pushed_at):
    if not pushed_at:
        return 0
    pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    days = (_now() - pushed).days
    return 8 if days < 31 else 6 if days < 92 else 4 if days < 183 else 2 if days < 366 else 0


def _score_axe3_theme(repo, tree, themes):
    haystack = " ".join([
        repo.get("description") or "", " ".join(repo.get("topics") or []),
        " ".join(t.get("path", "") for t in tree[:50]),
    ]).lower()
    matched = [th for th in themes if th in haystack]
    return min(20, len(matched) * 4), matched


def _score_axe4_perso(repo, tree, projets):
    haystack = " ".join([
        repo.get("description") or "", " ".join(repo.get("topics") or []),
        repo.get("full_name") or "", " ".join(t.get("path", "") for t in tree[:50]),
    ]).lower()
    proj_pts, matched = 0, []
    for proj in projets.get("projets_actifs", []):
        hits = [k for k in proj["keywords"] if k.lower() in haystack]
        if hits:
            proj_pts = max(proj_pts, 12 if len(hits) >= 2 else 6)
            matched.extend(hits)
    tool_pts = 0
    for outil in projets.get("outils_manquants", []):
        hits = [k for k in outil["keywords"] if k.lower() in haystack]
        if hits:
            tool_pts = max(tool_pts, 8 if len(hits) >= 2 else 4)
            matched.extend(hits)
    total = proj_pts + tool_pts
    confiance = "haute" if (len(set(matched)) >= 2 or proj_pts >= 12) else "basse"
    return total, confiance, sorted(set(matched))


def _verdict(score):
    if score >= 85:
        return "🔥 Pépite — explorer en priorité"
    if score >= 70:
        return "✅ Solide — vaut le détour"
    if score >= 50:
        return "🟡 Intéressant — garder en veille"
    return "⚪ Marginal — ignorer sauf besoin précis"


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

    axe1, d1 = _score_axe1_claude(tree, truncated)
    axe2, d2 = _score_axe2_qualite(repo, tree)
    axe3, themes = _score_axe3_theme(repo, tree, projets.get("themes_surveilles", []))
    axe4, conf4, matched4 = _score_axe4_perso(repo, tree, projets)

    axe1_val = axe1 if axe1 is not None else 0
    verdict_total = axe1_val + axe2 + axe3 + (axe4 if conf4 == "haute" else 0)
    flags = []
    if conf4 == "basse" and axe4 > 0:
        flags.append("⚠️ AXE4 à valider")
    if axe1 is None:
        flags.append("⚠️ AXE1 inconnu (arbre tronqué)")

    return {
        "status": "scored",
        "url": canon_url, "owner": owner, "repo": repo_name,
        "stars": repo.get("stargazers_count", 0), "pushed_at": (repo.get("pushed_at") or "")[:10],
        "scores": {
            "axe1_contenu_claude": axe1, "axe2_qualite": axe2,
            "axe3_thematique": axe3, "axe4_personnel": axe4,
            "total_100": verdict_total,
        },
        "verdict": _verdict(verdict_total),
        "axe4_confidence": conf4, "matched_keywords": matched4, "flags": flags,
        "details": {**d1, **d2, "themes": themes},
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
    """Cible l'onglet /videos d'une chaîne (sinon yt-dlp renvoie les onglets/playlists)."""
    if "youtu.be/" in url or "/watch" in url:
        return url
    if re.search(r"/(videos|streams|shorts|featured)/?$", url):
        return url
    return url.rstrip("/") + "/videos"


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


def cmd_scrape(args):
    yt_dlp = _check_ytdlp()
    url = args.channel_url
    if not YOUTUBE_URL_RE.match(url):
        raise SystemExit("❌ URL YouTube invalide (attendu youtube.com/@... ou /channel/...)")
    run_ts = _now().isoformat()
    projets = _load_projets()
    manifest = _read_json(MANIFEST_FILE, {"videos_seen": {}, "repos_seen": {}})
    repos_scored = _read_json(REPOS_FILE, {})
    tools_index = _read_json(TOOLS_FILE, {})

    flat_opts = {"extract_flat": True, "quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(flat_opts) as ydl:
        chan = ydl.extract_info(_videos_tab_url(url), download=False)
    entries = [e for e in _flatten_entries(chan) if e.get("id")][: args.max]
    chan_name = chan.get("uploader") or re.sub(r"\s*-\s*Videos$", "", chan.get("title") or "channel")
    slug = _slug(chan_name)

    videos, repo_urls_seen, partial = [], set(), False
    detail_opts = {"quiet": True, "skip_download": True, "writeautomaticsub": True,
                   "ignoreerrors": True}
    for entry in entries:
        vid = entry.get("id")
        try:
            with yt_dlp.YoutubeDL(detail_opts) as ydl:
                info = ydl.extract_info(f"https://youtu.be/{vid}", download=False)
        except yt_dlp.utils.DownloadError:
            continue
        if not info:
            continue
        transcript = _fetch_transcript(info)
        desc = info.get("description") or ""
        analysis_source = "transcription" if transcript else "description"
        text = transcript or desc
        links = extract_github_links(desc, transcript)
        for link in links:
            repo_urls_seen.add(link["url"])
        videos.append({
            "id": vid, "title": info.get("title"), "url": f"https://youtu.be/{vid}",
            "upload_date": info.get("upload_date"), "view_count": info.get("view_count"),
            "analysis_source": analysis_source,
            "github_repos": [link["url"] for link in links],
            "topics": score_topics(text),
            "insights": extract_insights(text),
            "tools": extract_tools(text, projets.get("themes_surveilles", [])),
            "description_preview": desc[:200],
        })
        _aggregate_tools(tools_index, vid, videos[-1]["tools"])
        manifest["videos_seen"][vid] = {"channel": slug, "scraped_at": run_ts}

    try:
        partial = _score_repos(repo_urls_seen, repos_scored, manifest, projets, args.refresh)
    except RateLimitExhausted as e:
        partial = True
        print(f"⚠️ {e} — résultats partiels sauvegardés, relance `scrape` pour reprendre")

    channel_doc = {"channel": chan_name, "slug": slug, "url": url,
                   "scraped_at": run_ts, "video_count": len(videos),
                   "videos": videos}
    manifest["last_scraped"] = run_ts
    _write_json_atomic(os.path.join(DATA_DIR, f"{slug}.json"), channel_doc)
    _write_json_atomic(REPOS_FILE, repos_scored)
    _write_json_atomic(TOOLS_FILE, tools_index)
    _write_json_atomic(MANIFEST_FILE, manifest)

    top = sorted([r for r in repos_scored.values() if r.get("scores")],
                 key=lambda r: r["scores"]["total_100"], reverse=True)[:5]
    print(json.dumps({
        "status": "partiel" if partial else "complet",
        "chaine": chan_name, "videos_analysees": len(videos),
        "repos_trouves": len(repo_urls_seen), "repos_notes": len(repos_scored),
        "top_repos": [{"url": r["url"], "score": r["scores"]["total_100"], "verdict": r["verdict"]}
                      for r in top],
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
    axe_key = {"claude": "axe1_contenu_claude", "qualite": "axe2_qualite",
               "theme": "axe3_thematique", "perso": "axe4_personnel"}.get(args.axe)
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
    out = []
    for path in _channel_files():
        doc = _read_json(path, {})
        for v in doc.get("videos", []):
            for ins in v.get("insights", []):
                if args.topic and ins["topic"] != args.topic:
                    continue
                if ins["relevance"] < args.min_score:
                    continue
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


def main():
    _load_env()
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")

    p_scrape = sub.add_parser("scrape")
    p_scrape.add_argument("channel_url")
    p_scrape.add_argument("--max", type=int, default=20)
    p_scrape.add_argument("--refresh", action="store_true")

    sub.add_parser("status")

    p_repos = sub.add_parser("repos")
    p_repos.add_argument("--min-score", type=int, default=0, dest="min_score")
    p_repos.add_argument("--axe", choices=["claude", "qualite", "theme", "perso"])

    p_topics = sub.add_parser("topics")
    p_topics.add_argument("--topic", choices=["ia", "entrepreneuriat", "mindset", "dev"])

    p_insights = sub.add_parser("insights")
    p_insights.add_argument("--topic", choices=["ia", "entrepreneuriat", "mindset"])
    p_insights.add_argument("--min-score", type=float, default=6, dest="min_score")

    p_tools = sub.add_parser("tools")
    p_tools.add_argument("--min-score", type=float, default=5, dest="min_score")

    sub.add_parser("new")

    p_score = sub.add_parser("score")
    p_score.add_argument("github_url")
    p_score.add_argument("--refresh", action="store_true")

    args = parser.parse_args()
    cmds = {"scrape": cmd_scrape, "status": cmd_status, "repos": cmd_repos,
            "topics": cmd_topics, "insights": cmd_insights, "tools": cmd_tools,
            "new": cmd_new, "score": cmd_score}
    if args.cmd not in cmds:
        parser.print_help()
        sys.exit(1)
    cmds[args.cmd](args)


if __name__ == "__main__":
    main()
