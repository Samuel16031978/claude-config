---
name: skill-sync-notion
description: "Synchronisation automatique des skills Samuel vers Notion et déclenchement de la routine Claude Code de sync GitHub. DÉCLENCHE ce skill OBLIGATOIREMENT après toute création ou modification d'un skill Samuel (nouveau SKILL.md, mise à jour d'un SKILL.md existant, \"maj nécessaire ?\", \"mets à jour ce skill\", \"crée un skill\", \"modifie le skill X\"). Ce skill doit s'exécuter comme étape finale systématique du workflow de création/modification de skill — jamais sauter cette étape."
---

# Skill Sync Notion — Synchronisation Skills ↔ Notion ↔ GitHub

## Rôle

Après toute création ou modification d'un skill Samuel, ce skill :
1. Met à jour (ou crée) la page Notion correspondante avec le contenu intégral du SKILL.md
2. Déclenche la routine Claude Code "Sync Skills" via son endpoint API pour qu'elle committe le delta dans GitHub

---

## Configuration

> 🔒 **JAMAIS de token en clair ici.** Les valeurs ci-dessous sont des **références** à des
> variables d'environnement, à définir dans `~/.claude/.env.local` (gitignoré). Un token réel
> dans ce fichier = fuite immédiate au moindre sync.

```
NOTION_PARENT_PAGE_ID    : 35734dfdcd3b8179b160fe16b555081a   # page "Skills Claude — Référentiel Samuel"
CLAUDE_CODE_ROUTINE_URL  : https://api.anthropic.com/v1/claude_code/routines/$ROUTINE_TRIGGER_ID/fire
CLAUDE_CODE_ROUTINE_TOKEN: $CLAUDE_CODE_ROUTINE_TOKEN   # depuis l'env, jamais en dur
NOTION_TOKEN             : $NOTION_TOKEN                # depuis l'env, jamais en dur
```

---

## Protocole d'exécution

### Étape 1 — Identifier le skill modifié

Extraire de la conversation :
- Nom du skill (ex : `rodin`, `training-adaptatif`)
- Contenu intégral du SKILL.md tel que validé dans la conversation
- Type d'opération : **création** (nouvelle page Notion) ou **mise à jour** (page existante)

### Étape 2 — Mettre à jour Notion

#### Si mise à jour (page existante)

Utiliser le MCP Notion `notion-update-page` avec `command: replace_content` :

```
page_id : [ID de la page Notion correspondant au skill]
command : replace_content
new_str : [contenu intégral du SKILL.md — corps uniquement, sans frontmatter YAML]
```

#### Si création (nouvelle page)

Utiliser le MCP Notion `notion-create-pages` :

```
parent : { page_id: "35734dfdcd3b8179b160fe16b555081a", type: "page_id" }
pages : [{
  properties: { title: "[nom-du-skill]" },
  content: "[contenu intégral du SKILL.md — corps uniquement, sans frontmatter YAML]",
  icon: "[emoji adapté au skill]"
}]
```

#### Règles de contenu Notion
- Ne jamais inclure le frontmatter YAML (`---name/description---`) dans Notion
- Inclure le corps complet : titre H1, toutes sections, tous exemples, tous tableaux
- Aucune troncature — le contenu Notion doit être identique au SKILL.md source

### Étape 3 — Déclencher la routine Claude Code

Une fois Notion mis à jour avec succès, déclencher la routine via HTTP POST :

```
POST https://api.anthropic.com/v1/claude_code/routines/$ROUTINE_TRIGGER_ID/fire
Authorization: Bearer $CLAUDE_CODE_ROUTINE_TOKEN
Content-Type: application/json

{
  "text": "Skill [nom-du-skill] mis à jour le [date]. Synchroniser claude-global/skills/ avec Notion."
}
```

La routine Claude Code se charge ensuite de :
- Lire la page Notion mise à jour
- Comparer avec le fichier dans `claude-global/skills/samuel/[nom-skill]/SKILL.md`
- Committer et pusher si delta détecté

### Étape 4 — Confirmer à Samuel

```
✅ Notion mis à jour : [nom-skill] → [URL page Notion]
✅ Routine Claude Code déclenchée → sync GitHub en cours
```

Si une étape échoue :

```
❌ [Étape] : [erreur]
→ Action manuelle requise : [instructions]
```

---

## Table de correspondance skills ↔ pages Notion

| Skill | Page ID Notion |
|---|---|
| rodin | 36f34dfdcd3b81cc815ec0bed1dd301d |
| training-adaptatif | 36f34dfdcd3b817ab765e11700f532b8 |
| coach-mental-sport-samuel | 36f34dfdcd3b81e4a8f9e997428718cc |
| planning-expert | 36f34dfdcd3b81cb8f7bd4a6fe424b67 |
| c-level-samuel | 36f34dfdcd3b81e392a3da411da213c7 |
| balanced-samuel | 36f34dfdcd3b811c993fe93f4dba56ad |
| marketing-samuel | 36f34dfdcd3b81afbdd6fca19d3f7ae4 |
| landing-page-samuel | 36f34dfdcd3b81bd8819c5883cc5fcc7 |
| pitch-deck-samuel | 36f34dfdcd3b817baea1d653f8ce5fe9 |
| saas-financial-samuel | 36f34dfdcd3b81bb88f0f84b23baa012 |
| lead-research-samuel | 36f34dfdcd3b817e9c0bc0e9c6990705 |
| rh-sc-renovations | 36f34dfdcd3b814ba1f6f0a1fadba57b |
| rh-cv-apprenti-ia | 36f34dfdcd3b81c4a605fbd62be1b9b3 |
| maitre-horizon | 36f34dfdcd3b819cae55f5e5b381715e |
| aide-reponse-avocat | 36f34dfdcd3b8157b6c4cf806f6120a3 |
| session-notion-samuel | 36f34dfdcd3b813da5dbcb4885e62495 |
| ai-transformation-samuel | 36f34dfdcd3b8105a84ae997e9131c14 |
| social-media-samuel | 36f34dfdcd3b8196bbbbf7a3a4841908 |
| avis-google | 36f34dfdcd3b81d08d41fc67f58cc6cb |

Pour un nouveau skill : créer la page (Étape 2 — création), récupérer l'ID retourné, l'ajouter à cette table.

---

## Routine Claude Code "Sync Skills" — Prompt de référence

```
Tu es chargé de synchroniser les skills Samuel entre Notion et le repo GitHub claude-global.

Pour chaque page dans "Skills Claude — Référentiel Samuel" (Notion page ID: 35734dfdcd3b8179b160fe16b555081a) :
1. Lire le contenu de la page via MCP Notion
2. Comparer avec le fichier claude-global/skills/samuel/<nom-skill>/SKILL.md dans le repo
3. Si le contenu diffère : mettre à jour le fichier, reconstruire le frontmatter YAML depuis la description connue
4. Si le fichier n'existe pas : le créer
5. Committer tous les fichiers modifiés avec le message "sync: update skills from Notion [date]"
6. Pusher sur main

En cas d'erreur sur un skill individuel : continuer les autres, lister les erreurs en fin de rapport.
Produire un rapport de synthèse : nombre de skills traités, mis à jour, créés, erreurs.
```

---

## Règles

- Ce skill s'exécute **toujours** après une création ou MAJ de skill — ne jamais sauter cette étape
- Si le MCP Notion n'est pas disponible dans la session : signaler et fournir le contenu à copier manuellement
- Si le token de la routine n'est pas encore configuré : exécuter Étape 2 seulement, et rappeler de déclencher la routine manuellement
- Ne jamais modifier le SKILL.md source — ce skill est en lecture seule sur les fichiers