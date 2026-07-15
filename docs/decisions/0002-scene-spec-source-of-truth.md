# ADR-0002: Scene Specification is the source of truth

- Status: accepted
- Date: 2026-07-15
- Issues: #1, #2, #5

## Context

Natural-language image prompts are lossy, tool-specific, and difficult to compare across iterations. Treating the latest prompt as the canonical state makes it unclear which decisions were approved, which reference supplied a property, and which parts must survive a local correction.

## Decision

Use a versioned Scene Specification as the canonical contract between analysis and execution. Prompts are compiled artifacts derived from that specification and the selected runtime capability.

The specification records:

- communication task and metaphor;
- transformation mode;
- main object and supporting elements;
- reference roles with `take` and `do_not_take` rules;
- semantic, identity, composition, and style locks;
- composition, camera, materials, light, palette, and background;
- preserve, change, and exclude constraints;
- output dimensions and post-production policy.

The machine contract is `assets/schemas/scene-spec.schema.json`.

## Consequences

- Every prompt must be traceable to one Scene Specification version.
- Local corrections update only `constraints.change` and directly affected fields.
- Tool-specific adapters may change prompt syntax but not the approved specification.
- Regression evaluation compares behavior and locks, not only prompt wording.
