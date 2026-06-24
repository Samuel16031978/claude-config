# Cross-Model (Claude Code + Codex) Workflow

based on [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) and [codex-cli-best-practice](https://github.com/shanraisshan/codex-cli-best-practice)

## Workflow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé              CROSS-MODEL CLAUDE CODE + CODEX WORKFLOW                   Ôöé
Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ
Ôöé                                                                         Ôöé
Ôöé  STEP 1: PLAN                                          Claude Code      Ôöé
Ôöé  ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ                                         Opus 4.6         Ôöé
Ôöé  Open Claude Code in plan mode (Terminal 1).           Plan Mode        Ôöé
Ôöé  Claude interviews you via AskUserQuestion.                             Ôöé
Ôöé  Produces a phased plan with test gates.                                Ôöé
Ôöé                                                                         Ôöé
Ôöé  Output: plans/{feature-name}.md                                        Ôöé
Ôöé                                                                         Ôöé
Ôöé                              Ôû╝                                          Ôöé
Ôöé                                                                         Ôöé
Ôöé  STEP 2: QA REVIEW                                     Codex CLI        Ôöé
Ôöé  ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ                                    GPT-5.4          Ôöé
Ôöé  Open Codex CLI in another terminal (Terminal 2).                       Ôöé
Ôöé  Codex reviews plan against the actual codebase.                        Ôöé
Ôöé  Inserts intermediate phases ("Phase 2.5")                              Ôöé
Ôöé  with "Codex Finding" headings.                                         Ôöé
Ôöé  Adds to the plan ÔÇö never rewrites original phases.                     Ôöé
Ôöé                                                                         Ôöé
Ôöé  Output: plans/{feature-name}.md (updated)                              Ôöé
Ôöé                                                                         Ôöé
Ôöé                              Ôû╝                                          Ôöé
Ôöé                                                                         Ôöé
Ôöé  STEP 3: IMPLEMENT                                     Claude Code      Ôöé
Ôöé  ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ                                    Opus 4.6         Ôöé
Ôöé  Start a new Claude Code session (Terminal 1).                          Ôöé
Ôöé  You implement phase-by-phase                                           Ôöé
Ôöé  with test gates at each phase.                                         Ôöé
Ôöé                                                                         Ôöé
Ôöé                              Ôû╝                                          Ôöé
Ôöé                                                                         Ôöé
Ôöé  STEP 4: VERIFY                                        Codex CLI        Ôöé
Ôöé  ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ                                      GPT-5.4          Ôöé
Ôöé  Start a new Codex CLI session (Terminal 2).                            Ôöé
Ôöé  Codex verifies the implementation                                      Ôöé
Ôöé  against the plan.                                                      Ôöé
Ôöé                                                                         Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## How cross-model workflow actually looks in production

![Cross-Model Workflow](assets/cross-model-workflow.png)

*Last Updated: 2026-03-06*
