# Workflows

## Workflow 1: Linux CIS Hardening Deployment
```
[Select CIS Benchmark for distro/version] ÔåÆ [Choose L1 or L2 profile]
  ÔåÆ [Run OpenSCAP baseline assessment] ÔåÆ [Review initial compliance score]
  ÔåÆ [Apply remediations (Ansible/manual)] ÔåÆ [Re-assess with OpenSCAP]
  ÔåÆ [Document exceptions] ÔåÆ [Deploy to production fleet]
  ÔåÆ [Schedule quarterly reassessment]
```

## Workflow 2: Automated Remediation with Ansible
```
[Clone Ansible Lockdown role for target distro]
  ÔåÆ [Configure variables (skip list, exceptions)]
  ÔåÆ [Test against staging servers]
  ÔåÆ [Review changes and application compatibility]
  ÔåÆ [Deploy to production in rolling batches]
  ÔåÆ [Run OpenSCAP validation after each batch]
```
