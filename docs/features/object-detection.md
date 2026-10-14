# F-VISION-001 — YOLO26 observations

Owner: NukeGeng
Status: planned — not implemented
Last verified: 2026-10-14, design requirements only.

## Purpose

Return phone/person boxes with provenance, not a misconduct judgment.

## Before coding

Pin a supported Ultralytics version and YOLO26 variant; document the pretrained checkpoint,
license, hash, class map, preprocessing, precision and effective thresholds.
Create an adapter behind core contracts. Do not import legacy phone confidence values as validated
v2 defaults. Decide batching, cancellation, deadlines and memory limits before exposing requests.

## Acceptance plan

- Real model availability is required for readiness; missing/broken weights give explicit failure.
- Check color order, original-image coordinates, class names and confidence candidates.
- Invalid/oversized images are rejected before uncontrolled decode/inference.
- Model/config hashes accompany successful observations.
- Test phone-like hard negatives, small/occluded phones and front/room camera conditions.
- Measure latency/throughput/RAM/VRAM with declared hardware and full pipeline boundaries.
- Report false alerts and event recall, not only frame counts or COCO AP.

## Dependencies and ownership

[Observation contract](../contracts/observations.md), [model/data lineage](../ml/provenance.md).
Hosted authorization, admission limits and resource fairness must be explicitly designed.
No model/data is downloaded or bundled in the foundation.
