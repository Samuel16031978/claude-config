---
name: gsd:ai-integration-phase
description: Generate an AI-SPEC.md design contract for phases that involve building AI systems.
argument-hint: "[phase number]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - AskUserQuestion
  - mcp__context7__*
requires: [phase]
---
<objective>
Create an AI design contract (AI-SPEC.md) for a phase involving AI system development.
Orchestrates gsd-framework-selector ÔåÆ gsd-ai-researcher ÔåÆ gsd-domain-researcher ÔåÆ gsd-eval-planner.
Flow: Select Framework ÔåÆ Research Docs ÔåÆ Research Domain ÔåÆ Design Eval Strategy ÔåÆ Done
</objective>

<execution_context>
@~/.claude/get-shit-done/workflows/ai-integration-phase.md
@~/.claude/get-shit-done/references/ai-frameworks.md
@~/.claude/get-shit-done/references/ai-evals.md
</execution_context>

<context>
Phase number: $ARGUMENTS ÔÇö optional, auto-detects next unplanned phase if omitted.
</context>

<process>
Execute end-to-end.
Preserve all workflow gates.
</process>
