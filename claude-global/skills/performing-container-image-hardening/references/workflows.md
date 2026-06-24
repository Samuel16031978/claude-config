# Workflow Reference: Container Image Hardening

## Hardening Pipeline

```
Base Image Selection
       Ôöé
       Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Multi-Stage Build Ôöé
Ôöé (builder + prod)  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôöé
       Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Remove Packages  Ôöé
Ôöé + Set User/Perms Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôöé
       Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Trivy Scan       Ôöé
Ôöé + Hadolint       Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôöé
       Ôû╝
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé CIS Benchmark    Ôöé
Ôöé Validation       Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Base Image Selection Guide

| Base Image | Size | Use Case | Packages |
|------------|------|----------|----------|
| scratch | 0 MB | Static Go/Rust binaries | None |
| distroless/static | 2 MB | Static binaries + CA certs | ca-certificates |
| distroless/base | 20 MB | Dynamic binaries | glibc, libssl |
| alpine:3.19 | 7 MB | General minimal | musl, busybox |
| debian:bookworm-slim | 80 MB | Debian ecosystem | apt, glibc |
| ubuntu:24.04 | 78 MB | Ubuntu ecosystem | apt, glibc |

## Dockerfile Hardening Checklist

- [ ] Multi-stage build separates build and runtime
- [ ] Minimal base image selected
- [ ] Non-root USER instruction present
- [ ] HEALTHCHECK instruction defined
- [ ] Base image pinned by digest
- [ ] COPY used instead of ADD
- [ ] No secrets in ENV or ARG
- [ ] Package cache cleaned (rm -rf /var/lib/apt/lists/*)
- [ ] Unnecessary packages removed
- [ ] setuid/setgid bits cleared
- [ ] Shell removed (if not needed)
