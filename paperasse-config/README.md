# Config paperasse

Configuration des skills [paperasse](https://github.com/romainsimon/paperasse) (agents IA
pour la bureaucratie fran├ºaise) et des soci├®t├®s.

> ÔÜá´©Å L'environnement Claude Code distant est **├®ph├®m├¿re** : les skills install├®s dans
> `~/.claude/` ne survivent pas au recyclage du conteneur. Ce dossier versionne donc la
> config et un script de r├®installation pour tout restaurer.

## R├®installer (skills + config)

```bash
bash paperasse-config/install.sh
```

Le script fait un vrai `git clone` (pour **pr├®server les symlinks internes** du repo :
`data/`, `scripts/`, `templates/`, `integrations/` partag├®s entre `comptable`,
`controleur-fiscal` et `commissaire-aux-comptes`), expose les **6 skills** via symlinks
dans `~/.claude/skills/`, puis restaure les 3 `company.json`.

## Skills install├®s

`comptable`, `controleur-fiscal`, `commissaire-aux-comptes`, `notaire`, `syndic`,
`fiscaliste` (ce dernier est absent du `marketplace.json` du repo mais bien pr├®sent ├á
la racine ÔÇö il est donc install├®).

## Soci├®t├®s (`companies/`)

| Fichier | Soci├®t├® | Forme | TVA | IS |
|---|---|---|---|---|
| `sc-renovations-sarl.json` | SC R├®novations | SARL | R├®el simplifi├® ÔÇö 3 taux (20 % / 10 % r├®no / 5,5 % r├®no ├®nerg├®tique) | IS r├®el simplifi├® |
| `holding-sasu.json` | Holding | SASU | Franchise (pure) ÔåÆ animatrice ├á pr├®voir | IS r├®el simplifi├® |
| `sci.json` | SCI | SCI | Franchise (option TVA possible sur locaux pro) | IS r├®el simplifi├® |

**Soci├®t├® active par d├®faut** : SC R├®novations (SARL). Le repo charge `company.json` depuis
le dossier courant d'abord, puis la racine de paperasse. Pour changer de soci├®t├® active :

```bash
ln -sfn companies/holding-sasu/company.json ~/.claude/paperasse/company.json
```

### ├Ç compl├®ter

Les champs `A_COMPLETER` (SIREN/SIRET, adresse, capital, RCS, nom du dirigeant) et
`A_CONFIRMER` (exercice fiscal) restent ├á renseigner dans chaque fichier.

## Secrets

Aucun secret n'est versionn├®. Les cl├®s API (Qonto, Stripe) vont dans `~/.claude/paperasse/.env`
(gitignor├®) ÔÇö voir `.env.example`.

## Remplir automatiquement depuis un SIREN

Sur une machine o├╣ l'API Annuaire des Entreprises est joignable (l'env Claude Code
distant la bloque), une commande suffit par soci├®t├® :

```bash
python3 paperasse-config/fill-from-siren.py sc-renovations-sarl <SIREN>
python3 paperasse-config/fill-from-siren.py holding-sasu       <SIREN>
python3 paperasse-config/fill-from-siren.py sci                <SIREN>
```

Cela renseigne nom, SIREN, SIRET, adresse, ville et code NAF (live + version
commit├®e). Restent ├á saisir ├á la main : capital social, RCS, nom du dirigeant,
exercice fiscal.
