# Contributing to VietAIS Sentinel

Start with [AGENTS.md](AGENTS.md) and [the documentation index](docs/README.md).
The first milestone is a tested, documented engine foundation, not a port of the legacy monorepo.

## Development and pull requests

Use Python 3.11 or 3.12 and uv. Run the verification commands in AGENTS.md.
Branch from the current main; submit one focused PR, document affected features and obtain human review.
Do not directly push main or merge your own PR. The owner configures required checks separately.
Ownership/permission/lifecycle changes must include explicit failure and isolation tests.
Changing a public schema requires a versioning decision and contract tests.

## AI-assisted contributions

Declare task scope before coding and hand over entry points, state ownership, errors and evidence.
AI may propose an ADR but may not silently accept it on behalf of the owner.
A passing test suite is not proof of model accuracy or production capacity.

## Code, model and data contributions

New code is contributed under AGPL-3.0-only. Keep third-party notices.
Do not import code unless its license and authorship permit the contribution.
Do not upload proprietary models, customer recordings, face images or credentials.
Model/data submissions need provenance, permitted uses, hashes and evaluation evidence.
Opening engine code does not grant permission to publish someone else's recordings or weights.
No Contributor License Agreement or alternative commercial relicensing arrangement is introduced here.

## Vulnerability reports

For sensitive reports, do not post credentials, student media or an exploit against a live customer.
Use the repository owner's private contact or GitHub private reporting if the owner enables it.
Private reporting has not been enabled or verified by this bootstrap.
