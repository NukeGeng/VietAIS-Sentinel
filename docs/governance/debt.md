# Debt and release blockers

Owner: NukeGeng
Status: active register
Last verified: 2026-10-14.

| ID | Impact | Owner | Resolve before | Exit evidence |
|---|---|---|---|---|
| D-001 | No detector/landmark implementation | NukeGeng | Analysis alpha | Adapter tests + model provenance + actual readiness |
| D-002 | No validated data or capacity result | NukeGeng | Any accuracy/capacity claim | Frozen protocol, real measurements and limits |
| D-003 | Hosted identity/limits/state unresolved | NukeGeng | Exposing hosted analysis | Trust design, isolation and overload/retry tests |
| D-004 | GitHub required reviews/checks not enforced here | NukeGeng | Collaborative protected release | Verified repository settings |
| D-005 | Container base tag not digest-pinned | NukeGeng | Production image release | Reviewed image digest and vulnerability policy |
| D-006 | No dependency audit/secret scanner gate yet | NukeGeng | Model/hosted alpha release | Reviewed scanner scope, tests and CI evidence |

These are explicit limitations, not excuses to mark the service production-ready.
Do not add arbitrary deadlines without an owner commitment; each item has a release trigger.
