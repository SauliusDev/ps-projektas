---
name: recommend-plugins
description: 'Scan the current project and Claude Code plugin marketplaces to recommend plugins worth installing — filtered to the actual stack. Detects already-installed plugins and avoids redundant suggestions. BMAD-aware: skips workflow-overlap plugins when BMAD is present.'
argument-hint: "[--install to auto-install High Value items]"
---

# Recommend Plugins

**Goal:** Scan the current project, fetch all configured Claude Code plugin marketplaces, and recommend plugins worth installing — filtered to the project's actual stack. No install bloat.

**Separation of concerns** (enforced throughout):
- **BMAD** = workflow orchestration. Never recommend plugins that duplicate BMAD's story/sprint/dev/architecture workflow.
- **Plugins** = MCP servers, LSP providers, skill packs, hook systems. Complement the development stack.

---

## CRITICAL INSTRUCTIONS

- Execute all stages in order. HALT at every checkpoint and wait for user input.
- Never install plugins without explicit user confirmation.
- Skip plugins already installed (enabled or disabled).
- If a marketplace fetch fails, note the failure and continue with remaining marketplaces.
- Speak in `communication_language` from project config if available, otherwise English.

---

## STAGE 1: Introduction

Greet the user in 2–3 sentences:
- This skill scans the project to understand the stack and currently installed plugins.
- It fetches all configured plugin marketplaces to find plugins worth adding.
- It only recommends plugins that actually fit — no copy-all-of-marketplace bloat.

If `--install` was passed as an argument, note it: "I'll auto-install High Value items after analysis."

Do NOT halt here — proceed directly to Stage 2.

---

## STAGE 2: Project Scan

Scan in parallel. Read everything simultaneously.

### 2a — Installed plugins
Run: `claude plugins list`
Parse output to build a map of:
- Plugin name + marketplace (e.g. `typescript-lsp@claude-plugins-official`)
- Status: enabled / disabled
- Scope: user / project

Note: disabled plugins count as "already installed" — do NOT re-recommend them. The user explicitly disabled them.

### 2b — Stack detection
Read whichever exist (in parallel):
- `package.json` → extract `name`, `dependencies`, `devDependencies`
- `requirements.txt` or `pyproject.toml`
- `Cargo.toml`
- `go.mod`
- `.claude/CLAUDE.md` or root `CLAUDE.md` — for project type hints
- Root directory listing — infer project type from structure

### 2c — BMAD detection
- List `.claude/skills/` — check for any `bmad-*` folders → **BMAD detected** flag
- Check for `_bmad/` directory → confirm BMAD flag

### 2d — Summarize findings

Output a concise scan summary:
```
Project scan complete
- Project: [name or "unnamed"]
- Stack: [language(s)] + [framework(s)] + [test framework] + [build tool]
- Type: [web app / VS Code extension / CLI / library / etc.]
- BMAD: [detected / not detected]
- Installed plugins (enabled): [list name@marketplace]
- Installed plugins (disabled): [list — will be excluded from recommendations]
```

---

## STAGE 3: Fetch Plugin Marketplace Inventory

### 3a — Discover configured marketplaces
Run: `claude plugins marketplace list`
Extract each marketplace name and its GitHub source (format: `owner/repo`).

### 3b — Fetch each marketplace's plugin inventory

For each marketplace with a GitHub source, fetch its full file tree:
```
https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1
```

Parse the `tree` array to extract all plugin directories (both `plugins/` and `external_plugins/` if present). For each plugin directory found, note:
- Plugin name (directory name)
- Whether it has a `.claude-plugin/plugin.json` (installable) or is LSP-only (no plugin.json, install requires separate setup)
- Marketplace it belongs to

If the GitHub API tree fetch fails for a marketplace, fetch its README as fallback:
```
https://raw.githubusercontent.com/{owner}/{repo}/main/README.md
```

### 3c — Fetch plugin descriptions

For each candidate plugin (not already installed, not obviously irrelevant), fetch its `plugin.json`:
```
https://raw.githubusercontent.com/{owner}/{repo}/main/{plugin-path}/.claude-plugin/plugin.json
```

Extract the `description` field. If no `plugin.json` exists, check for a `README.md` in that plugin's directory to understand what it provides.

Batch fetches in parallel where possible.

### 3d — Summarize inventory

```
Marketplace inventory
- [marketplace-name]: [N] plugins found ([list plugin names])
```

---

## STAGE 4: Analysis — Fit Assessment

For each discovered plugin, classify it using these rules in order:

### Skip immediately if:
- Already installed (enabled or disabled) — user has already made a decision
- Language LSP for a language not in the detected stack (e.g. pyright-lsp when no Python, swift-lsp when no Swift)
- Backend/infra service not in the stack (e.g. supabase, firebase, terraform, laravel-boost when not detected)
- Communication/social tool with no clear dev workflow use (e.g. imessage, fakechat, telegram for non-bot projects)
- Meta/example plugins (example-plugin, plugin-dev unless the project is building Claude plugins)
- BMAD is detected AND the plugin is primarily a dev workflow orchestrator that duplicates BMAD coverage

### High Value if:
- MCP server for a service/tool the project actively uses (detected in stack or config)
- LSP for a language actively used AND not yet installed
- Skill pack that covers a framework/pattern in active use
- E2E/browser testing tool when the project has a web UI layer or webviews (e.g. playwright for VS Code extensions with webviews)
- Git workflow utility that adds commands not already handled by BMAD or existing setup
- Code quality tool that operates at PR/review level (not duplicating existing test tooling)

### Consider if:
- Useful utility but overlaps partially with existing setup
- Service integration that might be used but isn't confirmed in the stack
- Output-style or UX preference tools (subjective, user may already have preferences)
- Claude Code meta-tools (recommenders, setup wizards) — useful to run once, not permanently

### BMAD coexistence rule:
If BMAD is detected, add this note to the output:
> BMAD is present — plugins that duplicate sprint/story/PR workflow management are excluded. Recommended plugins are stack tooling and MCP integrations that complement BMAD's implementation work.

---

## STAGE 5: Present Tiered Recommendations

```
## Plugin Recommendations — [project name]
[BMAD note if applicable]

### High Value — Install Immediately
These directly serve the detected stack.

| # | Plugin | Marketplace | Type | Why |
|---|--------|-------------|------|-----|
| 1 | [name] | [marketplace] | MCP/Skill/LSP | [one line tied to detected stack] |

### Consider — Evaluate for Fit
May overlap with existing setup; worth reviewing before installing.

| # | Plugin | Marketplace | Consideration |
|---|--------|-------------|---------------|

### Skip — Already Installed or Not Relevant
| Plugin | Reason |
|--------|--------|

---
Summary: [N] high value · [N] consider · [N] skip
Install command preview:
  claude plugins install [name]@[marketplace]
```

Then ask:
```
What would you like to do?
[A] Install all High Value items
[C] Install specific items — tell me which (use numbers or names)
[R] Show details for a plugin before deciding
[N] Analysis only — no installation needed
```

If `--install` was passed at invocation, skip this menu and proceed directly to Stage 6 with all High Value items.

**HALT** and wait for response.

---

## STAGE 6: Installation

### 6a — Install selected plugins

For each selected plugin, run:
```
claude plugins install [name]@[marketplace]
```

Report each result:
```
✓ playwright@claude-plugins-official — installed (restart may be required)
✗ github@claude-plugins-official — install failed: [error message]
```

If an install fails, note the error and continue with remaining items. Do not halt the entire batch.

### 6b — Post-install notes

After all installs complete, list any plugins that require additional setup (auth tokens, env vars, MCP server configuration) based on their plugin.json or README content. Keep this brief — one line per plugin that needs it.

### 6c — Project-scope disable (optional)

If the user wants to disable a plugin only for this project (not globally), offer to add it to `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "[name]@[marketplace]": false
  }
}
```

Ask: `[Y] Add project-level disables  [N] Skip`

**HALT** and wait, then apply if confirmed.

### 6d — Installation summary

```
Installation complete

Installed:
- [name]@[marketplace] — [one-line description]

Failed:
- [name] — [reason]

[N] plugins require additional setup — see notes above.

Restart Claude Code to activate newly installed plugins.
```

**HALT.** Skill complete.

---

## Reference: Plugin Priority Guide

This table is canonical guidance baked into this skill. Use it in Stage 4 regardless of the project.

| Plugin Category | High Value If | Consider If | Skip If |
|----------------|--------------|-------------|---------|
| Language LSP | Language is in active stack, LSP not installed | | Language not in stack |
| Browser/E2E testing (playwright) | Project has web UI, webviews, or visual components | | Pure backend/CLI only |
| GitHub MCP | Project is hosted on GitHub | | GitLab used instead |
| GitLab MCP | Project is hosted on GitLab | | GitHub used instead |
| Code review skill | No existing PR review workflow | BMAD present (partial overlap) | |
| Git workflow commands (/commit etc.) | No existing commit automation | BMAD handles commits | |
| Frontend design skill | React/Vue/Svelte + Tailwind/CSS in stack | | Backend only |
| Service MCP (supabase/firebase/etc.) | Service detected in stack/config | | Service not in stack |
| Communication MCPs (slack/discord) | Project is a bot or integrates the service | | General dev project |
| Output style hooks | User preference only | | |
| BMAD-overlap workflow plugins | | | BMAD detected |
| Meta/setup tools | First-time project setup | Project already well-configured | |
