# ADR-0001: Use a skill-only Codex plugin

- Status: accepted
- Date: 2026-07-15
- Issues: #1, #2

## Context

The repository must distribute one canonical Finuslugi visual-production skill while remaining compatible with the current Codex plugin model. A root-level standalone `SKILL.md` would be convenient for a local repository but would not provide the explicit plugin manifest and packaging boundary required for a reusable public plugin.

## Decision

Use a skill-only plugin structure:

```text
.codex-plugin/plugin.json
skills/finuslugi-3d-visual-pipeline/SKILL.md
skills/finuslugi-3d-visual-pipeline/agents/openai.yaml
skills/finuslugi-3d-visual-pipeline/references/
skills/finuslugi-3d-visual-pipeline/assets/
skills/finuslugi-3d-visual-pipeline/scripts/
skills/finuslugi-3d-visual-pipeline/evals/
```

The plugin manifest is the distribution boundary. `SKILL.md` is the runtime orchestration entry point. Detailed rules remain in canonical references and machine contracts.

## Consequences

- Installation and versioning happen at plugin level.
- Additional skills may be added later without changing the root packaging model.
- Runtime instructions must not be duplicated in README or AGENTS.
- Plugin metadata, skill metadata, changelog, and release tag must remain version-consistent.
