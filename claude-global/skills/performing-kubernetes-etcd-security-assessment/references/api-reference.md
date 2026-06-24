# API Reference ÔÇö Performing Kubernetes etcd Security Assessment

## Libraries Used
- **subprocess**: Execute kubectl, etcdctl commands
- **json**: Parse Kubernetes API resource output
- **re**: Extract etcd server URLs from API server arguments

## CLI Interface
```
python agent.py [--kubeconfig ~/.kube/config] encrypt
python agent.py access --endpoint https://127.0.0.1:2379 [--cert client.crt --key client.key --cacert ca.crt]
python agent.py secrets
python agent.py tls
python agent.py full [--endpoint https://127.0.0.1:2379]
```

## Core Functions

### `check_etcd_encryption(kubeconfig)` ÔÇö Verify encryption at rest
Inspects kube-apiserver pod args for `--encryption-provider-config`, audit logging, TLS.

### `check_etcd_access(endpoint, cert, key, cacert)` ÔÇö Test access controls
Uses etcdctl to check health and test for unauthenticated read access.
CRITICAL finding if data readable without credentials.

### `dump_secrets_check(kubeconfig)` ÔÇö Audit stored secrets
Lists all cluster secrets, categorizes by type, identifies sensitive naming patterns.

### `check_etcd_tls_config()` ÔÇö Verify TLS certificates
Checks etcd pod args for peer TLS, client TLS, and client certificate authentication.

### `full_assessment(kubeconfig, endpoint)` ÔÇö Comprehensive security scan
Combines all checks into single report with risk level classification.

## Security Checks
| Check | Flag | Risk |
|-------|------|------|
| Encryption at rest | --encryption-provider-config | CRITICAL if missing |
| Client TLS | --cert-file / --key-file | HIGH if missing |
| Peer TLS | --peer-cert-file / --peer-key-file | HIGH if missing |
| Client cert auth | --client-cert-auth=true | MEDIUM if missing |
| Unauthenticated access | etcdctl get without certs | CRITICAL |

## Dependencies
System: kubectl, etcdctl (etcd client)
No Python packages required.
