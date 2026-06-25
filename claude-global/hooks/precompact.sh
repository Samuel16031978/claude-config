#!/bin/bash
# Runs before context compaction — saves current work summary

SUMMARY_FILE="${CLAUDE_PROJECT_DIR}/.claude/precompact-summary.md"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

mkdir -p "$(dirname "$SUMMARY_FILE")"

cat > "$SUMMARY_FILE" << EOF
# Pre-Compact Summary — $TIMESTAMP

Context compaction triggered. Key state preserved above.
EOF

echo "Pre-compact summary saved"
