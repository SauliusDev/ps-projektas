
# General

## Context Loading

Read these first when starting work on this project:

- `docs/project-context.md` — project summary, goals, current state
- `_refs/1st-lab/` — 1st lab instructions and materials
- `_refs/2nd-lab/` — 2nd lab instructions and materials

## Rules

- `_notes/todo.md` is a personal scratchpad. **Read-only** — never edit, reformat, or "clean up". Use it as reference only.
- When the user references a lab, assignment, or moodle content, check `_refs/` before asking.
- `docs/project-context.md` is the source of truth for project scope and completed work — keep it in sync when major work finishes.

## Diagram Format

All UML diagrams in this project use **PlantUML** (`.puml` files) — not Mermaid.

- Working diagram files live in `_refs/export-og/` (exact representation of the current Magic model)
- Fixed/improved versions go in `_refs/export-fixed/`
- Source XML exports from MagicDraw are in `_refs/export-source/`
- When generating, fixing, or discussing any diagram (use case, class, activity, sequence, state, package), always produce PlantUML syntax
- PlantUML relationships: `-->` for associations, `.>` with `<<include>>` / `<<extend>>` for UC relationships, `--|>` for generalization, `<|--` for inheritance in class diagrams
- Phase 1 diagrams (use case, activity, state, class) keep Lithuanian names; Phase 2 diagrams (package, sequence) use English

# Magic systems module specifics

## Activity Diagram Decision Nodes (university requirement)

- Decision diamond must be **empty** — no question text inside: `if () then ([label])`
- The **"yes" branch** label describes the action/condition being taken, in square brackets: `([nori keisti])`
- The **"else" branch** is always labeled `([else])` — never write the negative condition (e.g. not `(ne)`, not `(nori keisti)`)
- PlantUML syntax: `if () then ([positive action]) ... else ([else]) ... endif`

