# Step 5: Extract — Targeted Searches + Candidate Summaries

## Your Task

Run targeted searches per selected artifact type. Filter aggressively. Show candidate summaries. User picks which to expand into full artifacts.

Use `project=` filter for each item in `selected_scope`. If multiple projects, run searches for each and merge results. If scope was a keyword (from path 2), use `query=` instead.

---

## Search Map

Run only searches for `selected_artifacts`. Run all applicable in parallel.

```
Skills   → search(type="observations", obs_type="feature,change",    limit=50, orderBy="relevance")
Rules    → search(type="observations", obs_type="decision,discovery", limit=50, orderBy="relevance")
Hooks    → search(type="observations", obs_type="bugfix,change",      limit=50, orderBy="relevance")
Agents   → search(type="observations", obs_type="discovery,feature",  limit=30, orderBy="relevance")
           search(type="sessions",                                     limit=30)
Commands → search(type="prompts",                                      limit=100, orderBy="relevance")
```

---

## Filtering

After searches return, identify the 5–10 strongest IDs per type by looking for:
- Same concept in 3+ sessions
- Explicit repeating pattern in titles
- High work_token observations (expensive = complex = worth encoding)

Batch-fetch full details for filtered IDs only:

```
get_observations(ids=[...top IDs per type...])
```

---

## Candidate Summary Output

Display one block per artifact type. Use this exact format:

```
🟣 SKILL CANDIDATES
────────────────────────────────────────────────────────────
  [A]  "framework-cookbook"    — Create 101-style plugin cookbook
                                 Triggered identically 3× (#32, #62, #74)
                                 Pattern: read _refs/X → write guide → save to _notes/

  [B]  "plugin-deep-dive"      — Comprehensive architecture analysis
                                 Done 3× (BMAD, Superpowers, ECC), 40–180min each

⚖️  RULE CANDIDATES
────────────────────────────────────────────────────────────
  [C]  "xml-tags-are-conventions"  — XML tags like <HARD-GATE> are semantic, not primitives (#23)
  [D]  "ecc-rules-reference"       — Reference ECC rules from CLAUDE.md, don't copy (#112)

🔴 HOOK CANDIDATES
────────────────────────────────────────────────────────────
  [E]  "session-context-loader"    — Inject prior session summary via hook stdout (#118)
  ⚠️  Low signal — only 1 bugfix recorded. Suggesting based on observed reference patterns.

🤖 AGENT CANDIDATES
────────────────────────────────────────────────────────────
  [F]  "plugin-analyst"        — Full architecture report for a given plugin path
                                 Done 3× taking 40–180min each (#92, #95, #15)

⚡ COMMAND CANDIDATES
────────────────────────────────────────────────────────────
  [G]  "/make-cookbook"        — "make cookbook for X" triggered 3× identically
  [H]  "/explain-skill"        — "explain how [skill] works" asked 5+ times

────────────────────────────────────────────────────────────
These are the strongest candidates grounded in actual observations.

Which would you like to expand and save?
Enter letters separated by spaces (e.g. A C F) or enter ALL:
```

**HALT — wait for input.**

Store selected candidates. Then load `./step-06-generate.md`.
