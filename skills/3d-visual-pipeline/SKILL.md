---
name: 3d-visual-pipeline
description: Analyze image references and produce a governed, style-consistent, validated three-dimensional image with explicit runtime routing, diagnostics, provenance, and visible delivery.
---

# 3D Visual Pipeline

## Mandatory sequence

1. Validate the request, source rights, and available references.
2. Define task, metaphor, subject, audience, output format, and exclusions.
3. Assign every reference one role: subject, composition, style, material, lighting, palette, or detail.
4. Record Semantic, Identity, Composition, and Style locks.
5. Compile the Scene Specification before generation.
6. Pass every repository asset through the governed registry.
7. Select exactly one versioned style pack.
8. Resolve required runtime capabilities and explicit fallback behavior.
9. Generate or edit; never hide degradation from the requested mode.
10. Run visual QA, diagnose defects, and repair only the failing dimensions.
11. Finalize exact text and marks outside the generative pass when required.
12. Attach the selected image visibly and record the output manifest.

## Stop conditions

Stop with a diagnostic rather than guessing when required inputs, rights, mandatory runtime capabilities, exact identity evidence, or visible delivery are missing.

## Quality gate

Score meaning 25, preservation 20, style 20, composition 15, geometry 10, and technical quality 10. Accept at 90 or above. A critical diagnostic overrides the weighted score.

## References

- `references/scene-specification.md`
- `references/style-selection.md`
- `references/runtime-capabilities.md`
- `references/asset-governance.md`
- `references/diagnostic-codes.md`
- `references/output-delivery.md`
