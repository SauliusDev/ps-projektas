---
name: create-agent-loaders
description: Create or refresh the root `AGENTS.md` and `GEMINI.md` loader files so they point to `.claude/CLAUDE.md`, the full `.claude/rules/` directory, and the shared `.claude/skills/` library. Use when the project should keep `.claude/` as the canonical AI configuration source and generate the root agent loader files.
---

# Create Agent Loaders

Create the root `AGENTS.md` and `GEMINI.md` files as thin loaders that route tooling back to `.claude/`.

## Run

From the repository root, run:

```bash
bash .claude/skills/create-agent-loaders/scripts/generate-root-loaders.sh
```

## Behavior

- Overwrites `AGENTS.md` and `GEMINI.md` in the repository root.
- Keeps `.claude/CLAUDE.md` as the canonical shared instructions source.
- Refers to `.claude/rules/` as a directory, not individual files.
- Refers to `.claude/skills/` as the shared skill library.
- Preserves the project-specific read-only rule for `_notes/todo.md`.

## Notes

- Use this skill after changing how root loader files should look.
- If the project moves away from `.claude/` as the canonical source, update the script before rerunning it.
