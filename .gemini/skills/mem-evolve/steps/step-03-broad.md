# Step 3B: Broad Discovery (path 3 — all sessions)

## Your Task

Scan all recorded sessions with no filter, group by project, show a project index, then let the user pick which projects to include in the scope.

## Execution

Run in parallel:

```
search(type="sessions",     limit=200)
search(type="observations", limit=200)
```

Group results by project name. For each project compute: session count, observation count, type breakdown, date range.

## Output — Project Index

```
📊 All Recorded Projects
────────────────────────────────────────────────────────────

  #   Project                  Sessions   Obs    Date Range
  ─── ───────────────────────  ────────   ────   ──────────────────
  1   agentic-dev-playground      30+      50    Apr 1 → Apr 2
  2   my-other-app                 6       88    Mar 1 → Mar 28
  3   side-project                 2       14    Feb 10 → Feb 11

  3 projects · 38 sessions · 152 observations total

  ───────────────────────────────────────────────────────────
  agentic-dev-playground
    🔵 26  discovery    architecture dives, system analysis
    🟣 13  feature      skill creation, workflows, guides
    ✅  6  change       docs, context files, diagrams
    ⚖️  4  decision     architecture choices, format decisions
    🔴  1  bugfix       UI tag sync fix

  my-other-app
    🔵 40  discovery    ...
    🟣 20  feature      ...
    ...
```

## Project Selection Menu

```
Select projects to analyze:

  [1]   Pick one project          — enter its number
  [2]   Pick multiple projects    — enter numbers separated by spaces
  [3]   All projects

Enter 1, 2, or 3:
```

**HALT — wait for input.**

- If `1`: `Enter project number:` → store that project in `selected_scope`
- If `2`: `Enter project numbers (e.g. 1 2 3):` → store those projects in `selected_scope`
- If `3`: store all project names in `selected_scope`

Then load `./step-04-artifacts.md`.
