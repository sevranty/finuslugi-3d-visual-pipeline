# 3DP task contract

## Project

```text
PROJECT_ID: 3D_VISUAL_PIPELINE
SHORT_ID: 3DP
REPOSITORY_URL: https://github.com/sevranty/3d-visual-pipeline
TASKS_URL: https://github.com/sevranty/3d-visual-pipeline/issues
DEFAULT_BRANCH: main
HANDOFF_MODE: delta-only
```

## Source order

1. Current user instruction
2. Current Issue `TASK_CONTEXT`
3. This file
4. `docs/decisions/0002-web-factory-os-orchestration.md`
5. `AGENTS.md`
6. Runtime source `skills/3d-visual-pipeline/SKILL.md`

## Execution boundary

- One Issue, one task branch, one Draft PR
- Confirm current `main` and exact task HEAD before every lifecycle write
- Write only inside the selected Issue `WRITE_SCOPE`
- Relations never grant cross-repository write access
- Record commands, exit codes, exact SHA, checks, review and merge evidence

## Protected resources

Runtime semantics, style versions, governed assets, historical tags and releases, secrets, environments, production and DNS stay unchanged unless the current Issue explicitly authorizes them.

## Orchestration

WebFactoryOS owns routing, registries, relations and naming grammar. 3DP owns implementation, validation and release evidence. See `docs/decisions/0002-web-factory-os-orchestration.md`.