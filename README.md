<p align="center">
  <img src="assets/finuslugi-base.png" alt="Финуслуги" width="180">
</p>

# Finuslugi 3D Visual Pipeline

Skill-only Codex plugin для управляемого производства 3D-иллюстраций Финуслуг: от коммуникационной задачи и набора референсов до проверенного финального изображения.

## Что делает репозиторий

Пайплайн разделяет дизайнерское решение и генерацию. Навык:

1. фиксирует задачу, метафору и главный объект;
2. назначает каждому референсу отдельную роль;
3. формирует Scene Specification;
4. выбирает версионированный style pack;
5. строит последовательность промптов;
6. выполняет предгенерационный контроль;
7. передает генерацию доступному image generation инструменту;
8. проводит визуальный QA и локальные итерации;
9. гарантирует пользовательскую выдачу финального изображения.

## Целевая архитектура

```text
finuslugi-3d-visual-pipeline/
|-- .codex-plugin/
|   `-- plugin.json
|-- assets/
|   |-- finuslugi-base.png
|   `-- finuslugi-inverted.png
|-- skills/
|   `-- finuslugi-3d-visual-pipeline/
|       |-- SKILL.md
|       |-- agents/
|       |-- references/
|       |-- assets/
|       |-- scripts/
|       `-- evals/
|-- AGENTS.md
|-- CHANGELOG.md
|-- LICENSE
`-- README.md
```

## Статус

`0.1.0` — начальная архитектура. Навык не считается production-ready до наполнения библиотеки утвержденных якорных изображений и прохождения визуальных regression-evals.

## Брендовые активы

- светлый или белый фон: `assets/finuslugi-base.png`;
- красный или темный фон: `assets/finuslugi-inverted.png`;
- фирменный цвет Финуслуг и MOEX: `#FF0508`.

## Локальная проверка

```bash
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_repository.py
```

## Лицензия

MIT. Правила использования товарных знаков и брендовых активов Финуслуг определяются правообладателем отдельно от лицензии на код и документацию.
