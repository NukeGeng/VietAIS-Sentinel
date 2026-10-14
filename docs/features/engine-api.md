# F-API-001 — Engine metadata API

Owner: NukeGeng
Status: implemented — foundation only
Last verified: 2026-10-14; [tests](../../tests/test_api.py).

## Actor and scope

Self-host operator or integrating developer checks process health and capability availability.
No tenant, exam, account or frame-analysis business endpoint exists.

## Contract and behavior

| Route | Result |
|---|---|
| GET /health/live | HTTP 200, process alive and package version |
| GET /health/ready | HTTP 503, ready=false because adapters are absent |
| GET /v1/capabilities | HTTP 200, API/engine version and all analysis capabilities false |
| GET /openapi.json | Generated schema; readiness response includes 503 |

Liveness does not prove GPU/model readiness. There is no fake analysis route.
The metadata endpoints are public and carry no student data; they are not an authentication design
for a future hosted analysis service. Do not deploy this bootstrap as an exam processing service.

## Implementation and checks

[HTTP app](../../src/vietais_sentinel/api/app.py), [tests](../../tests/test_api.py).
Run instructions: [local development](../operations/local-development.md).
Future inference needs a separate feature spec and hosted/self-host trust-boundary decision.
