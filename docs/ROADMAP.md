# Roadmap

Owner: NukeGeng
Status: proposed delivery order; foundation implemented
Last verified: 2026-10-14.

1. Foundation: standalone package, metadata API, schemas, documentation and CI (this PR).
2. Hosted/self-host trust and source lifecycle design: admission limits, normalization, retries,
   readiness, authentication boundary and implementation task scopes.
3. YOLO26 adapter alpha: pin compatible dependencies, artifact provenance, tests and golden inputs.
4. MediaPipe/head-pose/gaze: source isolation, calibration, quality/unknown states and evaluated outputs.
5. Dataset/training/evaluation pipeline: independent labels, grouped splits, repeatable model releases.
6. Temporal interpretation/explanation: baselines, time windows, false alerts and documented limits.
7. Standalone/self-host integration and managed hosting: contract tests, load, security and observability.
8. Release approval: code/model/data licensing, OSS source offer, capabilities and honest model card.

No delivery dates or quality/capacity thresholds have been approved yet.
Do not bypass the design and provenance gates by porting the complete legacy service.
