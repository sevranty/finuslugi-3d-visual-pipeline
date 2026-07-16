# ADR 0002: WebFactoryOS orchestration boundary

## Status

Accepted.

## Context

The 3d-visual-pipeline repository is tracked under WebFactoryOS orchestration for routing, registry, relation, naming, and status coordination. The local project must keep its execution contract complete and runnable without introducing WebFactoryOS as a runtime, build, test, release, workflow, package, API, or deployment dependency.

Active local metadata uses PROJECT_ID: 3D_VISUAL_PIPELINE and SHORT_ID: 3DP. Earlier identifiers are historical only and must not be introduced as active identity.

## Decision

- WebFactoryOS owns orchestration source data: routing, registry, relations, naming grammar, and orchestration status.
- 3d-visual-pipeline owns plugin code, skill code, assets, validators, release materials, execution evidence, and repository-local issue intake.
- Relations document coordination only. A relation never grants write access to this repository or from this repository to another repository.
- WebFactoryOS is not imported, vendored, invoked, or required by runtime, CI, tests, validation, release, deployment, or local development commands.
- This repository stores a compact local adapter in [TASK.md](../../TASK.md), links to canonical WebFactoryOS references, and does not copy global WebFactoryOS registries or policy bodies.

## Local write boundary

Allowed local orchestration-adapter files are:

- `AGENTS.md`
- `README.md`
- [TASK.md](../../TASK.md)
- this ADR
- `.github/ISSUE_TEMPLATE/01-execution.yml`

Protected resources remain owned by the product/runtime contract and must not be changed for orchestration adapter work:

- `.codex-plugin/**`
- `skills/3d-visual-pipeline/**`
- `assets/**`
- `release/**`
- historical commits and tags
- repository settings, secrets, environments, production, deployment, and DNS

## Consequences

Execution work can proceed locally using the skill, validators, issue form, and PR template in this repository. WebFactoryOS may point to the work and record relations, but final repository evidence is produced and reviewed in 3d-visual-pipeline.
