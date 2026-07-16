# ADR 0002 - WebFactoryOS orchestration boundary

## Status

Accepted

## Decision

WebFactoryOS is the external orchestration source for project routing, registries, relations and naming grammar.

The `3d-visual-pipeline` repository remains the sole source for plugin code, skill contracts, assets, validators, tests, release files and execution evidence.

A relation to another repository does not grant write access. WebFactoryOS is not a runtime, build, test, package, reusable-workflow, API or release dependency.

## Local contract

- `TASK.md` stores stable 3DP constants and local execution rules
- each Issue stores task-specific scope, protected resources and `DONE_WHEN`
- `AGENTS.md` points to the local and runtime sources without copying them
- handoff is delta-only

## Consequences

3DP can build, validate, install and release from a clean checkout without network access to WebFactoryOS. Global WFO policy is linked, not vendored or duplicated.