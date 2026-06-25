#!/bin/bash
# PreToolUse hook — blocks git commit if API key pattern detected in staged files

# Only intercept git commit
if [ "$CLAUDE_TOOL_NAME" != "Bash" ]; then
  exit 0
fi

if ! echo "$CLAUDE_TOOL_INPUT" | grep -q "git commit"; then
  exit 0
fi

# Check staged files for secret patterns
STAGED=$(git diff --cached --name-only 2>/dev/null)
if [ -z "$STAGED" ]; then
  exit 0
fi

PATTERNS=(
  'AIza[0-9A-Za-z_-]{35}'
  'sk-[a-zA-Z0-9]{48}'
  'AKIA[0-9A-Z]{16}'
  'ghp_[a-zA-Z0-9]{36}'
  'glpat-[a-zA-Z0-9_-]{20}'
  'xoxb-[0-9]+-[a-zA-Z0-9]+'
)

FOUND=0
for pattern in "${PATTERNS[@]}"; do
  if git diff --cached | grep -qE "$pattern"; then
    echo "SECRET DETECTED: pattern '$pattern' found in staged changes. Commit blocked." >&2
    FOUND=1
  fi
done

if [ $FOUND -eq 1 ]; then
  exit 2
fi

exit 0
