# Step 2Q: Quick Discovery (paths 1 & 2)

## Context

Arrived here from step-01 with either:
- `mode=current` → use cwd-derived project name
- `mode=keyword` → use the keyword the user entered

## Execution

### mode=current

Derive project name from cwd (last path segment). Run in parallel:

```
search(type="sessions",      project="{project}", limit=100)
search(type="observations",  project="{project}", limit=200)
```

### mode=keyword

Run in parallel:

```
search(query="{keyword}", limit=100)
search(type="sessions",   query="{keyword}", limit=50)
```

---

## Output

Show a compact summary of what was found, then immediately continue into the artifact menu without a second scope header:

```
Scope: {project name or keyword}
────────────────────────────────────────
  Sessions:     {N}     Date range: {earliest} → {latest}
  Observations: {N}

  {N}  discovery    — architecture dives, system analysis
  {N}  feature      — workflows, new capabilities
  {N}  change       — edits, updates, doc changes
  {N}  decision     — architectural and technical choices
  {N}  bugfix       — fixes and corrections
  {N}  refactor     — restructuring work
```

If zero results found:
```
No observations found for "{scope}".
Try option [3] All sessions from the main menu, or check that claude-mem has recorded sessions for this project.
```
Then stop.

---

Store scope as `selected_scope = ["{project or keyword}"]` and load `./step-04-artifacts.md`.
