# API Reference ÔÇö Performing ICS Asset Discovery with Claroty

## Libraries Used
- **requests**: HTTP client for Claroty xDome / CTD REST API

## CLI Interface
```
python agent.py --url <claroty_base_url> --token <api_token> assets [--type PLC] [--limit 100]
python agent.py --url <claroty_base_url> --token <api_token> vulns [--severity critical] [--limit 100]
python agent.py --url <claroty_base_url> --token <api_token> alerts
python agent.py --url <claroty_base_url> --token <api_token> topology
```

## ClarotyClient Class

### `get_assets(asset_type, limit)` ÔÇö Retrieve OT/IoT assets
**Endpoint:** `GET /api/v1/assets`
Filters by type: PLC, HMI, RTU, EWS, Switch, Sensor.

### `get_asset_detail(asset_id)` ÔÇö Detailed asset information
**Endpoint:** `GET /api/v1/assets/{id}`

### `get_vulnerabilities(severity, limit)` ÔÇö OT vulnerability list
**Endpoint:** `GET /api/v1/vulnerabilities`

### `get_alerts(status, limit)` ÔÇö Security alerts
**Endpoint:** `GET /api/v1/alerts`

### `get_network_segments()` ÔÇö Network segmentation map
**Endpoint:** `GET /api/v1/network/segments`

## Core Functions

### `discover_assets(...)` ÔÇö Categorize assets by type, vendor, criticality
### `assess_vulnerabilities(...)` ÔÇö Prioritize OT vulnerabilities by severity
### `get_alerts_summary(...)` ÔÇö Summarize active security alerts
### `network_topology(...)` ÔÇö Map Purdue model network zones

## Authentication
Bearer token via `Authorization: Bearer <token>` header.

## Dependencies
```
pip install requests
```
