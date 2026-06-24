---
name: intervals-icu-samuel
description: >
  Connexion en temps r├®el ├á intervals.icu pour calculer des s├®ances pr├®cises et g├®rer la charge d'entra├«nement.
  D├ëCLENCHE ce skill d├¿s que Samuel mentionne : CTL, ATL, TSB, charge, intervals.icu, "quelle s├®ance pour atteindre CTL X",
  "combien de temps pour charge Y", zones FC, FTP, "s├®ance du jour", calcul de charge, TRIMP, hrTSS,
  "quel impact sur mon CTL", "simuler une s├®ance", planifier une s├®ance sur intervals.icu.
  D├®clenche aussi quand Samuel donne des donn├®es Garmin et demande une s├®ance adapt├®e ├á un objectif CTL pr├®cis.
---

# Intervals.icu ÔÇö Skill Samuel

## R├┤le

Acc├®der aux donn├®es r├®elles intervals.icu (CTL/ATL/TSB, zones FC, historique) et calculer des s├®ances pr├®cises pour atteindre un CTL cible. Toutes les op├®rations passent par le script `intervals_icu.py` via Claude Code.

---

## Configuration

```
ATHLETE_ID : i171091
Cl├® API    : dans .env.local ÔåÆ INTERVALS_API_KEY
Base URL   : https://intervals.icu/api/v1/athlete/i171091
```

---

## Op├®rations disponibles

### 1. Lire CTL/ATL/TSB du jour
```bash
python3 intervals_icu.py wellness
```
Retourne : CTL, ATL, TSB, resting HR, date.

### 2. Lire les zones FC par sport
```bash
python3 intervals_icu.py zones [run|ride|swim]
```
Retourne : limites FC par zone pour le sport demand├®.

### 3. Calculer la charge n├®cessaire pour un CTL cible
```bash
python3 intervals_icu.py calc_charge --ctl_target 27
```
Retourne : charge (TRIMP) n├®cessaire aujourd'hui pour atteindre le CTL cible.

### 4. Convertir une charge en dur├®e/FC par sport
```bash
python3 intervals_icu.py session --charge 120 --sport run --zone 2
```
Retourne : dur├®e estim├®e, FC cible, allure estim├®e.

### 5. Pousser une s├®ance sur le calendrier
```bash
python3 intervals_icu.py push_event --date 2026-06-01 --name "Run Z2" --description "75 min Z2 FC 125-142"
```

### 6. Lire l'historique r├®cent (7 derniers jours)
```bash
python3 intervals_icu.py history --days 7
```
Retourne : liste s├®ances, charge, CTL/ATL par jour.

---

## Algorithme CTL/ATL (EWMA intervals.icu)

```
CTL(j) = CTL(j-1) + (charge_j - CTL(j-1)) / 42
ATL(j) = ATL(j-1) + (charge_j - ATL(j-1)) / 7
TSB(j) = CTL(j-1) - ATL(j-1)
```

**Calcul charge n├®cessaire pour CTL cible :**
```
charge_n├®cessaire = CTL_cible ├ù 42 - CTL_actuel ├ù (42 - 1)
                  = CTL_cible + (CTL_cible - CTL_actuel) ├ù 41
```

---

## Conversion charge ÔåÆ dur├®e par sport

Facteurs TRIMP par zone FC (profil Samuel, FC max 191 bpm) :

| Zone | FC (run) | Facteur TRIMP/min |
|---|---|---|
| Z1 | <114 | 0.9 |
| Z2 | 114-142 | 1.5 |
| Z3 | 142-158 | 2.2 |
| Z4 | 158-172 | 3.1 |
| Z5 | >172 | 4.0 |

**Dur├®e estim├®e = Charge cible / Facteur zone**

Pour v├®lo : facteur ├ù 0.75 (moins d'impact m├®canique ÔåÆ TRIMP plus faible ├á m├¬me FC).
Pour natation : facteur ├ù 0.85.

---

## R├¿gles d'utilisation

- Toujours lire CTL/ATL/TSB r├®els avant de calculer (`wellness`)
- Croiser avec `training-adaptatif` pour valider l'├®tat musculaire avant de proposer
- V├®rifier coh├®rence J+1 ├á J+3 apr├¿s calcul (`planning-expert`)
- Ne jamais pousser une s├®ance sur le calendrier sans confirmation explicite de Samuel
- Zones FC ├á relire depuis l'API si >7 jours sans mise ├á jour
