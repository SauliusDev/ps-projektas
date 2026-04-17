# Project Context — PS-Projektas

## What This Is

Academic project for the course **"Programų sistemų analizės ir projektavimo įrankiai"** (Software Systems Analysis and Design Tools), module code T120B029, 6 credits, at KTU.

The course teaches UML modeling and object-oriented design methodology. The project is team-based (~4 members) and requires designing and building a working software prototype.

**Owner:** Azuolas Balbieris  
**Goal:** Highest possible grade — dominate the class.

---

## The System Being Built

A **travel planning system** with the following characteristics:
- At least 2 user types (traveler, admin, guest — confirmed in Magic model)
- At least 3 complex use cases per team member (4 difficult core functions minimum)
- Requires a database
- Must use at least 1 external system (Google Maps API and Email server already modeled)
- Architecture: MVC/BCE with OOP principles
- Tech stack: React (or similar frontend) + backend TBD

The 4 core complex use cases revolve around **trip/journey creation**, including route generation, scoring algorithms, time validation, and food plan generation.

---

## Grading Formula

```
Final = P×0.5 + K×0.2 + E×0.3

P = (P1 + P2 + P3) / 3  — three project submissions
K = control test
E = exam
```

**Project submissions schedule:**
| Submission | Week | What's due |
|---|---|---|
| P1 | Week 7 | Use case, activity, state, class diagrams |
| P2 | Week 11 | Sequence diagrams, initial implementation, component diagram |
| P3 | Week 15 | Full system, deployment diagram, spec compliance check |

---

## UML Diagram Pipeline

Diagrams are built in **two phases with different language requirements:**

### Phase 1 — Conceptual (Lithuanian)
- Use case diagrams
- Activity diagrams (one per use case)
- State diagrams
- Class diagrams (domain model)

### Phase 2 — Implementation (English)
- Package diagrams
- Sequence diagrams (one per use case)
- Component diagrams
- Deployment diagram

**Tooling:** Magic Systems (MagicDraw 2024x) is the primary modeling tool for submission. **PlantUML (`.puml`)** is the LLM-readable working format — the PUML files represent the current MagicDraw model and are what the LLM reads, corrects, and reasons about. Final corrected diagrams get recreated in MagicDraw by the team for grading.

**BCE architecture** is applied throughout: Boundary (Views/UI), Control (Controllers), Entity (Models).

---

## Master Strategy

### Current practical pipeline (after refs cleanup)

```
Current baseline diagrams: _refs/diagrams-og/
        ↓  review against lectures + lab rubrics
Context sources: _refs/context/ + _refs/1st-lab/ + _refs/2nd-lab/
        ↓  apply fixes/updates
Updated diagrams: _refs/diagrams-new/
        ↓  redraw in MagicDraw for defense submissions
Final graded model
```

**Key principle:** keep active working material in `_refs/`; keep historical exports and experiments in `_archive/`.

### What is active now
- `_refs/diagrams-og/` — baseline PlantUML set used as "current model" in this repo.
- `_refs/diagrams-new/` — updated/fixed PlantUML set (currently focused on phase 1 diagrams).
- `_refs/context/` — AI-ready lecture material and module/admin references.
- `_refs/1st-lab/`, `_refs/2nd-lab/` — grading rubrics + report templates.

### What was moved to archive
- Legacy exports/parsers and large historical bundles moved under `_archive/export-source/`.
- Older lecture/misc/wireframe folders moved under `_archive/`.
- `_archive/` is retained for traceability; it is not the primary day-to-day source.

---

## Diagram Rendering Notes

PlantUML renders at different quality levels depending on diagram type:

| Diagram type | PUML render quality | Team reference approach |
|---|---|---|
| Activity diagrams | ✅ Good — use as-is | PUML render |
| State machine | ✅ Good | PUML render |
| Class diagram | ⚠️ Messy at scale | Generate Mermaid alongside PUML for human-readable view |
| Use case diagram | ❌ Poor at 40+ nodes | Use pre-rendered MagicDraw JPG from HTML export as visual reference |
| Sequence diagrams | ✅ Available in baseline | `_refs/diagrams-og/sequence/` |
| Package diagram | ✅ Available in baseline | `_refs/diagrams-og/package/architecture.puml` |

Pre-rendered MagicDraw JPG audit is tracked in `_refs/export-images-audit.md`. The original HTML export sources were moved to `_archive/export-source/magic-export/`.

---

## File Structure (Current State)

```
ps-projektas/
├── docs/
│   └── project-context.md          ← this file — read first
├── _refs/
│   ├── 1st-lab/                    ← P1 rubric, template, README summary
│   ├── 2nd-lab/                    ← P2 rubric, template, README summary
│   ├── context/
│   │   ├── info/                   ← module description + work rules
│   │   ├── presentations-llm/      ← lecture-00..07 markdown
│   │   └── transcripts-lmm/        ← lecture-01..07 markdown
│   ├── diagrams-og/                ← baseline PlantUML set (active source)
│   │   ├── activities/
│   │   │   ├── svecio_posisteme/png/
│   │   │   ├── naudotojo_posisteme/png/
│   │   │   └── administratoriaus_posisteme/png/
│   │   ├── package/architecture.puml
│   │   ├── sequence/               ← 8 sequence .puml + png renders
│   │   ├── class_diagram.puml
│   │   └── use_case.puml
│   ├── diagrams-new/               ← updated/fixed PlantUML set in progress
│   │   ├── activities/
│   │   │   ├── svecio_posisteme/png/
│   │   │   ├── naudotojo_posisteme/png/
│   │   │   └── administratoriaus_posisteme/png/
│   │   ├── class_diagram.puml
│   │   └── use_case.puml
│   └── export-images-audit.md      ← mapping for MagicDraw-exported JPG diagrams
├── _notes/
│   ├── todo.md
│   └── personal-insights.md
└── _archive/
    ├── export-source/              ← historical exports, parsers, and generated artifacts
    ├── lectures/ misc/ quick-04-14-lec/
    ├── uml/                        ← prior sequence diagram work
    └── use case/ wireframes/       ← older design material
```

---

## What's In the Magic Model (from archived XMI parse snapshot)

### Actors (12 total)
- **Keliautojas** (Traveler) — inherits from Naudotojas
- **Naudotojas** (User) — base authenticated user
- **Admin** (Administrator) — inherits from Naudotojas
- **Svečias** (Guest) — unauthenticated
- **Google Maps** — external system
- **El. pašto serveris** (Email server) — external system
- + project-model equivalents of the above

### Use Cases (43 total across 3 subsystems)
Organized into Admin, User (Naudotojas/Keliautojas), and Guest subsystems. Full list in `_archive/export-source/magic-uml/model-summary.md`.

### Classes (51 total)
17 domain entity classes + frontend controllers/views + project model classes. Full class diagram with typed attributes, operations, and 74 associations in `_archive/export-source/magic-uml/class/class.mmd`.

### Activities (48)
43 named activity diagrams (one per use case approximately). Individual files in `_archive/export-source/magic-uml/activity/`.

### Sequence Diagrams (8)
Including: Peržiūrėti pasiūlymus (Browse Deals) with 7 lifelines (Guest → Deals/MainView/DealController/Deal/SavedDealsController/UserController).

### State Machine (1)
Kelionė (Trip) lifecycle: `[*] → Ateinanti → Aktyvi → Praejusi → Archivuota`

---

## Key Constraints & Decisions

- Diagrams for P1 submission are in **Lithuanian** (use case, activity, state, class)
- Diagrams for P2/P3 and all code modeling are in **English** (package, sequence, component, deployment)
- Architecture follows **BCE (Boundary-Control-Entity)** pattern
- UI components use **"View" suffix** (not "Window") for boundary class naming
- **RouteController** handles all routing domain logic; **TripListController** orchestrates the overall journey creation workflow — separated concerns
- The example system taught in lectures is "UAB Kava" coffee vending machine IS — useful for understanding diagram conventions
- Lectures use **Enterprise Architect** in demos but the project uses **MagicDraw/Cameo 2024x**

---

## Lectures Quick Reference

| # | Transcript | Presentation | Topic |
|---|---|---|---|
| 0 | — | lecture-00.md | Course orientation, grading, tool setup |
| 1 | lecture-01.md | lecture-01.md | UML overview, MagicDraw, abstraction/decomposition/projection |
| 2 | lecture-02.md | lecture-02.md | Use case diagrams — actors, all 4 relationships, «include»/«extend» |
| 3 | lecture-03.md | lecture-03.md | Activity diagrams — nodes, guards, swimlanes, fork/join |
| 4 | lecture-04.md | lecture-04.md | Class diagrams — all relationship types, attributes, operations |
| 5 | lecture-05.md | lecture-05.md | State machine diagrams — composite, orthogonal, history states |
| 6 | lecture-06.md | lecture-06.md | Package diagrams, BCE stereotypes, design model transition |
| 7 | lecture-07.md | lecture-07.md | Sequence diagrams — lifelines, messages, combined fragments (alt/opt/loop) |

---

## Prior Work Done (before this session)

- Sequence diagram for "Create Journey" use case in Mermaid + PlantUML (`_archive/uml/`)
- BCE architecture color coding: green = boundary/views, red = controllers, yellow = entities
- All UI boundary classes renamed from "Window" → "View" suffix
- RouteController integrated into Create Journey sequence diagram
- Three-tier architecture boxes with UML stereotype notation applied

## Work Done Session 2026-04-17

- Locked architecture decisions to `_refs/diagrams-new/` as the only source for P2 package/sequence modeling.
- Added the P2 logical architecture package diagram to the design set.
- Generated and aligned sequence diagrams per use case against the use case model.
- Added BCE system class diagram updates aligned with sequence interactions.
- Audited MagicDraw HTML 2.0 export — found 45 pre-rendered JPG diagrams (1 use case, 1 class, 1 state, 42 activity); no sequence or package diagrams in export
- Created `_refs/export-images-audit.md` — full inventory table with filename↔diagram name mapping
- Clarified overall project strategy and pipeline (see Master Strategy above)
- Updated this project-context.md with current state and rendering quality notes
- Regenerated all 8 sequence diagrams in `_refs/diagrams-og/sequence/` using the lecture-style PlantUML format (BCE lifeline stereotypes, consistent skinparams, section blocks, and combined fragments)
- Consolidated active references under `_refs/` and moved large historical material to `_archive/`.
- Implementation status clarified: current branch is scaffold-level (mainly read/list and in-memory flows); PostgreSQL-backed CRUD remains planned for the next execution cycle.

## Work Done Session 2026-04-16

- Created this `docs/project-context.md` file
- Processed all 7 VTT lecture transcripts → `_refs/context/transcripts-lmm/` (Lithuanian → English, timestamped stripped, topic-structured).
- Processed all 8 PDF presentations → `_refs/context/presentations-llm/` (slide-by-slide, fully translated).
- Parsed full Magic UML XMI export and generated intermediate artifacts (now preserved in `_archive/export-source/`).
- Historical parser outputs and legacy export folders moved from active refs into `_archive/`.

## Immediate Next Steps

1. Continue reviewing `_refs/diagrams-og/` against lecture + lab rubric rules.
2. Keep applying fixes in `_refs/diagrams-new/` (activity/use-case/class first, then package/sequence as needed).
3. Normalize naming/consistency between `diagrams-og` and `diagrams-new`.
4. Finalize tech stack details for implementation mapping (frontend confirmed, backend still open).
5. Prepare redraw-ready package for MagicDraw submission from the stabilized PlantUML set.
