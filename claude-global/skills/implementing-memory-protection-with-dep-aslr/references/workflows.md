# Workflows
## Memory Protection Deployment
```
[Audit current mitigations: Get-ProcessMitigation -System]
  ÔåÆ [Enable system-level DEP, SEHOP, ASLR]
  ÔåÆ [Configure per-app mitigations for high-risk applications]
  ÔåÆ [Export XML, deploy via Intune/GPO]
  ÔåÆ [Test application compatibility] ÔåÆ [Monitor for crashes]
  ÔåÆ [Tune exceptions for incompatible apps]
```
