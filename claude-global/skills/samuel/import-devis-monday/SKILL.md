---
name: import-devis-monday
description: "Import d'un devis PDF OBAT vers le board Monday Chantiers (2134855206) : lots = éléments parents, lignes = sous-éléments, modes principal/TS, mapping LOT_MAP par mot-clé. Déclencheurs : import devis, devis OBAT, Monday chantier, travaux supplémentaires TS, parser devis PDF."
---

# Import Devis OBAT → Monday

Transforme un devis PDF OBAT en éléments structurés dans le tableau **Chantiers Samuel** (board `2134855206`) : chaque **lot = élément parent**, chaque **ligne = sous-élément**.

> ⚠️ Ce skill suppose la présence de deux scripts dans `scripts/` : `parse_obat_pdf.py` et
> `build_monday_mutations.py`. S'ils ne sont pas encore versionnés à côté du skill, les ajouter
> avant utilisation.

## Règle fondamentale (source d'erreurs)
Une ligne n'est un **item** que si elle a une **QUANTITÉ**. Les lignes sans quantité sont :
- un **en-tête de lot** (n° à 1 chiffre, ex. `1 Electricité`) → élément **parent** ;
- un **sous-en-tête** (n° à 2 niveaux, ex. `1.2 Electricité exterieure`) → sous-élément structurel ;
- une **précision** (texte seul ou n° répété sans qté, ex. `couleur 7016`, `Porte d'entrée`) → **fusionnée** dans la désignation de la ligne au-dessus, jamais créée séparément.

Le PDF respecte cette logique ; **l'export xlsx OBAT non** → toujours partir du PDF.

## Procédure

### 1. Parser le PDF
```bash
python3 scripts/parse_obat_pdf.py /chemin/devis.pdf /home/claude/devis.json
```
Vérifier la sortie (nb de lots, nb de sous-éléments, désignations fusionnées). Le nom du chantier est auto-extrait ; le proposer à Samuel et le laisser le raccourcir (ex. `Thorel`).

### 2. Déterminer mode + cible
Demander (1 question, options) si ce n'est pas explicite :
- **Mode** : `principal` (nouveau chantier) ou `ts` (travaux supplémentaires) — préciser le n° TS.
- **Groupe Monday** cible. Pour le retrouver : `get_board_info(2134855206)` → liste `groups`. En mode TS, cibler le **groupe du chantier existant**.
- **Libellé Chantier** (colonne texte) — souvent le nom court du client.

### 3. Créer les lots parents (phase 1)
```bash
python3 scripts/build_monday_mutations.py /home/claude/devis.json --mode ts --ts 1 --group GROUP_ID --chantier "Thorel" --phase parents
```
Exécuter la mutation via `monday all_monday_api`. **Conserver les IDs retournés dans l'ordre des alias p0, p1, p2…** (l'ordre est rappelé sur stderr).

### 4. Créer les sous-éléments (phase 2)
```bash
python3 scripts/build_monday_mutations.py /home/claude/devis.json --mode ts --ts 1 --phase subitems --parents ID0,ID1,ID2
```
Exécuter chaque batch (≤20) via `monday all_monday_api`. L'ordre des `--parents` doit être **exactement** celui de la phase 1.

### 5. Vérifier
Annoncer le récap (lots, sous-éléments par lot). La vue chantier (ex. `Thorel_Maison`) affiche le résultat.

## Constantes Monday (board 2134855206)

| Rôle | Colonne | ID |
|------|---------|----|
| Lot (statut) | Lot | `color_mkpme01j` |
| Chantier (texte) | Chantier | `text_mkp8ppet` |
| Devis (statut) | Devis | `color_mm3v8vky` (Base/TS1/TS2/TS3) |
| Quantité sous-élément | Quantité | `numeric_mkpd15zq` |
| Unité sous-élément | Unité | `text_mkpdvgev` |

Si la colonne **Devis** n'existe pas sur le board, la créer une fois : `create_column(board_id:2134855206, title:"Devis", column_type:status, defaults:labels Base/TS1/TS2/TS3)`.

### Mapping lot (mot-clé désignation → libellé statut)
B-PREPARATION · C-DEMOLITION · D-MACONNERIE · E-PLÂTRERIE · F-PLOMBERIE · G-CLIMATISATION · G-ELECTRICITE · H-MENUISERIE · I-REVÊTEMENT MURAL · J-REVÊTEMENT SOL · K-PEINTURE · L-TRAITEMENT DES DÉCHETS. (défini dans `build_monday_mutations.py` → `LOT_MAP`, par mot-clé, indépendant du n° de lot).

## Différences des deux modes

| | principal | ts |
|--|-----------|----|
| Blocs A / X / Y / Z | **ajoutés** (Ouverture, Réunions, Réception, Levée) | **omis** (déjà au principal) |
| Préfixe noms | aucun | `TSn ·` (parent) / `TSn-` (sous-éléments) |
| Colonne Devis | `Base` | `TSn` |
| Numérotation | native OBAT (1→N) | native OBAT du TS, préfixée → pas de collision |

Le code lot (couleur) est **identique** entre principal et TS pour un même métier → la vue "Lots" agrège base + TS par métier ; la colonne Devis isole la facturation des TS.

## Notes
- Limiter les noms à 255 caractères (le parser/générateur tronque déjà).
- Découper les mutations en batches ≤20 sous-éléments (limite de complexité Monday).
- En cas de devis multi-pages, le parser gère les sauts de page et filtre l'en-tête/pied légal.
