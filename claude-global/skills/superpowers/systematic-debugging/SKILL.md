---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue: test failures, bugs in production, unexpected behavior, performance problems, build failures, integration issues.

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully** ÔÇö don't skip past errors, read stack traces completely
2. **Reproduce Consistently** ÔÇö can you trigger it reliably? If not reproducible ÔåÆ gather more data, don't guess
3. **Check Recent Changes** ÔÇö git diff, recent commits, new dependencies, config changes
4. **Gather Evidence in Multi-Component Systems**

   For EACH component boundary:
   - Log what data enters component
   - Log what data exits component
   - Verify environment/config propagation
   - Check state at each layer

   Run once to gather evidence showing WHERE it breaks, THEN analyze.

5. **Trace Data Flow** ÔÇö where does bad value originate? Keep tracing up until you find the source.

### Phase 2: Pattern Analysis

1. Find working examples ÔÇö locate similar working code in same codebase
2. Compare against references ÔÇö read reference implementation COMPLETELY
3. Identify differences ÔÇö list every difference, however small
4. Understand dependencies ÔÇö what other components does this need?

### Phase 3: Hypothesis and Testing

1. Form single hypothesis: "I think X is the root cause because Y"
2. Test minimally ÔÇö make the SMALLEST possible change
3. Verify before continuing ÔÇö did it work? No ÔåÆ form NEW hypothesis
4. When you don't know ÔÇö say "I don't understand X", ask for help

### Phase 4: Implementation

1. Create failing test case first
2. Implement single fix addressing the root cause
3. Verify fix ÔÇö tests pass? No other tests broken?
4. If fix doesn't work ÔÇö STOP. Count attempts. If ÔëÑ 3: question the architecture.

**If 3+ Fixes Failed: Question Architecture**

Pattern indicating architectural problem:
- Each fix reveals new shared state/coupling in different place
- Fixes require "massive refactoring"
- Each fix creates new symptoms elsewhere

STOP and discuss with your human partner before attempting more fixes.

## Red Flags ÔÇö STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "It's probably X, let me fix that"
- "Here are the main problems: [lists fixes without investigation]"
- "One more fix attempt" (when already tried 2+)

**ALL of these mean: STOP. Return to Phase 1.**

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. |
| "Emergency, no time for process" | Systematic debugging is FASTER than thrashing. |
| "I see the problem, let me fix it" | Seeing symptoms Ôëá understanding root cause. |
| "One more fix attempt" (after 2+) | 3+ failures = architectural problem. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare | Identify differences |
| **3. Hypothesis** | Form theory, test minimally | Confirmed or new hypothesis |
| **4. Implementation** | Create test, fix, verify | Bug resolved, tests pass |

**Related skills:**
- **superpowers:test-driven-development** ÔÇö for creating failing test case (Phase 4)
- **superpowers:verification-before-completion** ÔÇö verify fix worked before claiming success
