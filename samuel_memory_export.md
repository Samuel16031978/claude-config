# Fichier M├®moire ÔÇö Samuel
> Export├® le 2026-06-02 depuis Claude Code (session Projet-Test)
> Enrichi par analyse approfondie du code source NutriTrack
> Destin├® ├á l'import dans Cowork ou tout autre outil AI repartant de z├®ro.

---

## 1. Profil Utilisateur

| Champ | Valeur |
|-------|--------|
| Pr├®nom | Samuel |
| Email | sc.realisations@gmail.com |
| GitHub | samuel16031978 |
| Ann├®e de naissance (estim├®e) | ~1978 (d'apr├¿s le handle GitHub) |
| Langue de travail | Fran├ºais (tous les ├®changes, code UI, domaine m├®tier) |
| Fuseau horaire | Non confirm├® |

### R├┤le & Expertise

Samuel est un **d├®veloppeur mobile full-stack** avec une expertise av├®r├®e en :
- Architecture d'applications React Native / Expo (routing, state, DB locale)
- TypeScript strict (discriminated unions, types mapp├®s, Zod, Drizzle ORM)
- Domaine nutritionnel (formules BMR Mifflin-St Jeor correctes, macros par objectif, scoring ├®quilibr├®)
- UX mobile : bottom sheets, FAB, pull-to-refresh, SafeAreaView, KeyboardAvoidingView
- Outillage IA : int├®gration Gemini, prompt engineering en fran├ºais, multi-API

**Niveau estim├®** : d├®veloppeur confirm├® ├á senior ÔÇö capable de sp├®cifier et produire une application compl├¿te coh├®rente en une session, avec des choix architecturaux pragmatiques et justifi├®s.

### Style de Travail
- Orient├® **r├®sultat** : livrables complets et fonctionnels, pas d'├®bauches
- **Pragmatique** : pr├®f├¿re les solutions simples et concr├¿tes aux abstractions g├®n├®riques
- Pense ├á l'**outillage de contexte** : exports m├®moire, branches nomm├®es, commits propres ÔÇö gestion rigoureuse du contexte inter-sessions
- Utilise plusieurs outils IA en parall├¿le (Claude Code + Claude.ai + Cowork) et orchestre leur collaboration via des fichiers partag├®s
- **D├®l├¿gue le d├®veloppement entier** ├á l'IA ÔÇö ne code pas ligne ├á ligne, supervise et valide

### Pr├®f├®rences de Communication
- Langue : **fran├ºais** (y compris commits, messages d'erreur, UI)
- Format : r├®ponses **structur├®es** avec Markdown (titres, tableaux, listes ├á puces)
- Tonalit├® : directe, sans introduction ni conclusion inutile
- Pr├®f├¿re les **r├®sultats** aux annonces : "voici le fichier" > "je vais cr├®er le fichier"
- Utilise les **├®mojis dans l'UI** mais pas dans la communication textuelle avec l'IA

---

## 2. Style de Code (Inf├®r├® du Source NutriTrack)

### Conventions de Nommage
| Contexte | Convention | Exemples |
|----------|------------|---------|
| Fonctions / variables | camelCase | `calculateTargets()`, `handleFoodSelected()` |
| Composants React | PascalCase | `BalanceScore`, `MealCard`, `NutrientBar` |
| Types / Interfaces | PascalCase | `UserProfile`, `DailyTotals`, `NutritionTargets` |
| Tables DB | snake_case | `user_profile`, `meal_logs`, `food_library` |
| Colonnes DB | snake_case | `height_cm`, `calories_kcal`, `target_weight_kg` |
| Valeurs d'enum (domaine) | **fran├ºais** snake_case | `'petit_dejeuner'`, `'sedentaire'`, `'perte'` |
| Constantes globales | SCREAMING_SNAKE_CASE | `COLORS`, `SPACING`, `MEAL_TYPES`, `ALLERGENS` |

### Patterns TypeScript Pr├®f├®r├®s
- **Discriminated unions** pour les enums domaine :
  ```typescript
  type GoalType = 'perte' | 'maintien' | 'prise';
  type MealType = 'petit_dejeuner' | 'dejeuner' | 'diner' | 'collation';
  ```
- **Record types** pour les mappings i18n :
  ```typescript
  const ALLERGEN_LABELS: Record<Allergen, string> = { gluten: 'Gluten', ... }
  ```
- **Omit** pour les payloads de mise ├á jour : `Omit<UserProfile, 'id' | 'updated_at'>`
- **Explicit nullables** : `target_weight_kg: number | null` (pas de `?` implicite)
- Zustand store typ├® : `create<MealsState>((set, get) => ({...}))`
- Pas de g├®n├®riques over-engineered ÔÇö clart├® > flexibilit├®

### Gestion d'Erreurs
- Erreurs techniques en **fran├ºais** : `'Cl├® API Gemini manquante. Configurez EXPO_PUBLIC_GEMINI_API_KEY dans .env.local'`
- Happy path assum├® pour les op├®rations DB (pas de try-catch syst├®matique)
- Guards UI avec early return : `if (!profile || !targets) return null;`
- `Alert.alert()` pour les erreurs user-facing (allerg├¿nes, incompatibilit├®s)

### Organisation du Code
- S├®paration stricte des couches : `types/` ÔåÆ `db/schema` ÔåÆ `db/queries/` ÔåÆ `store/` ÔåÆ `nutrition/` ÔåÆ `components/` ÔåÆ `app/`
- Fonctions de calcul **pures** dans `/src/nutrition/`
- Pas de custom hooks ÔÇö Zustand consomm├® directement dans les composants
- Pas de HOC ni wrapper g├®n├®rique
- `StyleSheet.create()` au niveau module (jamais inline)
- Modales d├®finies comme composants imbriqu├®s dans le fichier parent

### Commentaires
- **Minimaux** ÔÇö le code est auto-document├® par le nommage
- Aucun TODO/FIXME/NOTE trouv├® dans le code
- Pas de JSDoc ni de blocs multi-lignes
- Seul commentaire notable : le system prompt Gemini (explique les instructions IA)

### Design UI/UX
- **Emojis** dans les headers et labels UI : `'­ƒì¢ Repas du jour'`, `'­ƒÆí Conseils'`, `'­ƒîà Petit-d├®jeuner'`
- Pattern **FAB (Floating Action Button)** pour l'action principale
- **Bottom sheets** (animationType="slide") pour les modales de saisie
- **Cards** avec ombres subtiles : `elevation: 1`, `shadowOpacity: 0.05`
- Pull-to-refresh sur le dashboard
- Syst├¿me de spacing/border-radius coh├®rent via constantes (sm/md/lg/xl)
- Accessibilit├® : `SafeAreaView`, `KeyboardAvoidingView`, `keyboardShouldPersistTaps="handled"`

### Points d'Am├®lioration Connus (Inf├®r├®s)
- Validation des champs num├®riques repose sur `parseFloat()` (pas de Zod c├┤t├® UI)
- Pas de logging / instrumentation visible
- Pas de tests automatis├®s d├®tect├®s

---

## 3. Projets en Cours

### Projet principal : NutriTrack

| Champ | Valeur |
|-------|--------|
| Nom | NutriTrack |
| D├®p├┤t GitHub | `samuel16031978/projet-test` |
| R├®pertoire local | `/home/user/Projet-Test/nutritrack/` |
| Objectif | Application mobile de suivi nutritionnel personnalis├® |
| Statut | **MVP livr├®** ÔÇö commit `a2487ea` |
| Branche build | `claude/nutrition-tracker-app-OHQ9C` |
| Branche m├®moire | `claude/user-memory-export-WLgV5` |

#### Stack Technique Compl├¿te

| Couche | Technologie | Version |
|--------|-------------|---------|
| Langage | TypeScript strict | 5.9 |
| Framework mobile | React Native + Expo | 0.81.5 / 54.0.33 |
| Runtime | React | 19 |
| Routeur | Expo Router (file-based) | 6.0.23 |
| Base de donn├®es | SQLite + Drizzle ORM | 0.45.2 |
| ├ëtat global | Zustand | 5.0.13 |
| UI | React Native Paper | 5.15.1 |
| IA repas | Google Generative AI (Gemini 1.5 Flash) | 0.24.1 |
| Validation | Zod | 4.4.3 |
| Cam├®ra | Expo Camera | 17.0.10 |
| S├®curit├® | Expo Secure Store | 15.0.8 |
| Images | Expo Image Manipulator | ÔÇö |
| Cibles | iOS, Android, Web | ÔÇö |

#### Fonctionnalit├®s Impl├®ment├®es
1. **Onboarding** : nom, sexe, ├óge, poids, taille, objectif (`perte`/`maintien`/`prise`), niveau d'activit├®, allerg├¿nes, pr├®f├®rences alimentaires
2. **Saisie des repas** (3 m├®thodes) : recherche manuelle, analyse photo Gemini, scan code-barres Open Food Facts
3. **Calculs nutritionnels** : BMR (Mifflin-St Jeor), TDEE, macros cibles, fibres, sodium
4. **Score d'├®quilibre** (0ÔÇô100) : pond├®r├® calories 30% + prot├®ines 30% + glucides 20% + lipides 20%
5. **Conseils IA** personnalis├®s selon le profil
6. **Historique** des repas
7. **Alertes allerg├¿nes** et incompatibilit├®s r├®gime

#### Base de Donn├®es (4 tables SQLite)
| Table | R├┤le |
|-------|------|
| `user_profile` | Profil biom├®trique + objectifs + allergies + pr├®f├®rences |
| `food_library` | Aliments multi-sources (Open Food Facts, USDA, Gemini, manuel) |
| `meal_logs` | Repas loggu├®s avec type, horodatage, m├®thode de saisie, photo URI |
| `meal_entries` | Aliments dans un repas (table de jonction, quantit├® en grammes) |

#### Fichiers Cl├®s
| R├┤le | Chemin |
|------|--------|
| Entry point app | `nutritrack/app/_layout.tsx` |
| Dashboard | `nutritrack/app/(tabs)/index.tsx` |
| Ajout repas | `nutritrack/app/(tabs)/log.tsx` |
| Historique | `nutritrack/app/(tabs)/history.tsx` |
| Profil | `nutritrack/app/(tabs)/profile.tsx` |
| Onboarding | `nutritrack/app/onboarding.tsx` |
| Cam├®ra IA | `nutritrack/app/camera.tsx` |
| Code-barres | `nutritrack/app/barcode.tsx` |
| Sch├®ma DB | `nutritrack/src/db/schema.ts` |
| Calcul macros | `nutritrack/src/nutrition/macros.ts` |
| Score ├®quilibre | `nutritrack/src/nutrition/balance.ts` |
| BMR/TDEE | `nutritrack/src/nutrition/bmr.ts` |
| Stores Zustand | `nutritrack/src/store/mealsStore.ts`, `profileStore.ts` |
| API Gemini | `nutritrack/src/api/gemini.ts` |
| API Open Food Facts | `nutritrack/src/api/openFoodFacts.ts` |
| API USDA | `nutritrack/src/api/usda.ts` |
| Th├¿me | `nutritrack/src/constants/theme.ts` |

#### Variable d'Environnement Requise
```
EXPO_PUBLIC_GEMINI_API_KEY=<dans nutritrack/.env.local>
```

#### Alias TypeScript
```
@/* ÔåÆ src/*
```

---

## 4. Pr├®f├®rences & Comportements

### Comportements Valid├®s (├á reproduire)
- R├®pondre en **fran├ºais**
- TypeScript strict ÔÇö discriminated unions, pas de `any`
- S├®paration claire des couches : UI / logique / donn├®es / ├®tat
- Expo Router : fichiers dans `app/` = routes
- Drizzle ORM pour la DB SQLite (jamais d'acc├¿s direct)
- Zustand pour l'├®tat global (pas Redux)
- Commits `feat:`/`fix:` en fran├ºais, commits propres
- Pousser sur la bonne branche, **jamais cr├®er de PR sans demande**
- Code auto-document├® par le nommage, pas de commentaires inutiles
- Valeurs domaine en **fran├ºais** dans les enums/unions

### Comportements ├á ├ëviter
- Cr├®er une PR sans demande explicite
- Pousser sur `main`/`master` sans autorisation
- Inventer des URLs ou endpoints non confirm├®s
- Ajouter des commentaires de code obvieux
- Refactorer au-del├á de ce qui est demand├® (pas d'abstractions pr├®matur├®es)
- Cr├®er des README ou fichiers de documentation non demand├®s
- Utiliser des ├®mojis dans les r├®ponses texte (seulement dans l'UI des apps)
- R├®ponses avec introductions/conclusions verbeuses

### Notes sur les Retours
- Aucun feedback de correction dans cette session : le projet a ├®t├® livr├® et accept├® tel quel
- La demande d'export m├®moire structur├® montre une approche **syst├®matique et organis├®e**
- Samuel pense en termes de **workflow multi-outils** : il orchestre Claude Code, Claude.ai, Cowork

---

## 5. R├®f├®rences & Outils

### ├ëcosyst├¿me Outils
| Outil | Usage |
|-------|-------|
| Claude Code (web remote) | D├®veloppement, g├®n├®ration de code, gestion Git |
| Claude.ai | Enrichissement m├®moire, questions g├®n├®rales |
| Cowork | Outil AI destination de ce fichier m├®moire |
| GitHub (`samuel16031978/projet-test`) | D├®p├┤t source, branches, versioning |
| Google Gemini API | Reconnaissance visuelle des repas dans NutriTrack |
| Open Food Facts API | Lookup code-barres aliments |
| USDA Food Database | Base d'aliments compl├®mentaire |
| Expo / EAS | Build et d├®ploiement mobile |

### O├╣ Trouver les Infos
| Info | Emplacement |
|------|-------------|
| Code source NutriTrack | GitHub `samuel16031978/projet-test`, branche `claude/nutrition-tracker-app-OHQ9C` |
| Fichier m├®moire (ce fichier) | Racine du repo, `samuel_memory_export.md` |
| Sch├®ma base de donn├®es | `nutritrack/src/db/schema.ts` |
| Configuration Expo | `nutritrack/app.json` |
| D├®pendances | `nutritrack/package.json` |
| Variables d'environnement | `nutritrack/.env.local` (non commit├®, ├á recr├®er) |

---

## 6. Contexte de Session Claude Code

- **Environnement** : conteneur ├®ph├®m├¿re cloud ÔÇö repo clon├® ├á chaque session, contexte effac├® ├á la fin
- **├Ç faire au d├®marrage** : toujours `git status` + `git log` pour retrouver l'├®tat du repo
- **Convention de branche** : `claude/<description-courte>-<id-al├®atoire>`
- **Dernier ├®tat connu** : working tree propre, 2 branches distantes, MVP NutriTrack livr├®

---

## 7. Sections ├á Compl├®ter par Samuel

> Ces champs sont vides car non visibles dans le code ÔÇö ├á remplir manuellement ou via Claude.ai.

- **Autres projets en cours** (hors NutriTrack) : `___`
- **R├┤le professionnel exact** (freelance, CTO, indie dev, etc.) : `___`
- **Stack habituelle** (hors ce projet) : `___`
- **Priorit├®s actuelles** (feature ├á venir sur NutriTrack, autre projet ├á d├®marrer) : `___`
- **Contraintes de d├®ploiement** (App Store, TestFlight, Expo Go seulement ?) : `___`
- **Outils de design** (Figma, autre ?) : `___`
- **Pr├®f├®rences de test** (Jest, Detox, pas de tests ?) : `___`
- **Backend futur** (Supabase, Firebase, API custom ?) : `___`

---

*Fin du fichier m├®moire ÔÇö Samuel ÔÇö 2026-06-02*
