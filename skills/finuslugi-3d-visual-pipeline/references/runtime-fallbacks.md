# Runtime Fallbacks

A fallback is an explicit change of execution method caused by a missing capability. It is not permission to weaken the Scene Specification silently.

## General rule

For every missing mandatory capability, choose exactly one outcome:

1. `stop`: execution cannot preserve the approved contract;
2. `ask-for-input`: a missing source image, mask, or reference can resolve the block;
3. `staged-route`: several supported operations can preserve the contract with documented risk;
4. `disclosed-degradation`: a lower-fidelity result is acceptable only after explicit user approval.

The output manifest records the requested mode, selected mode, fallback decision, reason, and limitations.

## Capability-specific behavior

### Missing `edit`

- Do not regenerate the scene and present it as an edit.
- Stop and state that exact pixel-level preservation is unavailable.
- A new reinterpretation is allowed only as a separately approved transformation mode.

### Missing `mask-edit`

- For local corrections, prefer an available edit operation only when the executor can preserve all non-target regions reliably.
- Otherwise stop or request a tool/environment with regional editing.
- Full-scene regeneration is not an automatic fallback.

### Missing `multi-reference`

A staged route is allowed only when references have non-overlapping roles.

1. Create a base using the primary subject or composition source.
2. Apply style or material in a later supported edit/reference-conditioned stage.
3. Re-run all locks after every stage.
4. Record increased drift risk.

Stop when identity, geometry, or composition roles would be lost by staging.

### Missing `identity-preservation`

- Stop when exact likeness or product identity is mandatory.
- Offer reinterpretation only when the user accepts lower fidelity.
- Never label approximate resemblance as preserved identity.

### Missing `transparent-output`

- Use opaque output only after the user accepts post-production background removal.
- Record edge and halo risk.
- Do not claim native transparency.

### Missing `upscale`

- Deliver the validated native-resolution asset when it satisfies the output contract.
- If higher resolution is mandatory, stop or route to a dedicated approved upscaler.
- Do not enlarge with interpolation and label it generative upscale.

### Missing `exact-dimensions`

- Generate at the closest supported aspect ratio and resample only when the user accepts it.
- Preserve safe areas and record final resampling.
- Stop when exact pixels are a contractual requirement and resampling is prohibited.

### Missing `deliver`

- Tool success is insufficient.
- Retry the delivery path without changing the generated asset.
- Emit `DELIVERY_MISSING` and keep the task incomplete until the image is visible.

## Fallback record

```yaml
fallback:
  applied: true
  from_mode: "mask-edit"
  to_mode: "edit"
  decision: "disclosed-degradation"
  reason: "The active runtime does not expose an explicit mask operation."
  approved_by_user: true
  risks:
    - "Non-target pixels may drift."
```

When `applied` is `false`, `from_mode`, `to_mode`, `reason`, and `risks` are omitted.

## Rejection conditions

Reject the run when:

- a mandatory capability is `unknown` but execution proceeds;
- requested and selected modes differ without a fallback record;
- the fallback changes transformation mode without user approval;
- limitations are omitted;
- delivery failure is ignored;
- the output manifest claims a capability that the runtime profile does not support.
