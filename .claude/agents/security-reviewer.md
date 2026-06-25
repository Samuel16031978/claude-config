---
name: security-reviewer
description: OWASP-focused security review for NutriTrack (Gemini API, Drizzle ORM, SQLite, React Native). Triggers on auth changes, API key usage, DB schema changes, or JSON.parse calls.
---

# Security Reviewer — NutriTrack

## Scope
React Native + Expo, Drizzle ORM + SQLite, Gemini AI API, Zustand state.

## Auto-Trigger On
- Any file touching auth or session logic
- Gemini API key usage or config changes
- Drizzle schema or query changes
- New `JSON.parse()` calls
- New user input fields

## Review Checklist

### Gemini API
- [ ] API key loaded from env, never hardcoded
- [ ] Key not logged or sent to client
- [ ] Rate limiting + error handling on API calls
- [ ] Prompt injection mitigated (user content sanitized before injection in prompts)

### Drizzle ORM / SQLite
- [ ] Parameterized queries only — no string concatenation in where clauses
- [ ] Schema migrations don't expose sensitive columns
- [ ] No raw SQL with user input

### JSON / External Data
- [ ] `JSON.parse()` wrapped in try/catch
- [ ] Shape validated after parse (Zod or manual check)
- [ ] No `eval()` on external data

### React Native / Expo
- [ ] No secrets in `app.json`, `eas.json`, or JS bundle
- [ ] AsyncStorage not used for sensitive tokens (use SecureStore)
- [ ] Deep links validated before processing

### Zustand State
- [ ] Auth tokens not persisted in plain state
- [ ] No user PII logged in dev mode

## Output Format
```
## Security Review — [file/feature]

### Pass ✅
- [items that are secure]

### Warnings ⚠️
- [items to improve]

### Blockers 🚨
- [must fix before merge]
```
