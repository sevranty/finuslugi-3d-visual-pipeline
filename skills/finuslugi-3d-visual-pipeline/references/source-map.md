# Source Map

## Primary production source

- `3D Иллюстрации Финуслуг.pdf`
  - title: Работа с ChatGPT и Nano Banana;
  - pipeline version: 1.0;
  - year: 2026;
  - distilled topics: designer-first decision, metaphor search, reference roles, composition lock, technical brief, diagnostic first generation, staged correction, complex-scene sequence, and final upscale.

## Visual architecture sources

- `FDS [visual-architecture] Архитектура визуальных стилей Финуслуг v2 (август 2025).docx`
- `FDS [visual-style] Стиль Modern Flat v2.1 (2026-02-24).docx`
- `FDS [visual-style] Стиль Silver-Gold v3.1 (2026-02-24).docx`
- `FDS [visual-style] Стиль Obsidian Gold v1.0 (2026-02-24).docx`

## Normalization decisions

- The PDF defines the production sequence but not a complete skill contract.
- Style details are separated into versioned style-pack references.
- The Scene Specification is the source of truth; prompts are compiled outputs.
- Exact text and logos are post-generation assets by default.
- User-facing image delivery is an explicit mandatory state.

## Version policy

When a source document changes:

1. update the affected canonical reference;
2. increment the style or skill version when behavior changes;
3. update `CHANGELOG.md`;
4. add or update an eval case;
5. keep this source map synchronized.
