---
name: ask-panel
description: "Panel des 4 : Claude orchestre 3 IA contributrices (ChatGPT, Gemini, DeepSeek) via le connecteur Notion (sans API), confronte les voix selon le protocole-panel (consensus 3/4 + 6 règles anti-biais) et note en boucle jusqu'à la cible. Polyvalent : améliore un SKILL.md ou tranche une idée business (lancer/abandonner). Déclencheurs : panel des 4, ask-panel, confronter les IA, noter jusqu'à 10/10, idée à lancer ou abandonner."
user-invocable: true
argument-hint: "\"<question>\" [cible: skill|idée]"
allowed-tools:
  - Read
  - Bash
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-search
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-fetch
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-create-pages
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-update-page
---

# Ask Panel — le panel des 4

Exécute le **protocole-panel** de Samuel : Claude est l'**orchestrateur**, et ChatGPT,
Gemini, DeepSeek sont des **contributeurs** dont les réponses arrivent par le **connecteur
Notion** (sans API — copier-coller par Samuel). Claude confronte les 4 voix (consensus 3/4),
arbitre les divergences, et **note en boucle** jusqu'à atteindre la cible ou conclure.

> **Source autoritaire** : la page Notion `⚖️ protocole-panel`
> (`https://app.notion.com/p/37d34dfdcd3b8175b952d837fd01271b`). En cas de doute, elle prime
> sur ce fichier. Version condensée des règles : `references/protocole-confrontation.md`.

## Migration depuis l'ancien `/ask-panel`

Remplace le flux à base de `ask_panel.py` (API Gemini/DeepSeek). Plus aucune API : les voix
non-Claude passent par le pont Notion (`references/notion-bridge.md`).

## Les 4 voix

| Voix | Rôle | Accès page Notion |
|------|------|-------------------|
| **Claude** | orchestrateur (formule, confronte, arbitre, note) | natif (Claude Code) |
| **ChatGPT** | contributeur | connecteur Notion (offres payantes) |
| **Gemini** | contributeur | **copier-coller manuel** (pas de connecteur grand public) |
| **DeepSeek** | **contradicteur désigné** (règle 4) | via Notion AI (sélecteur de modèle) ou copier-coller |

Détails et sourcing : `references/voix-panel.md`.

## Cible (polyvalent)

- **`skill`** — améliorer une section d'un `SKILL.md` du dépôt (→ commit).
- **`idée`** — trancher une idée business : **LANCER / LANCER SOUS CONDITIONS / ABANDONNER**.

Grille de notation adaptative : `references/grille-notation.md`.

## Étapes

### 1. Sync
```bash
git pull origin main
```

### 2. Cadrer la cible + formuler la question (6 règles)
- **skill** : choisis le `SKILL.md` pertinent (lis les `description` de
  `claude-global/skills/*/SKILL.md`). Annonce : « Cette question concerne `<skill>`. Je
  continue ? [o/n] » et attends. Charge le contenu actuel comme état de départ.
- **idée** : reformule en brief (problème, marché, ressources de Samuel).
- **Formule la question selon les 6 règles obligatoires** de `protocole-confrontation.md` :
  cadrage neutre, quantification exigée, test de transposabilité, **un contradicteur désigné**,
  niveau de confiance demandé, une variable par question.

### 3. Boucle de notation (`max_tours`, défaut 4)
Pour chaque tour `N`, via `references/notion-bridge.md` (base **Runs — Panels**) :
1. **Créer/MAJ le Run** : poster le *Prompt master* + l'état courant + une section par voix.
   `Statut = Envoyé`.
2. **Pause handoff** : affiche
   « 🤝 Run posté sur Notion. (1) Déclenche ChatGPT (connecteur) et DeepSeek (via Notion AI)
   sur la page. (2) Copie la question dans Gemini et colle sa réponse. Dis-moi quand c'est
   prêt. » et **attends** la confirmation de Samuel.
3. **Relire** la page (`notion-fetch`), extraire les 3 voix externes, **ajouter Claude**.
   `Statut = Réponses reçues`.
4. **Confronter** selon le workflow de `protocole-confrontation.md` : consensus (≥ 3/4),
   tableau des divergences, **arbitrage motivé par les données** (pas par la majorité),
   **détection du faux consensus** (sources communes), conclusions fragiles, **méta-vérif**.
   En cas de divergence non tranchable, pose la question d'arbitrage à Samuel et attends.
5. **Noter** : chaque voix → note /10 par dimension ; score global /10. `Statut = Consensus`.
6. **Décider** :
   - **CIBLE ATTEINTE** : global ≥ cible (défaut 9/10) → étape 4.
   - **ABANDON** : drapeau fatal (idée), plateau (gain < 0.5), ou `max_tours` → meilleur tour
     + recommandation franche → étape 4.
   - **ITÉRER** : synthétise le consensus en version améliorée → tour `N+1` (re-poster).
   - Si un **signal d'alarme méta** est rouge : proposer un tour de contre-expertise avant de
     figer.

### 4. Appliquer le résultat
- **skill** : réécris **uniquement** la section concernée du `SKILL.md` (consensus +
  arbitrages). Pas de section « dernière MAJ » (git fait l'historique). Puis :
  ```bash
  git add claude-global/skills/<skill>/SKILL.md
  git commit -m "maj <skill>: <résumé> — consensus <N>/4"
  git push origin main
  ```
- **idée** : renseigne sur le Run le **verdict consolidé** (LANCER/SOUS CONDITIONS/ABANDONNER),
  le score global, la trajectoire et `Décision (résumé)`. `Statut = Décidé`. Pas de commit.

### 5. Confirmer
```
✅ <skill mis à jour | verdict idée> : <cible>
📊 Notes : <trajectoire ex. 6 → 8 → 9> | consensus <N>/4 | <Y> arbitrés par Samuel
🔗 <commit court | URL du Run Notion>
```

## Règles
- **Aucune API** : seuls les outils Notion MCP, Bash et git sont permis.
- La boucle converge toujours (ATTEINTE ou ABANDON) — jamais d'infini.
- Points bloquants où attendre Samuel : choix du skill (étape 2), pause handoff (3.2), chaque
  arbitrage de divergence.
- Respecter le protocole-panel : 6 règles de formulation + méta-vérification avant tout verdict.
- Ne jamais committer de secret ; ne pas pousser sur une autre branche sans accord.
