# Project-Local Codex Setup

This folder is the project-local home for Codex-specific files.

## What is here

- `AGENTS.md` - the main project instructions for Codex

## Why there is still a root `AGENTS.md`

Codex auto-discovers `AGENTS.md` by path scope. In practice, that means a repository-level loader file is still needed if you want the real instructions to live inside a hidden project folder.

So the structure is:

- root `AGENTS.md` - tiny loader shim for discovery
- `.codex/AGENTS.md` - actual project-specific Codex instructions

## Important limitation

Unlike Claude's project folder conventions, Codex does not currently offer a fully equivalent repo-local hidden config directory that replaces `AGENTS.md` for automatic instruction loading.

So this is the cleanest project-local layout that still works with Codex today.
