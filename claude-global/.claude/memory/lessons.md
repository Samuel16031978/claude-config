# Leçons apprises — mémoire d'agent (à relire AVANT d'agir)

> Boucle méta (Phase 3 du scraper, généralisée). Ce fichier capitalise **mes erreurs d'agent** et les
> **codes de bonne conduite** pour ne pas les reproduire. Distinct du savoir-métier de Samuel (qui vit dans
> la base Notion *Apprentissage*). Format : **erreur observée → règle à appliquer**.
> Capture : via le skill `save-lesson` quand Samuel me corrige. Source synchro : `claude-global/` → `~/.claude/`.

## Méthode & conception

- **Lire les intentions existantes AVANT de concevoir.** J'ai réinventé un système de scoring que Samuel
  possédait déjà (page Notion « Veille GitHub » : seuil install 80, gate `.claude/`, plafond étoiles). →
  Avant de bâtir, explorer ses **skills + pages Notion (surtout Projets)** pour ne pas dupliquer ni contredire.
- **Anticiper la taxonomie depuis QUI il est, pas par accident de test.** Ajouter les domaines/thèmes en
  lisant skills + hub Projets d'avance, plutôt que patcher chaîne par chaîne (réactif → proactif).
- **Découpler les objets quand un score sert plusieurs décisions.** Une note de repo (« installer ? ») et une
  priorité d'idée (« approfondir ? ») sont deux décisions : un seul nombre ne peut pas les porter sans se
  contredire (verdict Rodin). → modéliser un objet par décision.

## Données & robustesse

- **Dériver d'une source fraîche, jamais d'un agrégat mutable.** Une fiche par-chaîne lisait un global
  append-only (`tools-seen.json`) → résidu périmé (« make ×27 » sur une chaîne de natation). → Pour une vue
  scopée, agréger depuis la donnée fraîche (le doc de chaîne), pas le cache global.
- **Désambiguïser les identifiants qui sont des mots courants.** `make`/`notion`/`cursor` comme noms d'outils
  exigent un **contexte** (tokens tech voisins), sinon faux positifs hors de leur domaine.
- **Tolérer les schémas hérités.** Lire les anciennes clés avec des `.get(...)` quand le format évolue.

## Routage & destinations

- **Router selon la NATURE du thème, pas son potentiel.** Un savoir (sport/santé/dev-perso) ne va PAS dans une
  base business (Boîte à Idées). → projet→Boîte à Idées · savoir→Apprentissage. La nature prime sur le score.
- **Idempotence par clé stable** (URL) avant toute écriture Notion : dédup d'abord, créer ensuite.

## Git & process

- **Ne pas réécrire l'historique déjà mergé** pour satisfaire un hook (signatures/committer email) : les
  commits mergés restent ; repartir d'une branche propre depuis `main` pour le travail suivant.
- **Écritures sortantes (Notion, GitHub) : confirmer la politique avant la première écriture** dans une base
  active de Samuel ; ensuite suivre la règle convenue (ex. auto-route 🔥/⚡ en « À évaluer »).

## Veille externe → mes règles (promotion CONTRÔLÉE)

Le scraper YouTube peut m'alimenter : les insights `Type ∈ {meta-erreur, meta-bonne-pratique, process}` **ET**
`Thème ∈ {ia, dev, automatisation}` sont des **candidats-leçons d'agent** (technique, gestion d'erreurs,
conduite). MAIS `lessons.md` gouverne mon comportement → **ne JAMAIS ingérer automatiquement** : un avis
YouTube clickbait ne doit pas devenir ma règle. Filtrer avec **scepticisme** (cf. Rodin) ; ne promouvoir que
ce qui est solide et transposable. Un meta-* **hors-tech** (ex. erreurs fiscales SCI) reste un savoir-métier
(base Notion *Apprentissage*), PAS une règle d'agent.

Leçons adoptées depuis la veille :
- **Profondeur > nouveauté** : ne pas adopter un outil/une techno par hype ; approfondir ce qu'on maîtrise
  avant de switcher (source : @ia_irl, validé). Corollaire : rester sceptique face au battage médiatique.

## Codes de bonne conduite

Voir les règles globales (synchronisées dans `~/.claude/rules/`) : `coding.md` (limites fichier/fonction,
fail-fast, pas de `console.log`), `security.md` (jamais de secret en dur, scanner avant commit), `markdown-docs.md`,
`presentation.md`. Toute correction récurrente de Samuel y est ajoutée.
