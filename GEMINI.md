# Shared Gemini Instructions

Use `.claude/` as the canonical project context source.

Read:

- `.claude/CLAUDE.md`
- `.claude/rules/` in full
- `docs/project-context.md`
- `_refs/1st-lab/`
- `_refs/2nd-lab/`

Shared rules:

- `.claude/skills/` is the canonical shared skill library for this repository.
- Treat `.claude/rules/` as the full shared rules directory. Read all relevant files there, including any rules added later.
- `_notes/todo.md` is read-only and must never be edited, reformatted, or cleaned up.
- When the user references a lab, assignment, or Moodle content, check `_refs/` before asking.
- `docs/project-context.md` is the source of truth for project scope and completed work. Keep it in sync when major work finishes.

Diagram requirements:

- Use PlantUML (`.puml`) for all UML diagrams.
- Working diagram files live in `_refs/export-og/`.
- Fixed versions go in `_refs/export-fixed/`.
- Source XML exports live in `_refs/export-source/`.
- Use `-->`, `.>` with `<<include>>` / `<<extend>>`, `--|>`, and `<|--` as required by the project conventions.
- Phase 1 diagrams use Lithuanian names.
- Phase 2 diagrams use English.

Activity diagram decision nodes:

- Leave decision diamonds empty.
- Use a positive branch label in square brackets.
- Use `([else])` for the else branch.
- Never write the negative condition on the else branch.
