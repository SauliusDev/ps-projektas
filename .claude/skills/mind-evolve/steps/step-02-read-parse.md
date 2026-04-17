# Step 2: Read & Parse mind.md

## Your Task

Read `mind_path` and parse its sections. Also read `index.yaml` for sync metadata. Then show a compact summary.

## Execution

Read both files:
- `{mind_path}` (e.g. `_mind/mind.md`)
- `_mind/index.yaml`

Parse mind.md into named sections:
- `current_state` — text under `## Current State`
- `active_work` — bullet list under `## Active Work`
- `lessons_learned` — ✓ and ✗ bullets under `## Lessons Learned`
- `key_decisions` — bullets under `## Key Decisions`
- `journey` — narrative under `## Journey`

If mind.md does not exist or is empty:
```
⚠️  No mind.md found at {mind_path}.
Run /mind-sync first to generate the project memory file.
```
Then stop.

## Output

```
mind.md parsed — sync #{sync_count} · {line_count} lines · last updated {date}
────────────────────────────────────────────────────────────
  Active Work:      {N} items
  Lessons Learned:  {N} ✓ worked  /  {N} ✗ failed
  Key Decisions:    {N} entries
  Journey:          {N} lines
```

---

Load `./step-03-artifacts.md`.
