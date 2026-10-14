# VietAIS Sentinel — instructions for contributors and AI agents

This file is the single source of repository working rules. Read [docs/README.md](docs/README.md),
the current feature document, relevant ADRs, and the task acceptance criteria before editing.
Do not treat an archived plan or chat message as an implemented feature.

## Scope and truth

- This repository is the standalone public AI engine, including its pipelines.
- Backend business logic, billing, school accounts, web, desktop and mobile belong elsewhere.
- Current stage: foundation only. YOLO26 and MediaPipe adapters are not implemented.
- Never claim a model capability, benchmark, production readiness or completed test without evidence.
- Analysis failure is not a clean result. The engine reports observations, not disciplinary verdicts.
- New architecture, dependencies, public contract changes and model/data releases need owner review.
- No subagents unless the human explicitly requests delegation.

## Architecture

- Core contracts cannot import HTTP transport, detector libraries or SaaS implementation.
- Transport and adapters depend on core; they must not become a second policy implementation.
- Mutable tracking/calibration state belongs to a source stream, not a shared model singleton.
- Normalize source timestamps explicitly; arrival order is not a temporal model.
- Authenticate hosted callers separately from opaque attempt/source references.
- Bound request bytes, decoded images, in-flight inference and queues before exposing inference.
- API schemas in code are canonical; export/generate client artifacts rather than hand-copying them.

## Workflow

1. Check branch and working tree; preserve other people's changes.
2. One task / one reviewable outcome; record scope and acceptance checks.
3. Use feature/fix branches and a pull request. Do not directly push main, self-approve or auto-merge.
4. Code, tests, feature documentation and DONE/BUGS move together.
5. An architecture change requires an ADR; proposed is not accepted.
6. Handover: entry point, data flow, state owner, failures, test evidence and remaining debt.
7. Do not copy legacy source/history or customer media without review of provenance and rights.

## Local verification

```bash
uv sync --locked --dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest -q
uv run --locked python tools/check_repository.py
uv build
```

## Git identity and artifacts

- Expected author: NukeGeng <haovygamer@gmail.com>; stop and ask if config differs.
- Do not override author/committer or change Git identity unless the human explicitly authorizes it.
- No AI co-author trailer. Commit messages: Vietnamese, type(scope): description.
- No real .env, credentials, private keys, customer/student images or model weights in Git.
- Dataset/model metadata may be public only after rights and privacy review.
- Never rewrite shared history or force-push without explicit authority.
