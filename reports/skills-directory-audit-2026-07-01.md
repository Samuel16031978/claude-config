[← Retour au README](../README.md)

# Audit du dossier de skills — 1ᵉʳ juillet 2026

Audit de parité entre les skills perso **canoniques** du repo (`claude-global/skills/samuel/`)
et leur **installation consommée par Claude Code** (`~/.claude/skills/`), déclenché sur la branche
`claude/skills-directory-audit-hl3iky`.

## Paramètres

| Paramètre | Valeur |
|-----------|--------|
| Date | 2026-07-01 |
| Source de vérité | `claude-global/skills/samuel/` (29 skills) |
| Cible d'install | `~/.claude/skills/` |
| Manifeste | `claude-global/skills/samuel/.sync-manifest.json` |
| Routine | `claude-global/sync_skills.py` (`status` / `bundle` / `commit-manifest` / `install`) |

## Résumé

| Métrique | Valeur |
|----------|--------|
| Skills canoniques (repo) | 29 |
| Skills enregistrés au manifeste | 28 |
| Skills installés à plat (avant remédiation) | **0 / 29** |
| Reliquat périmé détecté | `~/.claude/skills/Samuel/` (4 skills, 26 juin) |
| Collisions de nom avec la marketplace | 0 |

## Constats

### 1. 🔴 Aucun skill perso n'était découvrable par Claude Code

Claude Code ne charge un skill que depuis un dossier **de premier niveau** :
`~/.claude/skills/<nom>/SKILL.md`. Or **0 des 29** skills canoniques y étaient installés à plat.
En pratique, aucun skill perso (`rodin`, `intervals-icu-samuel`, `youtube-scraper`, etc.) n'était
utilisable dans cet environnement.

### 2. 🟠 Reliquat périmé `Samuel/` (majuscule, pré-refactor)

`~/.claude/skills/Samuel/` (majuscule) traînait une copie datée du **26 juin**, antérieure au
refactor FR de juin 2026. Elle contenait 4 skills aux **anciens noms** :

| Ancien nom (reliquat) | Nom canonique actuel |
|-----------------------|----------------------|
| `marketing-samuel` | `marketing` |
| `training-adaptatif` | `training-ironman-2026` |
| `first-principles-business` | `first-principles-business` (inchangé) |
| `skill-sync-notion` | `skill-sync-notion` (inchangé) |

Deux problèmes cumulés : **casse** (`Samuel/` au lieu de `samuel/`, la casse que le refactor a
abandonnée) et **imbrication** (skills à 2 niveaux → invisibles pour Claude Code). C'est le
« doublon `Samuel/` majuscule » que les leçons disaient fusionné *dans le repo* — mais la cible
d'install en gardait une vieille trace.

### 3. 🟡 Dérive de manifeste : `youtube-scraper` non enregistré

`youtube-scraper` existe dans le repo avec son `SKILL.md` (outil veille phare, documenté dans
`CLAUDE.md`) mais **manque** dans `.sync-manifest.json` (28 entrées au lieu de 29). Conséquence :
`sync_skills.py status` le signale en permanence comme `MODIFIE` / « à ré-importer dans claude.ai ».

Deux causes possibles, à **arbitrer par Samuel** (le manifeste ne « voit » pas claude.ai) :
- soit `youtube-scraper` n'a jamais été importé dans claude.ai → le signal est **correct**, action =
  importer le bundle puis `commit-manifest` ;
- soit il l'est déjà et le manifeste n'a pas été re-figé → action = `commit-manifest` seul.

> Non corrigé automatiquement : re-figer le manifeste affirmerait « déjà synchro avec claude.ai »,
> ce que l'audit ne peut pas vérifier. Décision laissée à Samuel.

### 4. 🟢 Aucune collision de nom

Aucun des 29 noms perso n'entre en collision avec les 876 entrées de la marketplace de sécurité déjà
présentes à la racine → un `install` propre ne risque pas d'être silencieusement ignoré
(`_install_one` saute une cible qui est déjà un « dossier réel »).

## Remédiation

### Environnement (appliqué — éphémère)

Le conteneur distant est reconstruit à chaque session, donc ces deux actions sont à rejouer :

```bash
rm -rf ~/.claude/skills/Samuel            # purge le reliquat pré-refactor
cd claude-global && python3 sync_skills.py install   # symlink des 29 skills à plat
```

Après remédiation : **29 / 29** installés à plat, `Samuel/` (majuscule) supprimé.

### Repo (à décider)

- **Constat #3** : `python3 sync_skills.py commit-manifest` une fois `youtube-scraper` confirmé côté
  claude.ai, pour enregistrer les 29 skills et éteindre le faux signal `MODIFIE`.

## Pérennité

Le point #1 se reproduira à chaque nouveau conteneur tant que `install` n'est pas rejoué. Piste
d'amélioration (hors périmètre de cet audit) : intégrer `sync_skills.py install` au script de
démarrage de l'environnement distant pour garantir la parité dès l'ouverture de session.
