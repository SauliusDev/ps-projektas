---
name: recommend-ecc
description: 'Analyze a project and recommend what to adopt from the ECC (Everything Claude Code) repository — rules, skills, hooks. Use when setting up Claude Code for a new project or improving an existing setup. Respects BMAD/ECC separation: BMAD owns workflow, ECC provides coding guidance.'
argument-hint: "[optional: rules|skills|all] [--install to auto-install High Value items]"
---

# Recommend ECC

**Goal:** Scan the current project, fetch the ECC repository, and recommend the specific ECC artifacts worth adopting — filtered to the project's actual stack. No bloat.

**Separation of concerns** (enforced throughout):
- **BMAD** = workflow orchestration (story lifecycle, PRDs, sprints, dev stories, agent personas). Never suggest ECC workflow agents if BMAD is present.
- **ECC** = coding guidance (rules, conventions, utility skills, hooks). Complements BMAD — does not replace it.

---

## CRITICAL INSTRUCTIONS

- Execute all stages in order. HALT at every checkpoint and wait for user input.
- Never suggest ECC workflow skills/agents if BMAD is detected in the project.
- Never install files without explicit user confirmation.
- If a GitHub fetch fails, try the fallback URL or note the failure and continue with available data.
- Speak in `communication_language` from project config if available, otherwise English.

---

## STAGE 1: Introduction and Scope Confirmation

Greet the user and explain in 2–3 sentences:
- This skill scans the project to understand the stack and existing Claude Code setup.
- It fetches the ECC repo to find rules, skills, and hooks worth adopting.
- It only recommends what actually fits — no copy-all-of-ECC bloat.

Present scope options:
```
What should I analyze?
[1] Full sync — rules + skills (recommended)
[2] Rules only — better coding standards, always loaded
[3] Skills only — on-demand pattern references
[4] I have a specific area in mind — tell me
```

If `--install` was passed as an argument, note it: "I'll auto-install High Value items after analysis."

**HALT** and wait for scope selection.

---

## STAGE 2: Project Scan

Scan in parallel. Read everything simultaneously.

### 2a — Documentation
- List files in `_notes/` (if exists) — look for stack notes, guides, scope docs
- Read `_notes/ecc-project-scope-guide.md` if it exists — use as supplementary guidance
- List files in `docs/` (if exists)
- Read `CLAUDE.md` (root level, if exists)
- Read all files in `.claude/rules/` — these are already-loaded rules; nothing from ECC should duplicate them

### 2b — Installed Claude Code artifacts
- List `.claude/skills/` — note all installed skill folder names
- Check for any `bmad-*` skills → **BMAD detected** flag
- Check for `_bmad/` directory → **BMAD detected** flag (double-confirm)

### 2c — Stack detection
Read whichever exist:
- `package.json` → extract `name`, `dependencies`, `devDependencies`
- `requirements.txt` or `pyproject.toml`
- `Cargo.toml`
- `go.mod`
- Root directory listing (infer project type from structure)

### 2d — Summarize findings

**Missing directory handling:**
- If `.claude/rules/` does not exist or is empty: record "no existing rules" — this means all ECC common rules are GAPs. Also check CLAUDE.md for inline coding conventions that might cover the same ground before classifying as a gap.
- If `CLAUDE.md` does not exist: record "no CLAUDE.md" — Stage 6e will skip the CLAUDE.md update offer unless one is created.
- If `.claude/skills/` does not exist: record "no installed skills" — all ECC skills are candidates.

Output a concise scan summary:
```
Project scan complete
- Project: [name or "unnamed"]
- Stack: [language(s)] + [framework(s)] + [test framework]
- BMAD: [detected / not detected]
- Existing rules: [list rule file names, or "none"]
- Existing skills: [count total, list non-bmad skills; count bmad-* separately]
- Notes found: [list relevant docs]
```

---

## STAGE 3: Fetch ECC Repository

Retrieve ECC inventory using WebFetch. Attempt in order:

**Primary — GitHub API tree (full inventory in one call):**
```
https://api.github.com/repos/affaan-m/everything-claude-code/git/trees/main?recursive=1
```
Parse the `tree` array. Extract:
- All `path` values under `rules/common/` → common rule files
- All `path` values under `rules/{lang}/` where `{lang}` matches detected stack languages → language rule files
- All directory names directly under `skills/` → available skills
- Any files under `hooks/`

**Fallback — README (if API fails or returns empty):**
```
https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/README.md
```
Parse the README for skill/rule listings. **IMPORTANT:** Only list artifacts explicitly named in the README. Do not infer or guess artifact names — if the README is sparse or yields no listing, proceed to the "both fetches fail" branch below.

**Summarize ECC inventory:**
```
ECC inventory
- Common rules: [list file names]
- [Language] rules: [list — only languages matching detected stack]
- Skills available: [list skill names]
- Hooks: [list if any]
```

If both fetches fail: note the failure, check if maybe the repo exists locally at `_blueprint/refs/everything-claude-code/` if not offer user to git clone the repo there and read from it. If local fetch also fails, report that ECC inventory is unavailable and skip to Stage 5 with only project scan data to work with.

---

## STAGE 4: Analysis — Gap Detection

Cross-reference project state against ECC inventory. Apply these rules:

### Rules analysis

For each ECC common rule file:
1. Check if an equivalent already exists in `.claude/rules/` (by content intent, not just filename)
2. Mark as **GAP** if no equivalent — candidate for adoption
3. Mark as **COVERED** if project already has equivalent coverage — skip it

For language rules:
- Only consider rules for detected stack languages
- Apply same GAP/COVERED logic
- Skip if CLAUDE.md already captures the same decisions inline

### Skills analysis

For each ECC skill:
- **Skip immediately** (do not recommend) if:
  - It is a workflow methodology skill: `autonomous-loops`, `continuous-learning*`, `workflow*`, `plan*`
  - It is an ECC meta-tool: `configure-ecc`, `skill-comply`, `skill-stocktake`, `skill-sync`
  - BMAD is detected AND the skill overlaps with BMAD workflow (story execution, PRD, sprint, architecture planning)
  - The project doesn't use the relevant framework/language

- **Candidate for recommendation** if:
  - It covers a framework the project actively uses (e.g. React, Supabase, Docker, Prisma)
  - It is a utility skill applicable to the detected test framework (e.g. `tdd-workflow`)
  - The project has no equivalent skill installed

### BMAD + ECC coexistence rule

If BMAD is detected, add this note to the output:
> BMAD is present — ECC workflow agents are excluded. Recommended ECC artifacts are coding guidance only and are designed to be invoked by BMAD agents during implementation.

---

## STAGE 5: Present Tiered Recommendations

Present three tiers:

```
## Recommend ECC — Recommendations for [project name]
[BMAD note if applicable]

### High Value — Adopt Immediately
These fill clear gaps and improve every session.

| # | Artifact | Type | Path in ECC | Why |
|---|---|---|---|---|
| 1 | [name] | rule/skill | [ecc path] | [one line tied to detected stack] |

### Consider — Evaluate for Fit
May overlap with existing conventions; review before installing.

| # | Artifact | Type | Consideration |
|---|---|---|---|

### Skip — Already Covered or Not Relevant
| Artifact | Reason |
|---|---|

---
Summary: [N] high value · [N] consider · [N] skip
```

Then ask:
```
What would you like to do?
[A] Install all High Value items
[C] Install specific items — tell me which (use numbers or names)
[R] Review an item's content before deciding
[N] Analysis only — no installation needed
```

If `--install` was passed at invocation, skip this menu and proceed directly to Stage 6 with all High Value items.

**HALT** and wait for response.

---

## STAGE 6: Installation

For each selected item, execute:

### 6a — Fetch content

Fetch the raw file from GitHub:
- Rule: `https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/{ecc-path}`
- Skill: fetch each file in the skill's directory (start with the main SKILL.md, then supporting files)

If the user provided a local ECC path (from Stage 3 fallback), read from there instead.

If fetching an individual file fails, report it (`✗ [path] — fetch failed, skipping`) and continue to the next item. Do not halt the entire installation for a single file failure.

### 6b — Determine destination

| Item type | Destination |
|---|---|
| Common rule | `.claude/rules/{filename}` |
| Language rule | `.claude/rules/{lang}-{filename}` (prefix with language to avoid collisions) |
| Skill | `.claude/skills/{skill-name}/SKILL.md` (create folder) |
| Hook | Ask user — hooks go in `.claude/hooks/` or per-project config |

### 6c — Conflict check

If the destination file already exists:
```
[filename] already exists. What should I do?
[O] Overwrite with ECC version
[K] Keep existing — skip this file
[D] Show diff first
```

### 6d — Write files

Write each confirmed file. Report each write:
```
✓ .claude/rules/coding-style.md — ECC common coding standards
✓ .claude/skills/tdd-workflow/SKILL.md — TDD pattern reference
```

### 6e — CLAUDE.md skills table (optional)

If CLAUDE.md does not exist: skip this step entirely — do not offer to create one.

If any **skills** were installed and CLAUDE.md exists, offer to add or update a Skills table in CLAUDE.md:

```markdown
## Skills

| Situation | Invoke |
|---|---|
| [use case] | `[skill-name]` |
```

If BMAD is present, also suggest this Workflow section addition:
```markdown
## Workflow
BMAD Method owns the development lifecycle.
ECC skills above are available for stack-specific patterns — invoke them during implementation.
```

Ask: `[Y] Add to CLAUDE.md  [N] Skip`

**HALT** and wait, then apply if confirmed.

### 6f — Installation summary

```
Installation complete

Files installed:
- [relative path] — [one-line description]

[CLAUDE.md updated: yes/no]

[N] item(s) deferred (already existed, kept existing version).
```

**HALT.** Skill complete.

---

## Reference: Artifact Priority Guide

This table is canonical guidance baked into this skill. Use it in Stage 4 analysis regardless of whether `_notes/ecc-project-scope-guide.md` exists.

| ECC Artifact | Always Keep | Conditional | Skip |
|---|---|---|---|
| `rules/common/coding-style.md` | Yes | | |
| `rules/common/testing.md` | Yes | | |
| `rules/common/security.md` | Yes | | |
| `rules/common/git-workflow.md` | Yes | | |
| `rules/common/development-workflow.md` | | Only if no BMAD | |
| `rules/common/agents.md` | | | If BMAD present |
| `rules/common/hooks.md` | | Only if using ECC hooks | |
| `rules/{lang}/coding-style.md` | | If lang matches stack | |
| `rules/{lang}/testing.md` | | If lang matches stack | |
| Skills (framework-specific) | | If framework is in use | |
| Skills (workflow methodology) | | | Always — BMAD owns workflow |
| ECC meta-tools | | | Always |
