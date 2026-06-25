---
name: plan
description: Structured planning before implementing a feature. Produces scope, steps, risks, and open questions. Use before any non-trivial feature implementation.
allowed-tools: Read, Glob, Grep
---

# Plan Skill

## When to Use
Before implementing any feature that touches more than 2 files or requires a design decision.

## Output Structure

```markdown
## Plan — [Feature Name]

### Scope
- What this covers
- What this explicitly excludes

### Steps
1. [concrete step]
2. [concrete step]
...

### Files Affected
- `path/to/file.ts` — [what changes]

### Risks
- [risk] → [mitigation]

### Open Questions
- [question that needs answer before starting]

### Definition of Done
- [ ] [testable criterion]
```

## Rules
- Read relevant existing code before planning
- No step should be "implement X" — break down to actual edits
- Flag any step that requires user decision before proceeding
- Keep plans under 30 lines — if longer, split into sub-plans
