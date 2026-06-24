---
name: github-installer
description: Clone un d├®p├┤t GitHub et installe ses fichiers Claude Code (skills, agents, commands) dans le projet courant
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# GitHub Installer Skill

Installe les fichiers Claude Code d'un d├®p├┤t GitHub distant dans le projet courant.

## Task

Re├ºois une URL de d├®p├┤t GitHub, clone-le temporairement, copie les fichiers `.claude/` pertinents, v├®rifie l'exhaustivit├®, puis nettoie.

## Instructions

### 1. Pr├®pare le r├®pertoire temporaire

```bash
REPO_URL="[URL fournie dans le contexte]"
REPO_NAME=$(basename $REPO_URL .git)
TMP_DIR="/tmp/github-watch-$REPO_NAME-$(date +%s)"
mkdir -p "$TMP_DIR"
```

### 2. Clone le d├®p├┤t (shallow pour la rapidit├®)

```bash
git clone --depth=1 "$REPO_URL" "$TMP_DIR"
```

Si le clone ├®choue, arr├¬te et rapporte l'erreur.

### 3. Inventaire complet des fichiers Claude Code

Compte **tous** les fichiers de fa├ºon r├®cursive (sous-dossiers inclus) :

```bash
echo "=== Inventaire source ==="
echo "Skills (dossiers) : $(find "$TMP_DIR/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)"
echo "Agents (.md r├®cursif) : $(find "$TMP_DIR/.claude/agents" -name "*.md" 2>/dev/null | wc -l)"
echo "Commands (.md r├®cursif) : $(find "$TMP_DIR/.claude/commands" -name "*.md" 2>/dev/null | wc -l)"
echo "Rules (.md) : $(find "$TMP_DIR/.claude/rules" -name "*.md" 2>/dev/null | wc -l)"
echo "Total fichiers .claude/ : $(find "$TMP_DIR/.claude" -type f 2>/dev/null | wc -l)"
```

Si `.claude/` est absent du d├®p├┤t, signaler et arr├¬ter proprement.

### 4. Copie r├®cursive fichier par fichier

> **Principe** : on fusionne au niveau du fichier individuel ÔÇö jamais au niveau du dossier.
> Un dossier existant localement n'est PAS un conflit ; seul un fichier au m├¬me chemin l'est.

```bash
SKILLS_OK=0; SKILLS_CONFLITS=0
AGENTS_OK=0; AGENTS_CONFLITS=0
CMDS_OK=0; CMDS_CONFLITS=0
CONFLITS_LISTE=""

# --- Skills : copie dossier entier uniquement si absent ---
while IFS= read -r skill_dir; do
  skill_name=$(basename "$skill_dir")
  if [ ! -d ".claude/skills/$skill_name" ]; then
    cp -r "$skill_dir" ".claude/skills/$skill_name"
    SKILLS_OK=$((SKILLS_OK+1))
  else
    SKILLS_CONFLITS=$((SKILLS_CONFLITS+1))
    CONFLITS_LISTE="$CONFLITS_LISTE\n  ÔÜá skills/$skill_name/ (skill d├®j├á pr├®sent)"
  fi
done < <(find "$TMP_DIR/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)

# --- Agents : r├®cursif, fichier par fichier, cr├®e les sous-dossiers au besoin ---
while IFS= read -r src_file; do
  rel_path="${src_file#$TMP_DIR/.claude/agents/}"
  dest_file=".claude/agents/$rel_path"
  mkdir -p "$(dirname "$dest_file")"
  if [ ! -f "$dest_file" ]; then
    cp "$src_file" "$dest_file"
    AGENTS_OK=$((AGENTS_OK+1))
  else
    AGENTS_CONFLITS=$((AGENTS_CONFLITS+1))
    CONFLITS_LISTE="$CONFLITS_LISTE\n  ÔÜá agents/$rel_path (fichier existant conserv├®)"
  fi
done < <(find "$TMP_DIR/.claude/agents" -name "*.md" 2>/dev/null)

# --- Commands : r├®cursif, fichier par fichier, cr├®e les sous-dossiers au besoin ---
while IFS= read -r src_file; do
  rel_path="${src_file#$TMP_DIR/.claude/commands/}"
  dest_file=".claude/commands/$rel_path"
  mkdir -p "$(dirname "$dest_file")"
  if [ ! -f "$dest_file" ]; then
    cp "$src_file" "$dest_file"
    CMDS_OK=$((CMDS_OK+1))
  else
    CMDS_CONFLITS=$((CMDS_CONFLITS+1))
    CONFLITS_LISTE="$CONFLITS_LISTE\n  ÔÜá commands/$rel_path (fichier existant conserv├®)"
  fi
done < <(find "$TMP_DIR/.claude/commands" -name "*.md" 2>/dev/null)

echo "Copie termin├®e : skills=$SKILLS_OK agents=$AGENTS_OK commands=$CMDS_OK"
[ -n "$CONFLITS_LISTE" ] && echo -e "Conflits d├®tect├®s :$CONFLITS_LISTE"
```

### 5. V├®rification d'exhaustivit├® (AVANT nettoyage)

> Cette ├®tape doit tourner **avant** `rm -rf $TMP_DIR`. Elle confirme que rien n'a ├®t├® oubli├®.

```bash
echo "=== V├®rification post-copie ==="
MANQUANTS=0

# V├®rifie chaque fichier source contre la destination
while IFS= read -r src_file; do
  rel_path="${src_file#$TMP_DIR/.claude/}"
  dest_file=".claude/$rel_path"
  if [ ! -f "$dest_file" ]; then
    # Distingue conflit connu vs fichier vraiment absent
    echo "  ABSENT : $rel_path"
    MANQUANTS=$((MANQUANTS+1))
  fi
done < <(find "$TMP_DIR/.claude" -name "*.md" 2>/dev/null)

# Skills : v├®rifie les dossiers
while IFS= read -r skill_dir; do
  skill_name=$(basename "$skill_dir")
  [ ! -d ".claude/skills/$skill_name" ] && echo "  SKILL ABSENT : $skill_name" && MANQUANTS=$((MANQUANTS+1))
done < <(find "$TMP_DIR/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)

if [ $MANQUANTS -eq 0 ]; then
  echo "Ô£ô Exhaustivit├® confirm├®e ÔÇö aucun fichier manquant hors conflits d├®clar├®s"
else
  echo "ÔÜá $MANQUANTS fichiers absents apr├¿s copie ÔÇö v├®rifier manuellement avant de continuer"
fi
```

### 6. Nettoie le r├®pertoire temporaire

```bash
rm -rf "$TMP_DIR"
echo "Ô£ô /tmp/ nettoy├®"
```

### 7. Commits group├®s par cat├®gorie

Commite en groupes logiques (pas un commit par fichier) :

```bash
# Skills
git add ".claude/skills/"
git commit -m "feat: [github-watch] [repo] ÔÇö [N] skills ([noms principauxÔÇª])"

# Agents
git add ".claude/agents/"
git commit -m "feat: [github-watch] [repo] ÔÇö [N] agents ([cat├®gories principalesÔÇª])"

# Commands
git add ".claude/commands/"
git commit -m "feat: [github-watch] [repo] ÔÇö [N] commandes ([cat├®gories principalesÔÇª])"
```

### 8. Enregistre dans le registre

Ajoute ou met ├á jour l'entr├®e dans `.claude/installed-repos.json` :

```json
{
  "name": "[owner/repo]",
  "url": "[URL du d├®p├┤t]",
  "installed_at": "[TODAY]",
  "last_checked": "[TODAY]",
  "stars_at_install": [N],
  "files_installed": {
    "agents": [N],
    "commands": [N],
    "skills": [N]
  },
  "conflicts": [N],
  "update_available": false
}
```

Si le d├®p├┤t existe d├®j├á dans le registre : mettre ├á jour `last_checked` et `files_installed` uniquement.
Si c'est une nouvelle entr├®e : ajouter ├á la fin du tableau JSON.

```bash
git add .claude/installed-repos.json
git commit -m "feat: [github-watch] registre mis ├á jour ÔÇö [repo]"
```

## Expected Output

```
Installation depuis [repo] :
Ô£ô Skills install├®s  : [N] ([liste])
Ô£ô Agents install├®s  : [N]
Ô£ô Commands install├®es: [N]
Ô£ô V├®rification OK   : exhaustivit├® confirm├®e
Ô£ô Registre mis ├á jour : .claude/installed-repos.json
ÔÜá Conflits ignor├®s  : [N] fichiers d├®j├á pr├®sents (liste compl├¿te ci-dessus)
```

## R├¿gles

- Copie toujours r├®cursive (find), jamais de glob plat `*.md` niveau racine seulement
- Un sous-dossier existant localement n'est PAS un conflit ÔÇö fusionner fichier par fichier
- V├®rification d'exhaustivit├® OBLIGATOIRE avant rm -rf
- Ne jamais ├®craser un fichier existant
- Toujours nettoyer `/tmp/` apr├¿s v├®rification
- Commits group├®s par cat├®gorie (skills / agents / commands / registre)
- Toujours mettre ├á jour le registre apr├¿s installation
- Si le d├®p├┤t n'a pas de dossier `.claude/`, signaler et arr├¬ter proprement
