---
name: finuslugi-3d-visual-pipeline
description: Analyze visual references and design briefs, compile a versioned Finuslugi 3D style specification, route execution through a capability-checked image runtime, generate or edit a new image, diagnose deviations, and deliver a validated final asset. Use when the user provides one or more references and asks for a new Finuslugi-style 3D illustration, a controlled restyle, a composition-preserving variation, or a local correction of an existing generation.
---

# Finuslugi 3D Visual Pipeline

## Scope

Use this skill to transform an idea or reference into a new, style-consistent Finuslugi image. The skill owns analysis, specification, runtime routing, prompt planning, iteration control, QA, and delivery. The selected image-generation runtime owns the actual generation or edit execution.

Do not treat a reference as a complete brief. Do not jump directly from an image to one long prompt.

## Mandatory workflow

1. **Validate the input.**
   - Confirm that a usable reference or editable image is present.
   - Distinguish a reference from the image that must be edited.
   - Read `references/input-contract.md`.
2. **Define the communication task.**
   - Fix the key message, product advantage, metaphor, main object, supporting elements, intended channel, and required aspect ratio.
   - When the metaphor is missing, propose options before any production prompt.
3. **Select the transformation mode.**
   - Choose exactly one primary mode from `references/transformation-modes.md`.
4. **Analyze and map references.**
   - Assign a specific role to every reference.
   - Use one approved Finuslugi creative as the style reference when available.
   - Use no more than two additional references unless the user explicitly accepts higher ambiguity.
   - Read `references/reference-analysis.md`.
5. **Lock the approved decisions.**
   - Record semantic, identity, composition, and style locks.
   - State what may change and what must not change.
6. **Build the Scene Specification.**
   - Use the complete contract in `references/scene-specification.md`.
   - Validate structured instances against `assets/schemas/scene-spec.schema.json` when the environment supports file-based validation.
   - The Scene Specification, not the final prompt, is the source of truth.
7. **Select exactly one style pack and version.**
   - Apply the selection rules in `references/style-selection.md`.
   - Modern Flat: `references/style-modern-flat.md`.
   - Silver-Gold: `references/style-silver-gold.md`.
   - Obsidian Gold: `references/style-obsidian-gold.md`.
   - Preserve controlled-rollout status and any review requirement.
   - Never combine style invariants unless a documented derivative style has been approved.
8. **Plan the prompt sequence.**
   - Use one prompt for simple scenes.
   - Use staged prompts for complex scenes.
   - Follow `references/prompt-architecture.md` and `references/generation-sequence.md`.
9. **Route through an explicit runtime profile.**
   - Derive mandatory capabilities from the requested mode, reference roles, locks, and output contract.
   - Read `references/runtime-capabilities.md` and validate the active profile against `assets/schemas/runtime-capabilities.schema.json` when file-based validation is available.
   - Select the route using `references/runtime-routing.md`.
   - When a mandatory capability is absent or unknown, follow `references/runtime-fallbacks.md`; never degrade silently.
   - Record profile ID, adapter ID, actual tool/model, requested mode, selected mode, fallback decision, and limitations before execution.
10. **Run the pre-generation gate.**
    - Reject contradictions, undefined reference roles, missing locks, missing output dimensions, style-rule violations, and unsupported mandatory capabilities.
    - Do not continue through an undocumented capability downgrade.
11. **Generate or edit through the selected runtime.**
    - Preserve the declared locks.
    - Do not ask the generator to invent the communication concept.
    - Execute only the selected route.
12. **Inspect the result visually.**
    - Check meaning, geometry, composition, style, brand, and technical quality.
    - Apply the gates in `references/quality-gates.md`.
13. **Iterate diagnostically.**
    - Select a stable code from `references/diagnostic-codes.md`.
    - Preserve approved parts.
    - Change one scene layer or one tightly related group per iteration.
    - Re-evaluate runtime capabilities when the requested correction mode changes.
    - Follow `references/iteration-rules.md`.
14. **Finalize and deliver.**
    - Add exact text and logos outside the generative pass whenever possible.
    - Use the correct Finuslugi logo asset for the background.
    - Confirm that the final image is visible in the user-facing response.
    - Validate a structured record against `assets/schemas/output-manifest.schema.json` when file-based output is available.
    - Follow `references/output-delivery.md`.

## Non-negotiable rules

- Designer decision first; generation second.
- Every reference has one explicit function.
- A sketch is a composition map, not a style source.
- Do not fully copy a reference unless the user explicitly requests a permitted edit of that exact image.
- Do not use subjective correction language such as “make it better” or “make it expensive”. Translate it into a measurable visual defect.
- Do not repair composition, geometry, material, lighting, reflections, and detail in one request.
- Do not generate a Finuslugi logo. Use the supplied brand asset.
- Do not claim a capability that is unknown or unsupported.
- Do not replace edit, mask edit, identity preservation, transparency, or upscale with a lower-fidelity route without disclosure and approval.
- Tool success without a visible image is `DELIVERY_MISSING`.
- A high weighted score does not override a critical defect.
- Do not claim completion until the final image has passed QA and is delivered to the user.

## Final response minimum

The user-facing result must contain the final image. Supporting text may state the selected style pack, transformation mode, runtime route, fallback, and non-critical limitations. Never return an empty final response after successful generation.

## Canonical references

- Workflow state machine: `references/workflow.md`
- Reference roles and locks: `references/reference-analysis.md`
- Scene contract: `references/scene-specification.md`
- Style selection: `references/style-selection.md`
- Prompt structure: `references/prompt-architecture.md`
- Runtime capabilities: `references/runtime-capabilities.md`
- Runtime routing: `references/runtime-routing.md`
- Runtime fallbacks: `references/runtime-fallbacks.md`
- Diagnostic codes: `references/diagnostic-codes.md`
- Quality gates: `references/quality-gates.md`
- Delivery contract: `references/output-delivery.md`
- Source traceability: `references/source-map.md`
- Normalization conflicts: `references/style-conflict-log.md`
