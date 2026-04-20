
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

## Diagram Format - KTU course module specifics

All UML diagrams in this project use **PlantUML** (`.puml` files) — not Mermaid.

- Working diagram files live in `_refs/export-og/` (exact representation of the current Magic model)
- Fixed/improved versions go in `_refs/export-fixed/`
- Source XML exports from MagicDraw are in `_refs/export-source/`
- When generating, fixing, or discussing any diagram (use case, class, activity, sequence, state, package), always produce PlantUML syntax
- PlantUML relationships: `-->` for associations, `.>` with `<<include>>` / `<<extend>>` for UC relationships, `--|>` for generalization, `<|--` for inheritance in class diagrams
- Phase 1 diagrams (use case, activity, state, class) keep Lithuanian names; Phase 2 diagrams (package, sequence) use English
- at least 4 difficult use cases colored reddish color
- use case nodes: decision, action, merge, and reference action nodes extends/includes

## Diagram Validation (REQUIRED before marking work done)

- ELK is alpha and not bundled in the VS Code extension — never use `!pragma layout elk`
- Graphviz 14.1.5 is incompatible with the local PlantUML CLI — CLI validation will fail for use case / class diagrams; the VS Code extension uses its own renderer and works fine
- Use case diagrams for this project use **Mermaid** (`.mmd`) — PlantUML cannot produce a clean LR layout for them

After writing or editing any `.puml` file, **always** validate it renders without errors:

```bash
plantuml -tpng -o /tmp/puml_check <file.puml>
# Then check the output PNG for syntax error images:
strings /tmp/puml_check/<name>.png | grep -qi "syntax\|error" && echo "ERROR" || echo "OK"
```

To validate a whole directory at once:
```bash
find <dir> -name "*.puml" | while read f; do
  plantuml -tpng -o /tmp/puml_check "$f" 2>/dev/null
  png="/tmp/puml_check/$(basename ${f%.puml}).png"
  strings "$png" 2>/dev/null | grep -qi "syntax\|error" && echo "ERROR: $f" || echo "OK: $f"
done
```

**Important notes:**
- Sequence diagrams use PlantUML's built-in renderer — no external dependency
- Package and class diagrams require **Graphviz** (`dot`). If `dot` is missing from PATH, run `brew link graphviz`
- Do not report diagrams as done until the validation passes
- After batch-writing files via bash, the VSCode PlantUML extension may show stale "No valid diagram found" errors from cached old renders. Fix: `Ctrl+Shift+P → Developer: Reload Window`

### Mermaid `.mmd` validation (REQUIRED before marking work done)

After writing or editing any `.mmd` file, **always** validate it parses without errors using the Mermaid CLI:

```bash
npx mmdc -i <file.mmd> -o /tmp/mmd_check.png 2>&1 | grep -i "error\|warn"
# No output = clean. Any output = fix before proceeding.
```

To validate a whole directory at once:
```bash
for f in <dir>/*.mmd; do
  result=$(npx mmdc -i "$f" -o /tmp/mmd_check.png 2>&1 | grep -i "error\|warn")
  [ -z "$result" ] && echo "OK: $f" || echo "ERROR: $f — $result"
done
```

**Common Mermaid parse mistakes to avoid:**
- Arrow typo: `.--> ` is invalid — always use `.-> ` for dashed arrows
- Edge labels with `«»` characters must be inside double quotes: `-. "«extend»" .->`
- Do NOT use `\n` in edge labels — Mermaid does not support it; use a space or `<br/>` in node labels only

# Magic systems module specifics

## Activity Diagram Decision Nodes (university requirement)

- Decision diamond must be **empty** — no question text inside: `if () then ([label])`
- The **"yes" branch** label describes the action/condition being taken, in square brackets: `([nori keisti])`
- The **"else" branch** is always labeled `([else])` — never write the negative condition (e.g. not `(ne)`, not `(nori keisti)`)
- PlantUML syntax: `if () then ([positive action]) ... else ([else]) ... endif`

