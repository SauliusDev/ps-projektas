# Step 1: Greeting

## Your Task

Greet the user and confirm which mind.md to use. Do not read any files yet.

## Output

```
╔══════════════════════════════════════════════════════════╗
║             mind-evolve · Pattern Extractor              ║
╚══════════════════════════════════════════════════════════╝

Reads your project's mind.md memory file and generates
reusable Claude Code artifacts: skills, rules, hooks,
agents, and commands.

Source: _mind/mind.md

  [1] Use current project mind.md  (above path)
  [2] Specify a different path

Enter 1 or 2:
```

**HALT — wait for user input.**

- If `1` → set `mind_path = "_mind/mind.md"`, load `./step-02-read-parse.md`
- If `2` → ask: `Enter path to mind.md:` → set `mind_path` to that value, load `./step-02-read-parse.md`
