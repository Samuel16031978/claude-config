---
name: checkpoint
description: "Produire un fichier `checkpoint-YYYY-MM-DD-HHMM.md` qui capture tout ce qu'une nouvelle session devra savoir pour reprendre exactement là où on s'est arrêté. Le fichier est conçu pour être collé ou chargé en tout premier message d'une session vierge"
---

## Objectif

Produire un fichier `checkpoint-YYYY-MM-DD-HHMM.md` qui capture tout ce qu'une nouvelle session devra savoir pour reprendre exactement là où on s'est arrêté. Le fichier est conçu pour être collé ou chargé en tout premier message d'une session vierge.

## Ce que le fichier doit contenir

### 1. En-tête (5 lignes max)

```
# Checkpoint — <date heure>
Projet : <nom ou chemin du projet>
Modèle actif : <modèle Claude utilisé>
Contexte au moment du checkpoint : <% si visible>
```

### 2. État du travail

**Ce qui est fait** — liste des tâches terminées depuis le début de la session, avec résultat concret (fichier créé, bug corrigé, feature livrée…).

**Ce qui reste** — liste des tâches en cours ou à venir, dans l'ordre de priorité. Si une tâche est à moitié faite, préciser exactement où elle s'est arrêtée.

### 3. Décisions prises

Les choix techniques, architecturaux ou métier qui ont été actés pendant la session. Inclure le *pourquoi* quand il est connu, car c'est ce qui permet de ne pas refaire le débat dans la session suivante.

### 4. Blocages et points d'attention

Tout ce qui était bloqué, contourné, ou qui mérite une vigilance particulière. Les erreurs rencontrées et leur statut (résolu / contourné / non résolu).

### 5. Fichiers clés

Liste des fichiers créés, modifiés ou à surveiller. Format : chemin + une ligne de contexte sur leur rôle dans l'état actuel.

### 6. Prochaine action immédiate

Une seule phrase : la toute première chose à faire au démarrage de la nouvelle session. Cette phrase devient le premier message de la session vierge, suivi du contenu complet du checkpoint.

## Format de sortie

Écrire le fichier dans le répertoire de travail courant (ou `~/.claude/checkpoints/` si pas de projet actif).

Nommer le fichier `checkpoint-YYYY-MM-DD-HHMM.md` avec la date et l'heure locales.

Après écriture, afficher :

1. Le chemin complet du fichier
2. Un résumé en 3 bullet points de ce qui a été capturé
3. La commande exacte pour recharger : `Charge ce fichier en premier message : <chemin>`

## Règles

- Être factuel et dense — ce n'est pas un rapport, c'est un briefing opérationnel
- Pas de formules de politesse, pas de résumé narratif — aller droit au but
- Si l'utilisateur a mentionné des contraintes spécifiques (deadline, interlocuteur, convention de code), les inclure dans "Points d'attention"
- Le fichier doit être autonome : quelqu'un qui ne connaît pas la session doit pouvoir reprendre sans poser de questions