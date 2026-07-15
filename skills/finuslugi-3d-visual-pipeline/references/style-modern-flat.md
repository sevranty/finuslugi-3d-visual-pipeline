# Style Pack: Modern Flat

```yaml
style_id: modern-flat
version: "2.1"
status: canonical
source_status: primary Finuslugi visual language
```

## Purpose

Modern Flat is the main Finuslugi illustration language for brand, product, marketing, and AI-assisted scenes. It combines flat geometric construction with volumetric gradients, directional light, cinematic depth, and clean vector-ready surfaces.

## Semantic character

- technological and contemporary;
- energetic, ambitious, optimistic;
- professional without corporate stiffness;
- suitable for finance, digital lifestyle, mobility, growth, and personal achievement.

## Primary invariants

### Geometry

- flat geometric silhouettes with modeled planes;
- clear structured contours;
- layered depth and atmospheric perspective;
- medium or high detail, never icon-grade simplification for a full scene;
- dynamic but readable three-quarter viewpoints are preferred when appropriate.

### Light and volume

- one clearly readable directional source;
- heroic backlight or controlled rim light reinforces the silhouette;
- volume is created with gradients and clean shadows, not texture noise;
- light halos and soft transitions are allowed when they preserve edge clarity;
- detailed but not photorealistic.

### Palette

Target visual-weight distribution:

- approximately 40% neutral base;
- approximately 30% deep cold tones;
- approximately 20% warm supporting tones;
- no more than 10% brand red `#FF0508` as the focal accent.

Supporting colors may include orange, warm accents, turquoise, deep blue, white, and neutral gray when the communication task requires them.

### Composition

- clear hero in the foreground or middle ground;
- context supports the story rather than competing with the hero;
- depth is built in layers;
- preserve a 15% vertical safe area at the top and bottom;
- preserve a 10% horizontal safe area for adaptive cropping;
- default digital-first format is 16:9; 1:1 and 4:5 are allowed for social outputs.

### People and environments

- people are active professionals, investors, or digital users;
- smart-casual or business clothing is appropriate;
- emotion is calm confidence rather than exaggerated excitement;
- city, office, cafe, digital interface, travel, winter, industry, or nature may be used as modular context;
- devices, graphs, light panels, and achievement symbols must support the message.

## Prompt vocabulary

Prefer explicit visual markers such as:

- `modern flat illustration`;
- `flat geometric forms with volumetric gradients`;
- `heroic directional backlight`;
- `clean layered shadows`;
- `vector-clean surfaces`;
- `cinematic depth without photorealism`;
- `structured three-quarter view`;
- `brand red accent #FF0508 limited to a focal detail`.

Do not rely on the phrase `Modern Flat style` without describing the parameters.

## Prohibitions

Reject or correct:

- photorealism or hyperrealism;
- painterly, canvas, watercolor, or noisy textures;
- anime or fantasy stylization;
- flat minimalism without depth, gradients, or light modeling;
- low-detail icons substituted for a full illustration;
- random palette outside the brand system;
- red dominating more than 10% of the visual weight;
- uncontrolled glow that destroys contours;
- key objects inside the safe area.

## Pre-generation markers

A valid prompt plan must state:

- flat geometric construction;
- volumetric gradient modeling;
- directional or heroic light;
- clean shadows without texture noise;
- non-photorealistic finish;
- target aspect ratio and safe area;
- explicit use and limit of `#FF0508` when red is present.

## QA

The style gate fails when any primary invariant is absent or when a prohibition is visible. Manual QA must check:

1. geometry and contour clarity;
2. gradient-built volume;
3. consistent backlight and shadows;
4. palette distribution;
5. red-accent limit;
6. composition readability and safe areas;
7. sufficient detail without photorealism;
8. readiness for manual vector refinement when required.

## Production note

AI output is a controlled draft or production component, not an automatic master asset. A production export requires design-system validation, manual cleanup when necessary, asset registration, and versioning.
