# Diagnostic Codes

This file defines stable machine-readable defect codes for local image correction and regression evaluation.

## Semantic and subject

- `SEMANTIC_MISMATCH`: the image communicates the wrong message or product advantage.
- `METAPHOR_WEAK`: the intended metaphor exists but does not read without explanation.
- `SUBJECT_MISMATCH`: the main object is wrong or belongs to the wrong object class.
- `IDENTITY_DRIFT`: a required person, product, or recognizable object no longer matches the identity lock.

## Composition and geometry

- `COMPOSITION_DRIFT`: approved placement, scale, hierarchy, or negative space changed.
- `CAMERA_MISMATCH`: viewpoint, perspective, crop, or lens character differs from the specification.
- `GEOMETRY_ERROR`: shape, construction, proportion, or topology is implausible or inconsistent.
- `COUNT_MISMATCH`: the number of required supporting elements is wrong.
- `CROP_ERROR`: a mandatory object or safe area is unintentionally cropped.

## Style and rendering

- `STYLE_DRIFT`: one or more primary invariants of the selected style pack are violated.
- `MATERIAL_ERROR`: material family, roughness, reflectivity, or surface response is wrong.
- `PALETTE_ERROR`: color distribution or a required brand color is wrong.
- `LIGHTING_ERROR`: key, fill, rim, shadow, or contrast logic is inconsistent.
- `REFLECTION_ERROR`: reflections are missing, excessive, physically implausible, or stylistically forbidden.
- `BACKGROUND_ERROR`: background color, texture, gradient, or transparency is wrong.
- `DETAIL_ERROR`: detail density is too low, too high, noisy, or inconsistent.

## Brand and technical

- `LOGO_ERROR`: the logo is generated, distorted, wrong for the background, or not an approved asset.
- `TEXT_ERROR`: exact text is unreadable, misspelled, duplicated, or generated when post-production was required.
- `ARTIFACT_ERROR`: visible generation artifact, watermark, pseudo-text, broken edge, or unintended object.
- `RESOLUTION_ERROR`: output dimensions or effective detail are below the required contract.
- `FORMAT_ERROR`: file format, background mode, or alpha handling is wrong.
- `DELIVERY_MISSING`: generation succeeded but the final image is not visible in the user-facing response.

## Iteration rule

Every correction request must reference one primary diagnostic code. A second code is allowed only when both defects belong to the same scene layer. Preserve all approved locks and explicitly list the parts that must remain unchanged.
