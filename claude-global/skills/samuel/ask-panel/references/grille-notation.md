# Ask Panel — grille de notation

Grille **adaptative** selon la cible. Chaque voix note la cible courante puis le score global
décide de la suite de la boucle. La **formulation** des questions et la **confrontation** des
réponses suivent `protocole-confrontation.md` (6 règles anti-biais + workflow + méta-vérif) —
la notation ci-dessous s'applique APRÈS confrontation, pour piloter la boucle vers la cible.

## Schéma JSON attendu par voix

Chaque voix produit (ou Claude transcrit depuis sa réponse Notion) :
```json
{
  "voix": "claude|chatgpt|gemini|notion-ai",
  "notes": { "<dimension>": 0-10, ... },
  "note_globale": 0-10,
  "critique": "points faibles concrets + amélioration proposée",
  "drapeau_fatal": false
}
```

## Dimensions

### Cible = SKILL.md
| Dimension | 0-3 | 4-6 | 7-8 | 9-10 |
|-----------|-----|-----|-----|------|
| Clarté | confus | lisible avec effort | clair | limpide, sans jargon inutile |
| Complétude | lacunes majeures | couvre l'essentiel | complet | exhaustif et cadré |
| Exactitude | erreurs | approximations | correct | rigoureux, vérifiable |
| Exécutabilité | inopérant | partiel | fonctionne | reproductible tel quel |

### Cible = idée business
| Dimension | 0-3 | 4-6 | 7-8 | 9-10 |
|-----------|-----|-----|-----|------|
| Désirabilité | personne n'en veut | intérêt incertain | demande réelle | besoin fort et prouvé |
| Faisabilité | hors de portée | tendu | atteignable | faisable avec les ressources de Samuel |
| Viabilité | pas de modèle | marge fragile | rentable | économie solide et scalable |
| Risque/différenciation | faille fatale | risques lourds | défendable | avantage durable et clair |

> Lentille premiers principes pour la faisabilité : `../../first-principles-business/SKILL.md`.

## Agrégation et décision

- **Score global du tour** = moyenne des `note_globale` des 4 voix (3 si une voix manque).
- **Gate de faille fatale** (idée business uniquement) : si une voix lève `drapeau_fatal=true`
  **ou** si la dimension Risque ≤ 2, examiner l'**ABANDON** en priorité (ne pas continuer à
  itérer sur une idée morte).
- **Cible atteinte** : score global ≥ cible (défaut **9/10**, configurable jusqu'à **10/10**).
- **Plateau** : gain de score global < **0.5** entre deux tours consécutifs → arrêter et
  restituer le meilleur tour.
- **Itérer** : sinon, synthétiser les critiques en consensus (≥ 3/4) et produire la version
  améliorée pour le tour suivant.

## Trajectoire

Journaliser la trajectoire des scores (ex. `6 → 8 → 9`) pour le résumé final et, en cas
d'idée business, pour la page Notion. La trajectoire rend visible la convergence (ou son
absence, qui justifie l'abandon).
