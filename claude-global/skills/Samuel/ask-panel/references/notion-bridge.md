# Ask Panel — pont Notion (sans API)

Le connecteur Notion sert de **support d'échange entre les IA**. Aucune API : seuls les outils
MCP Notion sont utilisés. Le stockage suit la base existante de Samuel.

## Outils MCP

Préfixe serveur variable selon l'environnement (ici `mcp__9998ab9a-7b0b-4817-878b-367952b8f929__`) :
- `notion-search` — retrouver la base / un Run.
- `notion-fetch` — lire un Run (récupérer les réponses des IA) ou le schéma d'une data source.
- `notion-create-pages` — créer un Run sous la base.
- `notion-update-page` — poster le prompt, insérer les réponses, écrire le verdict, MAJ statut.

## Base de stockage : « 🗂️ Runs — Panels »

- Page base : `https://app.notion.com/p/0b7d4fa9b15446feb9318267ed6135dc`
- Data source (parent des Runs) : `collection://48030c02-acce-48aa-adf3-208226e3d1ff`
- Template de référence : `🧩 Template — Run panels`
  (`https://app.notion.com/p/b3de52be4fa145629fc7355eaa3fc6e4`).

### Schéma (propriétés du Run)
| Propriété | Type | Valeur |
|-----------|------|--------|
| `Sujet` | title | titre neutre du Run |
| `Domaine` | select | `Fiscal` / `Business` / `Perso` / `Autre` |
| `Statut` | status | `Draft` → `Envoyé` → `Réponses reçues` → `Consensus` → `Décidé` |
| `date:Date:start` | date | date du Run (ISO `YYYY-MM-DD`) |
| `Prompt master` | text | résumé du prompt envoyé aux panels |
| `Décision (résumé)` | text | rempli au verdict |

Créer le Run avec `notion-create-pages`, `parent = { data_source_id }`.

## Contenu d'une page Run

```
> Run généré par ask-panel — conforme au protocole-panel. Orchestrateur : Claude.

## SNAPSHOT (faits + chiffres)
## Question / décision à prendre
## Contraintes (non négociables)
## Prompt master (à envoyer tel quel)
   (bloc de code = le prompt formulé selon les 6 règles)
## Réponses du panel (brut)
   ### 🟣 Claude — orchestrateur   (rempli auto)
   ### 🟢 ChatGPT                  (connecteur — déclenché par Samuel)
   ### 🔵 Gemini                   (copier-coller manuel — pas de connecteur)
   ### 🟠 DeepSeek — contradicteur (via Notion AI ou copier-coller)
## Consensus (matrice : Point | Pour | Contre | Décision)
## Verdict consolidé   (note globale /10, trajectoire, recommandation tranchée)
```

## Cycle de lecture/écriture par tour

1. `notion-create-pages` (tour 1) ou `notion-update-page` (tours suivants) : poster le Run +
   le prompt + les sections de voix. `Statut = Envoyé`.
2. **Pause handoff** : Samuel déclenche ChatGPT (connecteur) + DeepSeek (via Notion AI) sur la
   page, et relaie Gemini à la main. Voir `voix-panel.md`.
3. `notion-fetch` : relire le Run, parser les 3 sections externes + ajouter Claude.
   `Statut = Réponses reçues`. Si une section est vide : signaler, proposer 3/4 ou relancer.
4. Confronter, noter, écrire la matrice de consensus. `Statut = Consensus`.

## Sortie finale

- **idée business** : écrire le **Verdict consolidé** dans le Run + renseigner
  `Décision (résumé)`. `Statut = Décidé`. C'est le livrable.
- **SKILL.md** : le Run garde la trace ; le livrable est le commit git (cf. `SKILL.md` étape 4).

## Règles

- Toujours chercher la base/le Run avant d'en créer (éviter les doublons).
- Ne jamais écrire de secret/token sur la page.
- En cas d'erreur MCP : signaler ; ne pas figer un résultat partiel comme s'il était validé.
