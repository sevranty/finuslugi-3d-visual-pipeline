# ADR-0005: Route image execution by observed capabilities

- Status: accepted
- Date: 2026-07-15
- Issue: #6

## Context

The canonical skill must work with ChatGPT image generation, Nano Banana-style executors, and future tools. Product names do not reliably describe whether an active runtime can edit, mask-edit, use multiple references, preserve identity, upscale, produce transparency, or deliver an image visibly.

## Decision

Before execution, derive mandatory capabilities from the Scene Specification and requested operation. Select a versioned runtime profile whose observed capabilities satisfy every mandatory requirement. Treat `unknown` as unsupported. Record the selected profile, adapter, actual tool/model, requested and selected modes, fallback decision, and limitations in output manifest version 1.1.

A missing capability causes an explicit stop, request for input, staged route, or user-approved disclosed degradation. Hidden fallback is prohibited. Tool success without visible delivery is `DELIVERY_MISSING`.

## Consequences

- Style packs remain independent from generator syntax.
- Runtime adapters cannot weaken semantic, identity, composition, or style locks.
- Adding or changing a runtime profile requires eval and changelog updates.
- Exact identity, mask edit, transparency, and upscale may block a run when unsupported.
