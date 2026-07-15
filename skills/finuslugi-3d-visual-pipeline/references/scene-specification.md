# Scene Specification

The Scene Specification is the canonical contract between analysis and generation. Do not treat the final natural-language prompt as the source of truth.

Machine contract: `../assets/schemas/scene-spec.schema.json`.

## Valid example

```yaml
spec_version: "1.0"
task:
  message: "Private investment service protects and concentrates client value."
  product_advantage: "Controlled access to premium investment opportunities."
  metaphor: "A protected vault with a restrained golden opening."
  target_channel: "landing-hero"
transformation_mode: "brand-adaptation"
subject:
  main_object: "compact faceted vault"
  action_or_state: "closed and secure with a narrow golden light at the door edge"
  mandatory_features:
    - "recognizable vault silhouette"
    - "single door seam"
    - "gold limited to the seam and lock detail"
  supporting_elements: []
references:
  - id: "ref-style-001"
    roles:
      - "style"
    take:
      - "matte black material"
      - "gold accent discipline"
      - "soft frontal light"
      - "pure black background"
    do_not_take:
      - "original object"
      - "original composition"
      - "text or logo"
  - id: "ref-geometry-001"
    roles:
      - "geometry"
    take:
      - "vault door construction"
      - "compact proportions"
    do_not_take:
      - "steel material"
      - "photographic lighting"
      - "environment"
locks:
  semantic:
    - "security"
    - "premium value"
    - "controlled access"
  identity: []
  composition_level: 2
  style:
    id: "obsidian-gold"
    version: "1.0"
composition:
  aspect_ratio: "1:1"
  main_object_position: "centered"
  frame_coverage: 0.62
  depth_order:
    - "black background"
    - "vault body"
    - "gold door-seam accent"
  negative_space: "uniform black margin around the object"
camera:
  viewpoint: "slight three-quarter front view"
  perspective: "controlled product perspective"
  crop: "full object visible with no floor plane"
visual:
  geometry:
    - "low-poly"
    - "faceted"
    - "clean edges"
    - "sharp folds"
    - "icon-readable silhouette"
  materials:
    - "matte obsidian-black body"
    - "satin gold accents below 20 percent"
  lighting:
    - "soft controlled frontal light"
    - "no HDR"
    - "no mirror reflections"
    - "no floor shadow"
  palette:
    - "#000000"
    - "#1A1A1A"
    - "#FFD700"
    - "#C7A256"
  background: "pure black #000000"
  detail_level: "icon-grade"
constraints:
  preserve:
    - "vault silhouette"
    - "centered composition"
    - "pure black background"
    - "gold accent limit"
  change: []
  exclude:
    - "stone texture"
    - "chrome"
    - "environment"
    - "extra colors"
    - "generated text"
    - "generated logo"
output:
  width_px: 1024
  height_px: 1024
  background_mode: "opaque"
  file_format: "png"
  text_added_after_generation: true
  logo_added_after_generation: true
```

## Field rules

### Task

- `message` is the communication meaning that must survive every iteration.
- `product_advantage` states the benefit, not only the product name.
- `metaphor` describes the visual causal idea.
- `target_channel` determines dimensions, safe areas, and post-production requirements.

### Subject

- `mandatory_features` must contain every recognizable or functional feature required for acceptance.
- Each supporting element is an object with `name`, exact integer `count`, and `purpose`.
- Use an empty supporting-element array only when the composition intentionally contains one isolated object.

### References

Each reference requires:

- stable `id`;
- one or more roles from the canonical reference-role vocabulary;
- explicit `take` properties;
- explicit `do_not_take` properties.

Do not assign incompatible sources to the same role without a recorded priority decision.

### Locks

- `semantic` cannot be empty.
- `identity` may be empty when no exact person, product, or recognizable object must be preserved.
- `composition_level` is an integer from 0 to 4.
- style `id` and exact style `version` are mandatory.

### Composition

- `frame_coverage` is a decimal ratio from `0.05` to `0.95`, not a prose value.
- `depth_order` lists layers from back to front.
- `negative_space` states location and purpose.

### Visual

- `detail_level` is one of `icon-grade`, `standard`, `hero`, or `board-ready`.
- Materials, light, palette, and background must repeat the selected style-pack invariants explicitly.

### Constraints

- `preserve` records approved properties that must remain stable.
- `change` is empty for the first generation and contains only the active correction target during an iteration.
- `exclude` records copied details, prohibited style markers, and common generation defects.

### Output

- Minimum width and height are 512 pixels.
- Resolve channel and dimensions before generation instead of inventing arbitrary values.
- Exact text and the approved Finuslugi logo are normally applied after the generative pass.
