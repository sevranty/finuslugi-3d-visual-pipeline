<p align="center">
  <img src="assets/finuslugi-base.png" alt="Финуслуги" width="180">
</p>

# Finuslugi 3D Visual Pipeline

Skill-only Codex plugin для управляемого производства 3D-иллюстраций Финуслуг: от коммуникационной задачи и набора референсов до проверенного финального изображения.

**Версия:** `0.2.0`  
**Статус:** governed public release candidate

## Что делает навык

Пайплайн разделяет дизайнерское решение, исполнение генератором и доказательную проверку. Навык:

1. фиксирует задачу, метафору и главный объект;
2. назначает каждому референсу отдельную роль;
3. проверяет права, approval status и разрешённые роли ассетов;
4. формирует Scene Specification как источник правды;
5. выбирает один версионированный style pack;
6. строит один промпт или последовательность промптов;
7. выбирает image runtime по фактическим capabilities;
8. запрещает скрытые fallback и деградацию режима;
9. проводит визуальный QA и диагностические локальные итерации;
10. фиксирует output manifest и гарантирует видимую выдачу изображения.

## Установка

Полная инструкция: `skills/finuslugi-3d-visual-pipeline/references/installation.md`.

### Codex plugin

Добавьте публичный репозиторий `sevranty/finuslugi-3d-visual-pipeline` через доступный в клиенте интерфейс управления плагинами. Используйте тег `v0.2.0` после его публикации либо точный release commit, указанный в release manifest.

### Repository-scoped skill

```bash
mkdir -p .agents/skills
cp -R skills/finuslugi-3d-visual-pipeline .agents/skills/finuslugi-3d-visual-pipeline
```

Проверка установки:

```bash
python3 skills/finuslugi-3d-visual-pipeline/scripts/smoke_test_installation.py
```

## Целевая архитектура

```text
finuslugi-3d-visual-pipeline/
|-- .codex-plugin/plugin.json
|-- assets/
|   |-- manifest.json
|   |-- manifest-history.json
|   |-- checksums.sha256
|   |-- anchors/
|   |-- anti-patterns/
|   `-- exploratory/
|-- docs/decisions/
|-- release/0.2.0/
|-- skills/finuslugi-3d-visual-pipeline/
|   |-- SKILL.md
|   |-- agents/
|   |-- references/
|   |-- assets/schemas/
|   |-- scripts/
|   `-- evals/
|-- validation/
|-- AGENTS.md
|-- CHANGELOG.md
|-- RELEASE_CHECKLIST.md
|-- LICENSE
`-- README.md
```

## Канонические контракты

- runtime-порядок: `skills/finuslugi-3d-visual-pipeline/SKILL.md`;
- Scene Specification: `skills/finuslugi-3d-visual-pipeline/references/scene-specification.md`;
- runtime-capabilities: `skills/finuslugi-3d-visual-pipeline/references/runtime-capabilities.md`;
- asset-governance: `skills/finuslugi-3d-visual-pipeline/references/asset-governance.md`;
- output manifest: `skills/finuslugi-3d-visual-pipeline/assets/schemas/output-manifest.schema.json`;
- visual regression: `skills/finuslugi-3d-visual-pipeline/evals/visual-cases.json`;
- installation.md: `skills/finuslugi-3d-visual-pipeline/references/installation.md`;
- versioning и release: `skills/finuslugi-3d-visual-pipeline/references/versioning-and-release.md`;
- compatibility: `skills/finuslugi-3d-visual-pipeline/references/compatibility.md`.

## Style packs

| Style pack | Версия | Статус |
|---|---:|---|
| Modern Flat | 2.1 | основной канонический |
| Silver-Gold | 3.1 | канонический контракт, контролируемое применение |
| Obsidian Gold | 1.0 | канонический контракт, контролируемое применение |

Техническая валидность style pack не означает автоматическое согласование конкретного продуктового или маркетингового применения.

## Runtime routing

Канонический skill не привязан к названию генератора. Он проверяет capabilities `generate`, `reference-conditioned`, `edit`, `mask-edit`, `multi-reference`, `identity-preservation`, `transparent-output`, `upscale`, `exact-dimensions` и `deliver`.

Поддержаны контрактные профили:

- `chatgpt-image-generation@1`;
- `nano-banana-style@1`;
- будущие adapters, соответствующие runtime-capabilities schema.

Неизвестная обязательная capability трактуется как неподдерживаемая. Успех инструмента без изображения в пользовательском ответе — `DELIVERY_MISSING`.

## Asset governance

- каждый визуальный файл имеет stable ID, version, source, owner, rights, approval, permitted roles и SHA-256;
- unregistered binary отклоняется;
- exploratory references не являются style source;
- AI-generated logo — критический `LOGO_ERROR`;
- public golden допускается только при approved + rights-cleared + public-distribution-approved;
- светлый фон использует `assets/finuslugi-base.png`;
- красный или тёмный фон использует `assets/finuslugi-inverted.png`;
- фирменный цвет Финуслуг и MOEX — `#FF0508`.

## Visual regression

Репозиторий содержит девять deterministic SVG goldens — по три на Modern Flat, Silver-Gold и Obsidian Gold — и пять diagnostic anti-pattern fixtures. Они проверяют контракты, а не заявляют качество production art или конкретной генеративной модели.

Покрыты simple, complex, local-correction и delivery flows, включая `PALETTE_ERROR`, `MATERIAL_ERROR`, `BACKGROUND_ERROR`, `LOGO_ERROR`, `COMPOSITION_DRIFT` и `DELIVERY_MISSING`.

## Проверка

```bash
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_repository.py --no-report
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_runtime_contract.py
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_asset_registry.py
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_visual_regression.py
python3 skills/finuslugi-3d-visual-pipeline/scripts/smoke_test_installation.py
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_release.py
```

Все validators используют только Python standard library. `validate_release.py` проверяет version alignment, installation smoke, публичный состав репозитория, release manifest, права и publication gates.

## Совместимость и ограничения

Поддерживаются Codex plugin packaging, repository-scoped Agent Skills fallback и Python 3.10+. Конкретные возможности генератора остаются runtime-наблюдением. Exact identity preservation не гарантируется.

Матрица совместимости находится в `skills/finuslugi-3d-visual-pipeline/references/compatibility.md`.

## Цифровой след

- архитектура: [Issue #1](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/1);
- канонический навык: [Issue #2](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/2);
- style packs: [Issue #3](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/3);
- visual regression: [Issue #4](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/4);
- deterministic validation: [Issue #5](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/5);
- runtime contract: [Issue #6](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/6);
- asset governance: [Issue #7](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/7);
- release: [Issue #8](https://github.com/sevranty/finuslugi-3d-visual-pipeline/issues/8).

## Лицензия

MIT применяется к коду и оригинальной документации репозитория. Права на товарные знаки, логотипы, внутренние исходные документы и сторонние референсы регулируются отдельно. Публикация логотипов в этом репозитории не предоставляет downstream-пользователям права на товарный знак.
