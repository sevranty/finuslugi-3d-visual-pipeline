# Style Pack: Obsidian Gold

```yaml
style_id: obsidian-gold
version: "1.0"
status: canonical-controlled
source_status: controlled premium concept
```

## Purpose

Obsidian Gold is a premium 3D visual layer for status, value, security, private service, investment, vault, and exclusive-product scenarios. The object reads as an isolated digital sculpture, not as a scene.

## Primary invariants

### Material

- base material is `matte obsidian-black` or `faceted obsidian-black`;
- do not describe the material as natural stone;
- the base is matte and non-reflective;
- gold may be polished or satin, but only as a controlled accent;
- gold covers no more than 15-25% of the visible object area.

### Geometry

- low-poly, faceted, geometric, angular, or parametric construction;
- clean edges and sharp folds;
- compact minimalist silhouette;
- object must remain recognizable as an icon at small size;
- miniature, toy-like, or icon-grade proportion may be used to preserve clarity.

### Light

- soft controlled frontal light;
- ultra-minimalist lighting;
- no HDR treatment;
- no mirror reflections;
- icon-grade output normally has no visible floor shadow;
- gold may emit or catch a restrained focal glow.

### Composition and background

- one isolated object;
- no environment or scenic context;
- default aspect ratio is 1:1;
- production background is exactly `#000000`;
- the final prompt must end with: `The background is black.`

### Canonical tokens

| token | value or rule |
|---|---|
| `obsidian.black` | `#000000` |
| `obsidian.deep` | `#1A1A1A` |
| `gold.primary` | `#FFD700` |
| `gold.secondary` | `#C7A256` |
| `material.obsidian` | matte, no reflections |
| `material.gold` | polished or satin, accent only |
| `light.soft.frontal` | soft frontal light; no HDR; no floor shadow for icon-grade output |

## Prompt vocabulary

A canonical prompt must express the parameters rather than using the style name as a magic phrase.

Required markers:

- `3D rendering of`;
- `matte obsidian-black` or a clearly equivalent matte obsidian base;
- `gold accents`;
- `low-poly`, `faceted`, or `parametric` geometry;
- `clean edges` and `sharp folds`;
- `digital sculpture`;
- isolated object;
- `The background is black.` as the final sentence;
- 1:1 output unless a documented derivative is approved.

Recommended base structure:

```text
3D rendering of a [OBJECT] made from matte obsidian-black with restrained gold accents, low-poly and faceted, abstract and geometric, with a minimalist icon-readable silhouette, clean edges and sharp folds, stylized as a digital sculpture under soft controlled frontal light. The background is black.
```

## Prohibitions

Reject or correct:

- `obsidian stone`, realistic stone grain, rock, marble, or mineral texture;
- photo, photorealistic, realistic product photography;
- HDR, chrome, mirror, reflective, glossy, or jewelry-render treatment;
- light, graphite, colored, textured, or gradient background;
- environment, room, landscape, floor, stage, or scene;
- extra colors outside obsidian-black and gold accents;
- gold used as the main fill or exceeding 25%;
- multiple independent hero objects;
- visible uncontrolled floor shadow;
- prompt that does not end with `The background is black.`

## Pre-generation gate

Before execution, confirm:

1. one isolated object;
2. object remains recognizable as a compact icon;
3. matte obsidian-black base;
4. gold target is 15-25% or lower;
5. low-poly/faceted/parametric geometry;
6. soft frontal light;
7. no HDR, reflections, stone texture, environment, or extra colors;
8. exact black background;
9. default 1:1 output;
10. required closing sentence is present.

## QA

The style gate fails when any of the following is visible:

- background is not pure black;
- object reads as natural stone;
- surface is glossy, chrome, or mirror-like;
- gold dominates the object;
- an environment or scenic floor appears;
- additional colors appear;
- silhouette is too complex to read as an icon;
- multiple hero objects compete;
- lighting becomes dramatic HDR rather than controlled minimal frontal light.

Any environment-based derivative must receive a new style ID and version. It is not an allowed variation of `obsidian-gold@1.0`.
