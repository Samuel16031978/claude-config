#!/usr/bin/env bash
# R├®installation reproductible des skills paperasse + restauration de la config soci├®t├®.
# L'environnement Claude Code distant est ├®ph├®m├¿re : relancer ce script restaure tout.
#
# Usage : bash paperasse-config/install.sh
set -euo pipefail

REPO_URL="https://github.com/romainsimon/paperasse"
PAPERASSE_DIR="$HOME/.claude/paperasse"
SKILLS_DIR="$HOME/.claude/skills"
CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_COMPANY="sc-renovations-sarl"   # soci├®t├® active par d├®faut

SKILLS=(comptable controleur-fiscal commissaire-aux-comptes notaire syndic fiscaliste)

echo "==> Clonage de paperasse (git clone : pr├®serve les symlinks internes)"
rm -rf "$PAPERASSE_DIR"
git clone --depth 1 "$REPO_URL" "$PAPERASSE_DIR"

echo "==> Installation des 6 skills (symlinks de premier niveau)"
mkdir -p "$SKILLS_DIR"
for s in "${SKILLS[@]}"; do
  if [ ! -f "$PAPERASSE_DIR/$s/SKILL.md" ]; then
    echo "ATTENTION : $s/SKILL.md introuvable, ignor├®" >&2; continue
  fi
  rm -rf "${SKILLS_DIR:?}/$s"
  ln -s "../paperasse/$s" "$SKILLS_DIR/$s"
  echo "   - $s"
done

echo "==> Restauration de la config des 3 soci├®t├®s"
mkdir -p "$PAPERASSE_DIR/companies/sc-renovations-sarl" \
         "$PAPERASSE_DIR/companies/holding-sasu" \
         "$PAPERASSE_DIR/companies/sci"
cp "$CONFIG_DIR/companies/sc-renovations-sarl.json" "$PAPERASSE_DIR/companies/sc-renovations-sarl/company.json"
cp "$CONFIG_DIR/companies/holding-sasu.json"        "$PAPERASSE_DIR/companies/holding-sasu/company.json"
cp "$CONFIG_DIR/companies/sci.json"                 "$PAPERASSE_DIR/companies/sci/company.json"

echo "==> Soci├®t├® active par d├®faut : $DEFAULT_COMPANY"
ln -sfn "companies/$DEFAULT_COMPANY/company.json" "$PAPERASSE_DIR/company.json"

echo "==> V├®rification des symlinks internes (ressources partag├®es)"
for l in comptable/data comptable/scripts comptable/templates comptable/integrations; do
  [ -e "$PAPERASSE_DIR/$l" ] && echo "   OK  $l" || { echo "   CASS├ë $l" >&2; exit 1; }
done

echo ""
echo "Termin├®. Pensez ├á : cp paperasse-config/.env.example ~/.claude/paperasse/.env  puis renseigner les cl├®s API si besoin."
