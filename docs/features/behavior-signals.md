# F-BEHAVIOR-001 — Face, gaze, head pose and temporal signals

Owner: NukeGeng
Status: planned — not implemented
Last verified: 2026-10-14, design requirements only.

## Purpose

MediaPipe landmarks support gaze/head-pose estimation; they do not classify intent by themselves.
Separate head yaw/pitch/roll, eye direction, face visibility, blink signals and temporal interpretation.
Prioritize the front-facing source for gaze; room-camera inputs need different quality expectations.

## Before coding

Specify model bundle/version/hash, coordinate and mirror conventions, calibration artifacts,
per-source state ownership and disposal, capture-time normalization, sampling and gap handling.
Gaze/head-pose output fields require a reviewed contract extension; they are not in schema 1.0.

## Acceptance plan

- Interleaved participants/sources never reuse another person's tracking/calibration.
- Out-of-order frames, reconnect epochs, duplicates and gaps have defined behavior.
- Insufficient face/eye quality yields unknown/unavailable, not a confident direction.
- Head pose is not treated as eye direction.
- Natural writing/reading/movement is included in evaluation.
- Split by participant/recording; measure direction error, coverage and false alerts.
- Any temporal classifier/calibration/explanation has independent evidence and limitations.
- No assertion that LSTM or a legacy AIS formula must win; compare justified baselines.

See [boundaries](../architecture/boundaries.md) and [provenance](../ml/provenance.md).
