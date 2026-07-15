# Iteration Rules

## Order of correction

1. communication meaning;
2. composition;
3. camera and crop;
4. geometry and proportions;
5. materials;
6. lighting and shadows;
7. reflections and integration;
8. detail;
9. upscale and export.

## Single-layer rule

Each correction changes one scene layer or one tightly related pair, such as lighting and its dependent shadows. Do not combine composition, geometry, material, lighting, and reflection changes in one request.

## Preservation statement

Before every iteration, list all approved parts that must remain unchanged. The correction prompt must include them explicitly.

## Regeneration rule

Prefer editing the current approved candidate. Regenerate from scratch only when:

- the semantic concept is wrong;
- the main object is wrong;
- the composition cannot be recovered through editing;
- the selected style pack was wrong;
- severe global artifacts affect the whole image.

## Iteration log

For every iteration record:

- candidate ID;
- diagnostic code;
- preserved features;
- changed layer;
- prompt or edit instruction;
- QA result;
- decision: accept, revise, or reject.
