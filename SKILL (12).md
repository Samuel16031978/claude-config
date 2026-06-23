---
name: notion-protocol
description: "Protocole d'architecture et lecture/écriture Notion sous contrainte MCP (texte brut, IDs uniques, patterns append/update)."
---

# Notion Protocol

## Règles d'architecture (5 règles)

### Règle 1 — Architecture
- Chaque entité importante = une page dédiée avec ID unique
- Les bases de données Notion sont préférées aux pages simples pour les listes structurées
- Hiérarchie : Workspace > Section > Base de données / Page
- Ne jamais dupliquer le même contenu dans deux pages

### Règle 2 — Protocole de lecture
- Toujours lire via `notion-fetch` avec l'ID de page exact
- En cas d'ambiguïté sur l'ID : utiliser `notion-search` d'abord
- Lire le contenu complet avant toute modification
- Les IDs Notion sont au format UUID : `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` ou sans tirets

### Règle 3 — Protocole d'écriture
- **Append** : ajouter du contenu en bas d'une page existante (ne pas écraser)
- **Update** : modifier un bloc spécifique via son ID de bloc
- **Jamais** : réécrire une page entière sauf création initiale
- Toujours confirmer l'écriture avec un `notion-fetch` post-update

### Règle 4 — Versioning
- Pour les documents stratégiques : ajouter date de dernière modification en bas de page
- Format : `*Dernière mise à jour : YYYY-MM-DD*`
- Conserver l'historique des décisions importantes dans un bloc dédié

### Règle 5 — Création de page
- Définir le parent (page ou base de données) avant création
- Titre = identifiant métier clair (pas « Note 1 », mais « Brief Chantier Dupont »)
- Ajouter les propriétés de base immédiatement après création

## Applications par domaine

| Domaine | Pattern Notion recommandé |
|---------|---------------------------|
| Skills Claude | Base de données avec propriétés nom/description/date |
| Chantiers SC Rénovations | Page par chantier + sous-pages lots |
| CRM prospects | Base de données avec vues filtrées par statut |
| Planning sportif | Calendrier Notion ou base de données date |
| Notes réunion | Page par réunion, rattachée au projet |

## Checklist pré-écriture

- [ ] J'ai lu la page cible avec `notion-fetch`
- [ ] Je connais l'ID exact de la page ou du bloc à modifier
- [ ] Je suis en mode append (pas réécriture totale)
- [ ] Le contenu ne contient pas de secret ou token
- [ ] La modification est cohérente avec l'architecture existante
