# 1st Lab — P1 Submission Materials

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Submission:** Project Checkpoint 1 (week 7)
**Worth:** 10 points (component of P = (P1+P2+P3)/3, where P counts 50% of final grade)
**Language:** Lithuanian (original source files)

---

## Folder Contents

| File | Type | Purpose |
|---|---|---|
| `Instrukcija1Atsiskaitymui.pdf` | Instructions | Official grading rubric + diagram requirements for P1 defense |
| `1AtaskaitosTurinys.docx` | Template | Blank report template with required section structure |
| `README.md` | This file | AI-indexable summary of folder contents |

---

## What P1 Requires (Must-Have Diagrams)

Mandatory artifacts in the Magic/Teamwork Cloud model file:
1. **At least 1 Use Case diagram** (structured into subsystems by package, with 3+ use cases per team member, ≥2 actors total)
2. **Activity diagram for each use case** (linked to the UC; min 2 swimlanes: user + system)
3. **1 Domain Class diagram** (entity stereotypes, attributes, cardinalities, role names, direction)
4. **At least 1 State diagram** for a key entity class
5. **GUI sketches** for essential use cases (≥3 different screens)
6. **Chosen programming language/technology** statement

---

## Report Structure (from `1AtaskaitosTurinys.docx`)

```
1. Kuriamos sistemos aprašymas            (System being developed — description)
2. Sistemos naudotojo sąsajos eskizai     (GUI sketches)
3. Sistemos reikalavimų specifikacija     (System requirements specification)
   3.1. Panaudojimo atvejų modelis        (Use case model)
   3.2. Dalykinės srities modelis         (Domain model)
   3.3. Pasirinkta programavimo kalba     (Chosen technology)
```

**Per-use-case specification table** must contain:
- PA number, name, responsible student's initials
- Tikslas (Goal)
- Aprašymas (Description)
- Prieš/Po sąlyga (Pre/Post conditions)
- Aktorius (Actor)
- Susiję PA: include/extend/generalization relationships

---

## Grading Rubric (from `Instrukcija1Atsiskaitymui.pdf`)

Total: **10 points**. Pass threshold: ≥5 required to defend.

| Criterion | Points | Failure penalty |
|---|---|---|
| Report uploaded to Moodle + all required diagrams present + proper model structure | 1 | Cannot defend |
| Diagrams clean/readable/no crossing lines | 0.5 | 0 |
| ≥3 UCs per team member, ≥2 actors total | 0.5 | score<5 |
| UCs in subsystems, proper include/extend/generalization | 1 | score<5 |
| Activity diagrams linked to UCs, ≥2 swimlanes | 0.5 | score<5 |
| GUI sketches (≥3 screens) for essential UCs | 0.5 | 0 |
| Logical activity content, include/extend in activity, proper fork/join/decision/merge, objects+states | 2 | 0 |
| Entity stereotypes, names+attributes, cardinalities on relationships | 0.5 | score<5 |
| Relationship ends named, direction + name | 0.5 | 0 |
| Proper generalization/aggregation/composition, enumeration, logical content | 2 | 0 |
| State diagram for specific class, states named, transition triggers, students can explain attribute→state mapping | 1 | 0 |
| Student can answer questions about UML element semantics + demonstrate creation in tool | −1 per unanswered, score<5 if 3 unanswered | — |

---

## Required UML Element Vocabulary (P1)

**Use Case diagram:**
- use case, actor, association, include, extend, extension point, generalization, package
- must link UC → activity diagram (scenario)

**Activity diagram:**
- swimlanes, action node (call behavior, send signal, accept event, time event), structured activity, conditional node, loop node, object node, pin, node/pin state, decision, merge, fork, join
- traceability: objects ↔ classes, object states ↔ state diagram states, swimlane participants ↔ actors; include/extend in UC → call behavior action in activity

**Class diagram:**
- Class, object, attribute, operation, association, aggregation, composition, generalization, dependency
- relationship end names, cardinality, direction
- attribute/operation specifications
- navigability

**State diagram:**
- simple state, submachine state, composite state, orthogonal state, terminate, entry point, exit point, junction, choice, fork, join, history, deep history
- state specification, transition specification

---

## Recommended Model Package Structure (carries over to P2/P3)

```
1. Reikalavimų modelis (Requirements model)
   1.1. Panaudojimo atvejų modelis (Use case model — UC diagram, actors, subsystem packages, UCs with activity diagrams)
   1.2. Esybių modelis (Entity model — domain class diagram, entities, state diagrams)

2. Projekto modelis (Design model — introduced in P2)
   2.1. Naudotojo sąsajos modelis (boundary classes)
   2.2. Veiklos logikos modelis (control + sequence diagrams)
   2.3. Duomenų modelis (entity classes)

3. Realizacijos modelis (Implementation model — P3)
   3.1. Komponentų modelis
   3.2. Diegimo modelis
```

**Key rule:** elements carry over between phases — do NOT recreate, TRANSFORM them (entity classes from requirements → design → implementation).

---

## Defense Format

- Report uploaded to Moodle (shared by whole team, no printing needed)
- Individual defense — each student opens the model file, answers questions about models, UML elements, tool usage

---

## Cross-References

- Full course context: `docs/project-context.md`
- Module rules: `_refs/moodle/README.md`
- Lecture coverage for P1 topics: lectures 1–5 (UML intro, UC, activity, class, state)
- P2 submission materials: `_refs/2nd-lab/README.md`
