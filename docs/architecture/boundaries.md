# System boundaries

Owner: NukeGeng
Status: accepted direction; only the foundation is implemented
Last verified: 2026-10-14, architecture direction confirmed in project discussion.

## Public engine

All engine pipelines belong here: model adapters, preprocessing, feature extraction,
temporal analysis, explanation, API, tests, training/evaluation tooling and self-host documentation.
The engine must work without VietAIS SaaS accounts, tables, billing or UI.
Model artifacts and data have their own rights and provenance gates.

## Private platform (outside this repository)

Rust media/local-storage core; .NET/FullStackHero business modules; Marten projections;
Vue web/mobile interfaces; Swift macOS and a Windows host still to be selected.
The platform owns verified tenant/device grants, exam policy, evidence retention/review and billing.
Nothing here claims these private services have been implemented.

## Dependency direction

API and future model adapters depend on core contracts. Core does not import FastAPI,
Ultralytics, PyTorch or private platform implementation.
The architecture tests cover this narrow import boundary, not all distributed-system properties.

Weights may be shared for inference; mutable tracking/calibration must be isolated per source.
Caller references are not authentication. Hosted deployment requires identity, admission control,
bounded bytes/queues, correct task lifetime, idempotency and error reporting before analysis exposure.
Authentic observations are inputs to policy and human review, not proof of cheating.

## Event and data ownership

The platform owns durable business/evidence events and projections, not the detector.
Do not store every raw image or high-rate landmark as a business event by default.
Define replay, duplication, late arrival, cancellation and coverage-gap behavior before implementation.
Marten projection rebuild does not rerun model inference or recover missing recordings.
