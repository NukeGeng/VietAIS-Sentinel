# Model and dataset provenance

Owner: NukeGeng
Status: required release policy; tooling not implemented
Last verified: 2026-10-14.

## Dataset record

Record dataset ID/version, source, permitted uses, consent/access basis, retention, manifest hashes,
annotation schema/instructions, annotators, QA corrections and original recording groups.
Split by participant/recording before frames. Include device/environment and front/room camera slices.
Test data must not tune thresholds or determine training changes without a new evaluation protocol.
Customer recordings are not automatically training data or publishable OSS fixtures.

## Training run record

Record code commit and dirty-state indicator, environment lock, model/pretrained hash,
dataset/split manifest hashes, effective hyperparameters, seed, hardware, start/end times,
logs and output checkpoint hashes. Log actual values after defaults/overrides are resolved.
Training, evaluation and inference should have separate dependency/environment records.
Reproducibility includes known GPU nondeterminism; do not promise bit-identical results without proof.

## Evaluation and deployment

Record protocol, frozen test split, thresholds selected on validation, per-class and event metrics,
negative results, confusion examples, latency/throughput and RAM/VRAM measurement scope.
A deployment manifest binds model hash, pipeline/code version, preprocessing/class map,
precision, calibration/threshold config hash and evaluation report.
Each observation refers to that lineage. Model release approval is a human gate.

## Tooling direction

Consider DVC for artifact/data versions and MLflow for runs; neither is installed in this bootstrap.
Use [the model-run template](../templates/model-run.md) initially.
Large artifacts live in access-controlled artifact storage; Git holds reviewed manifests only.
No default retention, cloud provider or permission to publish weights/data is decided here.
