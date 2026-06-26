# Ask Panel — les 4 voix et le protocole de déclenchement

Détaille chaque voix du panel, sa source, et comment Claude obtient sa réponse **sans API**.

## Les 4 voix

### 1. Claude (automatique)
Formule sa propre réponse à partir de l'état courant de la cible. Pour une idée business,
applique la lentille premiers principes de `claude-global/skills/Samuel/first-principles-business/SKILL.md`
(les 5 lois Musk). Aucune action externe.

### 2. ChatGPT (via son connecteur Notion)
ChatGPT lit la page Notion grâce à son connecteur natif et écrit sa réponse dans la section
prévue. Déclenché par Samuel depuis l'app ChatGPT.

### 3. Gemini (via app / connecteur)
Même principe : Samuel ouvre Gemini, lui fait lire la page (lien partagé ou connecteur) et
colle/écrit la réponse dans la section Gemini.

### 4. Notion AI (IA native Notion)
Notion AI répond directement dans la page via la commande IA de Notion. C'est la voix la
plus intégrée au pont. Peut remplacer DeepSeek de l'ancien panel.

## Pourquoi semi-automatique

Claude ne peut pas *déclencher* ChatGPT, Gemini ou Notion AI : chacune vit dans sa propre
app/abonnement. Le pont est donc **asynchrone** — Claude pose la question sur Notion, Samuel
lance les trois autres, puis Claude relit. C'est le prix de « zéro API ».

## Protocole par tour

1. Claude poste la question + l'état courant + un gabarit (cf. `notion-bridge.md`).
2. Claude affiche la **pause handoff** et attend la confirmation de Samuel :
   ```
   🤝 Question postée sur Notion (page : <titre>).
   Déclenche ChatGPT, Gemini et Notion AI sur cette page, puis réponds « prêt ».
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
