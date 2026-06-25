#!/bin/bash
# SessionStart hook — copies claude-global/ config to ~/.claude/
# Runs at start of every Claude Code session

GLOBAL_DIR="$(git rev-parse --show-toplevel 2>/dev/null)/claude-global"

if [ ! -d "$GLOBAL_DIR" ]; then
  echo "claude-global/ not found, skipping sync"
  exit 0
fi

# Sync skills
if [ -d "$GLOBAL_DIR/skills" ]; then
  cp -r "$GLOBAL_DIR/skills/." "$HOME/.claude/skills/" 2>/dev/null || true
fi

# Sync agents
if [ -d "$GLOBAL_DIR/agents" ]; then
  cp -r "$GLOBAL_DIR/agents/." "$HOME/.claude/agents/" 2>/dev/null || true
fi

# Sync rules
if [ -d "$GLOBAL_DIR/rules" ]; then
  cp -r "$GLOBAL_DIR/rules/." "$HOME/.claude/rules/" 2>/dev/null || true
fi

# Sync hooks
if [ -d "$GLOBAL_DIR/hooks" ]; then
  cp -r "$GLOBAL_DIR/hooks/." "$HOME/.claude/hooks/" 2>/dev/null || true
fi

# Sync settings
if [ -f "$GLOBAL_DIR/settings.json" ]; then
  cp "$GLOBAL_DIR/settings.json" "$HOME/.claude/settings.json" 2>/dev/null || true
fi

echo "claude-global synced to ~/.claude/"
