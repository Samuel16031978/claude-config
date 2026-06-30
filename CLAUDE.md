# CLAUDE.md — claude-config (Samuel Chembah)

> Repo renommé `Projet-Test` → `claude-config`. Source de vérité unique des skills perso.

## Leçons apprises

> **Mémoire d'agent auto-chargée** (erreur → règle, codes de bonne conduite). L'`@import` ci-dessous l'injecte
> dans le contexte à chaque session → relue avant d'agir, sans toucher au dispatcher de hooks.
> Les entrées datées ci-dessous restent l'historique chronologique.

@claude-global/.claude/memory/lessons.md

- 2026-06-26 connecteurs/intégrations : toujours vérifier (recherche web) qu'un connecteur existe réellement avant de l'inscrire dans une architecture — ne pas supposer. Ex : Gemini n'a aucun connecteur Notion grand public (relais copier-coller manuel), DeepSeek passe par Notion AI.
- 2026-06-27 sécurité : le skill `skill-sync-notion` (édité dans claude.ai) contenait un **token OAuth Anthropic et un token Notion en clair**. Rédigés avant tout commit, remplacés par des variables d'env. **Règle : jamais de token en dur dans un SKILL.md ; scanner avant chaque commit.** Tokens exposés → à révoquer/régénérer.
- 2026-06-27 sens de sync : Samuel édite ses skills **dans claude.ai**, pas dans GitHub. Le sens réel est **claude.ai → GitHub → Claude Code**. Le helper `status` ne compare que repo↔manifeste : il ne « voit » pas claude.ai et peut donc afficher un faux « synchro ».

## ⚠️ Veille YouTube — réflexe outil obligatoire

**Toute demande de scrape / analyse d'une chaîne ou d'une vidéo YouTube se traite avec
`claude-global/youtube_scraper.py`** (`scrape <url>` → `report <slug>` → routage Notion des 4 destinations),
**JAMAIS avec WebFetch / RSS / recherche web** — qui ne donnent qu'une liste de titres, sans scoring, sans
insights, sans routage. Détail du flux : skill `youtube-scraper` (`claude-global/skills/samuel/youtube-scraper/SKILL.md`).
Si `yt-dlp` manque : `pip install -r claude-global/requirements.txt`.

## Structure du dépôt

```
claude-config/
└── claude-global/                 # Outils et skills Claude Code
    ├── intervals_icu.py           # Client API intervals.icu
    ├── sync_skills.py             # Routine de sync des skills (GitHub ↔ Claude Code/AI)
    └── skills/samuel/             # 28 skills perso (liste complète dans README.md)
        ├── .sync-manifest.json    # Empreintes sha256 du dernier sync
        ├── skill-sync/            # Routine de parité via GitHub
        ├── ask-panel/             # Panel des 4 IA (via pont Notion, sans API)
        ├── intervals-icu-samuel/  # Charge d'entraînement intervals.icu
        └── …                      # rodin, stratege, ressources-humaines, planificateur, etc.
```

> ⚠️ **Source canonique = claude.ai** (Samuel y travaille). Le sens réel de synchro est
> **claude.ai → GitHub → Claude Code**, pas l'inverse. Les noms ont été refactorés en FR dans
> claude.ai (juin 2026) ; GitHub a été réaligné dessus (reverse sync).

> ⚠️ Casse unifiée en `samuel/` minuscule (l'ancien doublon `Samuel/` majuscule a été fusionné
> pour éviter une collision de casse au clone sur macOS/Windows).

## Configuration de l'environnement

### Politique réseau
Le domaine `intervals.icu` est autorisé dans la politique réseau de l'environnement.

### Variables d'environnement
`claude-global/.env.local` (non commité) doit contenir :
```
INTERVALS_API_KEY=<clé API intervals.icu>
```

## Skill intervals-icu-samuel

Connexion en temps réel à intervals.icu pour calculer des séances et gérer la charge d'entraînement de Samuel (Athlete ID : `i171091`).

**Déclencheurs :** CTL, ATL, TSB, charge, intervals.icu, "quelle séance", zones FC, FTP, TRIMP, hrTSS, planification séance.

### Commandes disponibles

```bash
cd claude-global

# Lire CTL/ATL/TSB du jour
python3 intervals_icu.py wellness

# Zones FC par sport
python3 intervals_icu.py zones [run|ride|swim]

# Charge nécessaire pour un CTL cible
python3 intervals_icu.py calc_charge --ctl_target 30

# Convertir une charge en séance
python3 intervals_icu.py session --charge 120 --sport run --zone 2

# Historique des 7 derniers jours
python3 intervals_icu.py history --days 7

# Pousser une séance sur le calendrier (confirmation Samuel requise)
python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2"
```

### Règles importantes
- Toujours lire `wellness` avant tout calcul
- Ne jamais pousser une séance sans confirmation explicite de Samuel
- La clé API ne doit jamais être commitée dans git

## Routine skill-sync (parité Claude Code ↔ Claude AI)

GitHub (`claude-config`) est la **source de vérité unique** des skills perso. La routine garde
les mêmes skills des deux côtés. Définition complète : `claude-global/skills/samuel/skill-sync/SKILL.md`.

```bash
cd claude-global
python3 sync_skills.py status   # quels skills ont changé depuis le dernier sync ?
python3 sync_skills.py bundle   # zippe les skills modifiés -> dist/skills/ (à importer dans claude.ai)
python3 sync_skills.py commit-manifest   # fige l'état après un sync réussi
python3 sync_skills.py install   # lie les skills (à plat) dans ~/.claude/skills pour Claude Code
```

- **Claude Code** : `install` (symlink) une fois, puis `git pull` suffit pour les mises à jour de contenu.
- **claude.ai** : import manuel du `.zip` par skill modifié (Settings → Skills) — la routine liste lesquels.
- `dist/` est gitignoré (bundles reconstructibles à la demande, jamais commités).
