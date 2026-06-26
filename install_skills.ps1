# Met a jour et installe les skills perso de Samuel dans Claude Code (~/.claude/skills).
# Usage : depuis la racine du repo claude-config, lancer  .\install_skills.ps1
# Pur PowerShell, aucune dependance Python. Pas de symlink (copie) => pas besoin d'admin.
$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $repo "claude-global\skills\samuel"
$dst  = Join-Path $HOME ".claude\skills"

Write-Host "git pull origin main..." -ForegroundColor Cyan
git -C $repo pull --ff-only origin main

New-Item -ItemType Directory -Force -Path $dst | Out-Null
$count = 0
Get-ChildItem $src -Directory | ForEach-Object {
    Copy-Item -Recurse -Force $_.FullName $dst
    $count++
}
Write-Host "$count skills installes vers $dst" -ForegroundColor Green
