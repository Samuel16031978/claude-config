---
name: intervals-icu-samuel
description: >
  Connexion en temps réel à intervals.icu pour calculer des séances précises et gérer la charge d'entraînement.
  DÉCLENCHE ce skill dès que Samuel mentionne : CTL, ATL, TSB, charge, intervals.icu, "quelle séance pour atteindre CTL X",
  "combien de temps pour charge Y", zones FC, FTP, "séance du jour", calcul de charge, TRIMP, hrTSS,
  "quel impact sur mon CTL", "simuler une séance", planifier une séance sur intervals.icu.
  Déclenche aussi quand Samuel donne des données Garmin et demande une séance adaptée à un objectif CTL précis.
---

# Intervals.icu — Skill Samuel

## Rôle

Accéder aux données réelles intervals.icu (CTL/ATL/TSB, zones FC, historique) et calculer des séances précises pour atteindre un CTL cible. Toutes les opérations passent par le script `intervals_icu.py` via Claude Code.

---

## Configuration

```
ATHLETE_ID : i171091
Clé API    : dans .env.local → INTERVALS_API_KEY
Base URL   : https://intervals.icu/api/v1/athlete/i171091
```

---

## Opérations disponibles

### 1. Lire CTL/ATL/TSB du jour
```bash
python3 intervals_icu.py wellness
```
Retourne : CTL, ATL, TSB, resting HR, date.

### 2. Lire les zones FC par sport
```bash
python3 intervals_icu.py zones [run|ride|swim]
```
Retourne : limites FC par zone pour le sport demandé.

### 3. Calculer la charge nécessaire pour un CTL cible
```bash
python3 intervals_icu.py calc_charge --ctl_target 27
```
Retourne : charge (TRIMP) nécessaire aujourd'hui pour atteindre le CTL cible.

### 4. Convertir une charge en durée/FC par sport
```bash
python3 intervals_icu.py session --charge 120 --sport run --zone 2
```
Retourne : durée estimée, FC cible, allure estimée.

### 5. Pousser une séance sur le calendrier
```bash
python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2 FC 125-142"
```

### 6. Lire l'historique récent (7 derniers jours)
```bash
python3 intervals_icu.py history --days 7
```
Retourne : liste séances, charge, CTL/ATL par jour.

---

## Algorithme CTL/ATL (EWMA intervals.icu)

```
CTL(j) = CTL(j-1) + (charge_j - CTL(j-1)) / 42
ATL(j) = ATL(j-1) + (charge_j - ATL(j-1)) / 7
TSB(j) = CTL(j-1) - ATL(j-1)
```

**Calcul charge nécessaire pour CTL cible :**
```
charge_nécessaire = CTL_cible × 42 - CTL_actuel × (42 - 1)
                  = CTL_cible + (CTL_cible - CTL_actuel) × 41
```

---

## Conversion charge → durée par sport

Facteurs TRIMP par zone FC (profil Samuel, FC max 191 bpm) :

| Zone | FC (run) | Facteur TRIMP/min |
|---|---|---|
| Z1 | <114 | 0.9 |
| Z2 | 114-142 | 1.5 |
| Z3 | 142-158 | 2.2 |
| Z4 | 158-172 | 3.1 |
| Z5 | >172 | 4.0 |

**Durée estimée = Charge cible / Facteur zone**

Pour vélo : facteur × 0.75 (moins d'impact mécanique → TRIMP plus faible à même FC).
Pour natation : facteur × 0.85.

---

## Règles d'utilisation

- Toujours lire CTL/ATL/TSB réels avant de calculer (`wellness`)
- Croiser avec `training-ironman-2026` pour valider l'état musculaire avant de proposer
- Vérifier cohérence J+1 à J+3 après calcul (`planificateur`)
- Ne jamais pousser une séance sur le calendrier sans confirmation explicite de Samuel
- Zones FC à relire depuis l'API si >7 jours sans mise à jour
