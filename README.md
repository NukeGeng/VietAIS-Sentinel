# VietAIS Sentinel

Open-source AI engine for explainable exam proctoring, combining object detection, gaze and
head-pose estimation, and temporal behavior analysis.

**Stage: foundation / pre-alpha. This checkout does not analyze frames yet.**

The engine is being rebuilt independently from the private VietAIS SaaS platform. The complete
engine pipelines belong in this repository. This is not an LMS, desktop/mobile app or tenant backend.
YOLO26 is the provisional detector; MediaPipe is the face-landmark direction. Their adapters,
training data and quality/capacity results have not been implemented or validated here.

## Available now

- Standalone Python package and FastAPI health/capability endpoints.
- Versioned observation contracts: explicit analysis failures, source context and model/config hashes.
- Foundation/architecture tests, locked dependencies and CI configuration.
- Feature-oriented documentation and AI-assisted contribution/review rules.

Inference readiness returns **503**, capabilities remain **false**, and no fake analysis endpoint
returns reassuring zero detections. Process liveness is not model readiness.

## Quick start

Python 3.11/3.12 and uv; no GPU, model download, cloud credential or SaaS account needed.

```bash
uv sync --locked --dev
uv run --locked uvicorn vietais_sentinel.api.app:app --host 127.0.0.1 --port 8001
```

Open http://127.0.0.1:8001/docs. For tests and Docker see
[local development](docs/operations/local-development.md).

## Documentation and contribution

Start with [docs/README.md](docs/README.md), [STATUS](docs/STATUS.md),
[ROADMAP](docs/ROADMAP.md) and [CONTRIBUTING](CONTRIBUTING.md).
AI contributors must read [AGENTS.md](AGENTS.md); design changes require a reviewed ADR.
[Verification](docs/operations/verification.md) distinguishes local evidence from pending CI.

## License and data

New engine code is licensed **AGPL-3.0-only**; see [LICENSE](LICENSE).
Third-party models/dependencies/datasets retain their own terms. No weights or customer recordings
are bundled. Review provenance and rights before publishing artifacts or importing legacy source.
Observations support human review; they are not automatic proof of misconduct.

## Tiếng Việt

VietAIS Sentinel là engine AI OSS độc lập; nền tảng SaaS, backend nghiệp vụ, web, desktop và mobile
được phát triển riêng. Repo hiện chỉ có nền móng chạy/kiểm tra được, không phải bản AI production.
Tài liệu kỹ thuật đi cùng code; không kế thừa số liệu hay kết luận của hệ thống cũ khi chưa đo lại.
