# P2 Traceability Checklist

Source plan: `docs/superpowers/specs/2026-04-17-travel-system-architecture-design.md`

- [x] Architecture and sequence modeling source of truth is locked to `_refs/diagrams-new/` only.
- [x] Keep the auto-generated `«edition»` traceability package after model transformation.
- [x] Requirements elements are transformed (not recreated) into design model artifacts.
- [x] Every sequence diagram follows BCE flow: actor -> boundary -> control -> entity/infrastructure.
- [x] Every sequence message maps to an existing class operation.
- [x] Every sender/receiver pair in sequences has a corresponding class relationship.
- [x] Use case `<<include>>` / `<<extend>>` relations are represented in sequences with `ref` / `opt` / `alt` fragments.
- [x] Combined fragments include covered lifelines.
- [x] Reply messages are present for synchronous calls (except allowed UI navigation case).
- [x] `alt` fragments include an `[else]` branch.
- [x] Controllers are split by feature responsibility and kept consistent across package, sequence, and class diagrams.

## Current check results

- `rg -c 'usecase\s+"' _refs/diagrams-new/use_case.puml` -> `41`
- `ls _refs/diagrams-new/sequence/*.puml | wc -l` -> `41`
- `rg 'ref|alt|opt' _refs/diagrams-new/sequence/*.puml | wc -l` -> `84`

