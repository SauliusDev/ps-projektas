# Step 7: Optional Docs + Ending

## Your Task

Offer to generate diagram descriptor docs for the skills just created, then show the ending message.

---

## Docs Offer

```
Skills have been generated.

Would you like descriptor docs with Mermaid diagrams for each skill?
These are short human-readable explanations saved to .claude/evolve/
(like the ones in _notes/custom-claude/skills/)

  [y]  Yes — generate docs
  [n]  No  — skip

Enter y or n:
```

**HALT — wait for input.**

---

## If yes — generate descriptor docs

For each **skill** that was written in step-06, create a doc at `.claude/evolve/{name}/SKILL.md`.

Each doc must include:

1. **Name + 2-line description** — what it does and why it exists
2. **When to Use** — 3–4 bullet points with concrete trigger conditions
3. **Mermaid flowchart** — showing the skill's internal steps, key decision points, and tool calls. Use `flowchart TD` with subgraph boxes per major phase.
4. **Key Design Decisions** — 2–4 bullet points explaining non-obvious choices
5. **Trigger Phrases** — exact phrases or slash command that activates it

Use the doc at `_notes/custom-claude/skills/mem-evolve/SKILL.md` as the reference format.

Write one file at a time, confirm each:
```
✓  Written: .claude/evolve/framework-cookbook/SKILL.md
```

---

## Ending Message

After all docs are written (or if user skipped):

```
╔══════════════════════════════════════════════════════════╗
║              mem-evolve · Complete                       ║
╚══════════════════════════════════════════════════════════╝

Generated from {N} observations across {scope}:

  Artifacts written:
  ✓  {list each artifact with its path}

  Docs written:        (if applicable)
  ✓  {list each doc path}

  Skipped:
  ✗  {list any skipped items}

─────────────────────────────────────────────────────────
  New skills are active in the next Claude Code session.
  New rules are active immediately.
  Hook changes require restarting Claude Code.
─────────────────────────────────────────────────────────
```
