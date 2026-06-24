---
name: gsd:review
description: Request cross-AI peer review of phase plans from external AI CLIs
argument-hint: "--phase N [--gemini] [--claude] [--codex] [--opencode] [--qwen] [--cursor] [--all]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
requires: [config, phase, plan-phase]
---

<objective>
Invoke external AI CLIs (Gemini, Claude, Codex, OpenCode, Qwen Code, Cursor) to independently review phase plans.
Produces a structured REVIEWS.md with per-reviewer feedback that can be fed back into
planning via /gsd:plan-phase --reviews.

**Flow:** Detect CLIs ÔåÆ Build review prompt ÔåÆ Invoke each CLI ÔåÆ Collect responses ÔåÆ Write REVIEWS.md
</objective>

<execution_context>
@~/.claude/get-shit-done/workflows/review.md
</execution_context>

<context>
Phase number: extracted from $ARGUMENTS (required)

**Flags:**
- `--gemini` ÔÇö Include Gemini CLI review
- `--claude` ÔÇö Include Claude CLI review (uses separate session)
- `--codex` ÔÇö Include Codex CLI review
- `--opencode` ÔÇö Include OpenCode review (uses model from user's OpenCode config)
- `--qwen` ÔÇö Include Qwen Code review (Alibaba Qwen models)
- `--cursor` ÔÇö Include Cursor agent review
- `--all` ÔÇö Include all available CLIs
</context>

<process>
Execute end-to-end.
</process>
