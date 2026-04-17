# Project Instructions For Codex

## Context Loading

Read these first when starting work on this project:

- `docs/project-context.md` - project summary, goals, current state
- `_refs/1st-lab/` - 1st lab instructions and materials
- `_refs/2nd-lab/` - 2nd lab instructions and materials

## Rules

- `_notes/todo.md` is a personal scratchpad. Read-only. Never edit, reformat, or clean it up.
- When the user references a lab, assignment, or Moodle content, check `_refs/` before asking.
- `docs/project-context.md` is the source of truth for project scope and completed work. Keep it in sync when major work finishes.

## Diagram Format

All UML diagrams in this project use PlantUML (`.puml` files), not Mermaid.

- Working diagram files live in `_refs/export-og/` as the exact representation of the current Magic model.
- Fixed or improved versions go in `_refs/export-fixed/`.
- Source XML exports from MagicDraw are in `_refs/export-source/`.
- When generating, fixing, or discussing any diagram (use case, class, activity, sequence, state, package), always produce PlantUML syntax.
- PlantUML relationships:
  - `-->` for associations
  - `.>` with `<<include>>` / `<<extend>>` for use case relationships
  - `--|>` for generalization
  - `<|--` for inheritance in class diagrams
- Phase 1 diagrams (use case, activity, state, class) keep Lithuanian names.
- Phase 2 diagrams (package, sequence) use English.

## Magic Systems Module Specifics

### Activity Diagram Decision Nodes

University requirement:

- Decision diamond must be empty. Do not put question text inside it: `if () then ([label])`
- The "yes" branch label describes the action or condition being taken, in square brackets: `([nori keisti])`
- The "else" branch is always labeled `([else])`
- Never write the negative condition on the else branch
- PlantUML form: `if () then ([positive action]) ... else ([else]) ... endif`
