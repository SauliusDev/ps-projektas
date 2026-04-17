# Moodle — Course Administrative Materials

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Credits:** 6 ECTS
**Institution:** Kaunas University of Technology (KTU), Faculty of Informatics
**Language:** Lithuanian (original source files)

---

## Folder Contents

| File | Type | Purpose |
|---|---|---|
| `info-about-module.md` | Reference | Module description, objectives, instructors, official description |
| `work-rules.md` | Reference | Grading formula, lab timeline (week-by-week plan), defense rules |
| `README.md` | This file | AI-indexable summary of folder contents |

---

## What's In Here

This folder captures the **official course-administration layer** — grading rules, deadlines, instructor contacts, module objectives — extracted from the Moodle course page. It's the source of truth for *how the module is run* (rules) rather than *what UML means* (lectures) or *how the project is evaluated* (lab instructions).

---

## Key Facts — `info-about-module.md`

**Module objective:**
> Provide knowledge of UML modeling and OOP design methodologies/principles and develop the ability to apply them to software system development — modeling with UML and realizing in software development environments.

**Learning outcomes:**
- Explain software system modeling and OOP principles
- Identify system requirements and describe them in UML
- Design software systems, choosing appropriate architectural decisions and tools
- Apply appropriate technologies and tools for software development

**Mode:** Contact — 75%+ of sessions held in-person on physical campus.

**Instructors:**
- **doc. dr. Lina Čeponienė** (coordinating lecturer, theory + labs) — `lina.ceponiene@ktu.lt` — Studentų g. 50-314 or MS Teams
- **dr. Andrej Ušaniov** (theory + labs) — `andrej.usaniov@ktu.lt` — Studentų g. 50
- **dr. Karolis Ryselis** (coordinating, labs) — `karolis.ryselis@ktu.lt` — Studentų g. 50
- **dr. Mantas Jurgelaitis** (labs) — `mantas.jurgelaitis@ktu.lt` — Studentų g. 50-410 or MS Teams
- **dr. Kęstutis Valinčius** (labs) — `kestutis.valincius@ktu.lt` — Studentų g. 50
- **Kristina Magylaitė** (labs) — `kristina.magylaite@ktu.lt` — Studentų g. 50-308

---

## Key Facts — `work-rules.md`

### Grading Formula

```
Final = P × 0.5 + K × 0.2 + E × 0.3

P = (P1 + P2 + P3) / 3   — project checkpoints
K = written test (kontrolinis, covers theory portion by Čeponienė)
E = exam (covers Sacharovas's portion)
```

**Bonus:** +1 point toward exam grade for presenting completed project in semester week 16 (requirements announced later).

### Teaching Model

- Theory: Čeponienė, Ušaniov, Ryselis
- Classes streamed via MS Teams, recorded in Teams channel
- Example system modeled throughout lectures: **UAB "Kava" coffee-vending IS**
- Supplementary gamified UML course available (password: `UML`)

### Lab Project Requirements

- Teams of ~4 students, self-organized
- Students choose team + topic (must agree with instructors)
- System requirements:
  - Uses a database
  - ≥2 user types
  - ≥3 use cases per team member (1 CRUD = 1 UC)
  - ≥1 external system used
  - Modeling language: UML
  - Implementation language: languages Magic tool can generate (C++, Java) OR any OOP language following MVC or analogous architecture

### Lab Schedule (week-by-week)

| Week | Activity |
|---|---|
| 1 | Team + topic approval, initial system description |
| 2 | Use case diagram — create |
| 3 | Use case diagram — refine |
| 4 | Activity diagrams |
| 5 | Domain class diagram |
| 6 | State diagrams |
| **7** | **P1 — 1st project defense** |
| 8 | Architecture design, sequence diagram for CRUD UC |
| 9 | Initial implementation, sequence diagrams continued, class diagrams |
| 10 | Sequence-vs-activity-vs-code conformance check |
| **11** | **P2 — 2nd project defense** |
| 12 | Component diagram, agreement on UCs to realize |
| 13 | Deployment diagram, system realization, spec conformance |
| 14 | System realization, spec conformance |
| **15** | **P3 — 3rd project defense** |
| 16 | Consultation |

**Re-defense policy:**
- First retake: one week after original defense
- Second retake: during exam session (time announced end of semester)

---

## Cross-References

- Full course context: `docs/project-context.md`
- P1 submission rubric + template: `_refs/1st-lab/README.md`
- P2 submission rubric + template: `_refs/2nd-lab/README.md`
- Lecture transcripts: `_refs/formatted/transcripts/`
- Lecture presentations: `_refs/formatted/presentations/`
- Original VTT recordings: `_refs/moodle-presentation-transcripts/`
- Original PDF slides: `_refs/moodle-presentations/`
