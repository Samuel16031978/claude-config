# CLAUDE.md — Projet-Test (Samuel Chembah)

## Leçons apprises

- 2026-06-26 connecteurs/intégrations : toujours vérifier (recherche web) qu'un connecteur existe réellement avant de l'inscrire dans une architecture — ne pas supposer. Ex : Gemini n'a aucun connecteur Notion grand public (relais copier-coller manuel), DeepSeek passe par Notion AI.

## Structure du dépôt

```
Projet-Test/
├── nutritrack/          # Application mobile nutrition (Expo/React Native)
└── claude-global/       # Outils et skills Claude Code
    ├── intervals_icu.py                              # Client API intervals.icu
    └── skills/samuel/intervals-icu-samuel/SKILL.md  # Définition du skill
```

## Configuration de l'environnement

### Politique réseau
Le domaine `intervals.icu` est autorisé dans la politique réseau de l'environnement.

### Variables d'environnement
`claude-global/.env.local` (non commité) doit contenir :
```
INTERVALS_API_KEY=<clé API intervals.icu>
```

## Skill intervals-icu-samuel

Connexion en temps réel à intervals.icu pour calculer des séances et gérer la charge d'entraînement de Samuel (Athlete ID : `i171091`).

**Déclencheurs :** CTL, ATL, TSB, charge, intervals.icu, "quelle séance", zones FC, FTP, TRIMP, hrTSS, planification séance.

### Commandes disponibles

```bash
cd claude-global

# Lire CTL/ATL/TSB du jour
python3 intervals_icu.py wellness

# Zones FC par sport
python3 intervals_icu.py zones [run|ride|swim]

# Charge nécessaire pour un CTL cible
python3 intervals_icu.py calc_charge --ctl_target 30

# Convertir une charge en séance
python3 intervals_icu.py session --charge 120 --sport run --zone 2

# Historique des 7 derniers jours
python3 intervals_icu.py history --days 7

# Pousser une séance sur le calendrier (confirmation Samuel requise)
python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2"
```

### Règles importantes
- Toujours lire `wellness` avant tout calcul
- Ne jamais pousser une séance sans confirmation explicite de Samuel
- La clé API ne doit jamais être commitée dans git
