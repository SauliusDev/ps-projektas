# codebase-size workflow

Measure this project's source code across auto-discovered zones, estimate token counts, and recommend which Claude model to use for architectural work.

---

## Step 1: Run zone commands

Run each command below from the project root. Capture file count, line count, and character count for each zone.

**your code** — production source files, excluding test directories and external deps:
```bash
# file count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/dist/*" \
  -not -path "*/build/*" \
  -not -path "*/__pycache__/*" \
  -not -path "*/test/*" \
  -not -path "*/tests/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/vendor/*" \
  -not -name "test_*" \
  -not -name "*.test.ts" \
  -not -name "*.test.js" \
  -not -name "*.spec.ts" \
  -not -name "*.spec.js" \
  | wc -l

# line count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/dist/*" \
  -not -path "*/build/*" \
  -not -path "*/__pycache__/*" \
  -not -path "*/test/*" \
  -not -path "*/tests/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/vendor/*" \
  -not -name "test_*" \
  -not -name "*.test.ts" \
  -not -name "*.test.js" \
  -not -name "*.spec.ts" \
  -not -name "*.spec.js" \
  | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'

# character count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/dist/*" \
  -not -path "*/build/*" \
  -not -path "*/__pycache__/*" \
  -not -path "*/test/*" \
  -not -path "*/tests/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/vendor/*" \
  -not -name "test_*" \
  -not -name "*.test.ts" \
  -not -name "*.test.js" \
  -not -name "*.spec.ts" \
  -not -name "*.spec.js" \
  | xargs cat 2>/dev/null | wc -c
```

**your tests** — files in test dirs or with test naming conventions:
```bash
# file count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/__pycache__/*" \
  \( -path "*/test/*" -o -path "*/tests/*" -o -name "test_*" -o -name "*.test.ts" -o -name "*.test.js" -o -name "*.spec.ts" -o -name "*.spec.js" \) \
  | wc -l

# line count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/__pycache__/*" \
  \( -path "*/test/*" -o -path "*/tests/*" -o -name "test_*" -o -name "*.test.ts" -o -name "*.test.js" -o -name "*.spec.ts" -o -name "*.spec.js" \) \
  | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'

# character count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/__pycache__/*" \
  \( -path "*/test/*" -o -path "*/tests/*" -o -name "test_*" -o -name "*.test.ts" -o -name "*.test.js" -o -name "*.spec.ts" -o -name "*.spec.js" \) \
  | xargs cat 2>/dev/null | wc -c
```

**docs** — markdown and rst files (excludes framework/tooling dirs):
```bash
# file count
find . -type f \( -name "*.md" -o -name "*.rst" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  | wc -l

# line count
find . -type f \( -name "*.md" -o -name "*.rst" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  -exec cat {} \; | wc -l

# character count
find . -type f \( -name "*.md" -o -name "*.rst" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  | xargs cat 2>/dev/null | wc -c
```

**config** — yaml, toml, json (skip lockfiles, excludes framework/tooling dirs and venvs):
```bash
# file count
find . -type f \( -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.json" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  -not -name "*.lock" \
  -not -name "pnpm-lock.yaml" \
  -not -name "package-lock.json" \
  -not -name "yarn.lock" \
  | wc -l

# line count
find . -type f \( -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.json" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  -not -name "*.lock" \
  -not -name "pnpm-lock.yaml" \
  -not -name "package-lock.json" \
  -not -name "yarn.lock" \
  | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'

# character count
find . -type f \( -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.json" \) \
  -not -path "*/.git/*" \
  -not -path "*/node_modules/*" \
  -not -path "*/.venv/*" \
  -not -path "*/venv/*" \
  -not -path "*/_blueprint/*" \
  -not -path "*/_bmad/*" \
  -not -path "*/.claude/skills/*" \
  -not -name "*.lock" \
  -not -name "pnpm-lock.yaml" \
  -not -name "package-lock.json" \
  -not -name "yarn.lock" \
  | xargs cat 2>/dev/null | wc -c
```

**external** — known vendor/reference directories:
```bash
# file count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  \( -path "*/node_modules/*" -o -path "*/.venv/*" -o -path "*/venv/*" \
     -o -path "*/vendor/*" -o -path "*/_blueprint/*" -o -path "*/_bmad/*" \) \
  -not -path "*/.git/*" \
  | wc -l

# line count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  \( -path "*/node_modules/*" -o -path "*/.venv/*" -o -path "*/venv/*" \
     -o -path "*/vendor/*" -o -path "*/_blueprint/*" -o -path "*/_bmad/*" \) \
  -not -path "*/.git/*" \
  | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'

# character count
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" \) \
  \( -path "*/node_modules/*" -o -path "*/.venv/*" -o -path "*/venv/*" \
     -o -path "*/vendor/*" -o -path "*/_blueprint/*" -o -path "*/_bmad/*" \) \
  -not -path "*/.git/*" \
  | xargs cat 2>/dev/null | wc -c
```

If any command produces no output or an error, record that zone as: files=0, lines=0, chars=0.

---

## Step 2: Calculate tokens per zone

For each zone, compute:
```
tokens = round(chars / 4 / 1000)   → result in 'k' units
```

Example: 815,032 chars → 815032 / 4 = 203,758 → ~204k tokens

---

## Step 3: Compute core total

```
core_tokens = your_code_tokens + your_tests_tokens   (in raw numbers, not 'k')
core_lines  = your_code_lines + your_tests_lines
core_files  = your_code_files + your_tests_files
```

---

## Step 4: Calculate chunk bar

In agentic workflows you work on focused slices, not the whole codebase at once.
Use a practical single-session working window of 80k tokens (CHUNK).

Constants:
- CHUNK     = 80000 tokens  (comfortable focused session)
- BAR_WIDTH = 20 characters (each █ represents one chunk)

Logic:
```
chunks_core = core_tokens / CHUNK          # float, e.g. 4.45
fill        = min(round(chunks_core), BAR_WIDTH)
empty       = BAR_WIDTH - fill
bar         = "█" * fill + "░" * empty
```

---

## Step 5: Compute agentic chunking estimates

```
import math

CHUNK = 80000

avg_file_tokens = core_tokens / core_files          # raw tokens, not k
avg_file_display = f"~{round(avg_file_tokens / 1000)}k" if avg_file_tokens >= 500 else f"~{round(avg_file_tokens)} tokens"

chunk_core      = math.ceil(core_tokens / CHUNK)
core_docs_raw   = core_tokens + docs_tokens
core_docs_tok   = round(core_docs_raw / 1000)       # for display
chunk_core_docs = math.ceil(core_docs_raw / CHUNK)

def session_label(n):
    if n <= 1:  return "fits in one session"
    else:       return f"~{n} focused sessions"

label_core      = session_label(chunk_core)
label_core_docs = session_label(chunk_core_docs)
```

---

## Step 6: Render the report

Print this exact format, substituting computed values:

```
╔══════════════════════════════════════════════╗
║           CODEBASE SIZE REPORT               ║
╚══════════════════════════════════════════════╝

  Zone              Files    Lines    ~Tokens
  ─────────────────────────────────────────────
  your code         {code_files:>5}  {code_lines:>7,}   ~{code_tok}k
  your tests        {test_files:>5}  {test_lines:>7,}   ~{test_tok}k
  docs              {docs_files:>5}  {docs_lines:>7,}   ~{docs_tok}k
  config            {conf_files:>5}  {conf_lines:>7,}   ~{conf_tok}k
  external          {ext_files:>5}  {ext_lines:>7,}  ~{ext_tok}k   (reference only)
  ─────────────────────────────────────────────
  core total        {core_files:>5}  {core_lines:>7,}  ~{core_tok}k   (code + tests)

──────────────────────────────────────────────
  Core size  ·  each █ ≈ 80k tokens

  {bar}  {core_tok}k total  (~{chunks_core:.1f} chunks)

──────────────────────────────────────────────
  Agentic chunking

  → Avg file          {avg_file_display:<12}  fits in one session
  → Core alone        ~{core_tok}k          {label_core}
  → Core + docs       ~{core_docs_tok}k          {label_core_docs}

  ──────────────────────────────────────────────
  {tip}
```

After printing the report, generate the `{tip}` — a single line of italic markdown advice
(prefix with `*`, suffix with `*`) tailored to the actual numbers. Base it on these signals:

- avg file < 5k tokens → files are small and focused; Sonnet handles any single file or
  small feature slice comfortably in one shot
- chunk_core <= 2 → entire core fits in ~2 sessions; you can load most of it at once for
  architectural work
- chunk_core 3–6 → mid-size project; slice by domain/module per session, use agent
  subagents for parallel exploration
- chunk_core > 6 → large project; always scope sessions to one domain; use Opus only for
  cross-cutting architectural reasoning, Sonnet for everything else
- docs_tok > core_tok → docs are heavier than the code; summarise or load selectively,
  don't dump all docs into context

Keep the tip to one or two sentences. Make it specific to the numbers, not generic.
Example: *Mid-size project — slice by domain per session. Sonnet handles individual
modules comfortably; reserve Opus for cross-cutting refactors that need the full picture.*

Formatting rules:
- `~Xk` means round to nearest whole k (e.g. 52k, 280k)
- Lines use comma thousands separator
- Column widths: keep alignment consistent — right-align numbers
- `{chunks_core:.1f}` — one decimal place, e.g. 4.5
- `{core_docs_tok}k` = round((core_tokens + docs_tokens) / 1000)
- If a zone has 0 files, still show the row with zeros — do not omit it
