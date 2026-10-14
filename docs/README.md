# Documentation index

Owner: NukeGeng
Status: implemented — foundation documentation
Last verified: 2026-10-14, bootstrap scope; see [verification](operations/verification.md).

Read this index before selecting a plan. Documentation status is not model readiness.

| Area | Canonical document | Scope |
|---|---|---|
| Current state | [STATUS](STATUS.md) | Implemented, planned, blocked |
| Architecture | [Boundaries](architecture/boundaries.md) | Public engine and private platform |
| Accepted decisions | [ADR-0001](decisions/0001-independent-engine.md), [ADR-0002](decisions/0002-model-license-direction.md) | Foundation and selected model/license direction |
| AI-assisted workflow | [Governance](governance/ai-assisted-development.md) | Six failure modes and merge gates |
| Engine API | [API feature](features/engine-api.md) | Health/capability routes |
| Object detection | [Object detection](features/object-detection.md) | YOLO26 work not implemented |
| Face and temporal signals | [Behavior signals](features/behavior-signals.md) | MediaPipe work not implemented |
| Contract | [Observation contract](contracts/observations.md) | Canonical Python schema |
| Model/data lineage | [Provenance](ml/provenance.md) | Required release evidence |
| Operations | [Local development](operations/local-development.md), [Verification](operations/verification.md) | Run and verify |
| Delivery | [Roadmap](ROADMAP.md), [Debt](governance/debt.md) | Ordered work and blockers |
| Templates | [Task](templates/task.md), [ADR](templates/adr.md), [Model run](templates/model-run.md) | Copy when needed |

Rules: code contracts are canonical for implemented fields; accepted ADRs define intended boundaries.
If code and design differ, record the discrepancy and review it; do not quietly rewrite either.
Keep one canonical feature page with links, not copies of the same specification per technology.
Private customer material is never placed here. Old research numbers require separate provenance.
