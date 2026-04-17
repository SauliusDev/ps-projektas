---
name: render-puml
description: "Render one or more .puml files to PNG. Handles the Graphviz 14.x compatibility fix required on this machine. Invoke via /render-puml."
---

# Render PlantUML Diagrams

## Background

The system has two Graphviz versions installed:
- `/opt/homebrew/opt/graphviz/bin/dot` — **14.1.5** (hardcoded in the brew `plantuml` wrapper) — **crashes** on complex diagrams with `UnparsableGraphvizException: IllegalStateException`
- `/opt/homebrew/bin/dot` — **12.2.1** — works correctly

The brew wrapper at `/opt/homebrew/bin/plantuml` was patched to use 12.2.1 (`GRAPHVIZ_DOT="/opt/homebrew/bin/dot"`). If it ever gets reset (e.g. after a `brew upgrade plantuml`), re-apply the fix.

## Render Command

```bash
plantuml -tpng <file.puml> -o <output_dir>/
```

To render all diagrams in export-og:
```bash
plantuml -tpng _refs/export-og/*.puml -o _refs/export-og/
```

## If Rendering Fails (wrapper reset)

Check which dot plantuml sees:
```bash
plantuml -testdot
```

If it shows 14.1.5, re-patch the wrapper:
```bash
# Edit /opt/homebrew/bin/plantuml
# Change: GRAPHVIZ_DOT="/opt/homebrew/opt/graphviz/bin/dot"
# To:     GRAPHVIZ_DOT="/opt/homebrew/bin/dot"
```

Or run the jar directly without the wrapper:
```bash
GRAPHVIZ_DOT="/opt/homebrew/bin/dot" java -Djava.awt.headless=true \
  -jar /opt/homebrew/Cellar/plantuml/1.2026.2/libexec/plantuml.jar \
  -tpng <file.puml> -o <output_dir>/
```

## Diagram Layout Notes

- All use case diagrams use `left to right direction` — do not remove it
- Condition labels on `<<extend>>` relationships must be kept (e.g. `(Jei norima...)`)
- Output files land next to the source unless `-o <dir>` is specified

## Steps When Invoked

1. Check `plantuml -testdot` — confirm Graphviz 12.2.1 is active
2. If not, re-patch `/opt/homebrew/bin/plantuml` (see above)
3. Run `plantuml -tpng <target> -o <output_dir>/`
4. Confirm output PNG size is > 50K (32K = error image, not a real render)
5. Report the output file path and size to the user
