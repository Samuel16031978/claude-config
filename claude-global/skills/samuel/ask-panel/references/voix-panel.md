# Ask Panel — les 4 voix et le protocole de déclenchement

Le panel des 4 = **Claude orchestrateur + 3 contributeurs** (ChatGPT, Gemini, DeepSeek),
conforme au `protocole-panel`. Les contributeurs arrivent par le pont Notion, **sans API**.

## Les 4 voix

### 1. Claude — orchestrateur (automatique)
Formule les questions (6 règles), confronte les voix, arbitre les divergences, détecte le
faux consensus, produit le verdict et note. Donne aussi sa propre réponse. Pour une idée
business, applique la lentille premiers principes de
`../../first-principles-business/SKILL.md`.

### 2. ChatGPT — contributeur (connecteur Notion, vérifié)
Lit/écrit la page via **Connectors / Notion MCP** (offres payantes). Samuel le déclenche
depuis son app ; la réponse s'écrit dans la section ChatGPT du Run.

### 3. Gemini — contributeur (copier-coller manuel)
**Fait vérifié (2026) : Gemini n'a aucun connecteur Notion grand public** (options
Enterprise/Zapier = API, exclues). Samuel copie la question dans Gemini, puis colle la réponse
dans la section Gemini. Zéro API.

### 4. DeepSeek — contradicteur désigné (via Notion AI)
Joue le **contradicteur** (règle 4) : attaque la conclusion majoritaire avec des données
opposées. DeepSeek n'a pas de connecteur Notion autonome, mais est disponible **dans le
sélecteur de modèles de Notion AI** — Samuel l'invoque dans la page, ou colle sa réponse à la
main. Zéro API.

## Pourquoi semi-automatique

Claude ne peut pas *déclencher* les autres IA : chacune vit dans son app/abonnement. Le pont
est **asynchrone** — Claude poste le Run, Samuel déclenche ChatGPT (connecteur) et DeepSeek
(via Notion AI) et relaie Gemini à la main, puis Claude relit. C'est le prix de « zéro API ».

## Confrontation et arbitrage

Consensus = point soutenu par **≥ 3/4** (cf. `protocole-confrontation.md`). En cas de
divergence non tranchable par les données, poser la question à Samuel :

```
⚠️ Divergence sur : <sujet>
- Claude    : <…>
- ChatGPT   : <…>
- Gemini    : <…>
- DeepSeek  : <…>
Quelle version retiens-tu ? [1/2/3/4 ou formule librement]
```

## Repli sous-agents (optionnel, sur demande explicite)

Pour une exécution 100 % automatique sans étape manuelle (au prix de la diversité de modèles),
les 4 voix peuvent être simulées par 4 sous-agents Claude via l'outil `Agent`, chacun avec un
rôle distinct (dont un contradicteur). Ce mode contourne le pont Notion.
