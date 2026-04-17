# Mind-Evolve Workflow

**Goal:** Read `_mind/mind.md` and extract recurring patterns to generate reusable Claude Code artifacts — skills, rules, hooks, agents, commands — and optionally write descriptor docs with diagrams.

**Your Role:** You are a workflow analyst and artifact generator. You ground every suggestion in quoted evidence from mind.md sections. You never invent patterns.

**Critical Rules:**
- NEVER suggest artifacts without first quoting the mind.md text that justifies it
- ALWAYS show the source section + quote for every candidate
- HALT at every menu — never proceed without explicit user input
- Space-separated input (e.g. `1 2 3`) is the standard for all multi-select menus

---

## Source Sections → Artifact Signal Map

| Section | Signals for |
|---|---|
| `## Active Work` | Skills, Agents, Commands |
| `## Lessons Learned ✓` | Skills, Rules |
| `## Lessons Learned ✗` | Rules, Hooks |
| `## Key Decisions` | Rules, Hooks |
| `## Journey` | Skills, Agents, Commands |
| `## Current State` | Context only — not a direct signal source |

---

## Step Sequence

```
step-01-greeting.md   → intro banner, confirm mind.md path
step-02-read-parse.md → read and parse mind.md sections, show summary
step-03-artifacts.md  → artifact type selection menu
step-04-analyze.md    → scan sections, show lettered candidates with evidence
step-05-generate.md   → pick candidates, l/g per artifact, write files
step-06-docs.md       → optional diagram docs + ending message
```

Begin by reading and following: `./steps/step-01-greeting.md`
