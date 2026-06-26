# Ask Panel — protocole de confrontation (condensé)

Version condensée du **`⚖️ protocole-panel`** de Samuel
(`https://app.notion.com/p/37d34dfdcd3b8175b952d837fd01271b`), source autoritaire. En cas de
divergence, la page Notion prime — la relire au démarrage via `notion-fetch`.

## Leçon fondatrice (échec keto, juin 2026)

Le panel avait conclu à tort, à cause de 4 biais. Les règles ci-dessous les neutralisent :
1. **Biais d'ancrage** — la question présentait un élément comme « contrainte ».
2. **Récupération paresseuse** — source surreprésentée citée sans test de transposabilité.
3. **Faux consensus** — 3 IA au corpus commun convergent vers la même erreur (3 voix ≠ 3
   validations indépendantes).
4. **Absence de quantification** — conclusions qualitatives jusqu'à ce qu'on exige des chiffres.

## Les 6 règles de formulation (OBLIGATOIRES)

1. **Neutraliser le cadrage** — ne jamais présenter un élément comme un problème.
   ❌ « X est-il un frein pour Y ? » ✅ « Quel est l'impact réel, positif comme négatif, de X
   sur Y ? Quantifie dans les deux sens. »
2. **Exiger la quantification** — « Réponds avec des chiffres et références précises. Si pas de
   donnée chiffrée, dis-le explicitement. »
3. **Forcer la transposabilité** — pour chaque étude : population, durée, contexte, et si elle
   est transposable au cas précis.
4. **Désigner un contradicteur dès le départ** — une IA attaque la conclusion majoritaire avec
   des données opposées (ici : DeepSeek).
5. **Demander le niveau de confiance** — faible/moyen/élevé + ce qui ferait changer d'avis.
6. **Une variable = une question** — ne pas mélanger plusieurs variables dans une question.

## Structure d'une question panel

```
QUESTION PANEL #[n] — [titre neutre]
CONTEXTE [factuel, sans jugement]
HYPOTHÈSE À TESTER [neutre, ouverte aux deux sens]
QUESTIONS PRÉCISES [numérotées, une variable dominante par question]
CONSIGNES TRANSVERSALES [chiffres ; transposabilité ; contradicteur ; confiance ; position tranchée]
FORMAT ATTENDU [structure de réponse souhaitée]
```

## Workflow de confrontation (à réception des voix)

1. **Extraire les consensus** (3/4 ou 4/4) — les lister explicitement.
2. **Isoler les divergences** — tableau comparatif par IA.
3. **Arbitrer** chaque divergence — position Claude motivée par les **données les plus solides**,
   pas par la majorité.
4. **Détecter le faux consensus** — si les IA citent la même source unique, signaler que la
   robustesse est illusoire et vérifier la source.
5. **Identifier les conclusions fragiles** — faible confiance ou mal sourcées.
6. **Produire le verdict consolidé** — tranché, avec conditions et hiérarchie si pertinent.

## Signaux d'alarme — méta-vérification (avant de figer un verdict)

- La question initiale était-elle cadrée neutre, ou orientait-elle la réponse ?
- Sources indépendantes, ou une source commune surreprésentée ?
- Conclusions chiffrées, ou seulement qualitatives ?
- Une étude clé appliquée hors de son domaine de validité ?

Si un signal est **rouge** → proposer un tour de contre-expertise avant de figer la conclusion.
