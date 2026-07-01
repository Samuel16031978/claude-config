# Mode d'emploi — Effacer son empreinte numérique des *data brokers* via un agent IA

> Fiche issue du scrape de la vidéo **« Qu'est-ce qui se passe quand tu demandes à ChatGPT
> d'effacer toute ton empreinte d'internet ? »** — chaîne **Henri · ExplorIA**
> (short : <https://youtu.be/xG4iLSn7kbk>). Scrapée le 2026-06-30 via `youtube_scraper.py`.

## 1. De quoi parle la vidéo (le vrai sujet)

Le titre dit « effacer ton empreinte » mais la technique réelle est un **opt-out de masse auprès des
*data brokers*** : ces sociétés (Whitepages, Spokeo, BeenVerified, et côté FR/EU les annuaires inversés
et courtiers en données) agrègent et **revendent** ton nom, adresse, téléphone, e-mails. La loi te donne
un **droit de suppression** (opt-out) site par site — mais c'est fastidieux à la main.

L'idée de la vidéo : faire faire ce travail répétitif par un **agent IA** capable de naviguer le web, en
4 temps : **trouver → rédiger → soumettre → entretenir**.

## 2. Pré-requis

- Un assistant IA avec **recherche web** ET un **mode agent navigateur** (qui clique/remplit des
  formulaires) : *ChatGPT Agent* ou *Claude in Chrome / Claude computer use* (cf. §5).
- Les infos que tu veux faire retirer : **nom complet** (+ variantes), **ville/adresse**, **téléphone(s)**,
  **e-mail(s)**. ⚠️ Tu fournis ces données à l'IA pour qu'elle les retrouve : ne fournis que le périmètre
  utile, et fais-le dans un compte/espace de travail dont tu maîtrises la confidentialité.

## 3. Le workflow en 4 prompts (prêts à copier)

Garde **le même fil de conversation** du début à la fin : chaque étape réutilise la liste produite avant.

### Prompt 1 — Découverte des courtiers
```
Tu es mon assistant en protection de la vie privée. Cherche sur le web tout ce qui est
public à mon sujet et dresse la liste de chaque data broker et site de recherche de
personnes (people-search) qui expose mes informations.

Mes données de recherche :
- Nom complet (+ variantes/orthographes) : <…>
- Ville / pays : <…>
- E-mail(s) : <…>
- Téléphone(s) : <…>

Pour CHAQUE site trouvé, donne-moi un tableau avec : nom du site · URL de ma fiche
exposée · type de données visibles · lien EXACT de la page d'opt-out/désinscription ·
méthode requise (formulaire web, e-mail, vérification d'identité, CAPTCHA).
Classe les sites du plus exposant au moins exposant.
```

### Prompt 2 — Rédaction des demandes de suppression
```
Reste dans ce fil. Pour chaque site listé, rédige la demande de suppression exacte à
envoyer. Personnalise-la (référence à ma fiche), invoque le droit applicable
(RGPD art. 17 « droit à l'effacement » en Europe ; CCPA si site US) et reste ferme et
concis. Donne-moi une version par site, prête à coller/envoyer.
```

### Prompt 3 — Soumission automatique (mode agent)
```
Active le mode agent / navigateur. Va sur chaque page d'opt-out de la liste et soumets
la demande de suppression à ma place. Avant CHAQUE envoi qui demande une vérification
d'identité, une confirmation par e-mail ou un CAPTCHA, arrête-toi et demande-moi de
valider. Tiens un tableau de suivi : site · statut (soumis / en attente / bloqué) · date.
```

### Prompt 4 — Entretien (récurrence)
```
Crée une routine de contrôle : chaque semaine, revérifie chaque site et ressoumets toute
demande ignorée ou réapparue, jusqu'à disparition complète. À chaque passage, rends-moi
un résumé : ce qui a disparu, ce qui résiste, et ce qui nécessite une action de ma part.
```

## 4. Limites à connaître (la vidéo survend un peu)

- **Beaucoup de sites bloquent les agents** : CAPTCHA, vérification e-mail/SMS, voire pièce d'identité.
  L'auto-soumission « sans rien faire » échoue souvent → garde un humain dans la boucle (d'où le « arrête-toi
  et demande » du prompt 3).
- **La récurrence « chaque semaine » n'est pas autonome** dans un chat classique : il faut soit relancer
  toi-même, soit une vraie planification (tâche programmée / agent persistant).
- **Tu réintroduis tes données** en les donnant à l'IA et aux sites — accepte ce compromis en connaissance
  de cause.
- **Levier EU souvent plus efficace que l'opt-out** : en tant que résident français, le **RGPD (droit à
  l'effacement)** et un signalement **CNIL** ont plus de poids ; pour la couverture durable, les services
  dédiés (Incogni, DeleteMe…) automatisent ça en continu, là où un chat fait surtout le *one-shot*.

## 5. ChatGPT ou Claude ? — ma recommandation

**Réponse courte : pour reproduire la vidéo telle quelle → ChatGPT. Pour le meilleur résultat réel → un mix,
avec Claude pour le cerveau (étapes 1-2) et une soumission supervisée.**

| Étape | Meilleur choix | Pourquoi |
|---|---|---|
| 1. Découverte (recherche web) | Égalité | Les deux cherchent bien ; demande des sources/URL vérifiables. |
| 2. Rédaction des demandes | **Claude** | Rédaction nuancée et cadrage juridique (RGPD/art. 17) soignés ; tu y es déjà à l'aise. |
| 3. Soumission agent navigateur | **ChatGPT (Agent)** | Le « mode agent » de la vidéo = navigateur virtuel intégré, grand public, soumet les formulaires en un seul produit. Équivalent Claude : *Claude in Chrome* / *computer use*, plus orienté dev/preview. |
| 4. Entretien planifié | Ni l'un ni l'autre seul | Un chat ne tourne pas tout seul → planifier (tâche/agent persistant) ou service dédié. |

**Concrètement pour toi (Samuel) :**
- Tu **reproduis exactement la vidéo** → **ChatGPT** avec le mode Agent : c'est le chemin le plus court pour
  l'auto-soumission « clé en main ».
- Tu veux **le meilleur livrable** → fais **les prompts 1 et 2 dans Claude** (découverte + rédaction des
  demandes : c'est là que la qualité compte, et c'est ton environnement), puis exécute la **soumission en mode
  supervisé** (ChatGPT Agent ou Claude in Chrome), CAPTCHA/vérifs validés par toi.
- Pour une **couverture durable** plutôt qu'un coup unique : appuie-toi sur le **RGPD/CNIL** et/ou un
  **service spécialisé**. L'agent IA est excellent pour *défricher et rédiger*, fragile pour *garantir la
  suppression dans le temps*.

> En une phrase : **ChatGPT gagne sur le geste « agent qui soumet », Claude gagne sur la matière
> « quoi envoyer et avec quel argument légal »** — combine-les, et ne compte pas sur l'auto-pilote total.
