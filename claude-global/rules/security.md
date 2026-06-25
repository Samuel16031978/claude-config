# Security Rules

## Secrets & Credentials
- Never hardcode API keys, tokens, passwords in source files
- Use environment variables or `.env.local` (gitignored)
- Never log secrets, tokens, or full request headers
- Scan before commit: reject if API key pattern detected

## Input Validation
- Validate all user input at system boundaries
- Sanitize before DB queries — never string-concatenate SQL
- Parse JSON with try/catch — never trust external data shape
- Validate file uploads: type, size, content

## API Security
- Always use HTTPS — no plaintext HTTP calls to external services
- Rate-limit external API calls — handle 429 gracefully
- Never expose internal errors to client responses
- Log failed auth attempts (without credentials)

## Dependencies
- No packages with known critical CVEs
- Pin versions in lock files
- Review new deps before adding

## OWASP Top 10 Minimums
- A01 Broken Access Control: enforce auth on every protected route
- A02 Cryptographic Failures: no MD5/SHA1 for passwords — use bcrypt/argon2
- A03 Injection: parameterized queries only
- A07 Auth Failures: secure session management, no JWT secrets in client code
