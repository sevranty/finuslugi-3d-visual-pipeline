# Prompt Architecture

## Two prompt layers

### Orchestration prompt

The request to ChatGPT or Codex contains the design decision and asks for a technically precise generation plan. It may ask for metaphor options only when no metaphor is approved.

### Production prompt

The request sent to the image generation tool executes the approved Scene Specification. It must not invent a new concept.

## Production prompt order

1. result type;
2. main subject;
3. action or state;
4. mandatory subject features;
5. supporting elements and count;
6. composition and negative space;
7. camera and crop;
8. geometry and materials;
9. lighting and shadows;
10. palette and background;
11. style invariants;
12. preservation constraints;
13. exclusions;
14. output dimensions or aspect ratio.

## Correction prompt order

1. list approved parts to preserve;
2. name one diagnostic defect;
3. describe the required corrected state;
4. name the one scene layer being changed;
5. repeat all critical locks;
6. forbid unrelated changes.

## Language rules

Avoid subjective instructions such as:

- make it better;
- make it more expensive;
- add realism;
- make it stylish.

Replace them with observable changes to geometry, material roughness, reflection strength, light direction, shadow density, color proportion, scale, or placement.

## Text and logo

Do not ask the model to redraw the Finuslugi logo. Avoid exact text inside the generative pass. Reserve a safe area and add exact text and the approved logo later.
