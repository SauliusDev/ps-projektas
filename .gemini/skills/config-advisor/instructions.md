# Config Advisor — Instructions

**MANDATORY:** Execute steps IN ORDER. Do not skip steps. Do not apply any suggestion — produce output only. Do not write to any `.claude/` file.

---

## HALT CHECK: Prerequisites

Before any step:

- Check that `.claude/` directory exists. If not: HALT. Display — "`.claude/` directory not found. This skill requires a Claude Code project with a `.claude/` folder."
- Check that `_mind/mind.md` exists. If not: HALT. Display — "`_mind/mind.md` is required but was not found. Ensure the file exists at `_mind/mind.md` before running this skill."

---

## Step 1: Load Existing Configuration

Load the current state of `.claude/` before touching any knowledge source. Every candidate from Steps 2–4 is checked against this baseline before being included in output.

- Read `.claude/CLAUDE.md` — note all principles, rules, and project context present. If this file does not exist, note that no CLAUDE.md baseline is present and continue.
- Read every file matching `.claude/rules/*.md` — note the filename and full content of each rule
- Read `.claude/settings.json` — note the `hooks` section specifically (what events are hooked, what commands run)
- List `.claude/skills/` — record directory names only (existing skill slugs). If this directory does not exist, record that no skills are currently installed.

Store this as your **existing config baseline**.

---

## Step 2: Analyze `_mind/mind.md`

Read `_mind/mind.md` in full. Scan the following sections:

**Lessons Learned — ✓ entries (validated patterns):**
- If a ✓ lesson describes a behavioral constraint Claude should follow → candidate CLAUDE.md principle or rule file
- If a ✓ lesson describes a validated project workflow used repeatedly → candidate skill

**Lessons Learned — ✗ entries (recurring mistakes):**
- If a ✗ lesson describes a mistake that a rule or hook could prevent → candidate rule file or hook

**Key Decisions section:**
- If a decision implies a repeatable project-specific workflow → candidate skill

For each candidate produced:
- Cross-reference against existing config baseline
- Label: **NEW** (not covered), **PARTIAL** (partially covered — note what covers it), **EXISTS** (fully covered)
- Drop EXISTS silently. Carry NEW and PARTIAL forward.

---

## Step 3: Analyze `~/.claude/usage-data/report.html`

Check whether `/home/ubuntu/.claude/usage-data/report.html` exists.

If it does NOT exist:
> Display to the user: "`~/.claude/usage-data/report.html` not found — skipping report analysis. Generate the Claude Code Insights report to enable this source."
> Continue to Step 4.

If it exists, read `/home/ubuntu/.claude/usage-data/report.html`. Parse the following sections as plain text — read through the HTML tags to the content:

**"Where Things Go Wrong" / Friction categories section:**
- Each friction category describes a recurring problem → candidate rule file or hook

**Checkbox items in "Suggested CLAUDE.md Additions":**
- Each item is a direct CLAUDE.md addition candidate

**"Existing CC Features to Try" section (hooks, custom skills, headless mode):**
- Each feature recommendation → candidate hook or skill

**"New Ways to Use Claude Code" / Usage Patterns section:**
- Each pattern → candidate rule or skill if it could be codified as a persistent constraint or reusable workflow

For each candidate produced:
- Cross-reference against existing config baseline
- Label: **NEW** (not covered), **PARTIAL** (partially covered — note what covers it), **EXISTS** (fully covered)
- Drop EXISTS silently. Carry NEW and PARTIAL forward.

---

## Step 4: Analyze `docs/*.md`

Check whether any `.md` files exist under `docs/`, excluding `docs/superpowers/` and all its subdirectories. The `docs/superpowers/` folder contains implementation specs and plans — not project documentation — and must be ignored entirely.

If no qualifying files found:
> Display to the user: "No files found at `docs/*.md` (excluding `docs/superpowers/`) — skipping docs analysis."
> Continue to Step 5.

If files exist, read each `.md` file under `docs/` that is NOT under `docs/superpowers/`. For each file, look for:

- Repeated command sequences (same commands appearing across multiple docs)
- Project-specific processes described with fixed steps (e.g., "to run migrations: step 1, step 2...")
- Testing patterns — coverage targets, how to run specific test types, test layout conventions
- Deployment or build patterns — ordered steps that always happen together
- Any phrase matching: "always do X before Y", "the process for Z is...", "when working on X you need to..."

For each recurring pattern identified, check whether a skill already exists in `.claude/skills/` that covers this scope (by name and purpose). If one exists, label EXISTS and drop it.

For each NEW or PARTIAL candidate, produce this sketch:

- **Name:** `/skill-name` (lowercase, hyphenated)
- **Purpose:** 1–2 sentences describing what the skill does and when to use it
- **Steps:**
  1. [first action the skill would take]
  2. [second action]
  3. ...
- **Uses:** [list specific files, commands, or tools the skill would call]

Label each sketch: **NEW** (not covered by any existing skill), **PARTIAL** (a related skill exists — note which one).
Carry all NEW and PARTIAL sketches forward to Step 5.

---

## Step 5: Assemble and Deduplicate

Collect all NEW and PARTIAL candidates from Steps 2, 3, and 4.

Remove exact duplicates: if the same suggestion was surfaced by multiple sources, keep it once and list all sources in the Source field.

Assign priority to each candidate:

- **High** — directly addresses a documented ✗ lesson from mind.md, or a friction category with two or more examples in report.html
- **Medium** — addresses a ✓ lesson pattern, a single-instance friction point, or codifies a validated workflow seen in docs
- **Low** — speculative, low-frequency, or a pattern seen only once with no corroborating signal

---

## Step 6: Present Report and Offer to Save

Output the full report in the conversation using this format. If a category has no candidates, output `_No suggestions for this category._` under that heading.

```
# Config Advisor Report

_Sources analyzed: [list which of the three sources were found and read]_
_Existing config loaded: [N rule files, N hooks, N skills]_

---

## 1. CLAUDE.md Additions

### [SHORT TITLE]
**Priority:** High | Medium | Low
**Source:** mind.md | report.html | docs/
**Rationale:** One sentence explaining why this matters.
**Add this:**
> [exact text to paste into CLAUDE.md]

---

## 2. Rule Files

### [RULE NAME] → `.claude/rules/[filename].md`
**Priority:** High | Medium | Low
**Source:** mind.md | report.html | docs/
**Rationale:** One sentence.
**Content:**
> [full body of the rule to write into the file]

---

## 3. Skills

### `/[skill-name]`
**Priority:** High | Medium | Low
**Source:** docs/ | mind.md | report.html
**Rationale:** One sentence.
**Sketch:**
- **Purpose:** [1–2 sentences]
- **Steps:**
  1. [step]
  2. [step]
- **Uses:** [files, commands, tools]

---

## 4. Hooks

### [HOOK NAME] → `settings.json`
**Priority:** High | Medium | Low
**Source:** mind.md | report.html | docs/
**Rationale:** One sentence.
**Config:**
\`\`\`json
{
  "hooks": {
    "[event]": [{
      "matcher": "[matcher or omit if no matcher needed]",
      "hooks": [{ "type": "command", "command": "[shell command]" }]
    }]
  }
}
\`\`\`
```

PARTIAL items append this line after Rationale:
`**Note:** Partially addressed by \`[existing file or config]\` — this extends it with [what is missing].`

---

After displaying the report, ask the user:

> "Would you like to save this report? Enter a path, press Enter for the default (`_notes/config-recommendations.md`), or type 'no' to skip."

- If the user provides a path: write the report content as a markdown file to that path.
- If the user presses Enter (no input): write the report to `_notes/config-recommendations.md`.
- If the user types 'no' or declines: end the skill.
