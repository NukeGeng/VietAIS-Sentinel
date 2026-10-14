# Current status

Owner: NukeGeng
Status: implemented — status inventory
Last verified: 2026-10-14, foundation.

| Component | Status | Evidence / next gate |
|---|---|---|
| Package and API metadata | Implemented | [API tests](../tests/test_api.py) |
| Observation schema | Implemented, pre-release | [Contract tests](../tests/test_contracts.py) |
| Documentation and CI configuration | Implemented | [Verification](operations/verification.md) |
| YOLO26 adapter | Planned | Pin dependency, weights provenance and adapter tests |
| MediaPipe adapter | Planned | Source isolation and calibration protocol |
| Temporal fusion / explanation | Planned | Ground truth, baselines, timestamps and evaluation |
| Training and evaluation tooling | Planned | [Provenance requirements](ml/provenance.md) |
| Hosted auth / scheduler / limits | Planned, analysis release blocker | Security and overload tests |
| Production release | Not ready | No validated inference, dataset or capacity result |

No model inference endpoint is published by this foundation. The process can be alive while
inference readiness is false. Every capability remains false until its implementation is verified.
The legacy project's test counts, gaze/phone results and capacity estimates are not v2 evidence.
