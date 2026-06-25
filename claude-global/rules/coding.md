# Coding Rules

## File & Function Limits
- Files: max 800 lines — split if larger
- Functions: max 50 lines — extract if longer
- Nesting: max 4 levels — flatten with early returns
- One export per file for components/classes

## Code Quality
- No dead code, commented-out blocks, or unused imports
- No magic numbers — use named constants
- Explicit over implicit — name things clearly
- Fail fast with early returns, not deep else chains

## Error Handling
- Only handle errors at system boundaries (user input, external APIs)
- Trust framework/library guarantees — no defensive wrapping of internal calls
- Errors must be logged with context, not swallowed silently

## Comments
- Default: no comments
- Add comment only when WHY is non-obvious (hidden constraint, workaround, subtle invariant)
- Never describe WHAT the code does — names do that

## TypeScript / JavaScript
- Strict mode — no `any` unless unavoidable with comment why
- Prefer `const` — use `let` only when reassignment needed
- Async/await over raw promises for readability
- No `console.log` in committed code — use proper logger

## Git
- Commits: present tense imperative ("add feature", not "added feature")
- One logical change per commit
- Never commit secrets, build artifacts, or node_modules
