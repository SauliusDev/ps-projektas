# Step 4: Analyze & Extract Candidates

## Your Task

Scan the relevant mind.md sections for each selected artifact type. Identify the strongest 3–7 candidates per type. Show them as a lettered list with a one-line description and the exact quoted evidence from mind.md that justifies each suggestion.

---

## Section → Artifact Signal Map

Only scan sections relevant to `selected_artifacts`:

| Artifact | Scan these sections | Look for |
|---|---|---|
| **Skills** | `active_work`, `journey` | Recurring workflow phrases, repeated approaches, "always do X first" patterns |
| **Rules** | `key_decisions`, `lessons_learned ✓` | Explicit constraints, architectural choices, "we decided to always..." |
| **Hooks** | `lessons_learned ✗`, `key_decisions` | Failures caused by skipping a step, "should have run X after Y" |
| **Agents** | `active_work`, `journey` | Multi-step processes taking significant effort, complex recurring tasks |
| **Commands** | `active_work`, `journey` | Repeated request patterns, phrases that look like slash commands |

---

## Filtering Rules

- Prefer entries that appear in **multiple sections** (same concept in active_work AND journey = stronger signal)
- Prefer `✗` lessons for hooks (they reveal what should be automated)
- Prefer long journey narrative segments (high detail = real recurring effort)
- Cap at 7 candidates per type — quality over quantity

---

## Candidate Summary Output

Display one block per selected artifact type using this exact format:

```
🟣 SKILL CANDIDATES
────────────────────────────────────────────────────────────
  [A]  "bmad-epic-bootstrap"     — Set up new epic with ledger + story files
                                   Evidence (Active Work): "Epic 01 — in progress: create story files"
                                   Evidence (Journey): "bootstrapped epics 01–03 using same ledger pattern"

  [B]  "mind-first-context"      — Read mind.md before any implementation task
                                   Evidence (Journey): "lost context mid-session, had to re-read docs"

⚖️  RULE CANDIDATES
────────────────────────────────────────────────────────────
  [C]  "no-direct-bmad-edits"    — Never edit _bmad/ without explicit request
                                   Evidence (Key Decisions): "treat _bmad as immutable module source"

  [D]  "compress-not-append"     — mind.md must never grow unboundedly
                                   Evidence (Key Decisions): "merge and compress — never append"

🔴 HOOK CANDIDATES
────────────────────────────────────────────────────────────
  [E]  "post-story-mind-sync"    — Run mind-sync after each story completion
                                   Evidence (Lessons ✗): "missed syncing after story 03, lost decisions"

🤖 AGENT CANDIDATES
────────────────────────────────────────────────────────────
  [F]  "epic-reviewer"           — Review completed epic for lessons and gaps
                                   Evidence (Active Work): "retrospective — pending: capture what failed in epic 01"

⚡ COMMAND CANDIDATES
────────────────────────────────────────────────────────────
  [G]  "/start-story"            — Kick off a story with full context load
                                   Evidence (Journey): "started each story by reading mind.md + PRD + epic spec"

────────────────────────────────────────────────────────────
Candidates grounded in mind.md — no invented patterns.

Which would you like to expand and save?
Enter letters separated by spaces (e.g. A C F) or enter ALL:
```

**HALT — wait for input.**

Store selected candidates. Then load `./step-05-generate.md`.
