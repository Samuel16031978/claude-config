# Plan — La veille comme volant d'inertie : 1 moteur, 2 verdicts, 4 destinations (roadmap par phases)

## Context

Parti d'un bug (`tenfoldmarc/llm-council-skill` scoré 28/100), le périmètre a grandi par dialogue, nourri par :
les **25 skills** de Samuel, **Rodin** (verdict *À pivoter*), et **5 sous-pages Notion** (hub Gestion de Projets,
PRD GPT Résumé YouTube, PRD Auto-alimentation Apprentissage, Process idée→roadmap, `👁 Veille GitHub Claude Code`,
Problèmes développeurs). Résultat : **le scraper n'est pas un scoreur isolé, c'est le capteur d'entrée d'un volant
d'inertie de connaissance** qui doit cultiver Samuel, améliorer ses process, et **m'améliorer moi en arrière-plan**.

Constats qui fondent le design :
- **Maillon documenté** : réalise la roadmap v3 du `PRD GPT Résumé YouTube` (« veille auto : monitoring chaînes »),
  alimente `Auto-alimentation Apprentissage` (routage par thème) et la `Boîte à Idées` (Potentiel 🔥/⚡/💡).
- **Scoring déjà en production** (`👁 Veille GitHub`) : `≥80 install · 60-79 surveiller · <60 ignoré` ; **plafond
  étoiles** (<100★→max70, <500★→<80) ; **gate `.claude/`** ; pertinence `automation/workflow/planning/CRM/BTP/sport` ;
  **MCP whatsapp/n8n/garmin/intervals = priorité absolue**.
- **Thèse de fond** (`Problèmes développeurs`) : *« L'IA a démocratisé construire, pas vendre. »* → business = poids
  **moyen** (décision Samuel).
- **Rodin** : découpler la note-outil de la priorité-idée (ne pas gonfler via la centralité-vidéo = biais clickbait).

**Décisions Samuel** : veille **unifiée** (1 moteur) mais **2 verdicts** distincts ; périmètre = **toute la vision
(phases 1→3)** livrée **par phases** ; pas de panel des 4 (Rodin suffit) ; forme de la boucle méta **décidée en
phase 3**.

## Vision — 4 destinations d'un même flux

| Destination | Décision servie | Cible | Phase |
|---|---|---|---|
| 🔧 **Outil-à-installer** | « je l'installe ? » | log `👁 Veille GitHub` | 1 |
| 💡 **Idée-à-approfondir** | « j'approfondis ? » | `💡 Boîte à Idées` (Potentiel) | 1 |
| 📚 **Me cultiver** | « j'apprends quoi ? » | pages Apprentissage par thème | 2 |
| 🧠 **M'améliorer (méta)** | « quelle erreur ne plus refaire / quelle bonne pratique ? » | `CLAUDE.md` Leçons + rules + memory | 3 |

## Moteur partagé — score repo /100 (sobre)

| Axe | Pts | Mesure |
|---|---|---|
| **Qualité** | 40 | stars · récence · README (inchangé, ex-AXE2) |
| **Pertinence Samuel** | 45 | domaines (keywords **FR+EN**, frontières de mots, README inclus) + projets actifs/outils manquants (confiance) |
| **Intégrabilité** | 15 | branchable stack : Claude/MCP/n8n/Monday |

Domaines : `ia(fort) · automatisation(fort) · dev · btp · sport · business(moyen) · trading-finance(faible)`.
Outils manquants **prioritaires** (= « priorité absolue » de sa veille) : MCP **whatsapp, n8n, garmin, intervals.icu**
(+ OBAT, Notion-bridge). Contexte vidéo **hors du moteur** (vit dans le verdict Idée) → cache `repos-scored.json`
reste video-agnostique.

### Les 2 verdicts (Phase 1)
- **🔧 `verdict_outil`** — règles éprouvées de Samuel : **gate `.claude/`** (sinon `n/a`), **plafond étoiles**
  (<100★→70, <500★→<80), seuils `≥80 installer · 60-79 surveiller · <60 ignorer`.
- **💡 `verdict_idee`** — décentré : **curation vidéo** (sujet central, ≤45) + **nouveauté** (`manifest.repos_seen`,
  ≤30) + **thème** (≤25) → `{score, potentiel(🔥/⚡/💡), theme}`. Pas de gate `.claude/`, pas de plafond étoiles.

`llm-council` attendu : **Outil ~60 (👁 surveiller)** + **Idée 🔥 (theme=ia, top file)** — réconciliation Rodin×PRD.

### Classification destination (Phase 1 = tags ; routage = Phase 2)
Chaque **insight** extrait reçoit un `tag_destination ∈ {cultiver, process, meta-erreur, meta-bonne-pratique}`
(heuristique : tournures + thème + mots-clés « erreur/piège/bonne pratique/convention »). En Phase 1 le tag est
**posé et affiché** ; le **routage Notion** vers Apprentissage/Process est la **Phase 2**.

## Roadmap par phases

- **Phase 1 (cette PR)** : moteur 2 verdicts + profil harmonisé + tags de destination sur les insights. Net,
  testable, non destructif.
- **Phase 2** : routage auto des insights taggés → pages Notion (Apprentissage par thème / Process / Boîte à Idées /
  log Veille GitHub) via MCP Notion (écritures validées par Samuel, pas d'auto-push silencieux).
- **Phase 3** : boucle méta d'auto-amélioration (erreurs à ne plus reproduire + codes de bonne conduite →
  `CLAUDE.md`/memory/rules, hook `SessionStart`, skill `save-lesson`). **Forme décidée au démarrage de la phase 3**
  (étendre l'existant vs base dédiée). Sources : erreurs surfacées par la veille **et** corrections de Samuel en session.

## Profil restructuré — `data/youtube-scrapes/projets-samuel.json` (Phase 1)

`domaines_veille` (7 domaines, keywords FR+EN + poids) · `projets_actifs` (+ « Agence Workflows PME/PMI ») ·
`outils_manquants` (+ MCP whatsapp/n8n/garmin/intervals) · `integrations_stack` (claude/mcp/n8n/monday) ·
`themes_apprentissage` (8, dont `divers` fallback). Compat : `themes_surveilles` dérivé = `[d.nom for d in
domaines_veille]` pour `extract_tools`.

## Changements de code Phase 1 — `youtube_scraper.py`

| Zone | Action |
|---|---|
| `_score_axe1_claude`→`_score_integrabilite` | Claude/MCP/n8n/Monday (≤15) |
| `_score_axe2_qualite`→`_score_qualite` | inchangé |
| `_score_axe3/4`→`_score_pertinence` | fusion domaines FR+EN (frontières de mots, README inclus) + projets/outils + confiance |
| `score_repo` schéma | `qualite, pertinence_samuel, integrabilite, total_100`, `pertinence_confidence` |
| `_verdict_outil(repo, integrabilite)` (nouveau) | gate `.claude/` + plafond étoiles + seuils 80/60 |
| `_verdict_idee(repo, citing_videos, manifest)` (nouveau, au report) | curation + nouveauté + thème → potentiel |
| `tag_destination(insight)` (nouveau) | heuristique cultiver/process/meta-erreur/meta-bonne-pratique |
| `cmd_report` | sections `🔧 Outils` + `💡 Idées à approfondir` + `📚 Insights (taggés)` ; payloads mappés |
| compat | `themes_surveilles` dérivé · `--axe` (`qualite/pertinence/integrabilite`) · string axes `Q/P/I` |

## Docs & Notion (Phase 1)

- `.claude/memory/scoring-profile.md` : réécrire en **1 moteur + 2 verdicts + 4 destinations** ; documenter domaines,
  MCP prioritaires, plafond étoiles, gate `.claude/`, tags de destination.
- `skills/samuel/youtube-scraper/SKILL.md` : 2 verdicts, profil, destinations, roadmap phases.
- Fiche chaîne Notion : porte les sections des verdicts + insights taggés (routage = Phase 2).

## Actions post-implémentation (Phase 1)

1. `scrape https://youtube.com/@ia_irl --months 3 --refresh` → 2 verdicts/repo + insights taggés.
2. `report ia-irl --format both` → upsert ligne « IA IRL » Notion, pas de doublon.
3. MAJ PR #6 (récap : moteur 2 verdicts + roadmap phases) + commit + push (`claude/youtube-scraper-github-26iaoq`).

## Backlog (post-Phase 1 — noté en cours de route)

- **Refonte page Notion « Gestion de Projets »** : rédiger un **prompt pour l'IA de Notion** (plutôt que pousser
  via MCP) pour faciliter la restructuration et contourner les barrières d'écriture MCP. → outille la Phase 2.
- **Exploiter les agents IA de Notion** : Notion propose désormais des agents IA non exploités — évaluer leur
  usage pour le routage/automatisation de la veille (Phase 2/3) plutôt que tout faire en MCP côté script.

## Vérification (Phase 1)

1. `_verdict_outil` : repo `.claude/` 600★ récent → ≥80 (✅) ; 50★ → plafonné 70 (👁) ; sans `.claude/` → `n/a`.
2. **`llm-council`** : Outil ~60 (👁) **ET** Idée 🔥 (theme=ia, top) — réconciliation prouvée.
3. Repo anglophone on-thème (MCP `ai/llm`) → pertinence sans token FR (fin du biais linguistique).
4. Repo = MCP whatsapp/n8n/garmin/intervals → priorité absolue dans les 2 verdicts.
5. Insights portent un `tag_destination` cohérent (ex. un « piège » → meta-erreur ; une « convention » → meta-bonne-pratique).
6. Cache `repos-scored.json` video-agnostique ; ligne Notion @ia_irl sans doublon.
