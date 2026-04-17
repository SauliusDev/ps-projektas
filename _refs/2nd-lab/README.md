# 2nd Lab — P2 Submission Materials

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Submission:** Project Checkpoint 2 (week 11)
**Worth:** 10 points (component of P = (P1+P2+P3)/3, where P counts 50% of final grade)
**Language:** Lithuanian (original source files)

---

## Folder Contents

| File | Type | Purpose |
|---|---|---|
| `Instrukcija2Atsiskaitymui.pdf` | Instructions | Official grading rubric + diagram requirements for P2 defense |
| `2AtaskaitosTurinys.docx` | Template | Blank report template with required section structure (extends P1) |
| `README.md` | This file | AI-indexable summary of folder contents |

---

## What P2 Requires (Must-Have New Artifacts)

Mandatory artifacts added to the model file for P2:
1. **1 Logical architecture package diagram** (shows all system packages, classes listed inside without attributes/ops)
2. **Sequence diagram per use case** (design-phase; messages map to class operations)
3. **System class diagram(s)** — all classes tagged with boundary/control/entity stereotype
4. **Working system prototype** implementing CRUD use cases agreed with instructor

Carries forward from P1: use case diagrams, activity diagrams, domain class diagram, state diagram, GUI sketches.

---

## Report Structure (from `2AtaskaitosTurinys.docx`)

```
1. Kuriamos sistemos aprašymas                  (from P1)
2. Sistemos naudotojo sąsajos eskizai           (from P1)
3. Sistemos reikalavimų specifikacija           (from P1, carried over)
   3.1. Panaudojimo atvejų modelis
   3.2. Dalykinės srities modelis
   3.3. Pasirinkta programavimo kalba, technologija
4. Sistemos projekto modelis                    (NEW in P2)
   4.1. Sistemos loginė architektūra            (Logical architecture — package diagram)
   4.2. Panaudojimo atvejų sekų diagramos       (Sequence diagrams per UC)
   4.3. Sistemos klasių diagrama                (System class diagram with boundary/control/entity)
   4.4. Sistemos prototipas                     (GUI screens of realized prototype)
```

---

## Grading Rubric (from `Instrukcija2Atsiskaitymui.pdf`)

Total: **10 points**. Pass threshold: ≥5 required to defend.

| Criterion | Points | Failure penalty |
|---|---|---|
| Report uploaded + all required diagrams (logical architecture, sequences per UC, system class with boundary/control/entity) + proper structure | 1 | Cannot defend |
| Working prototype for CRUD UCs agreed with instructor (cannot be chosen unilaterally) | 1 | Cannot defend |
| Diagrams clean/readable/minimal crossings | 0.5 | 0 |
| Requirements-model elements (entities, UCs, actors) TRANSFORMED into design model | 0.5 | 0 |
| Student explains chosen logical architecture; diagram logical, all classes/packages included | 0.5 | 0 |
| Sequence messages ↔ class operations in class diagram; CRUD sequences match activity diagrams and code | 2 | score<5 |
| Obvious correspondence between activity diagrams and sequence diagrams; include/extend from UC activities mapped to sequence ref/alt/opt | 2 | 0 |
| MVC principles not violated; sync/async used correctly; reply messages present where possible, named meaningfully, used correctly | 2 | 0 |
| System class diagram operations are ONLY those used in sequences; class relationships match sequence interactions | 0.5 | 0 |
| Student answers questions about UML elements + demonstrates creation in tool | −1 per unanswered, score<5 if 3 unanswered | — |

**Critical:** CRUD use cases to implement in the prototype MUST be agreed with the instructor IN ADVANCE during lab sessions.

---

## Required UML Element Vocabulary (P2)

**Sequence diagram:**
- lifeline, message (synchronous, asynchronous, reply, create, destroy, message to self, recursive)
- interaction use (ref), combined fragments: alt, opt, loop (fully described)
- reply messages MUST have names
- Robustness analysis stereotypes and rules:
  - actor → cannot call entity or control; only boundary
  - boundary → cannot call another boundary
  - (full BCE rule set applies)
- traceability: messages ↔ specific class operations; sequences match requirements-phase activity diagrams; include/extend from UC → ref/alt/opt fragments

**Class diagram (design):**
- stereotypes (boundary/control/entity), interfaces (provided, required)
- traceability: every operation in class diagram is used in at least one sequence; if sequence shows class A calling class B, class diagram must have relationship between A and B

**Package diagram:**
- Package, dependency

---

## Sequence Diagram Requirements Detail

- Messages in sequence must match class-diagram operations of the specific class
- Reply messages must be named
- Reply messages shown for all operation calls when possible (exceptions: window navigation)
- If UC has include/extend → sequence must use ref, alt/opt fragments at corresponding points
- MVC principles must hold throughout

---

## Prototype Implementation Notes

- Only CRUD-type use cases pre-agreed with instructor
- Alignment checked: specification ↔ implementation
- GUI screens from prototype must be demonstrable — students must explain correspondence to GUI sketches from report section 2

---

## Defense Format

- Report uploaded to moodle.ktu.edu before defense (team-shared, no printing needed)
- Individual defense — each student opens the model file
- Questions can cover: models, UML elements, tool usage, AND the realized implementation

---

## Cross-References

- Full course context: `docs/project-context.md`
- Module rules: `_refs/moodle/README.md`
- Lecture coverage for P2 topics: lectures 6 (package, BCE) and 7 (sequence)
- P1 submission materials: `_refs/1st-lab/README.md`
- Recommended package structure inherited from `_refs/1st-lab/README.md`
