# ADR-0002 — YOLO26, MediaPipe and open engine licensing

Owner: NukeGeng
Status: accepted direction; implementation and artifact review pending
Last verified: 2026-10-14, choices from project owner.

## Decision

YOLO26 is the provisional object detector. MediaPipe is the proposed face-landmark foundation;
gaze/head-pose estimators and temporal interpretation are separate components to validate.
New engine code is licensed AGPL-3.0-only. The full engine and its pipeline modifications are public;
the private platform is a separate product.

## Not implied

No trained model, dataset, accuracy, inference capacity or deployed license boundary is approved
by selecting these technologies. A different library or model export does not erase upstream rights.
Review code, weights, datasets, notices and actual platform integration before distribution.
No third-party weights are bundled. Code licensing does not authorize sharing private recordings.

## Alternatives and review trigger

RF-DETR remains a possible evaluated alternative, not a second shipped detector.
Changing the detector, licensing arrangement or engine/platform coupling requires an ADR and evidence.
A future permissive dependency does not require changing our own engine license automatically.

## References

[Ultralytics YOLO26](https://docs.ultralytics.com/models/yolo26/)
[Ultralytics licensing](https://www.ultralytics.com/license)
[MediaPipe Face Landmarker](https://developers.google.com/edge/mediapipe/solutions/vision/face_landmarker)
