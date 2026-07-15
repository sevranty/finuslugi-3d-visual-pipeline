# Reference Analysis and Locks

## Reference roles

Assign one or more explicit roles to every image, but avoid overlapping sources for the same role.

- `style`: materials, lighting, background, shadows, reflections, rendering quality.
- `subject`: main object identity or product form.
- `geometry`: construction, proportions, silhouette, mechanical logic.
- `composition`: position, scale, hierarchy, depth, negative space.
- `camera`: viewpoint, lens feeling, perspective, crop.
- `material`: one specific surface or finish.
- `palette`: color distribution only.
- `pose`: body or object pose only.

The main approved Finuslugi creative should normally own the `style` role. Use no more than two additional references unless the user explicitly accepts ambiguity.

A schematic drawing may own only `composition`, `pose`, or simple `geometry`. It must not define final rendering quality.

## Reference Analysis Card

Record:

- image identifier;
- assigned roles;
- visible main subject;
- action or state;
- composition and camera;
- materials and lighting;
- palette;
- mandatory recognizable features;
- accidental or replaceable features;
- source defects;
- confidence level: high, medium, or low.

## Locks

### Semantic lock

Meaning, action, product advantage, metaphor, and causal relationship that must survive every iteration.

### Identity lock

Recognizable person, product, vehicle, architecture, or object features that must remain stable.

### Composition lock

Use one level:

- `0`: composition is free;
- `1`: preserve only overall balance;
- `2`: preserve major mass placement;
- `3`: preserve composition closely;
- `4`: preserve composition as exactly as the tool allows.

### Style lock

Style pack ID, version, mandatory invariants, forbidden features, and allowed derivatives.

## Preserve-change-exclude table

For every production request, state:

- `preserve`: approved features that must remain unchanged;
- `change`: the current iteration target;
- `exclude`: additions, defects, and copied details that are forbidden.
