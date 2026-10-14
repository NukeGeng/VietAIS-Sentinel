# Observation schema 1.0

Owner: NukeGeng
Status: implemented — pre-release schema, no inference transport
Last verified: 2026-10-14; [contract tests](../../tests/test_contracts.py).

The canonical schema is [contracts.py](../../src/vietais_sentinel/core/contracts.py).
JSON Schema may be generated from the Python model; do not maintain handwritten duplicate DTOs.

## Fields and meaning

- context: opaque attempt/source references, connection epoch, nonnegative integer sequence,
  timezone-aware captured_at normalized into the agreed time domain before validation.
- analyzed_at: timezone-aware; cannot precede normalized captured_at.
- analysis_status: ok, invalid_input, model_unavailable, error, overload or deadline_exceeded.
- detections: phone/person, finite confidence in [0,1], normalized positive-area boxes.
- provenance: model identifier, weights SHA-256, pipeline version and effective config SHA-256.
- schema_version: 1.0. Unexpected fields and unknown statuses are rejected.

Successful analysis requires provenance. Failed analysis cannot carry successful detection output.
An empty successful detection list means no reported target detection for that frame, not no cheating.
There are no gaze fields, score, risk threshold, disciplinary verdict or evidence lifecycle yet.
This is an observation schema, not an HTTP frame-upload specification.

## Trust and source isolation

References are caller correlation values, not grants. A hosted deployment must authenticate the
caller and authorize source ownership; schema validation cannot perform that job.
Device clock normalization and reconnect/source mapping require an explicit integration contract.

## Versioning

This package is pre-release. Changes to public fields or meaning require a PR, compatibility notes,
schema/test updates and a version decision. An eventual stable API must define deprecation behavior.
Never assume the private platform can follow arbitrary main-branch changes.
