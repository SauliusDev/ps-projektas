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

### The full pipeline

```
MagicDraw model (current — incomplete/incorrect)
        ↓  exported as HTML 2.0 + XML
Raw export files in _refs/export-source/magic-export/
        ↓  parsed to LLM-readable PUML
PUML files in _refs/export-og/  ← LLM source of truth for current model
        ↓  LLM reads PUML + lecture transcripts + lab context
Corrected design in _refs/export-fixed/
        ↓  build the app from corrected PUML
Working app
        ↓  team redraws all diagrams in MagicDraw from corrected PUML
Final MagicDraw model (lecturer grades this)
```

**Key principle:** PUML files are how the LLM understands and reasons about the model. MagicDraw is only for final submission. The team never hand-writes PUML — they redraw the corrected PUML back into MagicDraw.

**Sequence and package diagrams are deferred.** They depend on the final app architecture and cannot be created until the tech stack and component boundaries are decided.

### Step 1 — Build Context Library ✅ DONE
All raw course materials converted to clean LLM-injectable markdown:
- `_refs/formatted/transcripts/lecture-01.md` … `lecture-07.md` — VTT transcripts stripped, translated Lithuanian → English, structured by topic
- `_refs/formatted/presentations/lecture-00.md` … `lecture-07.md` — PDF slides extracted slide-by-slide, translated, all diagrams described
- Lab instructions still to be processed (`_refs/1st-lab/`, `_refs/2nd-lab/`)

### Step 2 — Export & Parse Magic UML → PUML ✅ DONE
- Exported Magic model as HTML 2.0 + XML (`_refs/export-source/magic-export/`)
- Parsed export → PUML files in `_refs/export-og/` (exact representation of current Magic model)
- HTML 2.0 export also contains 45 pre-rendered JPG images (MagicDraw's own renders) — see `_refs/export-images-audit.md` for full inventory
- **Note:** HTML 2.0 export does NOT include sequence or package diagrams — those types were not exported

### Step 3 — Fix & Improve Diagrams (in progress)
- Read `_refs/export-og/` PUML files as the current model baseline
- LLM corrects logic errors, missing elements, broken relationships using lecture + lab context
- Write corrected versions to `_refs/export-fixed/`
- Track what changed so the team knows what to redraw in MagicDraw

### Step 4 — Implementation
- Map finalized diagrams to actual code (React + backend TBD)
- Implementation follows diagrams exactly — BCE layers, controller responsibilities, entity relationships
- Sequence diagrams authored at this stage (they describe the implementation flow)

### Step 5 — Team Delegation
- Share corrected PUML files from `_refs/export-fixed/` with team as redraw reference
- Team recreates them in MagicDraw for submission
- Team builds UI/design layer

---

## Diagram Rendering Notes

PlantUML renders at different quality levels depending on diagram type:

| Diagram type | PUML render quality | Team reference approach |
|---|---|---|
| Activity diagrams | ✅ Good — use as-is | PUML render |
| State machine | ✅ Good | PUML render |
| Class diagram | ⚠️ Messy at scale | Generate Mermaid alongside PUML for human-readable view |
| Use case diagram | ❌ Poor at 40+ nodes | Use pre-rendered MagicDraw JPG from HTML export as visual reference |
| Sequence diagrams | TBD — not yet authored | Will be PUML |
| Package diagram | TBD — not yet authored | Will be PUML |

Pre-rendered MagicDraw JPGs are in `_refs/export-source/magic-export/folder html 2.0/html 2.0_files/` — filename-to-diagram mapping is in `_refs/export-images-audit.md`.

---

## File Structure (Current State)

```
ps-projektas/
├── docs/
│   └── project-context.md          ← this file — read first
├── _refs/
│   ├── formatted/                  ← ✅ DONE — LLM-ready course material
│   │   ├── transcripts/
│   │   │   ├── lecture-01.md       ← Course intro, UML overview, MagicDraw, grading
│   │   │   ├── lecture-02.md       ← Use case diagrams, actors, «include»/«extend»
│   │   │   ├── lecture-03.md       ← Activity diagrams, nodes, swimlanes
│   │   │   ├── lecture-04.md       ← Class diagrams, relationships, cardinality
│   │   │   ├── lecture-05.md       ← State diagrams, composite/orthogonal, history
│   │   │   ├── lecture-06.md       ← Package diagrams, BCE/MVC architecture
│   │   │   └── lecture-07.md       ← Sequence diagrams, lifelines, combined fragments
│   │   └── presentations/
│   │       ├── lecture-00.md       ← Course orientation, grading, tool setup
│   │       ├── lecture-01.md       ← UML intro, taxonomy, Paysera example
│   │       ├── lecture-02.md       ← Use case diagrams (32 slides)
│   │       ├── lecture-03.md       ← Activity diagrams (20 slides)
│   │       ├── lecture-04.md       ← Class diagrams (30 slides)
│   │       ├── lecture-05.md       ← State machine diagrams (20 slides)
│   │       ├── lecture-06.md       ← Package diagrams, BCE stereotypes (17 slides)
│   │       └── lecture-07.md       ← Sequence diagrams (20 slides)
│   ├── export-source/              ← raw original Magic exports (do not edit)
│   │   ├── magic-export/           ← original XMI file from MagicDraw
│   │   └── magic-uml/              ← ✅ parsed Mermaid (exact representation of Magic model)
│   │       ├── model-summary.md    ← full index of all 200+ named elements
│   │       ├── use-case/use-case.mmd
│   │       ├── class/class.mmd
│   │       ├── package/package.mmd
│   │       ├── state-machine.mmd
│   │       ├── sequence/           ← 8 sequence diagrams
│   │       └── activity/           ← 43 individual activity diagrams
│   ├── export-og/                  ← older puml outputs (pre-dates XMI parse, mostly superseded)
│   │   ├── activities/
│   │   ├── class_diagram.puml
│   │   └── use_case.puml
│   ├── export-fixed/               ← EMPTY — target for fixed/improved Mermaid diagrams
│   ├── diagrams-og/                ← current PlantUML mirror used in this repo
│   │   ├── activities/             ← phase 1 activity diagrams
│   │   ├── package/architecture.puml
│   │   ├── sequence/               ← phase 2 sequence diagrams from project module export
│   │   ├── class_diagram.puml
│   │   └── use_case.puml
│   ├── moodle/                     ← course rules, grading info, module description
│   ├── moodle-presentation-transcripts/  ← original VTT files (Lithuanian)
│   ├── moodle-presentations/       ← original PDF lecture slides
│   ├── 1st-lab/                    ← lab 1 report template + instructions (not yet processed)
│   ├── 2nd-lab/                    ← lab 2 report template + instructions (not yet processed)
│   └── my-input/info.md            ← owner's project description
├── _notes/
│   ├── todo.md
│   └── personal-insights.md
└── _archive/
    └── uml/                        ← prior sequence diagram work (Mermaid + PlantUML)
```

---

## What's In the Magic Model (from XMI parse)

### Actors (12 total)
- **Keliautojas** (Traveler) — inherits from Naudotojas
- **Naudotojas** (User) — base authenticated user
- **Admin** (Administrator) — inherits from Naudotojas
- **Svečias** (Guest) — unauthenticated
- **Google Maps** — external system
- **El. pašto serveris** (Email server) — external system
- + project-model equivalents of the above

### Use Cases (43 total across 3 subsystems)
Organized into Admin, User (Naudotojas/Keliautojas), and Guest subsystems. Full list in `_refs/export-source/magic-uml/model-summary.md`.

### Classes (51 total)
17 domain entity classes + frontend controllers/views + project model classes. Full class diagram with typed attributes, operations, and 74 associations in `_refs/export-source/magic-uml/class/class.mmd`.

### Activities (48)
43 named activity diagrams (one per use case approximately). Individual files in `_refs/export-source/magic-uml/activity/`.

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

## Work Done Session 2026-04-16

- Created this `docs/project-context.md` file
- Processed all 7 VTT lecture transcripts → `_refs/formatted/transcripts/` (Lithuanian → English, timestamped stripped, topic-structured)
- Processed all 8 PDF presentations → `_refs/formatted/presentations/` (slide-by-slide, fully translated)
- Parsed full Magic UML XMI export (6MB, 75,964 lines) → 58 Mermaid files in `_refs/export-source/magic-uml/`
- Deleted `parse_html_export.py`, `parse_xmi.py`, `__pycache__` from `export-og/`
- Folder structure clarified: `export-source/` (raw + parsed originals), `export-og/` (old puml), `export-fixed/` (target for fixed diagrams)

## Immediate Next Steps

1. Process lab instructions (`_refs/1st-lab/`, `_refs/2nd-lab/`) → formatted md
2. Review PUML diagrams in `_refs/export-og/` for correctness against lecture requirements
3. Fix diagrams → write corrected versions to `_refs/export-fixed/`
4. For use case + class diagrams: generate human-readable Mermaid alongside the corrected PUML
5. Decide on tech stack for implementation (React confirmed for frontend, backend TBD)
6. Author sequence and package diagrams once architecture is settled
