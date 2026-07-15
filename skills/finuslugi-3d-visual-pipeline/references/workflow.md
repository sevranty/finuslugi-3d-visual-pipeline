# Workflow State Machine

## Canonical sequence

```text
INTAKE
  -> TASK_DEFINITION
  -> TRANSFORMATION_MODE
  -> REFERENCE_MAPPING
  -> LOCKS
  -> SCENE_SPECIFICATION
  -> STYLE_SELECTION
  -> PROMPT_PLAN
  -> PRE_GENERATION_GATE
  -> GENERATE_COMPOSITION
  -> QA_COMPOSITION
  -> REFINE_GEOMETRY
  -> QA_GEOMETRY
  -> REFINE_MATERIALS
  -> REFINE_LIGHTING
  -> REFINE_REFLECTIONS
  -> FINAL_QA
  -> FINALIZE
  -> DELIVER
```

`METAPHOR_SEARCH` may occur between `TASK_DEFINITION` and `TRANSFORMATION_MODE` when the communication metaphor has not been approved.

## Return paths

- Failed composition: return to `GENERATE_COMPOSITION`.
- Failed form or proportions: return to `REFINE_GEOMETRY`.
- Failed style material: return to `REFINE_MATERIALS`.
- Failed light or shadow logic: return to `REFINE_LIGHTING`.
- Failed reflections or integration: return to `REFINE_REFLECTIONS`.
- Failed delivery: return to `FINALIZE` or `DELIVER`; do not regenerate an already approved image.

A return must name the diagnostic code and the one scene layer being changed.

## Completion condition

The pipeline is complete only when:

1. the communication task reads correctly;
2. all critical quality gates pass;
3. the selected style pack and version are recorded;
4. the final file or generated image is available;
5. the image is shown in the user-facing response.
