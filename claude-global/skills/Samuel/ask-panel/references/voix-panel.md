# Ask Panel — les 4 voix et le protocole de déclenchement

Détaille chaque voix du panel, sa source, et comment Claude obtient sa réponse **sans API**.

## Les 4 voix

### 1. Claude (automatique)
Formule sa propre réponse à partir de l'état courant de la cible. Pour une idée business,
applique la lentille premiers principes de `claude-global/skills/Samuel/first-principles-business/SKILL.md`
(les 5 lois Musk). Aucune action externe.

### 2. ChatGPT (connecteur Notion — vérifié)
ChatGPT lit/écrit la page via sa fonction **Connectors / Notion MCP** (offres payantes
Plus/Pro/Team). Samuel déclenche ChatGPT depuis son app ; la réponse s'écrit dans la section
prévue de la page.

### 3. Notion AI (natif — porte d'entrée multi-modèles)
Notion AI répond directement dans la page via la commande IA de Notion. C'est la voix la plus
intégrée. Son **sélecteur de modèles** (GPT, Claude, DeepSeek selon le plan/région) permet
d'apporter une diversité de moteurs **dans l'abonnement Notion**, sans API. Remplace le
DeepSeek de l'ancien panel.

### 4. Gemini (copier-coller manuel — pas de connecteur)
**Fait vérifié (2026) : Gemini n'a aucun connecteur Notion grand public** (les options
existantes sont Gemini Enterprise en OAuth ou des automatisations Zapier/Make — toutes à base
d'API, donc exclues). Sa voix passe donc par **copier-coller manuel** : Samuel copie la
question dans Gemini, puis colle la réponse de Gemini dans la section Gemini de la page.
Toujours zéro API.

## Pourquoi semi-automatique

Claude ne peut pas *déclencher* les autres IA : chacune vit dans sa propre app/abonnement. Le
pont est donc **asynchrone** — Claude pose la question sur Notion, Samuel lance ChatGPT et
Notion AI (qui écrivent sur la page) et relaie Gemini à la main, puis Claude relit. C'est le
prix de « zéro API ».

## Protocole par tour

1. Claude poste la question + l'état courant + un gabarit (cf. `notion-bridge.md`).
2. Claude affiche la **pause handoff** et attend la confirmation de Samuel :
   ```
   🤝 Question postée sur Notion (page : <titre>).
   1) Déclenche ChatGPT et Notion AI sur cette page (ils y écrivent directement).
   2) Colle la question dans Gemini, puis colle sa réponse dans la section Gemini.
   Réponds « prêt » quand les 3 sections externes sont remplies.
   ```
3. À « prêt », Claude relit la page, extrait les 3 réponses externes, ajoute la sienne.
4. Si une voix manque, Claude le signale et propose : continuer à 3/4, ou relancer la pause.

## Confrontation et arbitrage

Consensus = un point soutenu par **≥ 3 voix sur 4**. En cas de **divergence** (aucune
majorité claire), pose la question à Samuel et attends :

```
⚠️ Divergence sur : <sujet>
- Claude    : <…>
- ChatGPT   : <…>
- Gemini    : <…>
- Notion AI : <…>
Quelle version retiens-tu ? [1/2/3/4 ou formule librement]
```

## Repli sous-agents (optionnel)

Si Samuel veut une exécution **100 % automatique sans étape manuelle** (au prix de la
diversité de modèles), les 4 voix peuvent être simulées par 4 sous-agents Claude via l'outil
`Agent` (un message, en parallèle), chacun recevant un rôle distinct. Ce mode contourne le
pont Notion ; à n'utiliser que sur demande explicite.
