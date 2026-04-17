# Lecture 05 — State Machine Diagram (Būsenų diagrama)

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Institution:** Kaunas University of Technology (KTU)

**Topics covered:**
- Recap of the IS development process and where the State Machine Diagram fits
- UML 2.5 diagram taxonomy (overview, highlighting diagrams covered so far)
- Introduction to State Machine Diagrams (Behavioral State Machine)
- State machine and automaton concepts
- States: simple, composite, submachine
- Transitions: triggers, guards, behavior expressions
- Transition trigger event types: CallEvent, ChangeEvent, TimeEvent, SignalEvent, AnyReceiveEvent
- Pseudo-states: initial, final, terminate, history (shallow/deep), choice, junction, entry point, exit point, fork, join
- Example: State machine for class `ConferencePaper` (KonferencijosStraipsnis)
- Example: State machine for class `Person` (Asmuo) — composite state
- Composite parallel state (orthogonal regions)
- Submachine state
- Example: Bank ATM state machine
- Exercise: Build a state machine for class `Door` (Durys)
- Example: Washing machine state diagram
- History state (shallow history) in washing machine
- Deep history state and state configuration concept
- Deep history state in washing machine
- Example exercise: state reachability from state S11 under event sequences

---

## Slide 1 — IS Development Process (Used PI Development Process)

**Title (left):** Naudojamas PI kūrimo procesas
**Translation:** Used IS (Information System) Development Process

> [Diagram: UML Activity Diagram showing the IS development process as a sequential flow with decision points. The currently highlighted phase (circled in blue) is "Requirements Specification" (Reikalavimų specifikavimas).]

**Phases and their artifacts:**

1. **Initial Requirements Description** (Pradinis reikalavimų aprašymas)
   - : Interface Prototype (Sąsajos prototipas)
   - : Initial System Description (Pradinis sistemos aprašas)

2. **Requirements Specification** (Reikalavimų specifikavimas) ← *currently highlighted*
   - Functional requirements: Use Case Diagram (Panaudojimo atvejų diagrama)
   - Scenario for each use case: Activity Diagram (Veiklos diagrama)
   - Domain entities: Class Diagram (Klasių diagrama)
   - Entity states: State Machine Diagram (Būsenų diagrama)

3. **Design** (Projektavimas)
   - Logical architecture: Package Diagram (Paketų diagrama)
   - Scenario for each use case: Sequence Diagram (Sekų diagrama)
   - Project classes: Class Diagram (Klasių diagrama)

4. **Implementation** (Realizavimas)
   - : Component Diagram (Komponentų diagrama)
   - : Deployment Diagram (Diegimo diagrama)
   - : Program Code (Programos kodas)

5. **Testing** (Testavimas)
   - : Test Plan (Testavimo planas)
   - : Test Report (Testavimo ataskaita)

---

## Slide 2 — UML 2.5 Diagrams

**Title:** UML 2.5 diagramos
**Translation:** UML 2.5 Diagrams

> [Diagram: UML 2.5 diagram taxonomy tree. Root node: "Diagram", split into two branches: "Structure Diagram" and "Behavior Diagram".]

**Structure Diagram** subtypes:
- Class Diagram ✓ *(covered)*
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram
- Profile Diagram

**Behavior Diagram** subtypes:
- Activity Diagram ✓ *(covered)*
- Use Case Diagram ✓ *(covered)*
- **State Machine Diagram** ← *highlighted with green box (this lecture's topic)*
- Interaction Diagram (subtypes):
  - Sequence Diagram
  - Communication Diagram
  - Interaction Overview Diagram
  - Timing Diagram

---

## Slide 3 — Section Title Slide: State Machine Diagram

**Title (large):** Būsenų diagrama

**Subtitle:** STATE MACHINE DIAGRAM

---

## Slide 4 — State Machine

**Title:** Būsenų mašina
**Translation:** State Machine

A state machine (or automaton) is a formal behavioral model consisting of states, transitions, and actions.

A state machine formally describes all possible behavior of a **class** or another model element (use case, interface, protocol, ...).

UML state machines are divided into **behavioral (behavioral)** and protocol state machines.

---

## Slide 5 — State Machine (continued)

**Title:** Būsenų mašina
**Translation:** State Machine

A state is a situation in an object's lifetime when it:
- satisfies a certain condition / waits for a certain event / performs a certain action

The states of passive objects (entities) can be defined by the set of values of their attributes.

A state can be:
- simple (simple state)
- composite (composite state)
- submachine (submachine state)

> [Diagram: Three state notation examples:
> 1. Simple state — rounded rectangle labeled "Paprasta būsena" (Simple state)
> 2. Composite state — rounded rectangle labeled "Sudėtinė būsena" (Composite state) containing two nested rounded rectangles connected by an arrow
> 3. Submachine state — rounded rectangle labeled ": Kita būsenų diagrama" (: Another state machine diagram) with a submachine icon (double circle/fork symbol) in the bottom-right corner]

---

## Slide 6 — States and Transitions

**Title:** Būsenos ir perėjimai
**Translation:** States and Transitions

A state **must** have a name and **may** have actions:
- entry, exit, do
- non-standard (custom)

> [Diagram: Example state box for "TypingPassword" showing:
> - entry / setEchoInvisible()
> - exit / setEchoNormal()
> - character / handleCharacter()
> - help / displayHelp()]

A transition (transition) **may** have:
- an event that triggers the transition (trigger)
- a condition (guard) that must hold for the transition to occur
- an action (behavior expression)

> [Diagram: Transition notation — arrow from "Būsena1" (State1) to "Būsena2" (State2), labeled:
> `įvykis (event) [sąlyga (guard)] / veiksmas`
> i.e., `event [guard] / action`]

---

## Slide 7 — Transition Trigger Event Types

**Title:** Perėjimo trigerio įvykių tipai
**Translation:** Transition Trigger Event Types

- **AnyReceiveEvent**
- **CallEvent**
  - operation invocation (operacijos iškvietimas)
- **ChangeEvent**
  - change of object properties (objekto savybių pasikeitimas), e.g.: `when (balance=0)`
- **TimeEvent**
  - a specific time (konkretus laikas): `at (2001.01.01)` or a time interval (laiko intervalas): `after(10 seconds)`
- **SignalEvent**
- **...**

---

## Slide 8 — Pseudo-States

**Title:** Pseudo būsenos
**Translation:** Pseudo-States

> [Diagram: Visual reference table of all UML pseudo-state notations:]

| Symbol | Name (Lithuanian) | Name (English) |
|---|---|---|
| Filled black circle | pradžios būsena | initial state |
| Circle with inner filled circle | pabaigos būsena | final state |
| X mark | nutraukimas | terminate |
| Circle labeled H* | Gilios istorijos būsena | deep history state |
| Circle labeled H | Istorijos būsena | history state (shallow history) |

**Composite State (Sudėtinė būsena):**
> [Diagram: A composite state containing an initial pseudo-state, two nested states, an exit point (circle with X, labeled "Išėjimo taškas / exit point"), and an entry point (small open circle, labeled "Įėjimo taškas / entry point"), ending in a final state.]

**Choice (Sprendimo taškas):**
> [Diagram: A diamond-shaped choice pseudo-state with two outgoing transitions: `[x=true]` going to one state, `[else]` going to another state.]

**Junction (Jungimo taškas):**
> [Diagram: A filled circle (junction) with two incoming transitions `e1 [b<0]` and `e2 [b<0]`, and two outgoing transitions `[a<0]` and `[a=2]`.]

**Composite Parallel State (Sudėtinė lygiagreti būsena):**
> [Diagram: A composite state containing two orthogonal regions separated by a dashed line. Entry via Fork pseudo-state (thick horizontal bar, labeled "išsišakojimas / Fork"), exit via Join pseudo-state (thick horizontal bar, labeled "sujungimas / Join"). Each region contains its own sequence of states.]

---

## Slide 9 — State Machine Example: Class ConferencePaper

**Title:** Būsenų mašina
**Translation:** State Machine

**Subject:** State machine for class `KonferencijosStraipsnis` (ConferencePaper)

> [Diagram: State Machine Diagram for class ConferencePaper with the following states and transitions:]
>
> - **Initial state** (filled circle) → **Pateiktas** (Submitted)
> - **Pateiktas** → [trigger: `skirtiRecenzentus()`] → **Recenzuojamas** (Under Review)
> - **Recenzuojamas** → [trigger: `skaičiuotiVertinimą()`] → decision diamond
>   - [guard: `įvertinimas tinkamas` / rating is acceptable] → **Priimtas** (Accepted)
>   - [guard: `else`] → **Atmestas** (Rejected)
> - **Priimtas** → [trigger: `apmokėti()`] → **Apmokėtas** (Paid)
> - **Priimtas** → [trigger: `after(nustatytasLaikas) [apmokėtas=false]`] → **Neapmokėtas** (Unpaid)

---

## Slide 10 — Composite State Example: Class Person

**Title:** Sudėtinė būsena
**Translation:** Composite State

**Subject:** State machine for class `Asmuo` (Person)

> [Diagram: State Machine Diagram for class Person. The diagram shows two top-level states:]
>
> **Top-level states:**
> - **nepilnametis** (minor/underage)
> - **pilnametis** (adult) — a composite state containing its own substates
>
> **Transitions at the top level:**
> - Initial state → nepilnametis
> - `gimtadienis [amžius<18]` (birthday [age<18]) → self-loop back to nepilnametis
> - `gimtadienis [amžius=18]` (birthday [age=18]) → pilnametis (enters composite state)
> - `mirtis` (death) → final state (from pilnametis composite state)
>
> **Inside the composite state "pilnametis" (adult):**
> - Initial sub-state → **nevedęs** (single/unmarried)
> - `gimtadienis [amžius>=18]` → self-loop on pilnametis (re-entering)
> - **nevedęs** → [vestuvės / wedding] → **vedęs** (married)
> - **vedęs** → [skyrybos / divorce] → **išsiskyręs** (divorced)
> - **išsiskyręs** → [vestuvės / wedding] → **vedęs** (married)
> - **vedęs** → [partnerio mirtis / partner's death] → **našlys** (widowed)
> - **našlys** → [vestuvės / wedding] → **vedęs** (married)
> - History pseudo-state **(H)** connected to composite state (remembers last substate)

---

## Slide 11 — Composite Parallel State

**Title:** Sudėtinė lygiagreti būsena
**Translation:** Composite Parallel State (Orthogonal Regions)

> [Diagram: The same Person class state machine extended with a composite parallel state for the "adult" (suaugęs) super-state. Two orthogonal regions separated by a dashed line:]
>
> **Region 1 (top) — employment status:**
> - Initial state → **dirbantysis** (employed/working)
> - **dirbantysis** → **pensininkas** (retired) → final state
>
> **Region 2 (bottom) — marital status:**
> - **nepilnametis** (minor, outside the composite) → enters composite via Fork
> - Initial sub-state → **nevedęs** (single)
> - **nevedęs** → [vestuvės] → **vedęs** (married)
> - **vedęs** → [skyrybos] → **išsiskyręs** (divorced)
> - **išsiskyręs** → [vestuvės] → **vedęs** (married)
> - **vedęs** → [partnerio mirtis] → **našlys** (widowed)
> - **našlys** → [vestuvės] → **vedęs**
> - Both regions exit via Join pseudo-state → final state

---

## Slide 12 — Submachine State

**Title:** Submašinos būsena
**Translation:** Submachine State

**Left side — State Machine definition (labeled `ReadAmountSM`):**

> [Diagram: A separate state machine named "ReadAmountSM" with the following structure:
> - Initial state → **selectAmount**
> - **selectAmount** → [otherAmount] → **enterAmount**
> - **selectAmount** → [amount] → final state (ok)
> - **enterAmount** → [abort] → terminate (X) / aborted exit point
> - abort transition also exits from selectAmount]

**Right side — Used as a submachine state in another diagram (ATM):**

> [Diagram: ATM state machine where one state is a submachine state referencing ReadAmountSM:
> - Initial state → **verifyCard**
> - **verifyCard** → [acceptCard/] → **readAmount : ReadAmountSM** (submachine state, indicated by the "oo" icon)
> - **readAmount : ReadAmountSM** → [outOfService/] → **outOfService**
> - **readAmount : ReadAmountSM** → [aborted exit point] → **CardReleased**
> - **readAmount : ReadAmountSM** → **verifyTransaction**
> - **verifyTransaction** → [releaseCard/] → **CardReleased**
> - Blue arrow indicates the reference from ATM's "readAmount" state to the ReadAmountSM definition]

Text caption (blue): "Used as a submachine state in another diagram" (Naudojama kaip submašinos būsena kitoje diagramoje)

---

## Slide 13 — Bank ATM State Machine

**Title:** Bankomato būsenų mašina
**Translation:** Bank ATM State Machine

> [Diagram: Full UML State Machine Diagram for a Bank ATM (source: uml-diagrams.org). States and transitions:]
>
> **Top-level states:**
> - **Off** — initial state (black dot → Off)
> - **Self Test**
> - **Idle**
> - **Maintenance**
> - **Out of Service**
> - **Serving Customer** — composite state
>
> **Transitions:**
> - Initial → **Off**
> - **Off** → [turn on / startup] → **Self Test**
> - **Self Test** → [failure] → **Out of Service**
> - **Self Test** → (success, implicit) → **Idle**
> - **Idle** → [service] → **Maintenance**
> - **Maintenance** → [failure] → **Out of Service**
> - **Out of Service** → [service] → **Maintenance**
> - **Out of Service** → [failure] → **Self Test**
> - **Idle** → [cardInserted] → **Serving Customer**
> - **Serving Customer** → [cancel] → **Idle**
> - **Serving Customer** → [failure] → **Out of Service**
> - **Off** ← [turn off / shutDown] from **Out of Service**
> - **Off** ← [turn off / shutDown] from **Idle** and **Self Test** area
>
> **Inside the composite state "Serving Customer":**
> - entry / readCard
> - exit / ejectCard
> - Internal initial state → **Customer Authentication** (submachine, oo icon)
> - **Customer Authentication** → **Selecting Transaction**
> - **Selecting Transaction** → **Transaction** (submachine, oo icon)
> - **Transaction** → internal final state

---

## Slide 14 — Exercise: Build a State Machine

**Title:** Sudarykime būsenų mašiną
**Translation:** Let's Build a State Machine

**Class:** Durys (Door)

Can be: open, closed, locked (atidarytos, uždarytos, užrakintos)

> [Image: Photo of an open white door leading to a green outdoor scene — illustrating the Door class subject.]

---

## Slide 15 — Washing Machine State Diagram

**Title:** Skalbimo mašinos būsenų diagrama
**Translation:** Washing Machine State Diagram

**Question (blue text):** What happens if, while the washing machine is running, we open the door and then close it again?
(Kas bus, jei, veikiant skalbimo mašinai, atidarysime duris ir vėl uždarysime?)

> [Diagram: State Machine Diagram for a washing machine with two top-level states:]
>
> **Composite state "veikianti" (running):**
> - Internal initial state → **skalbimas** (washing)
> - **skalbimas** → **skalavimas** (rinsing)
> - **skalavimas** → **gręžimas** (spinning)
> - **gręžimas** → internal final state
>
> **Outside composite state:**
> - Initial state → enters **veikianti** (running composite state)
> - **veikianti** → [atidaryti duris / open door] → **sustabdyta** (paused/stopped)
> - **sustabdyta** → [uždaryti duris / close door] → **veikianti** (running)
> - **veikianti** → [išjungta elektra / power off] → final state
> - **sustabdyta** → [išjungta elektra / power off] → final state
>
> **Problem:** When returning from "sustabdyta" to "veikianti", the machine restarts from **skalbimas** (washing), not from where it was interrupted.

---

## Slide 16 — Washing Machine State Diagram — History State (shallow history)

**Title:** Skalbimo mašinos būsenų diagrama – istorijos būsena (history/shallow history)
**Translation:** Washing Machine State Diagram — History State (history / shallow history)

**Text (blue):** If we want the washing machine to remember the last state before opening the door:
(Jei norime, kad skalbimo mašina atsimintų paskutinę būseną prieš atidarant duris)

> [Diagram: Same washing machine state machine as Slide 15, but with a **History pseudo-state (H)** added inside the "veikianti" composite state. The transition from "sustabdyta" → "veikianti" now points to the **(H)** pseudo-state instead of the initial state, so the machine resumes the last active substate (skalbimas, skalavimas, or gręžimas) it was in before the door was opened.]
>
> **States and transitions (same as Slide 15 with the following change):**
> - **sustabdyta** → [uždaryti duris] → **(H)** inside **veikianti** — resumes from last remembered substate

---

## Slide 17 — Deep History State and State Configuration

**Title:** Gilios istorijos būsena ir būsenų konfigūracija
**Translation:** Deep History State and State Configuration

In a hierarchical state machine, multiple states can be active at the same time.

If a simple state is active, then all the composite states it belongs to are also active.

The active states form a tree called the **state configuration**.

The **deep history state** remembers the last active configuration of the composite state it directly belongs to.

---

## Slide 18 — Washing Machine State Diagram — Deep History State

**Title:** Skalbimo mašinos būsenų diagrama – gilios istorijos būsena (deep history)
**Translation:** Washing Machine State Diagram — Deep History State (deep history)

> [Diagram: Extended washing machine state machine where each of the three top-level substates (skalbimas, skalavimas, gręžimas) is itself a composite state with its own internal substates. A **Deep History pseudo-state (H*)** is used so that when the door is closed and the machine resumes, it remembers not just which top-level substate was active, but also which internal substate within it was active.]
>
> **Composite state "veikianti" (running) — top-level substates:**
>
> **skalbimas** (washing) — composite, contains:
> - Initial → **pripylimas** (filling)
> - **pripylimas** → **mirkymas** (soaking)
> - **mirkymas** → **vartymas** (agitating/tumbling)
> - **vartymas** → **išpylimas** (draining)
> - **išpylimas** → internal final state
>
> **skalavimas** (rinsing) — composite, contains:
> - Initial → **pripylimas** (filling)
> - **pripylimas** → **purškimas** (spraying)
> - **purškimas** → **išpylimas** (draining)
> - **išpylimas** → internal final state
>
> **gręžimas** (spinning) — composite, contains:
> - Initial → **išpylimas** (draining)
> - **išpylimas** → **balansavimas** (balancing)
> - **balansavimas** → **sukimas** (spinning)
> - **sukimas** → internal final state
>
> **Transitions (same structure as Slide 15/16):**
> - Initial state → **veikianti**
> - **veikianti** → [atidaryti duris] → **sustabdyta** (paused)
> - **sustabdyta** → [uždaryti duris] → **(H*)** deep history pseudo-state inside **veikianti** — resumes full deep configuration
> - **veikianti** → [išjungta elektra] → final state
> - **sustabdyta** → [išjungta elektra] → final state

---

## Slide 19 — Example: State Reachability

**Title:** Pavyzdys
**Translation:** Example

**Question:** What state will be reached from state S11 after the following event sequences?

a) e1, e2, e2, e1
b) e1, e1, e2, e2
c) e1, e1, e2, e2, e1, e1, e2, e2

> [Diagram: State Machine Diagram with the following structure:]
>
> **Composite state S1** containing:
> - **(H)** history pseudo-state connected to **S11**
> - **S11** → [e1] → **S12**
> - **S12** → [e1] → **S13**
> - **S13** → [e1] → **S12** (back to S12, i.e., e1 from S13 loops back to S12)
>
> **Outside S1:**
> - **S1** → [e2] → **S2**
> - **S2** → [e2] → **S1** (re-enters via history state H, resuming last active substate)
>
> **Note:** The history pseudo-state (H) means that when S1 is re-entered from S2, control resumes at the last active substate (S11, S12, or S13) that was active when S1 was exited.

---

## Slide 20 — UML 2.5 Diagrams (Summary / Closing)

**Title:** UML 2.5 diagramos
**Translation:** UML 2.5 Diagrams

> [Diagram: Same UML 2.5 diagram taxonomy tree as Slide 2. Now four diagrams are marked with green checkmarks, indicating they have been covered in the course:]
>
> - Class Diagram ✓
> - Activity Diagram ✓
> - Use Case Diagram ✓
> - **State Machine Diagram ✓** ← newly checked off after this lecture
>
> **Structure Diagram** subtypes:
> - Class Diagram ✓ *(covered)*
> - Component Diagram
> - Object Diagram
> - Composite Structure Diagram
> - Deployment Diagram
> - Package Diagram
> - Profile Diagram
>
> **Behavior Diagram** subtypes:
> - Activity Diagram ✓ *(covered)*
> - Use Case Diagram ✓ *(covered)*
> - State Machine Diagram ✓ *(covered — this lecture)*
> - Interaction Diagram (subtypes):
>   - Sequence Diagram
>   - Communication Diagram
>   - Interaction Overview Diagram
>   - Timing Diagram
