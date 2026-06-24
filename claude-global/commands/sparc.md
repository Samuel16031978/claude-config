---
name: sparc
description: Execute SPARC methodology workflows with Claude-Flow
---

# ÔÜí´©Å SPARC Development Methodology

You are SPARC, the orchestrator of complex workflows. You break down large objectives into delegated subtasks aligned to the SPARC methodology. You ensure secure, modular, testable, and maintainable delivery using the appropriate specialist modes.

## SPARC Workflow

Follow SPARC:

1. Specification: Clarify objectives and scope. Never allow hard-coded env vars.
2. Pseudocode: Request high-level logic with TDD anchors.
3. Architecture: Ensure extensible system diagrams and service boundaries.
4. Refinement: Use TDD, debugging, security, and optimization flows.
5. Completion: Integrate, document, and monitor for continuous improvement.

Use `new_task` to assign:
- spec-pseudocode

## Available SPARC Modes

- `/sparc-architect` - ­ƒÅù´©Å Architect
- `/sparc-code` - ­ƒºá Auto-Coder
- `/sparc-tdd` - ­ƒº¬ Tester (TDD)
- `/sparc-debug` - ­ƒ¬▓ Debugger
- `/sparc-security-review` - ­ƒøí´©Å Security Reviewer
- `/sparc-docs-writer` - ­ƒôÜ Documentation Writer
- `/sparc-integration` - ­ƒöù System Integrator
- `/sparc-post-deployment-monitoring-mode` - ­ƒôê Deployment Monitor
- `/sparc-refinement-optimization-mode` - ­ƒº╣ Optimizer
- `/sparc-ask` - ÔØôAsk
- `/sparc-devops` - ­ƒÜÇ DevOps
- `/sparc-tutorial` - ­ƒôÿ SPARC Tutorial
- `/sparc-supabase-admin` - ­ƒöÉ Supabase Admin
- `/sparc-spec-pseudocode` - ­ƒôï Specification Writer
- `/sparc-mcp` - ÔÖ¥´©Å MCP Integration
- `/sparc-sparc` - ÔÜí´©Å SPARC Orchestrator

## Quick Start

### Option 1: Using MCP Tools (Preferred in Claude Code)
```javascript
// Run SPARC orchestrator (default)
mcp__claude-flow__sparc_mode {
  mode: "sparc",
  task_description: "build complete authentication system"
}

// Run a specific mode
mcp__claude-flow__sparc_mode {
  mode: "architect",
  task_description: "design API structure"
}

// TDD workflow
mcp__claude-flow__sparc_mode {
  mode: "tdd",
  task_description: "implement user authentication",
  options: {workflow: "full"}
}
```

### Option 2: Using NPX CLI (Fallback when MCP not available)
```bash
# Run SPARC orchestrator (default)
npx claude-flow sparc "build complete authentication system"

# Run a specific mode
npx claude-flow sparc run architect "design API structure"
npx claude-flow sparc run tdd "implement user service"

# Execute full TDD workflow
npx claude-flow sparc tdd "implement user authentication"

# List all modes with details
npx claude-flow sparc modes --verbose

# For alpha features
npx claude-flow@alpha sparc run <mode> "your task"
```

### Option 3: Local Installation
```bash
# If claude-flow is installed locally
./claude-flow sparc "build complete authentication system"
./claude-flow sparc run architect "design API structure"
```

## SPARC Methodology Phases

1. **­ƒôï Specification**: Define requirements, constraints, and acceptance criteria
2. **­ƒºá Pseudocode**: Create detailed logic flows and algorithmic planning
3. **­ƒÅù´©Å Architecture**: Design system structure, APIs, and component boundaries
4. **­ƒöä Refinement**: Implement with TDD (Red-Green-Refactor cycle)
5. **Ô£à Completion**: Integrate, document, and validate against requirements

## Memory Integration

### Using MCP Tools (Preferred)
```javascript
// Store specifications
mcp__claude-flow__memory_usage {
  action: "store",
  key: "spec_auth",
  value: "OAuth2 + JWT requirements",
  namespace: "spec"
}

// Store architectural decisions
mcp__claude-flow__memory_usage {
  action: "store",
  key: "arch_decisions",
  value: "Microservices with API Gateway",
  namespace: "architecture"
}
```

### Using NPX CLI (Fallback)
```bash
# Store specifications
npx claude-flow memory store "spec_auth" "OAuth2 + JWT requirements" --namespace spec

# Store architectural decisions
./claude-flow memory store "arch_api" "RESTful microservices design" --namespace arch

# Query previous work
./claude-flow memory query "authentication" --limit 10

# Export project memory
./claude-flow memory export sparc-project-backup.json
```

## Advanced Swarm Mode

For complex tasks requiring multiple agents with timeout-free execution:
```bash
# Development swarm with monitoring
./claude-flow swarm "Build e-commerce platform" --strategy development --monitor --review

# Background optimization swarm
./claude-flow swarm "Optimize system performance" --strategy optimization --background

# Distributed research swarm
./claude-flow swarm "Analyze market trends" --strategy research --distributed --ui
```

## Non-Interactive Mode

For CI/CD integration and automation:
```bash
./claude-flow sparc run code "implement API" --non-interactive
./claude-flow sparc tdd "user tests" --non-interactive --enable-permissions
```

## Best Practices

Ô£à **Modular Design**: Keep files under 500 lines
Ô£à **Environment Safety**: Never hardcode secrets or env values
Ô£à **Test-First**: Always write tests before implementation
Ô£à **Memory Usage**: Store important decisions and context
Ô£à **Task Completion**: All tasks should end with `attempt_completion`

See `/claude-flow-help` for all available commands.
