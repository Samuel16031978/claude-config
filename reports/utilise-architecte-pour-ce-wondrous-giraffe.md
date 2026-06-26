# Plan — Réécriture de `/ask-panel` en « panel des 4 » sans API, via pont Notion + boucle de notation

## Contexte (pourquoi)

Samuel possède déjà un `/ask-panel` : un panel de **3 voix** (Claude + Gemini + DeepSeek)
piloté par un script `ask_panel.py`, avec une **passe de consensus unique** (2/3), qui met à
jour un `SKILL.md` puis `git push`. Deux problèmes au regard de ce qu'il veut :

1. `ask_panel.py` appelle **des API** Gemini/DeepSeek → contraire à « rester dans mes
   forfaits d'abonnement, pas d'API ».
2. Une seule passe de consensus → pas de **boucle de notation jusqu'à 10/10**.

Inspiré par le connecteur Notion de ChatGPT, Samuel veut **faire évoluer** ce panel :
**4 voix sans API** (le connecteur Notion sert de **pont entre les IA**), une **boucle de
notation** qui tourne jusqu'à ~10/10, et un usage **polyvalent** (améliorer un `SKILL.md`
*ou* trancher une idée business à lancer/abandonner).

### Décisions validées avec Samuel
- **Voix non-Claude sans API** = **pont Notion semi-auto** : Claude écrit la question sur une
  page Notion ; Samuel déclenche ChatGPT / Gemini dans leurs apps (qui lisent la page via
  *leur* connecteur Notion) ; elles répondent sur la page ; Claude relit et confronte. Zéro
  API ; **une étape manuelle par tour**, assumée.
- **`/ask-panel` est remplacé** par cette nouvelle version (même invocation, entrailles
  réécrites ; `ask_panel.py` et ses API sont abandonnés).
- **Polyvalent** : la cible est paramétrable — un `SKILL.md` (cas actuel) **ou** une idée
  business (verdict LANCER/ABANDONNER). La grille de notation s'adapte.

> Limite assumée : Claude automatise tout **son** côté (sa voix, la notation, la boucle, la
> lecture/écriture Notion via MCP, le git). Il ne peut pas *déclencher* ChatGPT/Gemini — le
> pont est asynchrone, médié par la page Notion ; Samuel lance leur tour.

## Précédents réutilisés dans le dépôt
- `claude-global/skills/figmirror/references/iter-loop-spec.md` — boucle Créateur↔Critique
  éprouvée : scorecard, `max_iters`, règle de décision continue/arrête, fallback
  « meilleur tour », fichiers de rôle servant de system-prompt aux sous-agents. **Modèle.**
- `claude-global/skills/Samuel/first-principles-business/SKILL.md` — 5 lois Musk, lentille du
  panéliste « faisabilité » pour les idées business.
- `claude-global/skills/notion-watch-reporter/SKILL.md` + `.../Samuel/skill-sync-notion/SKILL.md`
  — conventions Notion MCP (`notion-search`, `notion-fetch`, `notion-create-pages`,
  `notion-update-page`) et style FR.

## Approche retenue

Créer le skill **`ask-panel`** (remplace le `/ask-panel` actuel ; invocation `/ask-panel`
préservée) dans le namespace de Samuel, calqué sur la structure de `figmirror`.

### Le panel des 4 voix
| Voix | Source | Mode |
|------|--------|------|
| **Claude** | natif (outil interne) | **automatique** |
| **ChatGPT** | son connecteur Notion | déclenché par Samuel (pont Notion) |
| **Gemini** | app / connecteur | déclenché par Samuel (pont Notion) |
| **Notion AI** (ou DeepSeek) | IA native Notion | déclenché par Samuel (pont Notion) |

### Boucle de notation (le cœur nouveau)
Pour `tour = 1..max_tours` (défaut **4**) :
1. **Poster** sur la page Notion : la question + l'état courant de la cible + un gabarit de
   réponse balisé (une section par voix).
2. **Pause handoff** : Claude affiche « 🤝 J'ai posté la question. Déclenche ChatGPT/Gemini/
   Notion AI sur la page, puis dis-moi quand c'est fait. » et **attend** la confirmation de
   Samuel.
3. **Relire** la page (`notion-fetch`) → récupérer les 3 réponses externes ; **ajouter la
   voix Claude**.
4. **Noter** : chaque voix donne une **note /10** + critique sur la cible courante ; agrégat
   = score global /10.
5. **Confronter** (consensus étendu à 4 voix) : point soutenu par **≥ 3/4** → consensus
   retenu ; **divergence** (pas de majorité) → poser la question à Samuel et attendre son
   arbitrage.
6. **Décider** :
   - **CIBLE ATTEINTE** si global ≥ cible (défaut **9/10**, configurable 10/10) → appliquer
     la mise à jour finale (cf. ci-dessous).
   - **ABANDON** si drapeau fatal (idée business) ou **plateau** (gain < 0.5 entre deux tours)
     ou `max_tours` atteint → restituer le meilleur tour + recommandation franche.
   - **ITÉRER** sinon : synthétiser le consensus en une version améliorée de la cible → tour
     suivant (re-poster sur Notion).

> La boucle converge toujours (ATTEINTE / ABANDON), jamais d'infini. 10/10 = idéal, pas
> condition bloquante.

### Application finale selon la cible (polyvalence)
- **Cible = SKILL.md** : réécrire **uniquement** la section concernée avec le consensus +
  arbitrages, puis `git add/commit/push`. Message : `maj <skill>: <résumé> — consensus N/4`.
- **Cible = idée business** : écrire le **verdict** (LANCER/ABANDONNER) + le journal des
  notes sur la page Notion ; **pas** de commit de SKILL.md.

### Git / branche
Mon commit créant ces fichiers va sur `claude/notion-connector-loop-models-vwv1j6`
(branche courante, déjà active). Le comportement git **à l'exécution** du skill (étape
SKILL.md) reste paramétrable ; je conserve le push vers `main` par défaut comme le flux
actuel de Samuel, en le documentant.

## Fichiers à créer
Sous `claude-global/skills/Samuel/ask-panel/` :
- `SKILL.md` — squelette d'orchestration. Frontmatter : `name: ask-panel`, `description` (FR,
  déclencheurs : « panel des 4 », « ask-panel », « confronter les IA », « noter jusqu'à
  10/10 », « idée à lancer ou abandonner »), `user-invocable: true`,
  `argument-hint: "\"<question>\" [cible: skill|idée]"`, `allowed-tools` : `Agent`, `Read`,
  `Bash`, et outils Notion MCP. Contient : sync, choix de cible (skill vs idée), la boucle de
  notation, le pont Notion, le consensus 3/4 + arbitrage, l'application finale, le résumé.
- `references/voix-panel.md` — les 4 voix, leur source, et le **protocole de pont Notion
  semi-auto** (gabarit de page, où chaque IA répond, étape de déclenchement manuel, relecture).
- `references/grille-notation.md` — grille **adaptative** : dimensions + ancres 0-10 pour le
  cas SKILL.md (clarté, complétude, exactitude, exécutabilité) et pour le cas idée business
  (désirabilité, faisabilité, viabilité, risque + drapeau fatal) ; règle de consensus 3/4 ;
  définition du plateau ; schéma JSON attendu par voix.
- `references/notion-bridge.md` — format de la page Notion (titre daté, section par voix,
  journal des tours), noms d'outils MCP, gestion du préfixe serveur MCP variable.

## Migration / nettoyage
- `ask_panel.py` (hors dépôt) devient **obsolète** : la nouvelle version n'appelle aucune
  API. À mentionner dans le SKILL.md (section « Migration »). Aucun fichier API à committer.
- Optionnel : ligne dans la table de `skill-sync-notion/SKILL.md` (mapping skill ↔ page Notion).

## Vérification (de bout en bout)
1. **Cible SKILL.md** : `/ask-panel "améliore la section X de <skill>"` → poste sur Notion,
   pause handoff, relit les 3 voix + Claude, note /10, confronte (3/4), itère, et à la cible
   atteinte réécrit la bonne section + commit.
2. **Cible idée business** : `/ask-panel "idée business : <…>"` → boucle de notation → verdict
   **LANCER** (bonne idée) ou **ABANDON** (faille fatale / plateau) **sans boucle infinie**.
3. **Pont Notion** : confirmer écriture de la question (`notion-create-pages`/`update-page`)
   et relecture des réponses (`notion-fetch`) ; vérifier la pause d'attente du déclenchement
   manuel.
4. **Zéro API** : vérifier qu'aucun appel réseau externe n'est fait — uniquement `Agent`
   (abonnement Claude) + outils Notion MCP (abonnement Notion) + git.
5. **Consensus/arbitrage** : forcer une divergence 1/1/1/1 → le skill pose la question
   d'arbitrage à Samuel et attend.
