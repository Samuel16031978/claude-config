# Workflows

## Workflow 1: Osquery Fleet Deployment
```
[Install FleetDM server] ÔåÆ [Generate enrollment secret]
  ÔåÆ [Package osquery with fleet config] ÔåÆ [Deploy to pilot group]
  ÔåÆ [Verify enrollment and scheduled queries] ÔåÆ [Deploy to production]
  ÔåÆ [Create dashboards from query results] ÔåÆ [Ongoing monitoring]
```

## Workflow 2: Threat Hunt with Osquery
```
[Define hypothesis] ÔåÆ [Write SQL query targeting hypothesis]
  ÔåÆ [Execute via FleetDM live query across fleet]
  ÔåÆ [Analyze results] ÔåÆ [Investigate anomalies]
  ÔåÆ [Document findings] ÔåÆ [Create scheduled detection if recurrent]
```
