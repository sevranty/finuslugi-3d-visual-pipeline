# Runtime Routing

Routing converts an approved Scene Specification into one explicit execution path. It does not modify the communication concept, style pack, or approved locks.

## Adapter input

Each route receives:

```yaml
adapter_request_version: "1.0"
scene_spec:
  version: "1.0"
  sha256: "64 lowercase hex characters"
requested_mode: "generate | reference-conditioned | edit | mask-edit | upscale"
required_capabilities:
  - "generate"
reference_bindings:
  - reference_id: "ref-style-001"
    roles:
      - "style"
    ordinal: 1
locks:
  preserve:
    - "approved property"
output:
  width_px: 1024
  height_px: 1024
  background_mode: "opaque"
```

## Reference-role mapping

| Scene Specification role | runtime handling |
|---|---|
| `style` | Condition material, palette, light, and rendering language. Never copy the source object by default. |
| `subject` | Condition the object class and mandatory visible features. |
| `identity` | Requires `identity-preservation`; otherwise stop or disclose a lower-fidelity reinterpretation. |
| `geometry` | Condition construction, silhouette, proportion, and topology. |
| `composition` | Condition position, scale, hierarchy, negative space, and depth order. |
| `camera` | Condition viewpoint, perspective, crop, and lens character. |
| `material` | Condition roughness, reflectivity, texture family, and surface response. |
| `palette` | Condition color distribution and focal accents. |
| `pose` | Condition body or object articulation without transferring identity unless separately declared. |
| `editable-source` | Marks the exact image whose pixels may be modified. Requires `edit`; a regional correction also requires `mask-edit`. |

## Route selection

1. Derive mandatory capabilities from the transformation mode and Scene Specification.
2. Read the active runtime profile.
3. Reject every profile with `unsupported` or `unknown` mandatory capabilities.
4. Rank remaining routes by preservation fidelity, not convenience.
5. Select exactly one route.
6. Record requested mode, selected mode, profile ID, adapter ID, and limitations before execution.
7. Execute only after the route is visible in the plan.

## Mode requirements

| requested mode | mandatory capabilities |
|---|---|
| new image without references | `generate`, `deliver` |
| style or subject reference | `generate`, `reference-conditioned`, `deliver` |
| synthesis from multiple references | `generate`, `reference-conditioned`, `multi-reference`, `deliver` |
| edit exact source | `edit`, `deliver` |
| local masked correction | `edit`, `mask-edit`, `deliver` |
| exact identity preservation | `identity-preservation`, plus the selected generate/edit capabilities |
| transparent asset | selected generate/edit capability, `transparent-output`, `deliver` |
| dedicated upscale | `upscale`, `deliver` |

## Preferred routes

### ChatGPT image generation

Use the native generation or edit operation when the required target images are present in the current conversation and the active tool exposes all mandatory capabilities. The final tool response must itself make the image visible.

### Nano Banana-style execution

Compile the same adapter request into the external executor syntax. ChatGPT remains responsible for reference mapping, route disclosure, QA, iteration control, and final delivery verification. External tool success is not delivery evidence.

## Prohibitions

- Do not select a route by product name alone.
- Do not silently replace `edit` with a new generation.
- Do not split multi-reference synthesis without explaining the staged route and preservation risk.
- Do not claim identity preservation when the profile marks it `conditional`, `unknown`, or `unsupported`.
- Do not mark a run complete before `deliver` is verified.
