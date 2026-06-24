# Projet : Assistant WhatsApp ÔåÆ N8N ÔåÆ Monday

**Priorit├®** : HAUTE ÔÇö projet bloqu├® ├á d├®bloquer
**Derni├¿re activit├®** : 2026-06-04

## Objectif

Un message WhatsApp arrive ÔåÆ N8N l'analyse ÔåÆ cr├®e/met ├á jour une t├óche Monday.com automatiquement. Claude sert d'IA de traitement au milieu.

## Architecture cible

```
[Client WhatsApp]
      Ôåô
[Evolution API] ÔåÆ webhook
      Ôåô
[N8N] ÔåÆ traitement + Claude
      Ôåô
[Monday.com] ÔåÆ cr├®ation/mise ├á jour t├óche
      Ôåô
[R├®ponse WhatsApp via Evolution API]
```

## ├ëtat actuel

- [ ] Evolution API configur├®e sur Render
- [ ] Webhook N8N ÔåÆ ├á v├®rifier
- [ ] Workflow N8N ÔåÆ ├á construire / reprendre
- [ ] Connexion Monday.com ÔåÆ ├á configurer
- [ ] Tests end-to-end ÔåÆ ├á faire

## Points bloquants connus

_(├á remplir lors de la prochaine session de debug)_

## D├®cisions techniques

- H├®bergement : Render (Evolution API)
- Orchestration : N8N (auto-h├®berg├® ou cloud)
- IA traitement : Claude API

## Prochains pas

1. V├®rifier que l'Evolution API r├®pond sur Render
2. Tester le webhook WhatsApp ÔåÆ N8N
3. Construire le workflow N8N avec n┼ôud Claude
4. Connecter Monday.com en sortie
