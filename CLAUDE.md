# CLAUDE.md ÔÇö Projet-Test (Samuel Chembah)

## Structure du d├®p├┤t

```
Projet-Test/
Ôö£ÔöÇÔöÇ nutritrack/          # Application mobile nutrition (Expo/React Native)
ÔööÔöÇÔöÇ claude-global/       # Outils et skills Claude Code
    Ôö£ÔöÇÔöÇ intervals_icu.py                              # Client API intervals.icu
    ÔööÔöÇÔöÇ skills/samuel/intervals-icu-samuel/SKILL.md  # D├®finition du skill
```

## Configuration de l'environnement

### Politique r├®seau
Le domaine `intervals.icu` est autoris├® dans la politique r├®seau de l'environnement.

### Variables d'environnement
`claude-global/.env.local` (non commit├®) doit contenir :
```
INTERVALS_API_KEY=<cl├® API intervals.icu>
```

## Skill intervals-icu-samuel

Connexion en temps r├®el ├á intervals.icu pour calculer des s├®ances et g├®rer la charge d'entra├«nement de Samuel (Athlete ID : `i171091`).

**D├®clencheurs :** CTL, ATL, TSB, charge, intervals.icu, "quelle s├®ance", zones FC, FTP, TRIMP, hrTSS, planification s├®ance.

### Commandes disponibles

```bash
cd claude-global

# Lire CTL/ATL/TSB du jour
python3 intervals_icu.py wellness

# Zones FC par sport
python3 intervals_icu.py zones [run|ride|swim]

# Charge n├®cessaire pour un CTL cible
python3 intervals_icu.py calc_charge --ctl_target 30

# Convertir une charge en s├®ance
python3 intervals_icu.py session --charge 120 --sport run --zone 2

# Historique des 7 derniers jours
python3 intervals_icu.py history --days 7

# Pousser une s├®ance sur le calendrier (confirmation Samuel requise)
python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2"
```

### R├¿gles importantes
- Toujours lire `wellness` avant tout calcul
- Ne jamais pousser une s├®ance sans confirmation explicite de Samuel
- La cl├® API ne doit jamais ├¬tre commit├®e dans git
