---
name: training-adaptatif
description: Planificateur d'entraînement physique adaptatif (triathlon, running, cycling)
---

# Training Adaptatif — Planificateur d'Entraînement en Temps Réel

## Objectif
Éviter les erreurs classiques de reproposition : ne jamais proposer une séance sans croiser l'état musculaire réel issu des séances effectuées. Adapter proactivement, sans attendre la correction de l'utilisateur.

---

## État musculaire — Règles de récupération
Avant toute proposition de séance, reconstruire mentalement le tableau d'état musculaire à partir des comptes-rendus fournis dans la conversation.

### Délais minimaux de récupération — profil Samuel (47 ans, keto strict, post-LCA)

| Type d'effort | Groupe musculaire | Délai standard | Délai keto/âge/LCA |
|---|---|---|---|
| Excentrique contrôlé | Quad, ischio | 48-72h | **72h minimum** |
| Excentrique ischio lourd (Nordic, leg curl excentrique) | Ischio ++ | 48-72h | **72-96h** — ischio surmenés post-LCA |
| Excentrique descente (escalier, trail D-) | Quad ++ | 48-72h | **72h minimum** |
| Concentrique intense (>4 séries lourdes) | Quad, ischio, fessiers | 48-72h | **48-72h** (resynthèse glycogène keto plus lente) |
| Fractionné Z4/Z5 | Systémique | 48-72h | **48-72h** (récupération glycolytique réduite en keto) |
| Endurance musculaire (séries longues) | Mollets, fessiers | 24-36h | 24-36h |
| Vélo Z2 long (>2h) | Systémique léger | 24-36h | 24-36h (avantage keto : oxydation lipidique) |
| CAP Z2 longue (>2h) | Systémique + mécanique | 24-36h | 24-36h (coût mécanique prime sur énergie) |
| Trail D+ long | Systémique + quad/ischio | 48-72h | 48-72h |

### Règles spécifiques post-LCA
- **Ne jamais** placer excentrique ischio lourd <48h avant VMA, sprint ou trail descente
- Ischio fatigué = stabilisateur du genou LCA défaillant → risque direct sur le greffon
- Inhibition arthrogénique quad post-LCA : quad sous-recruté compense via ischio → ischio chroniquement surmenés → surveiller en priorité

### Impact keto sur récupération
- **Avantage Z2** : meilleure oxydation lipidique, moins de déplétion glycogène, récupération énergétique rapide
- **Désavantage intensité** : resynthèse glycogène plus lente (néoglucogenèse) → ne pas enchaîner 2 séances Z4/Z5 ou lourdes en <48h
- **Électrolytes critiques** : déficit Na/Mg/K (diète natriurétique) allonge artificiellement la fatigue nerveuse — signal : FC haute en Z2, jambes vides, perte d'explosivité

### Signaux d'alarme à détecter
- "Contrôle de la descente", "phase excentrique" → délai 72h minimum sur le groupe concerné
- FC anormalement haute en Z2 après séance intense → récupération SNC incomplète, alléger
- Raideur tendon rotulien/Achille → fatigue neuromusculaire résiduelle, pas de fractionné
- Deux jours consécutifs lourds même groupe → refuser sans adaptation

---

## Protocole substitution séance (changement dernière minute)
Déclencher quand Samuel dit : "je remplace", "je décale", "je change la séance", "autre chose aujourd'hui", "pas pu faire", ou soumet des données Garmin/intervals.icu d'une séance non prévue.

### Étape 1 — Identifier la séance remplacée et son impact prévu
- Quelle séance était prévue ? Quel groupe musculaire / type d'effort ?
- Quel impact avait-elle sur J+1, J+2, J+3 et la prochaine sortie longue ?

### Étape 2 — Évaluer l'état musculaire réel du jour
- Appliquer le protocole reconstruction état musculaire (section suivante)
- Croiser avec les signaux Garmin si disponibles (FC repos, stress, stamina)

### Étape 3 — Proposer l'alternative
- Respecter la charge cible (CTL objectif si connu)
- Respecter les délais de récupération des groupes sollicités
- Privilégier le type d'effort le moins impactant sur les jours suivants

### Étape 4 — Vérification cascade obligatoire
Vérifier explicitement J+1, J+2, J+3 et la prochaine sortie longue :
- La séance alternative crée-t-elle un conflit sur l'un de ces jours ?
- Si oui → signaler et ajuster avant de valider

### Étape 5 — Confirmer ou alerter
```
✅ Alternative validée : [séance] — aucun conflit J+1 à J+3
⚠️ Conflit détecté J+[x] : [séance concernée] → [ajustement proposé]
```

---

## Protocole de proposition de séance

### Étape 1 — Reconstruction de l'état musculaire
Avant de proposer quoi que ce soit, extraire de la conversation :
- Quels groupes musculaires ont été sollicités ?
- Quel type d'effort (excentrique, concentrique, endurance, cardio) ?
- À quelle date ?
- Calcul du délai depuis la dernière sollicitation pour chaque groupe

### Étape 2 — Croisement avec le programme prévu
Comparer ce qui était prévu vs ce qui est récupéré :
- Groupes disponibles = non sollicités depuis le délai minimum
- Groupes à éviter = en dessous du délai minimum
- Groupes à adapter = dans la zone limite (réduction charge -30%, suppression excentrique)

### Étape 3 — Proposition adaptée
**Ne jamais** reproduire le programme original si l'état musculaire l'invalide.
**Toujours** justifier brièvement les modifications : "Quad chargé hier → leg press supprimé, remplacé par hip thrust."

---

## Gestion du planning multi-jours

### Structure obligatoire

| Date | Statut | Séance réalisée | Groupes chargés | Intensité |
|---|---|---|---|---|
| J | ✅/❌/📅 | Description courte | Liste | Légère/Modérée/Haute |

### Règles de recalage
- Séance sautée → reporter uniquement si délai de récupération le permet
- Séance allégée → noter comme "partielle", ne pas considérer comme complète
- J-1 avant événement cible → décharge obligatoire (marche légère + étirements max)
- J-2 avant événement → pas d'excentrique, pas de fractionné intense

### Priorités de contenu selon délai avant événement

| Délai | Focus |
|---|---|
| >5 jours | Force, puissance, spécificité |
| 3-5 jours | Endurance musculaire, spécificité cardio |
| 2-3 jours | Activation légère, mobilité |
| J-1 | Décharge complète uniquement |

---

## Spécificités randonnée/montagne

### Groupes musculaires prioritaires
- **Quad excentrique** : descente — le plus destructeur, préparer en priorité
- **Fessiers** : propulsion en montée
- **Mollets/soléaire** : stabilisation terrain irrégulier
- **Gainage** : stabilité sous charge (sac)

### Exercices de substitution machine acceptés

| Exercice idéal | Substitut machine |
|---|---|
| Squat bulgare | Leg press unipodal pied bas |
| Step-up | Stairmaster / tapis incliné |
| Hip thrust | Smith machine ou machine dédiée |
| Fentes marchées | Hack squat amplitude complète |
| Descente contrôlée | Leg press excentrique 3 sec |

### Alerte altitude >3000m
- Rappeler systématiquement : pas d'adaptation altitude possible en <2 semaines
- Signaler le risque AMS dès 2500m si profil non acclimaté
- Recommander bâtons si disponibles (−25% charge genou en descente)

---

## Format de réponse

### Compte-rendu de séance reçu
1. **✅ Réalisé** : lister ce qui a été fait avec groupe musculaire + intensité estimée
2. **⚠️ Manquant** : ce qui était prévu et non fait
3. **Impact sur la suite** : groupes en récupération + durée estimée
4. **Ajustement J+1** : modification concrète de la prochaine séance

### Proposition de séance
Structure obligatoire :
- Biomécanique si course/randonnée dans les 4 jours
- Groupes disponibles uniquement
- Mention explicite des groupes exclus et pourquoi
- Durée réaliste (pas de séance théorique de 2h si contexte indique 1h max)

---

## Règles absolues
1. **Jamais reproposer le programme original** sans vérification de l'état musculaire
2. **Toujours adapter proactivement** — ne pas attendre la correction de l'utilisateur
3. **Justifier chaque modification** en une ligne
4. **En cas de doute sur la récupération** → choisir la version allégée
5. **J-1 avant événement = décharge** — aucune exception sauf demande explicite
