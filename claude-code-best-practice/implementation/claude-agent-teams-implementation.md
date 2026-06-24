# Agent Teams Implementation

![Last Updated](https://img.shields.io/badge/Last_Updated-Mar_12%2C_2026-white?style=flat&labelColor=555)

<table width="100%">
<tr>
<td><a href="../">ÔåÉ Back to Claude Code Best Practice</a></td>
<td align="right"><img src="../!/claude-jumping.svg" alt="Claude" width="60" /></td>
</tr>
</table>

---

<a href="#time-orchestration"><img src="../!/tags/implemented-hd.svg" alt="Implemented"></a>

<p align="center">
  <img src="assets/impl-agent-teams.png" alt="Agent Teams in action ÔÇö split pane mode with tmux" width="100%">
</p>

Agent Teams spawn **multiple independent Claude Code sessions** that coordinate via a shared task list. Unlike subagents (isolated context forks within one session), each teammate gets its own full context window with CLAUDE.md, MCP servers, and skills loaded automatically.

---

## ![How to Use](../!/tags/how-to-use.svg)

The time orchestration workflow was built entirely by an agent team. To run the finished product:

```bash
cd agent-teams
claude
/time-orchestrator
```

This invokes the **Command ÔåÆ Agent ÔåÆ Skill** pipeline: the agent fetches Dubai's current time, and the skill renders an SVG time card to `agent-teams/output/dubai-time.svg`.

---

## ![How to Implement](../!/tags/how-to-implement.svg)

You can create a replica of the weather orchestration workflow using agent teams ÔÇö in this example, the time orchestration workflow was built entirely by an agent team.

### 1. Install [iTerm2](https://iterm2.com/) and tmux

```bash
brew install --cask iterm2
brew install tmux
```

### 2. Start iTerm2 ÔåÆ tmux ÔåÆ Claude

```bash
tmux new -s dev
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

### 3. Prompt with team structure

<a id="time-orchestration"></a>

Paste this prompt into Claude to bootstrap a complete time orchestrator workflow using agent teams:

Main prompt: **[agent-teams-prompt.md](../agent-teams/agent-teams-prompt.md)**

### Team Coordination Flow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé                         LEAD (You)                           Ôöé
Ôöé       "Create an agent team to build time orchestration"     Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                           Ôöé spawns team (all parallel)
              ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
              Ôû╝            Ôû╝            Ôû╝
   ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
   Ôöé Command        Ôöé Ôöé Agent    Ôöé Ôöé Skill        Ôöé
   Ôöé Architect      Ôöé Ôöé Engineer Ôöé Ôöé Designer     Ôöé
   Ôöé                Ôöé Ôöé          Ôöé Ôöé              Ôöé
   Ôöé agent-teams/   Ôöé Ôöé agent-   Ôöé Ôöé agent-teams/ Ôöé
   Ôöé .claude/       Ôöé Ôöé teams/   Ôöé Ôöé .claude/     Ôöé
   Ôöé commands/      Ôöé Ôöé .claude/ Ôöé Ôöé skills/      Ôöé
   Ôöé time-          Ôöé Ôöé agents/  Ôöé Ôöé time-svg-    Ôöé
   Ôöé orchestrator.mdÔöé Ôöé time-    Ôöé Ôöé creator/     Ôöé
   Ôöé                Ôöé Ôöé agent.md Ôöé Ôöé              Ôöé
   ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ ÔööÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
           Ôöé               Ôöé              Ôöé
           Ôû╝               Ôû╝              Ôû╝
   ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
   Ôöé            Shared Task List                      Ôöé
   Ôöé  ÔÿÉ Agree on data contract: {time, tz, formatted} Ôöé
   Ôöé  ÔÿÉ Command uses Agent tool (not bash)            Ôöé
   Ôöé  ÔÿÉ Agent preloads time-fetcher skill             Ôöé
   Ôöé  ÔÿÉ Skill reads time from context (no re-fetch)   Ôöé
   Ôöé  ÔÿÉ All files inside agent-teams/.claude/         Ôöé
   ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                       Ôöé
                       Ôû╝
          ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
          Ôöé  cd agent-teams && claude    Ôöé
          Ôöé    /time-orchestrator        Ôöé
          Ôöé   Command ÔåÆ Agent ÔåÆ Skill    Ôöé
          ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

