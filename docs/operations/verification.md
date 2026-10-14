# Verification record

Owner: NukeGeng
Status: local verification and foundation CI passed
Last verified: 2026-10-14, codex/bootstrap-oss.

## Scope

Only the foundation package, metadata routes, schema validation and repository controls.
No YOLO26/MediaPipe inference, real frames, model training, phone accuracy, WAN or GPU capacity measured.

## Local

Environment: macOS arm64, Python 3.11.15, uv 0.12.5; dependencies recorded in uv.lock.

| Command | Actual result |
|---|---|
| uv sync --locked --dev | Dependency lock usable; no vision weights downloaded |
| uv run --locked ruff check . | Passed |
| uv run --locked ruff format --check . | Passed |
| uv run --locked pytest -q | 28 passed, no warnings, 0.22 seconds |
| uv run --locked python tools/check_repository.py | Passed; 43 repository files checked |
| uv build | Wheel and source distribution built successfully |

The first test run exposed a Starlette TestClient deprecation for httpx. Development dependencies
now use the supported httpx2 client; the repeated run above had no warnings.
Docker CLI is present but the local Docker daemon is not running. A local container build/smoke
was therefore not performed. Linux container and Python 3.12 checks are delegated to CI and are
not claimed as passed until their actual results are available.

## CI

On foundation commit 4c7f2395f4237816210dad1cea54df9a6af3d122, all three Linux jobs passed:
Python 3.11, Python 3.12 and container build/smoke.
[CI evidence](https://github.com/NukeGeng/VietAIS-Sentinel/actions/runs/38542967959).
Container smoke verified HTTP 200 liveness and HTTP 503/ready=false as intended.
These results cover that commit; subsequent changes require their own successful checks.
Branch protection, required reviews and release permissions are not configured by this bootstrap.
