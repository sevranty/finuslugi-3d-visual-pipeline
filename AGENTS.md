# Agent contract

Use `skills/3d-visual-pipeline/SKILL.md` as the runtime source of truth.

Required order: input validation, reference mapping, locks, Scene Specification, asset gate, style selection, runtime routing, generation or edit, visual QA, targeted repair, finalization, and visible delivery.

Do not weaken validators, bypass asset governance, hide fallback behavior, or claim completion without a visible deliverable and recorded evidence.


## Orchestration adapter

Project constants, task intake, and branch/PR rules are in `TASK.md`. The WebFactoryOS boundary is recorded in `docs/decisions/0002-web-factory-os-orchestration.md`; WebFactoryOS is an orchestration source only and is not a runtime, build, test, release, workflow, package, API, or deployment dependency.
