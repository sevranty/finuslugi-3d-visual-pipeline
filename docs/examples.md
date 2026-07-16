# Usage examples

These examples are tool-agnostic. The runtime must disclose unsupported capabilities instead of silently changing the requested mode.

## Style transfer

**Input**

- one subject image with confirmed usage rights
- one style reference
- output ratio and resolution
- identity lock level

**Request**

Apply only the declared style reference. Preserve subject identity, geometry and composition unless the Scene Specification allows a change.

**Stop**

Stop when rights, the subject image, the style role or the required editing capability is missing.

**Visible delivery**

Attach the selected image and record reference roles, locks, runtime route, diagnostics, score and output path.

## Reinterpretation

**Input**

- a source idea or scene reference
- target subject and metaphor
- one selected style pack
- exclusions

**Request**

Rebuild the idea as a new scene. Preserve semantic intent, not source identity or exact composition.

**Stop**

Stop when the semantic goal, target subject or style pack is undefined.

**Visible delivery**

Attach the selected image and record the Scene Specification, deviations, repairs and final score.

## Local correction

**Input**

- one generated image
- one diagnosed defect
- an allowed edit region
- unchanged locks

**Request**

Correct only the failing dimension. Do not regenerate unaffected regions.

**Stop**

Stop when the runtime cannot perform a local edit without hidden full-image regeneration.

**Visible delivery**

Attach the corrected image and record the original diagnostic, edited region, runtime behavior and post-repair score.
