---
name: gsd:new-milestone
description: Start a new milestone cycle ÔÇö update PROJECT.md and route to requirements
argument-hint: "[milestone name, e.g., 'v1.1 Notifications']"
allowed-tools:
  - Read
  - Write
  - Bash
  - Agent
  - AskUserQuestion
requires: [new-project, phase, plan-phase]
---
<objective>
Start a new milestone: questioning ÔåÆ research (optional) ÔåÆ requirements ÔåÆ roadmap.

Brownfield equivalent of new-project. Project exists, PROJECT.md has history. Gathers "what's next", updates PROJECT.md, then runs requirements ÔåÆ roadmap cycle.

**Creates/Updates:**
- `.planning/PROJECT.md` ÔÇö updated with new milestone goals
- `.planning/research/` ÔÇö domain research (optional, NEW features only)
- `.planning/REQUIREMENTS.md` ÔÇö scoped requirements for this milestone
- `.planning/ROADMAP.md` ÔÇö phase structure (continues numbering)
- `.planning/STATE.md` ÔÇö reset for new milestone

**After:** `/gsd:plan-phase [N]` to start execution.
</objective>

<execution_context>
@~/.claude/get-shit-done/workflows/new-milestone.md
@~/.claude/get-shit-done/references/questioning.md
@~/.claude/get-shit-done/references/ui-brand.md
@~/.claude/get-shit-done/templates/project.md
@~/.claude/get-shit-done/templates/requirements.md
</execution_context>

<context>
Milestone name: $ARGUMENTS (optional - will prompt if not provided)

Project and milestone context files are resolved inside the workflow (`init new-milestone`) and delegated via `<files_to_read>` blocks where subagents are used.
</context>

<process>
Execute end-to-end.
Preserve all workflow gates (validation, questioning, research, requirements, roadmap approval, commits).
</process>
