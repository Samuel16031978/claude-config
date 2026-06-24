---
name: gsd:autonomous
description: Run all remaining phases autonomously ÔÇö discussÔåÆplanÔåÆexecute per phase
argument-hint: "[--from N] [--to N] [--only N] [--interactive]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
  - Agent
requires: [cleanup, phase, progress]
---
<objective>
Execute all remaining milestone phases autonomously. For each phase: discuss ÔåÆ plan ÔåÆ execute. Pauses only for user decisions (grey area acceptance, blockers, validation requests).

Uses ROADMAP.md phase discovery and Skill() flat invocations for each phase command. After all phases complete: milestone audit ÔåÆ complete ÔåÆ cleanup.

**Creates/Updates:**
- `.planning/STATE.md` ÔÇö updated after each phase
- `.planning/ROADMAP.md` ÔÇö progress updated after each phase
- Phase artifacts ÔÇö CONTEXT.md, PLANs, SUMMARYs per phase

**After:** Milestone is complete and cleaned up.
</objective>

<execution_context>
@~/.claude/get-shit-done/workflows/autonomous.md
@~/.claude/get-shit-done/references/ui-brand.md
</execution_context>

<context>
Optional flags:
- `--from N` ÔÇö start from phase N instead of the first incomplete phase.
- `--to N` ÔÇö stop after phase N completes (halt instead of advancing to next phase).
- `--only N` ÔÇö execute only phase N (single-phase mode).
- `--interactive` ÔÇö run discuss inline with questions (not auto-answered), then dispatch planÔåÆexecute as background agents. Keeps the main context lean while preserving user input on decisions.

Project context, phase list, and state are resolved inside the workflow using init commands (`gsd-tools query init.milestone-op`, `gsd-tools query roadmap.analyze`). No upfront context loading needed.
</context>

<process>
Execute end-to-end.
Preserve all workflow gates (phase discovery, per-phase execution, blocker handling, progress display).
</process>
