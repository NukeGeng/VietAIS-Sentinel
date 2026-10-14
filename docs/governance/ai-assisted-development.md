# Six controls for AI-assisted development

Owner: NukeGeng
Status: repository working policy; automated coverage is limited
Last verified: 2026-10-14.

## 1. Comprehension and technical debt

One task/PR has one outcome, owner, scope, exclusions, entry point, data/state flow, failure behavior
and acceptance tests. Handover must distinguish implemented, verified, planned and blocked.
Record debt with impact, owner, deadline/trigger and an exit test in [the debt register](debt.md).
An AI-written test passing is not independent proof; sensitive logic needs adversarial and contract tests.

## 2. Architecture and workflow drift

Follow accepted ADRs and module boundaries. New dependencies, storage authority, schemas and
state/workflow changes require review. Record choices in an ADR, not only chat.
Architecture tests enforce the core import boundary; scheduler, state and distributed invariants
need integration tests as those components are implemented.
Base/runtime upgrades are dedicated tasks, not incidental fixes in an unrelated feature.

## 3. Documentation loss and stale claims

Technical documents travel with code in Git. Use docs/README.md as the entry point.
Feature status, owner and verification scope are mandatory. Archive superseded designs explicitly.
A date alone does not prove accuracy. Check links automatically and content against code/evidence.
Never claim a passed remote check or model metric just because a workflow/report template exists.

## 4. Feature-oriented documentation

One canonical page per capability links requirements, actors, trust scope, workflow/state, API/events,
code, tests, failure paths and operations. Do not create independent backend/frontend versions.
Small features do not need every template. Export contracts from code rather than copy schemas.

## 5. Model/data lineage

Follow [provenance requirements](../ml/provenance.md). Raw data, labels, train config,
evaluation and deployment config have distinct versions. Resolve licenses/privacy before sharing.
Never substitute synthetic fixtures for a published accuracy or fairness result.

## 6. Actors, access and tenancy

The standalone engine owns observations; the platform owns people, tenant roles and exam policy.
Hosted engine authorization still needs caller/source grants, resource limits and isolation.
Client-supplied tenant/source IDs are not authority. API, jobs, caches and storage need consistent scope.
Platform roles should compose capabilities plus resource/tenant/assignment conditions.
Platform super-admin operations must not imply unrestricted access to student evidence.
Review these responsibilities before publishing any analysis endpoint.

## Definition of Ready

Goal, feature, owner, boundaries, trust scope, state/contract, failure modes and acceptance are recorded.
Unresolved architecture or model/data rights decisions are visible, not silently assumed.

## Definition of Done

Code + tests + feature documentation + DONE/BUGS are consistent. Actual verification evidence,
compatibility/rollback and remaining debt are attached to the PR. A human reviews before merge.

## Enforcement limits

CI currently checks lint/format, foundation tests, one import boundary, local Markdown links,
documentation metadata and prohibited artifact paths/extensions/size.
It is NOT a credential scanner, semantic documentation checker, license audit or full security audit.
Required branch checks, reviewer enforcement and private vulnerability reporting are GitHub settings
that the owner must enable; this bootstrap does not claim they are active.
