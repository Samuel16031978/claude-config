#!/bin/bash
# Persists session context to .claude/session-context.md on session Stop

SESSION_CONTEXT_FILE="${CLAUDE_PROJECT_DIR}/.claude/session-context.md"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

mkdir -p "$(dirname "$SESSION_CONTEXT_FILE")"

cat > "$SESSION_CONTEXT_FILE" << EOF
# Session Context — $TIMESTAMP

## Last Session
- Date: $TIMESTAMP
- Project: ${CLAUDE_PROJECT_DIR##*/}

## Notes
<!-- Claude writes key decisions and context here at session end -->
EOF

echo "Session context saved to $SESSION_CONTEXT_FILE"
