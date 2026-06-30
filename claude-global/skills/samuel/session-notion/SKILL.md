---
name: session-notion
description: "Sync automatique des sessions Claude vers un work log Notion structuré. DÉCLENCHE ce skill dès que Samuel mentionne logger une session, archiver une conversation, \"note ça dans Notion\", \"enregistre ce qu'on a fait\", \"résumé de session\", \"work log\", \"journal de bord\", \"trace cette décision\", \"garde une trace\", \"archive cette conversation\", \"fais un résumé pour Notion\". Déclenche aussi en fin de session productive (décision prise, livrable produit, action définie) pour proposer automatiquement l'archivage."
---

# Session → Notion Samuel — Work Log Automatique

## Contexte opérateur
Samuel travaille sur plusieurs projets en parallèle (SC Rénovations, formation, expansion). Les décisions prises, actions définies et livrables produits doivent être tracés pour éviter la perte d'information entre sessions.

---

## Routing — identifier le type de log

| Situation | Type de log | Format |
|---|---|---|
| Décision stratégique prise | Décision log | §A |
| Livrable produit (doc, skill, plan) | Livrable log | §B |
| Action définie avec deadline | Action log | §C |
| Résumé de session complète | Session summary | §D |
| Information à mémoriser | Mémoire log | §E |

---
## ⚠️ Gotchas — édition de pages Notion via MCP

### Matching `update_content` (search-replace)
Le contenu stocké conserve les **échappements markdown** : `\~`, `\>`, `\<` (et parfois `\*`, `\_`).
- `old_str` doit reproduire ces backslashes **à l'identique**, sinon le match échoue.
- Exemple : viser `CTL \~38-42`, PAS `CTL ~38-42`.
- Les caractères `× → · — – ≤ ↓` ne sont **pas** échappés → les laisser tels quels.

### Échec silencieux
L'outil renvoie `{page_id}` même si **aucun** `old_str` n'a matché (pas de distinction match total / partiel / nul).
→ **Toujours re-fetch la page après écriture** pour vérifier que la modif a pris.
Ne jamais conclure "c'est fait" sur la seule base du retour de l'outil.

### Stratégie sûre
- Cibler des `old_str` courts et distinctifs **sans** caractères échappés quand c'est possible.
- Grouper plusieurs `content_updates` indépendants en un appel (exécution séquentielle, stop au 1er échec).
- Pour supprimer un gros bloc : copier le texte **exact** depuis un fetch récent (échappements inclus).

## §A — Format Décision Log

```markdown
## Décision — [Titre court]
**Date** : [date]
**Projet** : [SC Réno / Formation / Expansion / Personnel]
**Contexte** : [1–2 lignes — pourquoi cette décision s'imposait]
**Décision** : [Ce qui a été décidé — précis et actionnable]
**Alternatives écartées** : [Ce qui n'a PAS été retenu + raison]
**Condition de révision** : [Quand reconsidérer cette décision]
**Next step** : [Action immédiate qui découle de cette décision]
```

---

## §B — Format Livrable Log

```markdown
## Livrable — [Nom du livrable]
**Date** : [date]
**Projet** : [projet]
**Type** : [skill / document / plan / script / analyse / autre]
**Description** : [Ce que c'est et à quoi ça sert]
**Localisation** : [Où trouver le fichier / skill / document]
**Statut** : [Brouillon / Validé / Déployé]
**Prochaine itération** : [Ce qui manque ou doit être amélioré]
```

---

## §C — Format Action Log

```markdown
## Action — [Titre de l'action]
**Date création** : [date]
**Projet** : [projet]
**Responsable** : [Samuel / Maxime / Pascale / autre]
**Description** : [Ce qui doit être fait — précis]
**Deadline** : [date ou "dès que possible"]
**Bloquants** : [Ce qui empêche de commencer, si applicable]
**Dépendances** : [Actions ou décisions préalables requises]
```

---

## §D — Format Session Summary

Structure bullet — 5 sections max :

```markdown
## Session — [Date] — [Thème principal]

### Ce qui a été fait
- [bullet 1]
- [bullet 2]

### Décisions prises
- [décision 1 + contexte en 1 ligne]

### Actions définies
- [ ] [action] → [responsable] → [deadline]

### Livrables produits
- [livrable + localisation]

### Points ouverts / à reprendre
- [question ou sujet non résolu]
```

---

## §E — Format Mémoire Log

```markdown
## Mémo — [Titre]
**Date** : [date]
**Catégorie** : [Contexte SC Réno / Finance / Légal / Technique / Personnel]
**Information** : [L'information à retenir — complète et autonome]
**Source** : [D'où vient cette information]
**Expiration** : [Date à laquelle cette info devient obsolète, si applicable]
```

---

## Workflow d'utilisation

### Fin de session productive (proposer automatiquement)
Si la session a produit une décision, un livrable ou une action, proposer :
> "Veux-tu que je génère un résumé Notion de cette session ?"

### Génération du log
1. Identifier le(s) type(s) de log adaptés (§A à §E)
2. Extraire les informations de la conversation
3. Produire le(s) bloc(s) markdown prêts à copier-coller dans Notion
4. Si Notion MCP disponible : proposer l'envoi direct

### Via Notion MCP (si connecté)
- Utiliser le MCP Notion disponible dans l'environnement Samuel
- Page cible recommandée : "Work Log [Année]" dans l'espace SC Rénovations ou Personnel
- Créer une entrée par session, ne pas écraser les entrées précédentes

---

## Règles
- Ne jamais résumer en perdant les décisions concrètes
- Toujours inclure le "next step" dans les logs de décision
- Les actions doivent être SMART (Spécifique, Mesurable, Attribuée, Réaliste, Temporelle)
- Proposer le log systématiquement après une session à fort enjeu