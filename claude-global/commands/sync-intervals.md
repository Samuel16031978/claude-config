# /sync-intervals

Synchronise les donn├®es intervals.icu vers GitHub pour que Claude.ai puisse les lire.

## Ce que tu fais

```bash
cd claude-global
python3 intervals_icu.py wellness > data/intervals_latest.json
python3 intervals_icu.py history --days 7 >> data/intervals_history.json
git add data/intervals_latest.json data/intervals_history.json
git commit -m "sync: intervals.icu data $(date +%Y-%m-%d)"
git push origin main
```

## Apr├¿s le push

Dis ├á Samuel : "Ô£à Sync intervals.icu termin├® ÔÇö Claude.ai peut lire les donn├®es."

## En cas d'erreur API

Si le script retourne une erreur :
- V├®rifie que INTERVALS_API_KEY est dans .env.local
- V├®rifie la connexion r├®seau
- Rapporte l'erreur ├á Samuel
