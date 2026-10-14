# Local development

Owner: NukeGeng
Status: implemented instructions for foundation
Last verified: 2026-10-14; [verification](verification.md).

## Requirements

Python 3.11 or 3.12, Git and uv. GPU, Ultralytics, MediaPipe, cloud credentials and SaaS accounts
are not required for this foundation.

```bash
uv sync --locked --dev
uv run --locked uvicorn vietais_sentinel.api.app:app --host 127.0.0.1 --port 8001
```

Open http://127.0.0.1:8001/docs. Liveness returns 200, readiness returns 503 by design.
Do not interpret that 503 as a broken install; adapters do not exist yet.

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest -q
uv run --locked python tools/check_repository.py
uv build
```

## Container

```bash
docker build -t vietais-sentinel:foundation .
docker run --rm -p 127.0.0.1:8001:8001 vietais-sentinel:foundation
```

Runs as UID/GID 10001. No model is downloaded and no volumes/secrets are required.
This container is a metadata foundation, not a production analysis deployment.
The base image is a version-family tag, not yet a reviewed digest.
