#!/usr/bin/env python3
"""Sync des skills perso de Samuel : GitHub = source de verite, Claude Code + Claude AI = consommateurs.

Detecte les skills modifies (hash de contenu vs manifeste versionne), construit des bundles .zip
prets a importer dans claude.ai, et met a jour le manifeste. Aucun secret, aucune API externe.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills" / "samuel"
MANIFEST_PATH = SKILLS_DIR / ".sync-manifest.json"
DIST_DIR = ROOT / "dist" / "skills"
CLAUDE_SKILLS_DIR = Path.home() / ".claude" / "skills"
SKILL_FILE = "SKILL.md"


def iter_skill_dirs() -> list[Path]:
    return sorted(
        p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / SKILL_FILE).exists()
    )


def skill_hash(skill_dir: Path) -> str:
    digest = hashlib.sha256()
    for file in sorted(skill_dir.rglob("*")):
        if file.is_file():
            digest.update(file.relative_to(skill_dir).as_posix().encode())
            digest.update(file.read_bytes())
    return digest.hexdigest()


def current_state() -> dict[str, str]:
    return {d.name: skill_hash(d) for d in iter_skill_dirs()}


def load_manifest() -> dict[str, str]:
    if not MANIFEST_PATH.exists():
        return {}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("skills", {})


def changed_skills(state: dict[str, str], manifest: dict[str, str]) -> list[str]:
    return sorted(name for name, value in state.items() if manifest.get(name) != value)


def cmd_status(_: argparse.Namespace) -> int:
    state = current_state()
    manifest = load_manifest()
    changed = set(changed_skills(state, manifest))
    removed = sorted(name for name in manifest if name not in state)
    print(f"Skills perso : {len(state)} | source : claude-global/skills/samuel/")
    for name in sorted(state):
        flag = "MODIFIE" if name in changed else "a jour"
        print(f"  [{flag:8}] {name}")
    for name in removed:
        print(f"  [SUPPRIME] {name}")
    if changed:
        print(f"\n{len(changed)} skill(s) a re-importer dans claude.ai : {', '.join(sorted(changed))}")
    else:
        print("\nClaude AI est synchro avec GitHub.")
    return 0


def _zip_skill(skill_dir: Path, out_path: Path) -> None:
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(skill_dir.rglob("*")):
            if file.is_file():
                archive.write(file, Path(skill_dir.name) / file.relative_to(skill_dir))


def cmd_bundle(args: argparse.Namespace) -> int:
    state = current_state()
    targets = sorted(state) if args.all else changed_skills(state, load_manifest())
    if not targets:
        print("Rien a empaqueter (aucun changement). Utilise --all pour tout reconstruire.")
        return 0
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for name in targets:
        _zip_skill(SKILLS_DIR / name, DIST_DIR / f"{name}.zip")
        print(f"  bundle -> dist/skills/{name}.zip")
    return 0


def cmd_commit_manifest(_: argparse.Namespace) -> int:
    payload = {"skills": current_state()}
    body = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    MANIFEST_PATH.write_text(body + "\n", encoding="utf-8")
    print(f"Manifeste mis a jour : {len(payload['skills'])} skills.")
    return 0


def _install_one(link: Path, source: Path, copy: bool) -> str:
    if link.is_symlink():
        link.unlink()
    if copy:
        shutil.copytree(source, link, dirs_exist_ok=True)
        return "copié"
    if link.is_dir():
        return "ignoré (dossier réel)"
    if link.exists():
        link.unlink()
    link.symlink_to(source.resolve(), target_is_directory=True)
    return "lié"


def cmd_install(args: argparse.Namespace) -> int:
    use_copy = args.copy or os.name == "nt"
    target_root = Path(args.target).expanduser() if args.target else CLAUDE_SKILLS_DIR
    target_root.mkdir(parents=True, exist_ok=True)
    skills = iter_skill_dirs()
    for skill_dir in skills:
        state = _install_one(target_root / skill_dir.name, skill_dir, use_copy)
        print(f"  {state:22} {skill_dir.name}")
    mode = "copie" if use_copy else "symlink"
    print(f"\n{len(skills)} skills installés vers {target_root} ({mode}).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sync des skills perso entre GitHub, Claude Code et Claude AI."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="liste les skills et detecte les modifs vs manifeste").set_defaults(
        func=cmd_status
    )
    bundle = sub.add_parser("bundle", help="construit les .zip a importer dans claude.ai")
    bundle.add_argument("--all", action="store_true", help="empaquette tous les skills, pas seulement les modifies")
    bundle.set_defaults(func=cmd_bundle)
    sub.add_parser("commit-manifest", help="ecrit le manifeste avec l'etat courant").set_defaults(
        func=cmd_commit_manifest
    )
    install = sub.add_parser("install", help="lie (ou copie) les skills vers ~/.claude/skills pour Claude Code")
    install.add_argument("--copy", action="store_true", help="copie au lieu de symlink (a relancer apres chaque git pull)")
    install.add_argument("--target", help="dossier cible (defaut ~/.claude/skills)")
    install.set_defaults(func=cmd_install)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
