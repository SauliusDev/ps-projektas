---
name: render-puml
description: "Render one or more .puml files to PNG. Uses the local Graphviz path available on this machine. Invoke via /render-puml."
---

# Render PlantUML Diagrams

## Background

This skill is for rendering existing PlantUML files. It does not generate `.puml` from MagicDraw exports.

The usable Graphviz path on this machine is:
- `/opt/homebrew/opt/graphviz/bin/dot`

The brew wrapper at `/opt/homebrew/bin/plantuml` may point to a missing path. If that happens, either patch the wrapper or run the jar directly with `GRAPHVIZ_DOT` set explicitly.

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

If it reports a missing dot path, re-patch the wrapper:
```bash
# Edit /opt/homebrew/bin/plantuml
# Set: GRAPHVIZ_DOT="/opt/homebrew/opt/graphviz/bin/dot"
```

Or run the jar directly without the wrapper:
```bash
GRAPHVIZ_DOT="/opt/homebrew/opt/graphviz/bin/dot" java -Djava.awt.headless=true \
  -jar /opt/homebrew/Cellar/plantuml/1.2026.2/libexec/plantuml.jar \
  -tpng <file.puml> -o <output_dir>/
```

## Diagram Layout Notes

- All use case diagrams use `left to right direction` — do not remove it
- Condition labels on `<<extend>>` relationships must be kept (e.g. `(Jei norima...)`)
- Output files land next to the source unless `-o <dir>` is specified

## Steps When Invoked

1. Check `plantuml -testdot` — confirm a valid Graphviz path is active
2. If not, re-patch `/opt/homebrew/bin/plantuml` (see above)
3. Run `plantuml -tpng <target> -o <output_dir>/`
4. Confirm output PNG size is > 50K (32K = error image, not a real render)
5. Report the output file path and size to the user
