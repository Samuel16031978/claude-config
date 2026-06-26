---
name: aide-reponse-avocat
description: "Génération de courriers pour répondre à un avocat (dossier de litige). Adapte le registre juridique, structure la réponse point par point. Déclencheurs : réponse avocat, courrier juridique, litige, répondre à un courrier d'avocat."
---

# Aide Réponse Avocat

## Description

Génère des courriers afin de répondre à l'avocat adverse dans un dossier de litige. Produit un projet de courrier que Samuel transmet ensuite à son propre avocat.

## Contexte

Dossier de litige avec points litigieux non résolus dans les échanges précédents. L'avocat adverse peut avoir fait appel à un expert. Samuel souhaite formuler des réponses pour son avocat lorsque les points évoqués précédemment n'ont pas été pris en considération.

## Utilisation

1. Fournir les courriers d'échange (les précédents + le dernier reçu)
2. Préciser la réponse souhaitée / les points à défendre
3. Le skill produit un projet de courrier adapté au registre juridique

## Règles

- Registre juridique, factuel, sans agressivité — la forme sert le fond
- Reprendre **chaque point litigieux** explicitement (numéroter) pour qu'aucun ne soit éludé
- Distinguer les faits établis des appréciations
- Toujours rappeler que le courrier doit être **validé et porté par l'avocat de Samuel** avant tout envoi
- Ne jamais affirmer une position de droit comme certaine : proposer, l'avocat tranche
