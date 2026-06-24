# Commands Report ÔÇö Changelog History

## Status Legend

| Status | Meaning |
|--------|---------|
| Ô£à `COMPLETE (reason)` | Action was taken and resolved successfully |
| ÔØî `INVALID (reason)` | Finding was incorrect, not applicable, or intentional |
| Ô£ï `ON HOLD (reason)` | Action deferred ÔÇö waiting on external dependency or user decision |

---

## [2026-03-13 04:23 PM PKT] Claude Code v2.1.74

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Field | Add `name` to frontmatter table ÔÇö display name for the skill | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 2 | HIGH | New Field | Add `disable-model-invocation` to frontmatter table ÔÇö prevents auto-loading | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 3 | HIGH | New Field | Add `user-invocable` to frontmatter table ÔÇö hides from `/` menu | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 4 | HIGH | New Field | Add `context` to frontmatter table ÔÇö fork to run in subagent context | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 5 | HIGH | New Field | Add `agent` to frontmatter table ÔÇö subagent type for context: fork | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 6 | HIGH | New Field | Add `hooks` to frontmatter table ÔÇö lifecycle hooks scoped to skill | ÔØî INVALID (skill-only field, not applicable to commands frontmatter) |
| 7 | HIGH | New Command | Add `/btw <question>` ÔÇö ask a quick side question without adding to conversation | Ô£à COMPLETE (added as #53 in Session tag) |
| 8 | HIGH | New Command | Add `/hooks` ÔÇö manage hook configurations for tool events | Ô£à COMPLETE (added as #30 in Extensions tag) |
| 9 | HIGH | New Command | Add `/insights` ÔÇö generate session analysis report | Ô£à COMPLETE (added as #17 in Context tag) |
| 10 | HIGH | New Command | Add `/plugin` ÔÇö manage Claude Code plugins | Ô£à COMPLETE (added as #33 in Extensions tag) |
| 11 | HIGH | New Command | Add `/skills` ÔÇö list available skills | Ô£à COMPLETE (added as #35 in Extensions tag) |
| 12 | HIGH | New Command | Add `/upgrade` ÔÇö open upgrade page to switch plan tier | Ô£à COMPLETE (added as #3 in Auth tag) |
| 13 | HIGH | Removed Command | Remove `/output-style` ÔÇö deprecated in v2.1.73, use `/config` instead | Ô£à COMPLETE (removed from Config tag) |
| 14 | HIGH | Removed Command | Remove `/bug` row ÔÇö now listed as alias under `/feedback` | Ô£à COMPLETE (removed row, added "Alias: /bug" to /feedback description) |
| 15 | HIGH | Changed Description | Update `/passes` ÔÇö repurposed from review passes to referral sharing | Ô£à COMPLETE (updated description, kept in Model tag) |
| 16 | HIGH | Changed Description | Update `/review` ÔÇö deprecated, replaced by `code-review` marketplace plugin | Ô£à COMPLETE (updated description in Project tag) |
| 17 | MED | Changed Description | Update `/stickers` ÔÇö changed from UI sticker packs to ordering physical stickers | Ô£à COMPLETE (updated description in Config tag) |

---

## [2026-03-15 12:50 PM PKT] Claude Code v2.1.76

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/color [color\|default]` to Config tag ÔÇö set prompt bar color for current session | Ô£à COMPLETE (added as #4 in Config tag) |
| 2 | HIGH | New Command | Add `/effort [low\|medium\|high\|max\|auto]` to Model tag ÔÇö set model effort level | Ô£à COMPLETE (added as #38 in Model tag) |
| 3 | MED | Changed Description | Update `/status` ÔÇö now "Open the Settings interface (Status tab)" instead of "Show a concise session status summary" | Ô£à COMPLETE (updated description at #20 in Context tag) |
| 4 | MED | Changed Description | Update `/desktop` ÔÇö now "Continue the current session in the Claude Code Desktop app. macOS and Windows only." | Ô£à COMPLETE (updated description at #49 in Remote tag) |
| 5 | LOW | Changed Argument | Update `/init` ÔÇö official docs dropped `[prompt]` argument hint | Ô£à COMPLETE (removed [prompt] hint at #45 in Project tag) |

---

## [2026-03-17 12:45 PM PKT] Claude Code v2.1.77

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Alias | Add `Alias: /branch` to `/fork` entry (v2.1.77 renamed forkÔåÆbranch) | Ô£à COMPLETE (added "Alias: /branch" to /fork at #59 in Session tag) |
| 2 | HIGH | New Aliases | Add aliases to 8 commands: `/clear` (+/reset, /new), `/config` (+/settings), `/desktop` (+/app), `/exit` (+/quit), `/rewind` (+/checkpoint), `/resume` (+/continue), `/remote-control` (+/rc), `/mobile` (+/ios, /android) | Ô£à COMPLETE (added alias notations to all 8 command descriptions) |
| 3 | MED | Changed Description | Update `/diff` ÔÇö "Open an interactive diff viewer showing uncommitted changes and per-turn diffs" | Ô£à COMPLETE (updated description at #44 in Project tag) |
| 4 | MED | Changed Description | Update `/memory` ÔÇö "Edit CLAUDE.md memory files, enable or disable auto-memory, and view auto-memory entries" | Ô£à COMPLETE (updated description at #37 in Memory tag) |
| 5 | MED | Changed Description | Update `/copy` ÔÇö "Copy the last assistant response to clipboard. Shows interactive picker for code blocks" | Ô£à COMPLETE (updated description at #27 in Export tag) |
| 6 | MED | Changed Description | Update `/mobile` ÔÇö "Show QR code to download the Claude mobile app" | Ô£à COMPLETE (updated description + aliases at #52 in Remote tag) |
| 7 | MED | Changed Description | Update `/remote-control` ÔÇö "Make this session available for remote control from claude.ai" | Ô£à COMPLETE (updated description + alias at #53 in Remote tag) |
| 8 | LOW | Frontmatter Scope | 6 skill-only fields still absent from report (intentional scoping) | ÔØî INVALID (skill-only fields ÔÇö same determination as v2.1.74 run) |

---

## [2026-03-18 11:38 PM PKT] Claude Code v2.1.78

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/voice` to Config tag ÔÇö toggle push-to-talk voice dictation | Ô£à COMPLETE (added as #15 in Config tag) |
| 2 | HIGH | Inverted Alias | Swap `/fork` ÔåÆ `/branch` as primary, `/fork` as alias | Ô£à COMPLETE (swapped to `/branch` at #56 in Session tag, re-sorted alphabetically) |
| 3 | MED | New Alias | Add `/allowed-tools` alias to `/permissions` | Ô£à COMPLETE (added alias to #7 in Config tag) |
| 4 | MED | New Argument | Add `[N]` argument syntax to `/copy` | Ô£à COMPLETE (updated to `/copy [N]` at #28 in Export tag) |
| 5 | LOW | Frontmatter Scope | 6 skill-only fields absent from report (intentional scoping) | ÔØî INVALID (skill-only fields ÔÇö same determination as v2.1.74 and v2.1.77 runs) |

---

## [2026-03-19 11:54 AM PKT] Claude Code v2.1.79

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Frontmatter Scope | 6 skill-only fields absent from report (intentional scoping) | ÔØî INVALID (skill-only fields ÔÇö same determination as v2.1.74, v2.1.77, and v2.1.78 runs) |

---

## [2026-03-20 08:33 AM PKT] Claude Code v2.1.80

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MED | New Field | Add `effort` to frontmatter table ÔÇö override model effort level when command is invoked (v2.1.80) | Ô£à COMPLETE (added as 5th field, then repositioned to 8th when full field set was added) |
| 2 | HIGH | QA Correction | Add 6 missing fields (`name`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`) ÔÇö official docs state commands support "the same frontmatter" as skills; previous INVALID determinations (v2.1.74ÔÇôv2.1.79) were incorrect | Ô£à COMPLETE (added all 6 fields, count updated 5 ÔåÆ 11, field order matches official docs) |
| 3 | HIGH | Cross-Report Fix | Add `effort` to skills report (`claude-skills.md`) ÔÇö field was missing there too | Ô£à COMPLETE (added as 8th field in skills report, count updated 10 ÔåÆ 11) |

---

## [2026-03-21 09:08 PM PKT] Claude Code v2.1.81

No priority action items ÔÇö report is fully in sync with official documentation (11 frontmatter fields, 63 built-in commands).

---

## [2026-03-23 09:48 PM PKT] Claude Code v2.1.81

No priority action items ÔÇö report is fully in sync with official documentation (11 frontmatter fields, 63 built-in commands).

---

## [2026-03-25 08:07 PM PKT] Claude Code v2.1.83

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/schedule [description]` to Remote tag ÔÇö Create, update, list, or run Cloud scheduled tasks | Ô£à COMPLETE (added as #56 in Remote tag, count updated 63 ÔåÆ 64) |

---

## [2026-03-26 01:01 PM PKT] Claude Code v2.1.84

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Field | Add `shell` to frontmatter table ÔÇö shell for `!command` blocks (`bash` or `powershell`) | Ô£à COMPLETE (added as 12th field before `hooks`, count updated 11 ÔåÆ 12) |
| 2 | LOW | Changed Argument | Add `[on\|off]` argument hint to `/fast` command | Ô£à COMPLETE (updated `/fast` to `/fast [on\|off]` at #40 in Model tag) |

---

## [2026-03-27 06:25 PM PKT] Claude Code v2.1.85

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Field | Add `paths` to frontmatter table ÔÇö glob patterns that limit when a skill is activated | Ô£à COMPLETE (added as 6th field after `user-invocable`, count updated 12 ÔåÆ 13) |

---

## [2026-03-28 06:05 PM PKT] Claude Code v2.1.86

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MED | Changed Argument | Update `/add-dir` ÔÇö add `<path>` required argument hint per official docs | Ô£à COMPLETE (updated at #44 in Project tag) |
| 2 | MED | Changed Argument | Update `/branch` ÔÇö add `[name]` optional argument hint per official docs | Ô£à COMPLETE (updated at #57 in Session tag) |
| 3 | MED | Changed Argument | Update `/model` ÔÇö add `[model]` optional argument hint per official docs | Ô£à COMPLETE (updated at #41 in Model tag) |
| 4 | MED | Changed Argument | Update `/plan` ÔÇö add `[description]` optional argument hint per official docs | Ô£à COMPLETE (updated at #43 in Model tag) |
| 5 | MED | Changed Argument | Update `/pr-comments` ÔÇö add `[PR]` optional argument hint per official docs | Ô£à COMPLETE (updated at #47 in Project tag) |
| 6 | MED | Changed Argument | Update `/passes` ÔÇö remove `[number]` argument hint (not in official docs) | Ô£à COMPLETE (updated at #42 in Model tag) |
| 7 | MED | Changed Argument | Update `/rename` ÔÇö change from `<name>` (required) to `[name]` (optional) per official docs | Ô£à COMPLETE (updated at #62 in Session tag) |
| 8 | LOW | Changed Argument | Update `/compact` ÔÇö change argument label from `[prompt]` to `[instructions]` per official docs | Ô£à COMPLETE (updated at #60 in Session tag) |
| 9 | LOW | Changed Argument | Update `/feedback` ÔÇö change argument label from `[description]` to `[report]` per official docs | Ô£à COMPLETE (updated at #24 in Debug tag) |

---

## [2026-03-31 06:55 PM PKT] Claude Code v2.1.88

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MED | Description Sync | Synced all 43 command descriptions to match official docs ÔÇö behavioral clarifications (`/vim` toggle, `/sandbox` toggle, `/hooks` view), expanded detail (`/effort` persistence, `/copy` SSH write, `/model` effort arrows), and wording alignment across Auth, Config, Context, Debug, Export, Extensions, Model, Project, Remote, and Session tags | Ô£à COMPLETE (all 64 descriptions now match official docs at code.claude.com/docs/en/commands) |

---

## [2026-04-01 12:26 PM PKT] Claude Code v2.1.89

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Changed Description | Update `/init` ÔÇö official docs now use `CLAUDE_CODE_NEW_INIT=1` instead of `=true` | Ô£à COMPLETE (updated env var value from `=true` to `=1` to match official docs) |

---

## [2026-04-02 09:14 PM PKT] Claude Code v2.1.90

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MED | Changed Description | Update `/permissions` ÔÇö official docs expanded to describe interactive dialog with scope rules, directory management, and auto mode denial review | Ô£à COMPLETE (updated description to match official docs) |
| 2 | MED | New Alias | Add `/bashes` alias to `/tasks` command per official docs | Ô£à COMPLETE (added "Alias: /bashes" to /tasks at #27 in Debug tag) |

---

## [2026-04-03 08:34 PM PKT] Claude Code v2.1.91

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/powerup` to Config tag ÔÇö Discover Claude Code features through quick interactive lessons with animated demos | Ô£à COMPLETE (added as #26 in Debug tag ÔÇö resolved in v2.1.92 run) |

---

## [2026-04-04 10:40 PM PKT] Claude Code v2.1.92

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/powerup` to Debug tag ÔÇö Discover Claude Code features through quick interactive lessons with animated demos | Ô£à COMPLETE (added as #26 in Debug tag, recurring from v2.1.91) |
| 2 | HIGH | New Command | Add `/setup-bedrock` to Auth tag ÔÇö Configure Amazon Bedrock authentication, region, and model pins through an interactive wizard | Ô£à COMPLETE (added as #3 in Auth tag) |
| 3 | HIGH | New Command | Add `/ultraplan <prompt>` to Model tag ÔÇö Draft a plan in an ultraplan session, review it in your browser, then execute remotely or send it back | Ô£à COMPLETE (added as #45 in Model tag) |
| 4 | HIGH | Removed Command | Remove `/vim` from Config tag ÔÇö removed in v2.1.92 (max-version: 2.1.91), use `/config` Editor mode instead | Ô£à COMPLETE (removed from Config tag) |
| 5 | HIGH | Removed Command | Remove `/pr-comments [PR]` from Project tag ÔÇö removed in v2.1.91 (max-version: 2.1.90), ask Claude directly | Ô£à COMPLETE (removed from Project tag) |
| 6 | MED | Changed Description | Update `/release-notes` ÔÇö now "View the changelog in an interactive version picker. Select a specific version to see its release notes, or choose to show all versions." | Ô£à COMPLETE (updated description at #27 in Debug tag) |

---

## [2026-04-08 09:35 PM PKT] Claude Code v2.1.96

No priority action items ÔÇö report is fully in sync with official documentation (13 frontmatter fields, 65 built-in commands).

---

## [2026-04-09 11:31 PM PKT] Claude Code v2.1.97

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/autofix-pr [prompt]` to Remote tag ÔÇö Spawn a web session that watches the current branch's PR and pushes fixes when CI fails or reviewers leave comments | Ô£à COMPLETE (added as #51 in Remote tag, count updated 65 ÔåÆ 68) |
| 2 | HIGH | New Command | Add `/teleport` to Remote tag ÔÇö Pull a Claude Code on the web session into this terminal. Alias: `/tp` | Ô£à COMPLETE (added as #59 in Remote tag) |
| 3 | HIGH | New Command | Add `/web-setup` to Remote tag ÔÇö Connect GitHub account to Claude Code on the web using local `gh` CLI credentials | Ô£à COMPLETE (added as #60 in Remote tag) |
| 4 | MED | Changed Description | Update `/add-dir` ÔÇö official docs now include caveat about `.claude/` config not being discovered from added directory | Ô£à COMPLETE (updated description at #46 in Project tag) |

---

## [2026-04-13 08:00 PM PKT] Claude Code v2.1.101

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/setup-vertex` to Auth tag ÔÇö Configure Google Vertex AI authentication, project, region, and model pins through an interactive wizard. Only visible when `CLAUDE_CODE_USE_VERTEX=1` is set | Ô£à COMPLETE (added as #4 in Auth tag, count updated 68 ÔåÆ 69) |

---

## [2026-04-14 11:13 PM PKT] Claude Code v2.1.107

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Field | Add `when_to_use` to frontmatter table ÔÇö additional context for when Claude should invoke the skill, appended to `description` in the listing (count 13 ÔåÆ 14) | Ô£à COMPLETE (added after `description` field, count updated 13 ÔåÆ 14) |
| 2 | HIGH | New Command | Add `/team-onboarding` to Project tag ÔÇö Generate a team onboarding guide from Claude Code usage history (count 69 ÔåÆ 70) | Ô£à COMPLETE (added as #52 in Project tag, count updated 69 ÔåÆ 70) |
| 3 | MED | Scope Decision | 5 bundled skills (`/batch`, `/claude-api`, `/debug`, `/loop`, `/simplify`) listed in official docs unified table but excluded per report's current scoping disclaimer | ÔØî INVALID (user chose to keep report scoped to built-in commands only ÔÇö disclaimer retained) |
| 4 | MED | Changed Description | Update `/doctor` ÔÇö add "Press `f` to have Claude fix any reported issues" | Ô£à COMPLETE (added status icons and `f` key fix detail to description) |
| 5 | MED | Changed Description | Update `/schedule` ÔÇö terminology changed from "Cloud scheduled tasks" to "routines" | Ô£à COMPLETE (updated terminology in description) |

---

## [2026-04-16 08:20 PM PKT] Claude Code v2.1.110

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MED | New Alias | Add `/undo` alias to `/rewind` entry ÔÇö added in v2.1.108 | Ô£à COMPLETE (added `/undo` alongside existing `/checkpoint` alias at #70 in Session tag) |

---

## [2026-04-18 07:54 PM PKT] Claude Code v2.1.114

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/recap` to Session tag ÔÇö Generate a one-line summary of the current session on demand (v2.1.108) | Ô£à COMPLETE (added as #72 in Session tag, count updated 70 ÔåÆ 75) |
| 2 | HIGH | New Command | Add `/focus` to Config tag ÔÇö Toggle the focus view showing only last prompt, tool-call summary, and final response (v2.1.110) | Ô£à COMPLETE (added as #8 in Config tag) |
| 3 | HIGH | New Command | Add `/tui [default\|fullscreen]` to Config tag ÔÇö Set the terminal UI renderer and relaunch with conversation intact (v2.1.110) | Ô£à COMPLETE (added as #17 in Config tag) |
| 4 | HIGH | New Command | Add `/ultrareview [PR]` to Project tag ÔÇö Run a deep, multi-agent code review in a cloud sandbox (v2.1.111) | Ô£à COMPLETE (added as #56 in Project tag) |
| 5 | HIGH | New Command | Add `/heapdump` to Debug tag ÔÇö Write a JavaScript heap snapshot and memory breakdown to `~/Desktop` for diagnosing high memory usage | Ô£à COMPLETE (added as #28 in Debug tag) |
| 6 | HIGH | Changed Description | Revert `/review` from deprecated ÔåÆ live built-in per official docs ("Review a pull request locally in your current session. For a deeper cloud-based review, see `/ultrareview`") ÔÇö reverses v2.1.74 update | Ô£à COMPLETE (updated description at #53 in Project tag, now references `/ultrareview`) |
| 7 | MED | Changed Description | Update `/effort` description ÔÇö official now lists `xhigh` level and opens interactive slider with no args (v2.1.111) | Ô£à COMPLETE (updated arg hint to include `xhigh` and description to mention interactive slider) |
| 8 | MED | Changed Description | Update `/theme` description ÔÇö official adds "Auto (match terminal)" option (v2.1.111) | Ô£à COMPLETE (added "Auto (match terminal)" to description at #16 in Config tag) |
| 9 | MED | Changed Description | Update `/model` description ÔÇö official notes it warns before switching mid-conversation (v2.1.108) | Ô£à COMPLETE (added mid-conversation warning detail at #46 in Model tag) |
| 10 | MED | New Alias | Add `/routines` alias to `/schedule` command per official docs | Ô£à COMPLETE (added `Alias: /routines` at #64 in Remote tag) |

---

## [2026-04-24 12:29 AM PKT] Claude Code v2.1.118

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Field | Add `arguments` to frontmatter table ÔÇö named positional arguments for `$name` substitution (count 14 ÔåÆ 15) | Ô£à COMPLETE (added after `argument-hint`, count updated 14 ÔåÆ 15) |
| 2 | HIGH | Changed Description | Update `/cost` ÔÇö now just an alias for `/usage` | Ô£à COMPLETE (description simplified to "Alias for `/usage`") |
| 3 | HIGH | Changed Description | Update `/stats` ÔÇö now alias for `/usage`, opens Stats tab | Ô£à COMPLETE (description updated to "Alias for `/usage`. Opens on the Stats tab") |
| 4 | HIGH | Changed Description | Update `/usage` ÔÇö canonical command absorbing `/cost` and `/stats`; note aliases | Ô£à COMPLETE (expanded to "Show session cost, plan usage limits, and activity stats. `/cost` and `/stats` are aliases") |
| 5 | MED | Changed Argument | Update `/voice` signature to `/voice [hold\|tap\|off]` | Ô£à COMPLETE (signature and description updated) |
| 6 | MED | Changed Description | Update `/theme` ÔÇö add custom themes support (`~/.claude/themes/`, plugins, "New custom themeÔÇª") | Ô£à COMPLETE (custom themes detail added to description) |
| 7 | MED | Changed Description | Update `/terminal-setup` ÔÇö replace terminal list (drop Warp; add Cursor, Windsurf, Zed) | Ô£à COMPLETE (terminal list replaced: VS Code, Cursor, Windsurf, Alacritty, Zed) |
| 8 | LOW | Changed Description | Update `/effort` ÔÇö note that `max` level is session-only | Ô£à COMPLETE (added "(session-only)" qualifier to `max` in description) |

---

## [2026-04-26 01:10 PM PKT] Claude Code v2.1.119

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Changed Description | Update `/branch` ÔÇö add `CLAUDE_CODE_FORK_SUBAGENT` env-var note explaining `/fork` divergence (v2.1.117) | Ô£à COMPLETE (appended fork-subagent note to description at #67 in Session tag) |
| 2 | MED | Changed Description | Update `/focus` ÔÇö add "Only available in fullscreen rendering" qualifier (v2.1.110) | Ô£à COMPLETE (appended fullscreen-only qualifier at #8 in Config tag) |
| 3 | MED | Changed Description | Update `/skills` ÔÇö add "Press `t` to sort by token count" (v2.1.110/111) | Ô£à COMPLETE (appended sort-by-token-count detail at #42 in Extensions tag) |
| 4 | MED | Changed Description | Update `/clear` ÔÇö reword to contrast with `/compact` per official docs | Ô£à COMPLETE (replaced description with "Start a new conversation with empty contextÔÇª use `/compact` instead" at #69 in Session tag) |
| 5 | LOW | Scope Decision | 6 bundled skills (`/batch`, `/claude-api`, `/debug`, `/fewer-permission-prompts`, `/loop`, `/simplify`) listed in upstream unified table but excluded per report scope | ÔØî INVALID (recurring from v2.1.107 ÔÇö user previously chose to keep report scoped to built-in commands only) |

---

## [2026-04-29 12:50 AM PKT] Claude Code v2.1.121

No priority action items ÔÇö report is fully in sync with official documentation (15 frontmatter fields, 75 built-in commands).

---

## [2026-05-01 03:31 PM PKT] Claude Code v2.1.126

No priority action items ÔÇö report is fully in sync with official documentation (15 frontmatter fields, 75 built-in commands).

---

## [2026-05-12 11:39 PM PKT] Claude Code v2.1.139

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Command | Add `/background [prompt]` to Session tag ÔÇö Detach current session to run as a background agent. Alias: `/bg` | Ô£à COMPLETE (added as #69 in Session tag, count updated 75 ÔåÆ 80) |
| 2 | HIGH | New Command | Add `/goal [condition\|clear]` to Session tag ÔÇö Claude keeps working across turns until condition met (v2.1.139) | Ô£à COMPLETE (added as #75 in Session tag) |
| 3 | HIGH | New Command | Add `/radio` to Config tag ÔÇö Open Claude FM lo-fi radio in your browser | Ô£à COMPLETE (added as #12 in Config tag) |
| 4 | HIGH | New Command | Add `/scroll-speed` to Config tag ÔÇö Adjust mouse wheel scroll speed interactively (v2.1.139) | Ô£à COMPLETE (added as #14 in Config tag) |
| 5 | HIGH | New Command | Add `/stop` to Session tag ÔÇö Stop the current background session; transcript and worktree are kept | Ô£à COMPLETE (added as #80 in Session tag) |
| 6 | LOW | Scope Decision | 6 bundled skills (`/batch`, `/claude-api`, `/debug`, `/fewer-permission-prompts`, `/loop`, `/simplify`) listed in upstream unified table but excluded per report scope | ÔØî INVALID (recurring from v2.1.107 and v2.1.119 ÔÇö user previously chose to keep report scoped to built-in commands only) |

---

## [2026-05-21 12:06 AM PKT] Claude Code v2.1.145

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Renamed Command | Rename `/extra-usage` ÔåÆ `/usage-credits` in Context tag (v2.1.144); keep `/extra-usage` noted as previous name; re-sort within Context group (`e`ÔåÆ`u`) | Ô£à COMPLETE (renamed at #27 in Context tag, moved after `/usage`, rows 23ÔÇô27 renumbered; count unchanged at 80) |
| 2 | MED | New Alias | Add `/share` alias to `/feedback` and broaden description to "Submit feedback, report a bug, or share your conversation. Aliases: `/bug`, `/share`" | Ô£à COMPLETE (updated description at #29 in Debug tag) |
| 3 | LOW | Changed Value | Add `xhigh` to the `effort` frontmatter field's options list (`low`, `medium`, `high`, `xhigh`, `max`) | Ô£à COMPLETE (added `xhigh` to effort field row; value-list sync, not a field add/remove) |
| 4 | LOW | Scope Decision | 9 bundled skills (`/batch`, `/claude-api`, `/debug`, `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`, `/simplify`, `/verify`) in upstream unified table excluded per report scope | ÔØî INVALID (recurring from v2.1.107/119/139 ÔÇö report intentionally scoped to built-in commands only) |

---

## [2026-05-25 04:25 PM PKT] Claude Code v2.1.150

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Scope Decision | 9 bundled skills (`/batch`, `/claude-api`, `/code-review`, `/debug`, `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`, `/verify`) in upstream unified table excluded per report scope; `/simplify` renamed ÔåÆ `/code-review` at v2.1.147 (still a bundled Skill, stays excluded) | ÔØî INVALID (recurring from v2.1.107/119/139/145 ÔÇö report intentionally scoped to built-in commands only) |

_No tracked drift: frontmatter fields 15/15 match official docs, built-in commands 80/80 match. Version badge bumped v2.1.145 ÔåÆ v2.1.150._
