---
name: ask-panel
description: "Panel des 4 : confronte 4 voix IA (Claude + ChatGPT + Gemini + Notion AI) en boucle de notation jusqu'à ~10/10, via le connecteur Notion (sans API). Améliore un SKILL.md ou tranche une idée business (lancer/abandonner). Déclencheurs : panel des 4, ask-panel, confronter les IA, noter jusqu'à 10/10, idée à lancer ou abandonner."
user-invocable: true
argument-hint: "\"<question>\" [cible: skill|idée]"
allowed-tools:
  - Read
  - Bash
  - Agent
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-search
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-fetch
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-create-pages
  - mcp__9998ab9a-7b0b-4817-878b-367952b8f929__notion-update-page
---

# Ask Panel — le panel des 4

Confronte **4 voix IA** sur une question, en **boucle de notation** jusqu'à atteindre la
cible (~10/10) ou conclure à l'abandon. Le **connecteur Notion** sert de pont entre les IA :
aucune API n'est appelée, tout reste dans les abonnements (Claude + Notion).

## Migration depuis l'ancien `/ask-panel`

Cette version **remplace** l'ancien flux à base de `ask_panel.py` (qui appelait les API
Gemini/DeepSeek). Le script et ses clés API ne sont **plus utilisés** : les voix non-Claude
arrivent désormais par le pont Notion (voir `references/notion-bridge.md`).

## Les 4 voix

| Voix | Source | Mode |
|------|--------|------|
| Claude | natif | automatique |
| ChatGPT | son connecteur Notion | déclenché par Samuel |
| Gemini | app / connecteur | déclenché par Samuel |
| Notion AI | IA native Notion | déclenché par Samuel |

Rôles détaillés et protocole de déclenchement : `references/voix-panel.md`.

## Cible (polyvalent)

Détermine la cible d'après la question (ou l'argument explicite) :
- **`skill`** — améliorer une section d'un `SKILL.md` du dépôt.
- **`idée`** — trancher une idée business (verdict **LANCER** / **ABANDONNER**).

La grille de notation s'adapte à la cible : `references/grille-notation.md`.

## Étapes

### 1. Sync
```bash
git pull origin main
```

### 2. Cadrer la cible
- Si **skill** : lis les `description` de `claude-global/skills/*/SKILL.md`, choisis le plus
  pertinent. **Annonce** : « Cette question concerne `<skill>`. Je continue ? [o/n] » et
  attends confirmation. Charge le contenu actuel comme état de départ.
- Si **idée** : reformule l'idée business en un brief de départ (problème, marché, ressources
  de Samuel).

### 3. Boucle de notation (`max_tours`, défaut 4)
Pour chaque tour `N`, applique le protocole de `references/notion-bridge.md` :
1. **Poster** sur la page Notion : la question + l'état courant de la cible + un gabarit avec
   une section vide par voix.
2. **Pause handoff** : affiche
   « 🤝 Question postée sur Notion. Déclenche ChatGPT, Gemini et Notion AI sur la page, puis
   dis-moi quand c'est prêt. » et **attends** la confirmation de Samuel.
3. **Relire** la page (`notion-fetch`), récupérer les 3 réponses externes, **ajouter la voix
   Claude** (formule ta propre réponse depuis l'état courant).
4. **Noter** : chaque voix donne une note /10 + critique selon la grille ; calcule le score
   global /10.
5. **Confronter** (consensus 4 voix) : point soutenu par **≥ 3/4** → retenu. Sinon
   **divergence** → pose la question d'arbitrage à Samuel (format dans `voix-panel.md`) et
   attends sa réponse.
6. **Décider** :
   - **CIBLE ATTEINTE** : global ≥ cible (défaut 9/10, configurable 10/10) → étape 4.
   - **ABANDON** : drapeau fatal (idée), ou plateau (gain < 0.5 vs tour précédent), ou
     `max_tours` atteint → restitue le meilleur tour + recommandation franche → étape 4.
   - **ITÉRER** : synthétise le consensus en une version améliorée de la cible → tour `N+1`.

### 4. Appliquer le résultat
- **Cible = skill** : réécris **uniquement** la section concernée du `SKILL.md` (consensus +
  arbitrages). Ne touche pas aux autres sections. Pas de section « dernière mise à jour »
  (l'historique vit dans git). Puis :
  ```bash
  git add claude-global/skills/<skill>/SKILL.md
  git commit -m "maj <skill>: <résumé court> — consensus <N>/4"
  git push origin main
  ```
- **Cible = idée** : écris sur la page Notion le **verdict** (LANCER/ABANDONNER), le score
  global et le **journal des tours** (trajectoire des notes). Pas de commit de SKILL.md.

### 5. Confirmer
```
✅ <skill mis à jour | verdict idée> : <cible>
📊 Notes : <trajectoire ex. 6 → 8 → 9> | consensus <N>/4 | <Y> arbitrés par Samuel
🔗 <commit court | page Notion>
```

## Règles
- **Aucune API** : seuls `Agent` (Claude), les outils Notion MCP et git sont permis.
- La boucle converge toujours (ATTEINTE ou ABANDON) — jamais d'infini.
- Toujours attendre la confirmation de Samuel aux deux points bloquants : choix du skill
  (étape 2) et pause handoff (étape 3.2), et à chaque arbitrage de divergence.
- Ne jamais committer de secret ; ne jamais pousser sur une autre branche sans accord.
