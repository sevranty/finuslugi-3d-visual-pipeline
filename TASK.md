# 3D Visual Pipeline task contract

## Project constants

```yaml
PROJECT_ID: 3D_VISUAL_PIPELINE
SHORT_ID: 3DP
TASK_PROFILE: execution
REPOSITORY_URL: https://github.com/sevranty/3d-visual-pipeline
TASKS_URL: https://github.com/sevranty/3d-visual-pipeline/issues
handoff_mode: delta-only
```

## Source order

1. `skills/3d-visual-pipeline/SKILL.md` is the runtime source of truth.
2. `docs/decisions/0002-web-factory-os-orchestration.md` defines the local WebFactoryOS orchestration boundary.
3. This file defines compact project constants and task intake rules.
4. WebFactoryOS canonical files are orchestration references only:
   - https://github.com/sevranty/web-factory-os/blob/main/AGENTS.md
   - https://github.com/sevranty/web-factory-os/blob/main/TASK.md
   - https://github.com/sevranty/web-factory-os/blob/main/docs/governance/ISSUE_CONTRACTS.md
   - https://github.com/sevranty/web-factory-os/blob/main/docs/NAMING_CONVENTION.md

## Local write boundary

3DP owns plugin and skill code, assets, validators, releases, issue intake, PR evidence, and execution results in this repository. WebFactoryOS owns routing, registry, relations, naming grammar, and orchestration status outside this repository.

Relations never grant write access. WebFactoryOS is not a runtime, build, test, release, workflow, package, API, or deployment dependency.

## Branch and PR rule

Each execution task uses a repository-local branch and pull request. The pull request must link the local 3DP issue, record base and final HEAD, list changed files, include validation evidence, and stay draft until exact-HEAD review is complete.
