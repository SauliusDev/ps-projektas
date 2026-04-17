# Step 1: Greeting

## Your Task

Greet the user and present the three discovery paths. Do not run any MCP calls yet.

## Output

```
╔══════════════════════════════════════════════════════════╗
║              mem-evolve · Workflow Extractor             ║
╚══════════════════════════════════════════════════════════╝

Analyzes your claude-mem session history and generates
reusable Claude Code artifacts: skills, rules, hooks,
agents, and commands.

How would you like to search your memory?

  [1] Current project  — scan sessions from this directory
  [2] Keyword search   — enter a topic, project name, or tag
  [3] All sessions     — broad scan, then pick what to analyze

Enter 1, 2, or 3:
```

**HALT — wait for user input.**

- If `1` → load `./step-02-quick.md` with mode=`current`
- If `2` → ask: `Enter keyword or project name:` then load `./step-02-quick.md` with mode=`keyword`
- If `3` → load `./step-03-broad.md`
