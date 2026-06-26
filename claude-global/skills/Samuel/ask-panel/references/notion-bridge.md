# Ask Panel — pont Notion (sans API)

Décrit comment Claude utilise le connecteur Notion comme **support d'échange entre les IA**.
Aucune API n'est appelée : seuls les outils MCP Notion sont utilisés.

## Outils MCP

Noms logiques (le préfixe du serveur MCP peut varier selon l'environnement ; ici
`mcp__9998ab9a-7b0b-4817-878b-367952b8f929__`) :
- `notion-search` — retrouver la page de panel.
- `notion-fetch` — lire la page (récupérer les réponses des autres IA).
- `notion-create-pages` — créer la page de session si absente.
- `notion-update-page` — poster la question, le gabarit, le verdict.

## Page de session

Une page Notion dédiée, ex. **« Panel des 4 — Sessions »**. Cherche-la avec `notion-search` ;
crée-la avec `notion-create-pages` si absente (éviter les doublons). Chaque session = un bloc
en tête de page, précédé d'un séparateur et titré par la date + la cible.

## Gabarit posté à chaque tour

```
─────────────────────────────
## [<date>] Tour <N> — <cible>

**Question :** <question>

**État courant :** <extrait de la cible à évaluer>

### Réponse Claude
(remplie automatiquement par Claude)

### Réponse ChatGPT
(à compléter)

### Réponse Gemini
(à compléter)

### Réponse Notion AI
(à compléter)
```

Chaque section IA demande explicitement : une **note /10**, une **critique** concrète, et le
cas échéant un **drapeau fatal** (cf. `grille-notation.md`).

## Cycle de lecture/écriture

1. `notion-update-page` : poster le gabarit du tour `N`.
2. **Pause handoff** : Samuel déclenche les 3 IA externes sur la page (voir `voix-panel.md`).
3. `notion-fetch` : relire la page, parser les 3 sections externes + ajouter Claude.
4. Si une section est vide : signaler, proposer de continuer à 3/4 ou relancer la pause.

## Sortie finale

- **Idée business** : `notion-update-page` pour écrire en tête de session le **verdict**
  (LANCER/ABANDONNER), le **score global** et la **trajectoire** des notes. C'est le livrable.
- **SKILL.md** : la page Notion garde la trace de la confrontation ; le livrable est le
  commit git (voir `SKILL.md` étape 4).

## Règles

- Toujours chercher la page avant d'en créer une (éviter les doublons).
- Ne jamais écrire de secret/token sur la page.
- En cas d'erreur MCP : signaler clairement, ne pas committer un résultat partiel comme s'il
  était validé.
