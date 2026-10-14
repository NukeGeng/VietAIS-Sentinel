# ADR-0001 — Independent engine and reviewable foundation

Owner: NukeGeng
Status: accepted — repository foundation
Last verified: 2026-10-14.

## Context

VietAIS is rebuilding its public AI engine separately from its private commercial platform.
The previous architecture and measurements must not be silently inherited.

## Decision

Start with a new Python 3.11/3.12 src-layout package, FastAPI metadata transport, strict observation
contracts and CI. Keep heavy vision/training dependencies outside the base runtime until a reviewed
adapter task pins their versions and tests them. No legacy source or Git history is imported.
Store technical documentation with code and organize feature pages by capability.

## Alternatives

Porting the old service would preserve hidden coupling. Shipping an apparently complete service
with stub detections would misrepresent readiness. Both are rejected for this bootstrap.

## Consequences

The first checkout runs without a GPU but does not analyze frames.
Readiness remains unavailable. Models, hosted controls and training are separate tasks.

## Revisit

Review Python/runtime support when YOLO26 and MediaPipe versions are pinned.
An API replacement, legacy import, or core dependency reversal requires a new/superseding ADR.
