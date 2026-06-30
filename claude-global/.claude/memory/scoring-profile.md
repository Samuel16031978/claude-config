# Profil de scoring — Veille YouTube → GitHub (Samuel)

> Lu par l'agent **avant toute évaluation de pertinence**. Décrit la méthodologie de notation.
> **Les listes vivantes ne sont PAS recopiées ici.** Source unique :
> [`data/youtube-scrapes/projets-samuel.json`](../../data/youtube-scrapes/projets-samuel.json) (version machine).
> Édite ce JSON pour faire évoluer le profil — le script et l'agent lisent les mêmes listes.

## Principe : 1 moteur, 2 verdicts, 4 destinations

La **vidéo** est un canal de découverte ; le **repo** est l'objet noté. Mais la note ne sert pas une seule
décision — elle en sert deux, et la veille alimente quatre destinations (volant d'inertie de connaissance).

| Destination | Décision | Cible |
|---|---|---|
| 🔧 Outil-à-installer | « je l'installe ? » | log Veille GitHub |
| 💡 Idée-à-approfondir | « j'approfondis ? » | Boîte à Idées |
| 📚 Me cultiver | « j'apprends quoi ? » | pages Apprentissage (Phase 2) |
| 🧠 M'améliorer (méta) | « erreur à éviter / bonne pratique ? » | CLAUDE.md / memory (Phase 3) |

## Moteur — score repo /100 (sobre, 3 axes)

### Qualité (40 pts — universel)
| Critère | Points |
|---|---|
| Stars | >1000=16 · 500-1000=13 · 100-500=10 · 20-100=6 · <20=3 |
| Activité (`pushed_at`) | <1 mois=15 · <3 mois=11 · <6 mois=7 · <1 an=3 · sinon 0 |
| README | >5 ko=9 · >1 ko=6 · présent=3 · absent=0 |

### Pertinence Samuel (45 pts — fusion thème + perso)
- **Domaines de veille** (`domaines_veille`, ≤25) : match **FR+EN à frontières de mots** (corrige le biais
  linguistique — un repo anglophone *"AI/LLM/agent"* matche le domaine `ia`). Points par domaine selon poids :
  fort=10 · moyen=7 · faible=4, plafonné à 25.
- **Projets/outils perso** (`projets_actifs`/`outils_manquants`, ≤20) : projet 0/6/12 + outil manquant 0/4/8.
  **Confiance** : si basse (matching mots-clés ambigu), cette part est **exclue du verdict** et flaggée
  `⚠️ Pertinence perso à valider`. MCP **whatsapp/n8n/garmin/intervals = priorité absolue** (outils manquants).

### Intégrabilité (15 pts — branchable dans la stack)
Détectée dans l'arbre + nom + description + topics. Claude (`.claude/`, `SKILL.md`, agents) ≤6 · MCP ≤4 ·
n8n ≤3 · Monday ≤2, cumulables, plafond 15. Arbre tronqué indéterminable → `unknown` (jamais 0).

**Verdict repo (bande descriptive)** : 🔥≥95 · ✅85-94 · 🟡70-84 · ⚪<70. Le contexte vidéo **n'entre pas** dans
ce score (il vit dans le verdict Idée) → le cache `repos-scored.json` reste video-agnostique.

## Verdict 🔧 Outil-à-installer (règles éprouvées de la veille GitHub)
- **Gate `.claude/`** : sans contenu Claude installable → `n/a` (pas un outil à installer).
- **Plafond par étoiles** : `<100★ → max 70` · `<500★ → max 79`.
- **Seuils** : `≥80 = ✅ installer · 60-79 = 👁 surveiller · <60 = ⚪ ignorer`.

## Verdict 💡 Idée-à-approfondir (décentré — pilote la Boîte à Idées)
**Pas** de gate `.claude/`, **pas** de plafond étoiles : la curation d'un vidéaste prime.
- **Curation vidéo** (≤45) : sujet central (repo seul cité + topic dominant fort) > simple mention.
- **Nouveauté** (≤30) : première apparition (`manifest.repos_seen` / `first_seen`) ; décroît si déjà vu.
- **Thème** (≤25) : topic vidéo → thème d'apprentissage (`ia/automatisation/dev/btp/sport/business/trading/divers`).
- Sortie : `potentiel 🔥 (≥75) · ⚡ (≥50) · 💡 (<50)` + thème.

> Un repo modeste mais **sujet central d'une vidéo on-theme** est une **idée 🔥** (toute l'attention) tout en
> gardant une **note repo sobre** — c'est le découplage qui évite le biais clickbait (verdict Rodin : *À pivoter*).

## Insights & outils (pertinence légère 0-10)
- **Insight** : densité thématique d'une fenêtre de transcription + bonus tournure à valeur. On garde
  `relevance ≥ 6`. Chaque insight reçoit un **`destination`** (cultiver/process/meta-erreur/meta-bonne-pratique).
- **Outil** : fréquence × match domaines. Agrégé par chaîne → stacks tendance.
