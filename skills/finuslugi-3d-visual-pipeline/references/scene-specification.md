# Scene Specification

The Scene Specification is the canonical contract between analysis and generation. Do not treat the final natural-language prompt as the source of truth.

## Required fields

```yaml
spec_version: "1.0"
task:
  message: ""
  product_advantage: ""
  metaphor: ""
  target_channel: ""
transformation_mode: "brand-adaptation"
subject:
  main_object: ""
  action_or_state: ""
  mandatory_features: []
  supporting_elements: []
references:
  - id: ""
    roles: []
    take: []
    do_not_take: []
locks:
  semantic: []
  identity: []
  composition_level: 2
  style:
    id: ""
    version: ""
composition:
  aspect_ratio: ""
  main_object_position: ""
  frame_coverage: ""
  depth_order: []
  negative_space: ""
camera:
  viewpoint: ""
  perspective: ""
  crop: ""
visual:
  geometry: []
  materials: []
  lighting: []
  palette: []
  background: ""
  detail_level: ""
constraints:
  preserve: []
  change: []
  exclude: []
output:
  width_px: 0
  height_px: 0
  background_mode: "opaque"
  file_format: "png"
  text_added_after_generation: true
  logo_added_after_generation: true
```

## Rules

- Do not leave an empty required field when the decision affects generation.
- Use exact supporting-element counts when count affects meaning.
- `change` must contain only the active iteration target after the first generation.
- A style ID without a version is invalid.
- Exact text and the Finuslugi logo should normally be applied after generation.
- When dimensions are unknown, resolve the output channel before generation rather than inventing arbitrary values.
