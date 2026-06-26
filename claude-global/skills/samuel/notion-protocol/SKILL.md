---
name: notion-protocol
description: "Protocole d'interaction Notion sous contrainte MCP (search snippets ≤500 chars + update-page uniquement) : architecture des pages en texte brut, IDs H2 searchables, structure 4 blocs SNAPSHOT/OBJECTIFS/CONTENU/LOG, protocoles de lecture et d'écriture append vs overwrite. Déclencheurs : écrire dans Notion, page Notion, SNAPSHOT, LOG append, protocole Notion, work log."
---

# Protocole d'interaction Notion

## Contexte et contrainte
Le MCP Notion (côté claude.ai) expose souvent uniquement `notion-search` (snippets 500 chars max) et `notion-update-page`, sans `notion-fetch`. Toute architecture doit être conçue sous cette contrainte.

---

## Règle 1 — Architecture obligatoire des pages

**Format texte brut uniquement**
- Interdit : tableaux natifs Notion, toggles, blocs imbriqués, colonnes
- Obligatoire : texte brut, titres H2 avec IDs uniques, listes simples

**IDs uniques searchables dans chaque H2** — Format : `NOM-PROJET-CODE-ANNÉE`
Exemples : `SNAPSHOT-S1-W23-2026`, `LOG-SCREN-THOREL-2026`, `DECISIONS-HOLDING-MP-2026`

**Structure standard 4 blocs (dans cet ordre)**
- `SNAPSHOT-[ID]` — état actuel court, seul bloc mutable
- `OBJECTIFS-[ID]` — référence stable, rarement modifiée
- `CONTENU-[ID]` — corps principal
- `LOG-[ID]` — historique append-only, jamais modifié en arrière

Le LOG se termine toujours par : `<!-- PROCHAINE_ENTREE -->`

**Granularité : une sous-page = une unité logique atomique**
- Une semaine, un chantier, un dossier, une décision
- Si contenu < 500 chars → lecture 100% garantie
- Jamais une seule grande page avec tout dedans

---

## Règle 2 — Protocole de lecture (séquence obligatoire)
Avant toute écriture, chercher dans cet ordre :
1. `notion-search("SNAPSHOT-[ID]")` → état actuel
2. `notion-search("LOG-[ID]")` → historique récent
3. `notion-search("CONTENU-[ID]")` → données si nécessaire

Principe clé : `notion-search` ne retourne JAMAIS 100% du contenu. Toujours partiel. Multiplier les requêtes si fragment critique manquant. Ne jamais supposer avoir tout lu.

---

## Règle 3 — Protocole d'écriture

**Pattern A — Append (pour LOG et historique)**
Utiliser pour : ajouter entrée log, noter événement, enregistrer séance, tracer décision.
- `command: insert_content`
- `position: end`
- Format d'une entrée : `[AAAA-MM-JJ] Action/événement — détail — statut`

**Pattern B — Snapshot overwrite (pour état actuel uniquement)**
Utiliser pour : mettre à jour CTL, statut chantier, décision active.
- `command: update_content`
- `old_str` : contenu exact récupéré par search (jamais de mémoire)
- `new_str` : nouveau contenu
- Condition stricte : utiliser uniquement si le snippet contient le texte exact complet du SNAPSHOT. Si doute → append uniquement.

**Anti-patterns interdits**
- `update_content` sans avoir lu `old_str` exact via search préalable
- Modifier le passé dans un LOG
- Écrire dans un tableau natif Notion
- Utiliser un `old_str` de mémoire (pas d'un snippet réel)

---

## Règle 4 — Versioning si update_content échoue
Si erreur "no match found" → ne jamais insister sur le replace. Stratégie de repli :
1. Append un bloc `OVERRIDE-[ID]-[DATE]` en fin de page avec le nouveau contenu
2. Mettre à jour le SNAPSHOT pour pointer vers la nouvelle version active

Claude identifie toujours la version courante via : `STATUT: active`

---

## Règle 5 — Création de nouvelle page
Structure minimale obligatoire :
- `SNAPSHOT-[ID]` : Statut + Dernière MAJ + 2-3 lignes d'état
- `CONTENU-[ID]` : Corps principal en texte brut
- `LOG-[ID]` : `[date] Création` + `<!-- PROCHAINE_ENTREE -->`

---

## Domaines d'application
S'applique sans exception à tous les espaces Notion de Samuel :
- Sport / Entraînement : semaines S0-S10, historique séances
- SC Rénovations : chantiers, devis, suivi clients
- Holding / Juridique : décisions AG, dossiers, contrats
- Skills Claude : référentiel, work log sessions
- Personnel : projets, décisions, notes

---

## Checklist avant toute écriture Notion
- ☐ J'ai cherché `SNAPSHOT-[ID]` avant d'écrire
- ☐ J'utilise `insert_content` pour le LOG (jamais `update_content` sur LOG)
- ☐ Mon `old_str` est issu d'un snippet réel, pas de ma mémoire
- ☐ La page cible est en texte brut (pas de tableau natif)
- ☐ Chaque section H2 a un ID unique searchable
- ☐ Le LOG se termine par `<!-- PROCHAINE_ENTREE -->`
