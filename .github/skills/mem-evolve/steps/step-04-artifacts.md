# Step 4: Artifact Type Selection

## Context

`selected_scope` is now set (one or more project names, or a keyword). All paths converge here.

## Output

Do NOT repeat the scope — it was already shown in the previous step. Go straight to the menu:

```
What would you like to extract?

  [1] Skills      — recurring workflows and approaches you repeat
  [2] Rules       — coding standards and decisions you consistently make
  [3] Hooks       — automation patterns (things that always happen after X)
  [4] Agents      — complex multi-step processes worth delegating
  [5] Commands    — shortcuts for tasks you run repeatedly
  [A] All of the above

Enter numbers separated by spaces (e.g. 1 2 3) or A:
```

**HALT — wait for input.**

Store selection as `selected_artifacts`. Then load `./step-05-extract.md`.
