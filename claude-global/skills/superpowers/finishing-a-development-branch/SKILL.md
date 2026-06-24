---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
---

# Finishing a Development Branch

## Overview

Guide completion of development work by presenting clear options and handling chosen workflow.

**Core principle:** Verify tests ÔåÆ Detect environment ÔåÆ Present options ÔåÆ Execute choice ÔåÆ Clean up.

**Announce at start:** "I'm using the finishing-a-development-branch skill to complete this work."

## The Process

### Step 1: Verify Tests

```bash
npm test / cargo test / pytest / go test ./...
```

If tests fail: stop, show failures, cannot proceed until tests pass.

### Step 2: Detect Environment

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
```

| State | Menu | Cleanup |
|-------|------|---------|
| `GIT_DIR == GIT_COMMON` (normal repo) | Standard 4 options | No worktree to clean up |
| `GIT_DIR != GIT_COMMON`, named branch | Standard 4 options | Provenance-based |
| `GIT_DIR != GIT_COMMON`, detached HEAD | Reduced 3 options (no merge) | No cleanup (externally managed) |

### Step 3: Determine Base Branch

```bash
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

### Step 4: Present Options

**Normal repo / named-branch worktree ÔÇö exactly 4 options:**

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

**Detached HEAD ÔÇö exactly 3 options:**

```
Implementation complete. You're on a detached HEAD.

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)
3. Discard this work

Which option?
```

Don't add explanation ÔÇö keep options concise.

### Step 5: Execute Choice

**Option 1: Merge Locally**
```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
git checkout <base-branch>
git pull
git merge <feature-branch>
# Verify tests on merged result
# Cleanup worktree, then delete branch
git branch -d <feature-branch>
```

**Option 2: Push and Create PR**
```bash
git push -u origin <feature-branch>
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets>

## Test Plan
- [ ] <verification steps>
EOF
)"
```
Do NOT clean up worktree ÔÇö user needs it for PR iteration.

**Option 3: Keep As-Is** ÔÇö don't cleanup worktree.

**Option 4: Discard** ÔÇö require typed "discard" confirmation first.

### Step 6: Cleanup Workspace

Only for Options 1 and 4. If worktree is under `.worktrees/`, `worktrees/`, or `~/.config/superpowers/worktrees/`:

```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
git worktree remove "$WORKTREE_PATH"
git worktree prune
```

Otherwise: harness owns this workspace, do NOT remove it.

## Quick Reference

| Option | Merge | Push | Keep Worktree | Cleanup Branch |
|--------|-------|------|---------------|----------------|
| 1. Merge locally | yes | - | - | yes |
| 2. Create PR | - | yes | yes | - |
| 3. Keep as-is | - | - | yes | - |
| 4. Discard | - | - | - | yes (force) |

## Red Flags

**Never:**
- Proceed with failing tests
- Delete work without typed "discard" confirmation
- Remove a worktree before confirming merge success
- Clean up worktrees you didn't create
- Run `git worktree remove` from inside the worktree
