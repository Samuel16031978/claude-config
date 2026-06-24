---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
---

# Subagent-Driven Development

Execute plan by dispatching fresh subagent per task, with two-stage review after each: spec compliance review first, then code quality review.

**Why subagents:** Fresh subagent per task prevents context pollution. You construct exactly what they need ÔÇö they never inherit your session's history.

**Core principle:** "Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration"

**Continuous execution:** Do not pause to check in with your human partner between tasks. Execute all tasks from the plan without stopping. The only reasons to stop are: BLOCKED status you cannot resolve, ambiguity that genuinely prevents progress, or all tasks complete.

## When to Use

**Use this (same session) when:**
- You have an implementation plan
- Tasks are mostly independent
- You want to stay in the current session

**Use executing-plans (parallel session) when:**
- You need to hand off to a separate session

## The Process

1. Read plan, extract all tasks with full context, create TodoWrite
2. For each task:
   - Dispatch implementer subagent with full task text + context
   - Handle questions if implementer asks (answer before proceeding)
   - Dispatch spec compliance reviewer subagent
   - If issues: implementer fixes, re-review until Ô£à
   - Dispatch code quality reviewer subagent
   - If issues: implementer fixes, re-review until Ô£à
   - Mark task complete in TodoWrite
3. After all tasks: dispatch final code reviewer for entire implementation
4. Use superpowers:finishing-a-development-branch

## Model Selection

- Mechanical tasks (1-2 files, clear spec) ÔåÆ fast, cheap model
- Integration tasks (multi-file, coordination) ÔåÆ standard model
- Architecture, design, review ÔåÆ most capable model

## Handling Implementer Status

- **DONE:** Proceed to spec compliance review
- **DONE_WITH_CONCERNS:** Read concerns, address if blocking correctness
- **NEEDS_CONTEXT:** Provide missing context and re-dispatch
- **BLOCKED:** Assess root cause ÔÇö context problem / reasoning need / task too large / plan error. Never retry same model without changes.

## Red Flags

**Never:**
- Start implementation on main/master without explicit user consent
- Skip reviews (spec compliance OR code quality)
- Proceed with unfixed issues
- Dispatch multiple implementation subagents in parallel (conflicts)
- Make subagent read plan file (provide full text instead)
- Skip spec compliance before code quality review
- Move to next task while either review has open issues

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** ÔÇö isolated workspace
- **superpowers:writing-plans** ÔÇö creates the plan this skill executes
- **superpowers:requesting-code-review** ÔÇö code review templates
- **superpowers:finishing-a-development-branch** ÔÇö complete after all tasks
