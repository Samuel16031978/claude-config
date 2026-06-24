# Changelog ÔÇö README CONCEPTS Section

Tracks drift between the README CONCEPTS table and official Claude Code documentation.

## Status Legend

| Status | Meaning |
|--------|---------|
| Ô£à `COMPLETE (reason)` | Action was taken and resolved successfully |
| ÔØî `INVALID (reason)` | Finding was incorrect, not applicable, or intentional |
| Ô£ï `ON HOLD (reason)` | Action deferred ÔÇö waiting on external dependency or user decision |

---

## [2026-03-02 11:14 AM PKT] Claude Code v2.1.63

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Broken URL | Fix Permissions URL from `/iam` to `/permissions` | Ô£à COMPLETE (URL updated to /permissions) |
| 2 | HIGH | Missing Concept | Add Agent Teams row to CONCEPTS table | Ô£à COMPLETE (row added with ~\/\.claude\/teams\/ location) |
| 3 | HIGH | Missing Concept | Add Keybindings row to CONCEPTS table | Ô£à COMPLETE (row added with ~\/\.claude\/keybindings\.json location) |
| 4 | HIGH | Missing Concept | Add Model Configuration row to CONCEPTS table | Ô£à COMPLETE (row added with \.claude\/settings\.json location) |
| 5 | HIGH | Missing Concept | Add Auto Memory row to CONCEPTS table | Ô£à COMPLETE (row added with ~\/\.claude\/projects\/<project>\/memory\/ location) |
| 6 | HIGH | Stale Anchor | Fix Rules URL anchor from `#modular-rules-with-clauderules` to `#organize-rules-with-clauderules` | Ô£à COMPLETE (anchor updated) |
| 7 | MED | Missing Concept | Add Checkpointing row to CONCEPTS table | Ô£à COMPLETE (row added with automatic git-based location) |
| 8 | MED | Missing Concept | Add Status Line row to CONCEPTS table | Ô£à COMPLETE (row added with ~\/\.claude\/settings\.json location) |
| 9 | MED | Missing Concept | Add Remote Control row to CONCEPTS table | Ô£à COMPLETE (row added with CLI \/ claude\.ai location) |
| 10 | MED | Missing Concept | Add Fast Mode row to CONCEPTS table | Ô£à COMPLETE (row added with \.claude\/settings\.json location) |
| 11 | MED | Missing Concept | Add Headless Mode row to CONCEPTS table | Ô£à COMPLETE (row added with CLI flag -p location) |
| 12 | LOW | Changed Description | Update Memory description to mention auto memory | Ô£à COMPLETE (description and location updated) |
| 13 | LOW | Changed Location | Update MCP Servers location to include `.mcp.json` | Ô£à COMPLETE (location updated to include .mcp.json) |
| 14 | LOW | Missing Badge | Add Implemented badge to Hooks row | Ô£à COMPLETE (Implemented badge added linking to .claude/hooks/) |

---

## [2026-03-02 11:57 AM PKT] Claude Code v2.1.63

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Table Consolidation | Consolidate CONCEPTS table from 22 rows to 10 rows ÔÇö fold related concepts as inline doc links | Ô£à COMPLETE (22 ÔåÆ 10 rows) |
| 2 | MED | Merged Concept | Fold Marketplaces into Plugins row as inline link | Ô£à COMPLETE (linked to /discover-plugins) |
| 3 | MED | Merged Concept | Fold Agent Teams into Sub-Agents row as inline link | Ô£à COMPLETE (linked to /agent-teams) |
| 4 | MED | Merged Concept | Fold Permissions, Model Config, Output Styles, Sandboxing, Keybindings, Status Line, Fast Mode into Settings row as inline links | Ô£à COMPLETE (7 concepts folded with doc links) |
| 5 | MED | Merged Concept | Fold Auto Memory and Rules into Memory row as inline links | Ô£à COMPLETE (linked to /memory and /memory#organize-rules-with-clauderules) |
| 6 | MED | Merged Concept | Fold Headless Mode into Remote Control row as inline link | Ô£à COMPLETE (linked to /headless) |
| 7 | LOW | Reorder | Reorder table by logical grouping: building blocks ÔåÆ extension ÔåÆ config ÔåÆ context ÔåÆ runtime | Ô£à COMPLETE (grouped by concern, not chronology) |

---

## [2026-03-07 08:40 AM PKT] Claude Code v2.1.71

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Broken URL | Fix `context-management` ÔåÆ `interactive-mode` in TIPS (lines 112, 115, 135) | Ô£à COMPLETE (3 occurrences replaced with interactive-mode) |
| 2 | HIGH | Broken URL | Fix `model-configuration` ÔåÆ `model-config` in TIPS (lines 115, 116, 135) | Ô£à COMPLETE (3 occurrences replaced with model-config) |
| 3 | HIGH | Broken URL | Fix `usage-billing` ÔåÆ `costs` in TIPS (line 115) | Ô£à COMPLETE (replaced with costs) |
| 4 | HIGH | Broken URL | Remove `cowork` URL in STARTUPS (line 167) ÔÇö page does not exist | Ô£à COMPLETE (hyperlink removed, plain text kept) |
| 5 | HIGH | Missing Concept | Add Scheduled Tasks row to CONCEPTS and Hot section (`/loop`, cron tools) | Ô£à COMPLETE (added by user to both tables + /loop tip + Boris tweet) |
| 6 | MED | Changed Location | Update Agent Teams location from `.claude/agents/<name>.md` to `built-in (env var)` | Ô£à COMPLETE (location updated to built-in env var) |

---

## [2026-03-10 01:18 PM PKT] Claude Code v2.1.72

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Broken URL | Fix Commands URL from `/slash-commands` to `/skills` in CONCEPTS table (line 24) ÔÇö `/slash-commands` serves Skills page content; docs say "commands merged into skills" | ÔØî INVALID (URL still resolves; user chose to keep as-is) |
| 2 | HIGH | Broken URL | Fix Commands URL from `/slash-commands` to `/skills` in TIPS section (line 108) ÔÇö same stale URL | ÔØî INVALID (URL still resolves; user chose to keep as-is) |
| 3 | MED | Missing Inline Link | Add Interactive Mode (`/interactive-mode`) as inline link to CLI Startup Flags row ÔÇö covers /compact, /clear, /context, /extra-usage | Ô£à COMPLETE (inline link added to CLI Startup Flags description) |
| 4 | MED | Missing Inline Link | Add Costs (`/costs`) as inline link to Settings row ÔÇö covers /usage, billing, pay-as-you-go | ÔØî INVALID (user chose to skip) |
| 5 | LOW | Missing Concept | Consider adding IDE Integrations row (VS Code, JetBrains, Desktop App, Web) or inline links to Best Practices | ÔØî INVALID (user chose to skip ÔÇö platform surfaces, not configuration concepts) |
| 6 | HIGH | Missing Concept | Add Code Review row to Hot table ÔÇö multi-agent PR analysis (research preview, Teams & Enterprise) | Ô£à COMPLETE (row added as first Hot entry with blog link and best practice tweet) |
| 7 | MED | New Badge | Create `!/tags/beta.svg` tag (yellow, 38x20px) and add to Code Review and Agent Teams in Hot table | Ô£à COMPLETE (beta.svg created; added to Code Review and Agent Teams rows) |
| 8 | MED | Reorder | Sort Hot table by release date (most recent first): Code Review ÔåÆ Scheduled Tasks ÔåÆ Voice Mode ÔåÆ Agent Teams ÔåÆ Remote Control ÔåÆ Git Worktrees ÔåÆ Ralph Wiggum | Ô£à COMPLETE (Voice Mode and Agent Teams swapped to match chronological order) |

---

## [2026-03-12 12:22 PM PKT] Claude Code v2.1.74

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Broken URL | Fix Commands URL from `/slash-commands` to `/skills` in CONCEPTS table (line 24) ÔÇö `/slash-commands` redirects to `/skills` page | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | LOW | Verification | All external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all 20+ URLs return valid pages) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` validated on target page | Ô£à COMPLETE (heading exists on /memory page) |
| 5 | LOW | Verification | All CONCEPTS descriptions checked against official docs | Ô£à COMPLETE (no description drift detected) |

---

## [2026-03-15 12:48 PM PKT] Claude Code v2.1.76

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | MED | Missing Badges | Remote Control (Hot) has zero badges ÔÇö only Hot item without any BP or Impl badge | Ô£à COMPLETE (BP badge added linking to official docs page) |
| 3 | LOW | Naming | "Sub-Agents" in README vs "subagents" (one word) in official docs ÔÇö cosmetic inconsistency | Ô£à COMPLETE (renamed to "Subagents" in CONCEPTS table) |
| 4 | LOW | Verification | All 27 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (descriptions accurate for all 13 CONCEPTS + 9 Hot rows) |

---

## [2026-03-17 12:46 PM PKT] Claude Code v2.1.77

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | HIGH | Changed Description | Hooks description says "Deterministic scripts" but hooks now include 4 types: command, HTTP, prompt, and agent ÔÇö only command hooks are deterministic | Ô£à COMPLETE (updated to "User-defined handlers (scripts, HTTP, prompts, agents)" in CONCEPTS table) |
| 3 | MED | Missing Concept | Desktop App has dedicated docs page at `/desktop` ÔÇö not in CONCEPTS or Hot table | ÔØî INVALID (user chose to skip ÔÇö Desktop is a platform surface, not a configuration concept) |
| 4 | MED | Changed URL | Hooks docs now split into Guide (`/hooks-guide`) and Reference (`/hooks`) ÔÇö CONCEPTS links only to Reference | Ô£à COMPLETE (Guide link added as inline link in Hooks row description) |
| 5 | LOW | Verification | All 28 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 6 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20 badge targets exist on filesystem) |
| 7 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs | Ô£à COMPLETE (Hooks description drift detected ÔÇö see #2) |

---

## [2026-03-18 11:43 PM PKT] Claude Code v2.1.78

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | HIGH | Changed URL+Name | Voice Mode in Hot table links to tweet instead of official docs `/voice-dictation`; official name is "Voice Dictation" | Ô£à COMPLETE (renamed to "Voice Dictation", linked to /voice-dictation, description updated; BP badge kept linking to tweet; also updated in STARTUPS table) |
| 3 | LOW | Verification | All 29 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 4 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 5 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-19 11:59 AM PKT] Claude Code v2.1.79

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | LOW | Verification | All 30 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 5 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-20 08:38 AM PKT] Claude Code v2.1.80

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Missing Concept | Add Channels row to Hot table ÔÇö push events from Telegram/Discord/webhooks into running sessions (research preview, v2.1.80) | Ô£à COMPLETE (row added as first Hot entry with beta badge and Reference link) |
| 2 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 3 | MED | Missing Deep Link | Git Worktrees URL should anchor to `#run-parallel-claude-code-sessions-with-git-worktrees` | Ô£à COMPLETE (anchor added to Git Worktrees URL in Hot table) |
| 4 | LOW | Missing Inline Link | Plugins row could add `[Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)` sub-link | Ô£à COMPLETE (Create Marketplaces inline link added to Plugins row) |
| 5 | LOW | Verification | All 31 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 6 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 7 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-21 09:12 PM PKT] Claude Code v2.1.81

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | LOW | Verification | All 32 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-23 09:53 PM PKT] Claude Code v2.1.81

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | LOW | Verification | All 33 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-25 08:12 PM PKT] Claude Code v2.1.83

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | MED | Changed URL | Simplify & Batch primary link points to tweet instead of official docs `/skills#bundled-skills` ÔÇö now officially bundled skills | Ô£à COMPLETE (primary link updated to /skills#bundled-skills; BP badge kept linking to Boris's tweet) |
| 3 | LOW | Verification | All 34 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 4 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 5 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |
| 8 | HIGH | Missing Concept | Add Auto Mode row to Hot table ÔÇö background safety classifier replaces permission prompts (research preview, Team/Enterprise) | Ô£à COMPLETE (row added as first Hot entry with beta badge, BP badge linking to @claudeai tweet, and blog link) |

---

## [2026-03-26 01:05 PM PKT] Claude Code v2.1.84

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | MED | Missing Concept | Add Slack integration to Hot table ÔÇö mention @Claude in Slack to route coding tasks to Claude Code web sessions | Ô£à COMPLETE (row added after Channels with @Claude location and web session description) |
| 3 | MED | Missing Concept | Add GitHub Actions / CI-CD to Hot table ÔÇö automate PR reviews, issue triage, and code generation in CI/CD pipelines | Ô£à COMPLETE (row added after Code Review with .github/workflows/ location and GitLab CI/CD inline link) |
| 4 | LOW | Verification | All 35 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-27 06:37 PM PKT] Claude Code v2.1.85

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | MED | Missing Concept | Add Chrome integration to Hot table ÔÇö browser automation via Claude in Chrome extension (beta, dedicated docs at `/chrome`) | Ô£à COMPLETE (row added after GitHub Actions with --chrome location and beta badge) |
| 3 | LOW | Verification | All 36 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 4 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 5 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-03-28 06:04 PM PKT] Claude Code v2.1.86

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | MED | Missing Badge | Chrome row in Hot table has no BP badge ÔÇö report exists at `reports/claude-in-chrome-v-chrome-devtools-mcp.md` | Ô£à COMPLETE (BP badge added linking to reports/claude-in-chrome-v-chrome-devtools-mcp.md) |
| 3 | LOW | Changed Description | Plugins description missing LSP servers ÔÇö official docs list `.lsp.json` as plugin component | Ô£à COMPLETE (added "and LSP servers" to Plugins description) |
| 4 | LOW | Verification | All 37 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading `.claude/rules/` exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate except Plugins LSP note ÔÇö see #3) |

---

## [2026-04-01 12:33 PM PKT] Claude Code v2.1.89

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Missing Concept | Add Computer Use row to Hot table ÔÇö screen control on macOS via built-in MCP server (research preview, v2.1.85+) | Ô£à COMPLETE (row added after Fullscreen Rendering with beta badge and Desktop inline link) |
| 2 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 3 | MED | Missing Concept | Add Fullscreen Rendering row to Hot table ÔÇö flicker-free alt-screen rendering with mouse support (research preview, v2.1.88+) | Ô£à COMPLETE (row added as first Hot entry with CLAUDE_CODE_NO_FLICKER=1 location) |
| 4 | LOW | Verification | All 38 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-02 09:17 PM PKT] Claude Code v2.1.90

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` serves Skills page ÔÇö docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves; user chose to keep as-is) |
| 2 | LOW | Verification | All 39 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-03 08:35 PM PKT] Claude Code v2.1.91

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (llms.txt) ÔÇö redirects to `/skills` page; docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 2 | LOW | Verification | All 40 external docs URLs validated against llms.txt sitemap (80 pages) ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (17 local targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-04 10:46 PM PKT] Claude Code v2.1.92

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Missing Concept | Add Ultraplan row to Hot table ÔÇö cloud-based plan drafting with browser review, inline comments, and flexible execution (`/ultraplan`) | Ô£à COMPLETE (row added after Power-ups with beta badge and /ultraplan location) |
| 2 | HIGH | Missing Concept | Add Claude Code Web row to Hot table ÔÇö run tasks on cloud infrastructure at claude.ai/code with PR auto-fix and parallel sessions | Ô£à COMPLETE (row added after Ultraplan with beta badge, claude.ai/code location, and Web Scheduled Tasks inline link) |
| 3 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills` page; docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 4 | MED | Missing Concept | Add Desktop App row to Hot table ÔÇö standalone app with visual diff, Dispatch, computer use, and parallel sessions | ÔØî INVALID (RECURRING from 2026-03-17; user considers it a platform surface, not a configuration concept) |

---

## [2026-04-08 09:37 PM PKT] Claude Code v2.1.96

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills` page; docs say "commands merged into skills" | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 2 | MED | Changed Name | "No Flicker Mode" in Hot table ÔÇö official docs page title is "Fullscreen rendering"; consider renaming or adding subtitle | ÔØî INVALID (user chose to keep "No Flicker Mode" per Boris's tweet naming convention; env var is `CLAUDE_CODE_NO_FLICKER`) |
| 3 | MED | Missing Concept | Add Desktop App row to Hot table ÔÇö standalone app with visual diff, Dispatch, computer use, and parallel sessions | ÔØî INVALID (RECURRING from 2026-03-17; user considers it a platform surface, not a configuration concept) |
| 4 | LOW | Verification | All 41 external docs URLs validated ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files | Ô£à COMPLETE (all 20+ badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-09 11:37 PM PKT] Claude Code v2.1.97

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Missing Concept | Add Agent SDK row to Hot table ÔÇö build production AI agents with Python/TypeScript SDKs (29 docs pages, `/en/agent-sdk/overview`) | Ô£à COMPLETE (row added after Claude Code Web with Quickstart and Examples inline links) |
| 2 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills`; canonical commands reference is now `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 3 | MED | Missing Inline Link | Add Environment Variables (`/env-vars`) inline link to CLI Startup Flags row ÔÇö new dedicated docs page | Ô£à COMPLETE (Env Vars inline link added after Interactive Mode) |
| 4 | LOW | Verification | All 42 external docs URLs validated against llms.txt sitemap (110 pages) ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (20+ badge targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-11 06:13 PM PKT] Claude Code v2.1.101

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (110 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 2 | LOW | Verification | All 43 external docs URLs validated against llms.txt sitemap (110 pages) ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (20+ badge targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-13 08:07 PM PKT] Claude Code v2.1.101

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (110 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 2 | LOW | Verification | All 44 external docs URLs validated against llms.txt sitemap (110 pages) ÔÇö no broken links found | Ô£à COMPLETE (all URLs return valid pages including /slash-commands redirect) |
| 3 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (20+ badge targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 4 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 5 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 6 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 7 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-14 11:17 PM PKT] Claude Code v2.1.107

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Missing Concept | Add Routines row to Hot table ÔÇö cloud automation on Anthropic infrastructure with schedule, API, and GitHub event triggers (`/en/routines`) | Ô£à COMPLETE (row added after Scheduled Tasks with beta badge, Desktop Tasks inline link) |
| 2 | HIGH | Stale URL | Update `web-scheduled-tasks` inline link in Claude Code Web row (line 45) to `/en/routines` ÔÇö URL not in sitemap, redirects to Routines page | Ô£à COMPLETE (inline link text changed to "Routines", URL updated to /routines) |
| 3 | HIGH | Stale URL | Update `web-scheduled-tasks` inline link in Scheduled Tasks row (line 55) to `/en/routines` ÔÇö same stale URL | Ô£à COMPLETE (URL updated to /routines) |
| 4 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (119 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 5 | MED | Changed Description | Update Scheduled Tasks description from "up to 3 days" to "up to 7 days" ÔÇö docs now specify seven-day expiry for recurring tasks | Ô£à COMPLETE (description updated to "up to 7 days") |
| 6 | MED | Missing Concept | Add Devcontainers row to Hot table ÔÇö preconfigured dev containers with security isolation and firewall rules (`/en/devcontainer`) | Ô£à COMPLETE (row added after Routines with .devcontainer/ location) |

---

## [2026-04-16 08:20 PM PKT] Claude Code v2.1.110

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Fix `web-scheduled-tasks` URL in TIPS (line 223) to `/en/routines` ÔÇö URL not in sitemap; same stale URL fixed in Hot table on 2026-04-14 but TIPS instance was missed | Ô£à COMPLETE (URL updated to /routines) |
| 2 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (111 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user chose to keep as-is) |
| 3 | MED | Changed Description | Update "up to 3 days" to "up to 7 days" in TIPS (line 223) ÔÇö same description updated in Hot table on 2026-04-14 but TIPS instance was missed | Ô£à COMPLETE (description updated to "up to 7 days") |
| 4 | LOW | Verification | All 45 external docs URLs validated against llms.txt sitemap (111 pages) ÔÇö 1 broken link found (see #1) | Ô£à COMPLETE (web-scheduled-tasks flagged) |
| 5 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (20+ badge targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 6 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 7 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 8 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 9 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 10 | LOW | Verification | All CONCEPTS descriptions checked against official docs ÔÇö no drift detected | Ô£à COMPLETE (all descriptions accurate) |

---

## [2026-04-18 07:53 PM PKT] Claude Code v2.1.113

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Changed Description | Auto Mode row (line 48) still references `claude --enable-auto-mode` ÔÇö flag removed in v2.1.111; auto mode now starts via `--permission-mode auto` or Shift+Tab cycle (Max subscribers default with Opus 4.7) | Ô£à COMPLETE (location updated to `--permission-mode auto`, `Shift+Tab`; description notes flag removal and Max+Opus-4.7 default) |
| 2 | HIGH | Missing Concept | Add Ultrareview row to Hot table ÔÇö cloud-based multi-agent code review (`/ultrareview`, v2.1.86+, dedicated docs at `/en/ultrareview`); free 3 runs for Pro/Max | Ô£à COMPLETE (row added after Routines with beta badge, /ultrareview location, Tasks-tracking inline link) |
| 3 | HIGH | Missing Concept | Add Tasks row ÔÇö `/tasks` command for tracking background work (referenced on Ultrareview page); replaces TodoWrite per `reports/claude-global-vs-project-settings.md` | Ô£à COMPLETE (row added after Scheduled Tasks with /tasks location, BP badge linking to global-vs-project-settings report) |
| 4 | MED | Changed Description | No Flicker Mode row (line 47) ÔÇö official docs now lead with `/tui fullscreen` command (v2.1.110); env var is the pre-v2.1.110 legacy path per /fullscreen page | Ô£à COMPLETE (location updated to `/tui fullscreen`, `CLAUDE_CODE_NO_FLICKER=1`; description notes /tui as canonical, env var as legacy) |
| 5 | MED | Stale Command Name | TIPS line 249 references `/fewer-permission-prompts` ÔÇö official skill name is `/less-permission-prompts` per v2.1.111 changelog (local skill folder is `fewer-permission-prompts` but the user-visible command should match the official name) | Ô£à COMPLETE (TIPS line 249 updated to /less-permission-prompts) |
| 6 | LOW | Changed Description | Scheduled Tasks row (line 60) ÔÇö Week 15 added Monitor tool + self-pacing `/loop` (LLM picks its own interval); description doesn't mention this | Ô£à COMPLETE (description appended with self-pacing/Monitor tool note) |
| 7 | LOW | Changed Description | Git Worktrees row (line 63) ÔÇö v2.1.105/106 added `EnterWorktree`/`ExitWorktree` tools and `isolation: "worktree"` subagent frontmatter; description doesn't mention these | Ô£à COMPLETE (location updated to include EnterWorktree/ExitWorktree and isolation frontmatter; description notes v2.1.106+ subagent worktree support) |
| 8 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (119 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 17+ runs) |
| 9 | LOW | Verification | All 45+ external docs URLs validated against llms.txt sitemap (119 pages) ÔÇö no NEW broken links found beyond the recurring `/slash-commands` redirect | Ô£à COMPLETE (all flagged URLs return valid pages) |
| 10 | LOW | Verification | All local badge file paths validated ÔÇö no missing files (20+ badge targets checked) | Ô£à COMPLETE (all badge targets exist on filesystem) |
| 11 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on /memory page | Ô£à COMPLETE (section heading "Organize rules with `.claude/rules/`" exists) |
| 12 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on /common-workflows page | Ô£à COMPLETE (section heading exists) |
| 13 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on /permission-modes page | Ô£à COMPLETE (section heading exists) |
| 14 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on /skills page | Ô£à COMPLETE (section heading exists) |
| 15 | LOW | Verification | Fullscreen page confirms `/tui fullscreen` is canonical command and `tui` is settings field (v2.1.110) | Ô£à COMPLETE (page fetched and quoted) |
| 16 | LOW | Verification | Permission-modes page confirms `--enable-auto-mode` flag is no longer documented; auto mode now requires Max plan + Opus 4.7 | Ô£à COMPLETE (page fetched; flag absent from docs) |
| 17 | LOW | Verification | Ultrareview page exists at `/en/ultrareview` (v2.1.86+), confirms `/ultrareview` and `/tasks` commands | Ô£à COMPLETE (page fetched and content captured) |

---

## [2026-04-24 12:32 AM PKT] Claude Code v2.1.118

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Changed Description | Hooks row (line 28) lists 4 handler types ("scripts, HTTP, prompts, agents") ÔÇö official `/en/hooks` page now documents 5 types with `mcp_tool` added (v2.1.118 changelog: "Hooks can invoke MCP tools directly" via `type: "mcp_tool"`) | Ô£à COMPLETE (description updated to "scripts, HTTP, MCP tools, prompts, agents") |
| 2 | MED | Empty Description | Workflows row (line 27) description cell is empty (only Orchestration Workflow badge) ÔÇö official `/en/common-workflows` page covers step-by-step guides for exploring, fixing, refactoring, testing | Ô£à COMPLETE (description filled with official-docs-sourced text: "Step-by-step guides for exploring codebases, fixing bugs, refactoring, and testing ÔÇö orchestration patterns for multi-step tasks") |
| 3 | LOW | Changed Description | Consider mentioning `/usage` (v2.1.118 merged `/cost`+`/stats`) inline in CLI Startup Flags row ÔÇö new slash command replacing two legacy ones | Ô£à COMPLETE (inline note "`/usage` (merged `/cost`+`/stats` in v2.1.118)" appended after Env Vars) |
| 4 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (117 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 18+ runs) |
| 5 | LOW | Verification | Hooks page `/en/hooks` fetched ÔÇö confirmed 5 handler types including `mcp_tool` (v2.1.118) | Ô£à COMPLETE (live fetch documented 5-type schema) |
| 6 | LOW | Verification | Ultrareview page `/en/ultrareview#track-a-running-review` anchor fetched and confirmed | Ô£à COMPLETE (section exists, describes `/tasks` integration) |
| 7 | LOW | Verification | Checkpointing page `/en/checkpointing` fetched ÔÇö `/undo` alias (v2.1.108) NOT surfaced in docs, only in changelog; no CONCEPTS update required | Ô£à COMPLETE (docs page content matches existing description) |
| 8 | LOW | Verification | All local badge file paths ÔÇö no changes since v2.1.113 run on 2026-04-18 | Ô£à COMPLETE (stable since prior run) |
| 9 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` ÔÇö not re-checked this run; stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 10 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 11 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 12 | LOW | Verification | Bundled Skills anchor `#bundled-skills` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 13 | LOW | Verification | claude-code-guide agent cross-check ÔÇö no contradictions with dedicated agent; surfaced /recap (v2.1.108), /usage (v2.1.118), MCP-tool hooks (v2.1.118) as corroborating evidence | Ô£à COMPLETE (both agents aligned) |

---

## [2026-04-26 01:10 PM PKT] Claude Code v2.1.119

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (139 pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 19+ runs) |
| 2 | HIGH | Wrong Target URL | Tasks row (line 62) primary URL points to `/ultrareview#track-a-running-review` ÔÇö anchor is valid but target is the ultrareview tracking section, not the broader Tasks system; canonical home is the local report `reports/claude-global-vs-project-settings.md#tasks-system` | Ô£à COMPLETE (primary URL updated to `reports/claude-global-vs-project-settings.md#tasks-system`; ultrareview tracking anchor preserved as inline link "Ultrareview tracking" at end of description) |
| 3 | MED | Beta Badge Currency | Routines / No Flicker Mode / Computer Use / Code Review have `![beta]` in README but their docs pages no longer mark them as beta ÔÇö re-evaluate and demote where appropriate | ÔØî INVALID (verification fetched all 4 docs pages ÔÇö Routines: "in research preview"; Fullscreen: "research preview"; Computer Use: "research preview on macOS"; Code Review: "in research preview" ÔÇö README beta badges are accurate; the agent's 0.6-confidence read of body content was contradicted by `<Note>` banner text) |
| 4 | MED | Description Disambiguation | Scheduled Tasks row (line 61) description conflates `/loop` (local, session-scoped, 7-day expiry) and `/schedule` (cloud Routines on Anthropic infrastructure) ÔÇö official `/en/scheduled-tasks` page now formally distinguishes Cloud / Desktop / Loop as three surfaces | Ô£à COMPLETE (description now explicitly names "Three surfaces" with `/loop` local, `/schedule` cloud Routines, and Desktop scheduled tasks called out separately) |
| 5 | LOW | Missing Concept (optional) | Fast Mode is currently only a side-link inside Settings (line 31) ÔÇö has its own dedicated `/en/fast-mode` page with `Ôå»` indicator and `/fast` toggle (v2.1.36+); could be a Hot row | Ô£à COMPLETE (Hot row inserted between Power-ups and Computer Use with beta badge; removed redundant Fast Mode side-link from Settings to prevent duplication) |
| 6 | LOW | Missing Inline Link | Memory row could surface `reports/claude-agent-memory.md` as an inline link ÔÇö auto-memory is referenced but the local deep-dive isn't linked from CONCEPTS | Ô£à COMPLETE ("Auto Memory Deep-dive" inline link added between Auto Memory docs and Rules in the Memory row) |
| 7 | LOW | Missing Inline Link | Skills row could surface `reports/claude-skills-for-larger-mono-repos.md` as an inline link ÔÇö exists locally but only referenced from TIPS | Ô£à COMPLETE ("Skills for Mono-repos" inline link appended after Official Skills in the Skills row) |
| 8 | LOW | Optional Concept | Vim visual mode (v2.1.118), Theme Customization (`~/.claude/themes/`, v2.1.118), and PowerShell tool (v2.1.111) could be Settings side-links ÔÇö minor concepts surfaced by claude-code-guide cross-check | ÔØî INVALID (Vim mode is covered by existing Keybindings side-link; Themes have no dedicated docs page distinct from Settings; PowerShell tool has no dedicated docs page ÔÇö no concrete sub-link target warrants addition) |
| 9 | LOW | Verification | All 35+ external CONCEPTS docs URLs validated against llms.txt sitemap (139 pages) ÔÇö only the recurring `/slash-commands` redirect flagged; all other URLs resolve to expected pages | Ô£à COMPLETE (no NEW broken URLs) |
| 10 | LOW | Verification | All local badge file paths validated ÔÇö all 20+ `best-practice/`, `implementation/`, and `reports/` targets exist on filesystem | Ô£à COMPLETE (no missing local files) |
| 11 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` confirmed on `/en/memory` page | Ô£à COMPLETE (stable since v2.1.113) |
| 12 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` confirmed on `/en/common-workflows` page | Ô£à COMPLETE (stable) |
| 13 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` confirmed on `/en/permission-modes` page | Ô£à COMPLETE (stable) |
| 14 | LOW | Verification | Bundled Skills anchor `#bundled-skills` confirmed on `/en/skills` page | Ô£à COMPLETE (stable) |
| 15 | LOW | Verification | Ultrareview anchor `#track-a-running-review` confirmed on `/en/ultrareview` page | Ô£à COMPLETE (stable since v2.1.118) |
| 16 | LOW | Verification | claude-code-guide cross-check ÔÇö corroborated dedicated agent's findings on Vim mode (v2.1.118), Theme (v2.1.118), Effort xhigh (v2.1.111+ Opus 4.7), Worktrees (v2.1.105+); no contradictions | Ô£à COMPLETE (both agents aligned) |
| 17 | LOW | Verification Checklist Update | Added new rule (#7) "Beta Badge Currency" to verification-checklist.md ÔÇö covers re-evaluating beta badges against upstream docs page lifecycle | Ô£à COMPLETE (rule added) |

---

## [2026-04-29 12:53 AM PKT] Claude Code v2.1.121

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap (139+ pages) ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 20+ runs) |
| 2 | MED | Changed Description | Ultrareview row (line 44) doesn't mention `claude ultrareview [target]` non-interactive subcommand introduced in v2.1.120 ÔÇö docs confirm `--json` and `--timeout` flags for CI usage | Ô£à COMPLETE (location updated to include `claude ultrareview [target]`; description appends non-interactive subcommand with `--json` and `--timeout` flags note, v2.1.120+) |
| 3 | MED | Changed Description | MCP Servers row (line 29) doesn't mention `alwaysLoad` setting added in v2.1.121 ÔÇö bypasses tool-search deferral so a server's tools are always loaded into context | Ô£à COMPLETE (description appended with `alwaysLoad` note explaining tool-search deferral bypass, v2.1.121+) |
| 4 | MED | Changed Description | Hooks row (line 28) doesn't mention `updatedToolOutput` capability added in v2.1.121 ÔÇö PostToolUse hooks can now replace tool output via `hookSpecificOutput.updatedToolOutput` | Ô£à COMPLETE (description appended with `hookSpecificOutput.updatedToolOutput` note for PostToolUse output replacement, v2.1.121+) |
| 5 | LOW | Changed Description | Subagents row (line 24) doesn't mention forked subagents now available on external builds via `CLAUDE_CODE_FORK_SUBAGENT=1` (v2.1.117) ÔÇö was previously internal-only | Ô£à COMPLETE (description appended with `CLAUDE_CODE_FORK_SUBAGENT=1` note for external builds, v2.1.117+) |
| 6 | LOW | Missing Inline Link | Settings row (line 31) inline links cover Permissions/Model Config/Output Styles/Sandboxing/Keybindings but not Auto Mode Config (`/auto-mode-config`) ÔÇö exists as standalone page | Ô£à COMPLETE (Auto Mode Config inline link appended after Keybindings) |
| 7 | LOW | Verification | All 35+ external CONCEPTS docs URLs spot-validated ÔÇö Subagents, Skills, MCP, Ultrareview pages confirmed; only the recurring `/slash-commands` redirect flagged | Ô£à COMPLETE (no NEW broken URLs) |
| 8 | LOW | Verification | All local badge file paths validated ÔÇö all 22 `best-practice/`, `implementation/`, `reports/`, `.claude/`, `CLAUDE.md` targets exist on filesystem | Ô£à COMPLETE (no missing local files) |
| 9 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` ÔÇö stable since v2.1.113 (not re-fetched this run) | Ô£à COMPLETE (stable) |
| 10 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 11 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 12 | LOW | Verification | Bundled Skills anchor `#bundled-skills` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 13 | LOW | Verification | Ultrareview anchor `#track-a-running-review` confirmed on `/en/ultrareview` page ÔÇö section exists and describes `/tasks` integration | Ô£à COMPLETE (stable since v2.1.118) |
| 14 | LOW | Verification | claude-code-guide cross-check ÔÇö corroborated dedicated agent's findings on v2.1.117ÔÇôv2.1.121 changes (forked subagents external, alwaysLoad, updatedToolOutput, claude ultrareview subcommand); also surfaced Bedrock/Vertex/Foundry, Desktop, IDE Integrations as long-standing missing concepts | Ô£à COMPLETE (both agents aligned; all "missing platform surfaces" already INVALID per recurring user decision) |

---

## [2026-05-01 03:34 PM PKT] Claude Code v2.1.126

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale Version | README badge pinned at v2.1.121 (Apr 29) ÔÇö latest is v2.1.126 (May 01); 5 versions behind | Ô£à COMPLETE (badge bumped to v2.1.126 May 01 2026 3:34 PM PKT) |
| 2 | MED | New Concept (optional) | v2.1.126 introduced `claude project purge [path]` subcommand with `--dry-run`/`--all` flags ÔÇö currently absent from CLI Startup Flags row; could be inline note | Ô£ï ON HOLD (deferred ÔÇö single-version-old subcommand; revisit if user requests CLI Startup Flags refresh) |
| 3 | MED | New Concept (optional) | v2.1.126 added gateway-driven model picker ÔÇö `/model` lists models from `ANTHROPIC_BASE_URL`'s `/v1/models` endpoint when gateway is Anthropic-compatible | Ô£ï ON HOLD (deferred ÔÇö niche LLM-gateway feature; only relevant for self-hosted-gateway users; not surfaced in CONCEPTS by design) |
| 4 | LOW | Changed Description (optional) | v2.1.122 expanded `--from-pr` to accept GitLab MR + Bitbucket PR + GitHub Enterprise PR URLs (originally GitHub only) ÔÇö CLI Startup Flags row doesn't surface this | Ô£ï ON HOLD (deferred ÔÇö `--from-pr` not currently surfaced as inline link; would require new sub-link addition) |
| 5 | HIGH | Stale URL | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 21+ runs) |
| 6 | MED | Missing Concept (recurring) | Dedicated agent re-flagged Output Styles, Permissions, Sandboxing, Headless Mode, Desktop App, IDE Integration as missing standalone rows | ÔØî INVALID (RECURRING from 2026-03-10/2026-03-17/2026-04-08/2026-04-09; user considers all six platform surfaces or covered as Settings sub-links ÔÇö not standalone concepts) |
| 7 | MED | Missing Concept (recurring) | Dedicated agent flagged Auto Memory needs its own row separate from Memory | ÔØî INVALID (RECURRING ÔÇö current Memory row already surfaces both `/en/memory#auto-memory` and `reports/claude-agent-memory.md` as inline links; user's chosen pattern for cross-cutting feature) |
| 8 | LOW | Stale Finding | Dedicated agent flagged Tasks row primary URL needs `/en/agent-sdk/todo-tracking` cross-reference | ÔØî INVALID (already RESOLVED on 2026-04-26 ÔÇö user explicitly moved Tasks primary URL to `reports/claude-global-vs-project-settings.md#tasks-system` and kept ultrareview tracking as inline link; agent's analysis is stale) |
| 9 | LOW | Verification | All 23 local badge file paths validated ÔÇö `best-practice/`, `implementation/`, `reports/`, `.claude/`, `.mcp.json`, `CLAUDE.md` all exist | Ô£à COMPLETE (no missing local files) |
| 10 | LOW | Verification | Spot-validated external CONCEPTS URLs (`/en/cli-reference`, `/en/agent-teams`, `/en/changelog`, `/en/mcp`) ÔÇö all return valid pages | Ô£à COMPLETE (no NEW broken URLs) |
| 11 | LOW | Verification | Beta badge currency (rule #7) ÔÇö fetched `/en/agent-teams` and confirmed `<Warning>` banner: "Agent teams are experimental and disabled by default" ÔÇö README beta badge accurate | Ô£à COMPLETE (no demotions warranted) |
| 12 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 13 | LOW | Verification | Git Worktrees anchor `#run-parallel-claude-code-sessions-with-git-worktrees` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 14 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 15 | LOW | Verification | Bundled Skills anchor `#bundled-skills` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 16 | LOW | Verification | Ultrareview anchor `#track-a-running-review` ÔÇö stable since v2.1.118 | Ô£à COMPLETE (stable) |
| 17 | LOW | Verification | claude-code-guide cross-check ÔÇö independent research surfaced same v2.1.122ÔÇô126 changes (`claude project purge`, gateway model picker, `--from-pr` expansion); also re-surfaced long-standing platform-surface concepts (Desktop, IDE Integration, Bedrock/Vertex/Foundry) which are RECURRING INVALID per user policy; no contradictions | Ô£à COMPLETE (both agents aligned) |

---

## [2026-05-12 11:36 PM PKT] Claude Code v2.1.139

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Stale Version | README badge pinned at v2.1.128 (May 08) ÔÇö latest is v2.1.139 (May 11); 11 versions behind | Ô£à COMPLETE (badge bumped to v2.1.139 May 12 2026 11:36 PM PKT in Phase 2.6) |
| 2 | HIGH | Stale URL/Anchor (NEW) | Git Worktrees row primary URL points to `/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees` ÔÇö but a dedicated `/en/worktrees` page now exists (covers `--worktree`/`-w` flag, `.worktreeinclude`, WorktreeCreate/Remove hooks, non-git VCS) AND the legacy common-workflows anchor has been renamed to `#run-parallel-sessions-with-worktrees` (word "git" dropped). Both verified live | Ô£à COMPLETE (URL switched to `/en/worktrees` dedicated page; Location column expanded with `--worktree`/`-w`, `.worktreeinclude`, `WorktreeCreate`/`WorktreeRemove` hooks per user authorization) |
| 3 | HIGH | Missing Concept (NEW) | v2.1.139 introduced **Agent View** (`claude agents`, `--bg`, `/bg`) ÔÇö research preview "one screen for many background sessions" with peek/attach/dispatch. Dedicated docs page `/en/agent-view` confirmed live | Ô£à COMPLETE (Hot row added after Agent Teams with `![beta]` badge per `<Note>` "research preview" banner; description notes supervisor hosting and reboot persistence) |
| 4 | HIGH | Missing Concept (NEW) | v2.1.139 introduced **/goal** command ÔÇö keep Claude working across turns until a model-evaluated condition holds (session-scoped Stop hook wrapper). Dedicated docs page `/en/goal` confirmed live | Ô£à COMPLETE (Hot row added after Tasks; description compares to `/loop` and auto mode per docs framing) |
| 5 | MED | Missing Concept (NEW) | **Deep Links** (`claude-cli://open?repo=ÔÇª&q=ÔÇª`) introduced v2.1.91 ÔÇö custom URL scheme for runbooks/alerts/dashboards. Dedicated docs page `/en/deep-links` confirmed live; never surfaced in CONCEPTS across any prior run | Ô£à COMPLETE (Hot row added after Remote Control ÔÇö both are session-launching surfaces; description mentions runbooks/alerts/dashboards use cases and OS-level handler registration) |
| 6 | LOW | Missing Concept (NEW) | v2.1.139 added `/scroll-speed` command ÔÇö tunes mouse wheel scroll speed with live preview | Ô£ï ON HOLD (deferred ÔÇö minor UX command, no dedicated docs page; would only fit as a CLI Startup Flags sub-link if at all) |
| 7 | HIGH | Stale URL (recurring) | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 22+ runs) |
| 8 | MED | Missing Concept (recurring) | Dedicated agent re-flagged Output Styles, Permissions, Sandboxing, Headless Mode, Desktop App, IDE Integration, .claude Directory, Tools Reference as missing standalone rows | ÔØî INVALID (RECURRING from 2026-03-10/2026-03-17/2026-04-08/2026-04-09/2026-05-01; user considers all platform surfaces or covered as Settings sub-links ÔÇö not standalone concepts) |
| 9 | MED | Missing Concept (recurring) | Dedicated agent flagged Auto Memory needs its own row separate from Memory | ÔØî INVALID (RECURRING ÔÇö current Memory row already surfaces both `/en/memory#auto-memory` and `reports/claude-agent-memory.md` as inline links; user's chosen pattern) |
| 10 | LOW | Verification | All 4 NEW candidate URLs validated via WebFetch: `/en/worktrees` (live, full dedicated page), `/en/agent-view` (live, research preview banner), `/en/goal` (live, /goal command page), `/en/deep-links` (live, v2.1.91+ banner) | Ô£à COMPLETE (all 4 NEW URLs return expected canonical pages) |
| 11 | LOW | Verification | Local badge file paths validated ÔÇö `best-practice/`, `implementation/`, `reports/`, `.claude/`, `.mcp.json`, `CLAUDE.md` targets exist on filesystem | Ô£à COMPLETE (no missing local files) |
| 12 | LOW | Verification | Beta Badge Currency (rule #7) ÔÇö fetched `/en/agent-view` and confirmed `<Note>` banner: "Agent view is a research preview and requires Claude Code v2.1.139 or later" ÔÇö if added, a beta badge would be accurate | Ô£à COMPLETE (badge recommendation noted for action item #3) |
| 13 | LOW | Verification | Memory anchor `#organize-rules-with-clauderules` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 14 | LOW | Verification | Git Worktrees anchor ÔÇö heading renamed in `/en/common-workflows` from `#run-parallel-claude-code-sessions-with-git-worktrees` to `#run-parallel-sessions-with-worktrees` (word "git" dropped); legacy anchor still resolves but is no longer canonical | ÔÜá´©Å FLAGGED (captured under action item #2; treated as part of the stale URL action, not a separate item) |
| 15 | LOW | Verification | Auto Mode anchor `#eliminate-prompts-with-auto-mode` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 16 | LOW | Verification | Bundled Skills anchor `#bundled-skills` ÔÇö stable since v2.1.113 | Ô£à COMPLETE (stable) |
| 17 | LOW | Verification | Ultrareview anchor `#track-a-running-review` ÔÇö stable since v2.1.118 | Ô£à COMPLETE (stable) |
| 18 | LOW | Verification | claude-code-guide cross-check ÔÇö independent research corroborated v2.1.139 additions (Agent View, /goal, /scroll-speed) and surfaced same Deep Links page; also re-surfaced long-standing platform-surface concepts (Desktop, IDE Integration, .claude Directory, Tools Reference) which are RECURRING INVALID per user policy; no contradictions | Ô£à COMPLETE (both agents aligned on NEW v2.1.139 findings) |

---

## [2026-05-21 12:07 AM PKT] Claude Code v2.1.145

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Wrong Location (NEW) | Checkpointing row (line 36) Location reads `automatic (git-based)` ÔÇö factually wrong. Live `/en/checkpointing` fetch confirms checkpoints track "all changes made by its file editing tools", explicitly "do not track files modified by bash commands", and are "Not a replacement for version control" ÔÇö *"Think of checkpoints as 'local undo' and Git as 'permanent history'."* The 2026-04-24 run only checked the (empty) Description column, never the Location, so this slipped through every prior run. Recommend `automatic (file-edit tracking)` | Ô£à COMPLETE (user authorized; line 36 Location updated `automatic (git-based)` ÔåÆ `automatic (file-edit tracking)`) |
| 2 | MED | Missing Concept (NEW) | **Sessions** has a dedicated `/en/sessions` page (resume, `/rename`, fork/branch via `--fork-session`) never surfaced in CONCEPTS across any prior run; concepts-agent flagged at 0.6 confidence as possibly a runtime surface rather than an authoring concept | ÔØî INVALID (user chose to skip ÔÇö consistent with the standing "platform/runtime surface, not configuration concept" rejection pattern) |
| 3 | HIGH | Stale URL (recurring) | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 23+ runs) |
| 4 | MED | Missing Concept (recurring) | Dedicated + claude-code-guide agents re-flagged IDE Integration, Desktop App, Output Styles, Permissions, Sandboxing, Headless Mode, .claude Directory, Tools Reference as missing standalone rows | ÔØî INVALID (RECURRING from 2026-03-10/2026-03-17/2026-04-08/2026-05-01/2026-05-12; user considers all platform surfaces or covered as Settings/Memory sub-links ÔÇö not standalone concepts) |
| 5 | LOW | Verification | Fast Mode URL `/en/fast-mode` fetched live ÔÇö page valid ("Speed up responses with fast mode"), research preview, `/fast` toggle + `"fastMode": true` setting, Opus 4.7 default since v2.1.142; resolves concepts-agent's 0.5-confidence doubt ÔÇö README Fast Mode row (line 52) is fully accurate | Ô£à COMPLETE (row confirmed accurate, no change needed) |
| 6 | LOW | Verification | Latest version confirmed v2.1.145 via raw CHANGELOG.md (blob URL returns no body ÔÇö used raw.githubusercontent.com per the documented workaround); v2.1.145 adds JSON session listing + OTEL agent identity ÔÇö nothing CONCEPTS-worthy | Ô£à COMPLETE (version verified; badge bumped v2.1.144 ÔåÆ v2.1.145 in Phase 2.6) |
| 7 | LOW | Verification | External CONCEPTS docs URLs spot-validated (`/en/checkpointing`, `/en/fast-mode`, CHANGELOG raw) + remainder stable since v2.1.139 run ÔÇö only the recurring `/slash-commands` redirect flagged | Ô£à COMPLETE (no NEW broken URLs) |
| 8 | LOW | Verification | Local badge file paths ÔÇö no CONCEPTS table structural changes since v2.1.139; `best-practice/`, `implementation/`, `reports/`, `.claude/`, `.mcp.json`, `CLAUDE.md` targets stable | Ô£à COMPLETE (stable since prior run) |
| 9 | LOW | Verification | Beta Badge Currency (rule #7) ÔÇö `/en/fast-mode` confirms "research preview" `<Note>` banner; README `![beta]` on Fast Mode accurate | Ô£à COMPLETE (no demotions warranted) |
| 10 | LOW | Verification | Anchors (`#organize-rules-with-clauderules`, `#run-parallel-...-worktrees`, `#eliminate-prompts-with-auto-mode`, `#bundled-skills`, `#track-a-running-review`) ÔÇö stable since v2.1.113/v2.1.139 | Ô£à COMPLETE (stable) |
| 11 | LOW | Verification | claude-code-guide cross-check ÔÇö independent 80-concept sweep corroborated coverage; surfaced Auto Dream + MCP Tool Search as possible Memory/MCP sub-links and re-surfaced platform surfaces (RECURRING INVALID). Its version numbers were unreliable (e.g. "MCP introduced Dec 2024", fuzzy v-numbers) ÔÇö deferred to dedicated agent + live fetches for all dates; no contradictions affecting CONCEPTS | Ô£à COMPLETE (agents aligned; guide's fuzzy versioning noted, not used) |

---

## [2026-05-25 04:27 PM PKT] Claude Code v2.1.150

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Wrong Location (NEW) | Simplify & Batch row (line 70) Location `/simplify`, `/batch` and the row name are stale ÔÇö `/simplify` was **renamed to `/code-review`** in v2.1.147. Triple-confirmed: CHANGELOG *"Renamed `/simplify` to `/code-review`ÔÇª pass `--comment` to post findings as inline GitHub PR comments"*; `/en/skills` bundled-skills list now reads `/code-review, /batch, /debug, /loop, /claude-api` (no `/simplify`); `/en/code-review` docs note *"The command was named `/simplify` before v2.1.147."* Naming collision with existing cloud Code Review row (line 59) ÔÇö fix approach needs user choice | Ô£à COMPLETE (user chose "Bundled Skills" rename; row 70 renamed `Simplify & Batch` ÔåÆ `Bundled Skills`, Location `/simplify`, `/batch` ÔåÆ `/code-review`, `/batch`; avoids collision since row is really the bundled-skills concept) |
| 2 | LOW | Optional Inline Link (NEW) | Code Review row (line 59, cloud GitHub App) could add inline link to the local `/code-review` command (`/en/commands`) ÔÇö docs now formally cross-reference the local "twin" of the cloud feature | Ô£à COMPLETE (user approved; `[Local /code-review](https://code.claude.com/docs/en/commands)` inline link appended to Code Review row line 59) |
| 3 | HIGH | Stale URL (recurring) | Commands URL `/slash-commands` not in official sitemap ÔÇö redirects to `/skills`; canonical commands reference is `/en/commands` | ÔØî INVALID (RECURRING from 2026-03-10; URL still resolves via redirect; user has chosen to keep as-is across 24+ runs) |
| 4 | MED | Missing Concept (recurring) | Dedicated + claude-code-guide agents re-flagged Sessions, IDE Integration, Desktop App, Output Styles, Permissions, Sandboxing, Headless Mode, Context Window as missing standalone rows | ÔØî INVALID (RECURRING from 2026-03-10/2026-03-17/2026-04-08/2026-05-01/2026-05-12/2026-05-21; user considers all platform/runtime surfaces or covered as Settings/Memory sub-links ÔÇö not standalone concepts) |
| 5 | LOW | Beta Badge Currency (rule #7) | Re-evaluated beta badges against upstream lifecycle ÔÇö `/en/code-review` `<Note>`: "Code Review is in research preview"; `/en/channels` requires v2.1.80+ research preview; `/en/fast-mode` research preview (Opus 4.7 default since v2.1.142) | Ô£à COMPLETE (all README beta badges accurate; no demotions warranted) |
| 6 | LOW | Verification | Latest version confirmed v2.1.150 via raw CHANGELOG.md (blob URL returns no body ÔÇö used raw.githubusercontent.com per documented workaround). v2.1.146ÔÇô150 add `/usage` per-category breakdown (2.1.149), GFM task-list checkboxes (2.1.149), `worktree.bgIsolation` (2.1.143), Fast Mode Opus 4.7 default (2.1.142) ÔÇö nothing new CONCEPTS-worthy beyond #1 | Ô£à COMPLETE (version verified; badge bumped v2.1.145 ÔåÆ v2.1.150 in Phase 2.6) |
| 7 | LOW | Verification | All 22 local badge/link target files validated via filesystem check (`best-practice/`, `implementation/`, `reports/`, `.claude/`, `.mcp.json`, `CLAUDE.md`, `orchestration-workflow/`) ÔÇö all exist | Ô£à COMPLETE (no missing local files) |
| 8 | LOW | Verification | External CONCEPTS URLs spot-validated live: `/en/skills` (bundled-skills section present), `/en/code-review` (research preview, disambiguates cloud vs local), CHANGELOG raw; remainder stable since v2.1.145 run ÔÇö only recurring `/slash-commands` redirect flagged | Ô£à COMPLETE (no NEW broken URLs) |
| 9 | LOW | Verification Checklist Update | Added rule #9 "Bundled Skill / Command Rename Tracking" ÔÇö scan CHANGELOG (last N versions) + `/en/commands` + `/skills#bundled-skills` for command/skill renames or removals affecting Location-column command names | Ô£à COMPLETE (rule added; origin: `/simplify`ÔåÆ`/code-review` rename was changelog-only, missed by docs-page-listing checks) |
| 10 | LOW | Verification | Anchors stable since v2.1.113/v2.1.139 (`#organize-rules-with-clauderules`, `#run-parallel-...-worktrees`, `#eliminate-prompts-with-auto-mode`, `#bundled-skills`, `#track-a-running-review`) | Ô£à COMPLETE (stable) |
| 11 | LOW | Verification | claude-code-guide cross-check ÔÇö independent 95-concept sweep corroborated coverage but **missed the `/simplify`ÔåÆ`/code-review` rename** (changelog-only event invisible to docs-page listing; dedicated agent caught it via raw CHANGELOG); re-surfaced platform surfaces (RECURRING INVALID); version numbers fuzzy, deferred to live CHANGELOG | Ô£à COMPLETE (agents aligned on coverage; rename gap noted) |
