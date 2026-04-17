# Shared AI Instructions

This repository keeps the canonical shared AI context under `.claude/`.

Read these first:

- `.claude/CLAUDE.md`
- `.claude/rules/` in full

Primary project context:

- `docs/project-context.md`
- `_refs/1st-lab/`
- `_refs/2nd-lab/`

Rules:

- `.claude/skills/` is the shared skill library for this repository.
- Treat `.claude/rules/` as the full shared rules directory. Read all relevant files there, including any rules added later.
- `_notes/todo.md` is read-only and must never be edited, reformatted, or cleaned up.
- When the user references a lab, assignment, or Moodle content, check `_refs/` before asking.
- `docs/project-context.md` is the source of truth for project scope and completed work. Keep it in sync when major work finishes.

Diagram format:

- All UML diagrams use PlantUML (`.puml`), not Mermaid.
- Working diagram files live in `_refs/export-og/`.
- Fixed or improved versions go in `_refs/export-fixed/`.
- Source XML exports from MagicDraw are in `_refs/export-source/`.
- PlantUML relationships:
  - `-->` for associations
  - `.>` with `<<include>>` / `<<extend>>` for use case relationships
  - `--|>` for generalization
  - `<|--` for inheritance in class diagrams
- Phase 1 diagrams keep Lithuanian names.
- Phase 2 diagrams use English.

Activity diagram decision nodes:

- Decision diamonds must be empty: `if () then ([label])`
- Positive branch labels go in square brackets, for example `([nori keisti])`
- Else branches are always `([else])`
- Never put the negative condition on the else branch
- Use `if () then ([positive action]) ... else ([else]) ... endif`
