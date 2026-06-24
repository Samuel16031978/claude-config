---
name: gsd:new-project
description: Initialize a new project with deep context gathering and PROJECT.md
argument-hint: "[--auto]"
allowed-tools:
  - Read
  - Bash
  - Write
  - Agent
  - AskUserQuestion
requires: [config, phase, plan-phase]
---
<runtime_note>
**Copilot (VS Code):** Use `vscode_askquestions` wherever this workflow calls `AskUserQuestion`. They are equivalent ÔÇö `vscode_askquestions` is the VS Code Copilot implementation of the same interactive question API.
</runtime_note>

<context>
**Flags:**
- `--auto` ÔÇö Automatic mode. After config questions, runs research ÔåÆ requirements ÔåÆ roadmap without further interaction. Expects idea document via @ reference.
</context>

<objective>
Initialize a new project through unified flow: questioning ÔåÆ research (optional) ÔåÆ requirements ÔåÆ roadmap.

**Creates:**
- `.planning/PROJECT.md` ÔÇö project context
- `.planning/config.json` ÔÇö workflow preferences
- `.planning/research/` ÔÇö domain research (optional)
- `.planning/REQUIREMENTS.md` ÔÇö scoped requirements
- `.planning/ROADMAP.md` ÔÇö phase structure
- `.planning/STATE.md` ÔÇö project memory

**After this command:** Run `/gsd:plan-phase 1` to start execution.
</objective>

<execution_context>
@~/.claude/get-shit-done/workflows/new-project.md
@~/.claude/get-shit-done/references/questioning.md
@~/.claude/get-shit-done/references/ui-brand.md
@~/.claude/get-shit-done/templates/project.md
@~/.claude/get-shit-done/templates/requirements.md
</execution_context>

<process>
Execute end-to-end.
Preserve all workflow gates (validation, approvals, commits, routing).
</process>
