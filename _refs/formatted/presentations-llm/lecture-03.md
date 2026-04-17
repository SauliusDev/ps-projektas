# Lecture 03 — Activity Diagram (Veiklos diagrama)

**Course:** Software Systems Analysis and Design Tools (T120B029)

**Topics covered:**
- Placement of the Activity Diagram in the IS development process
- Introduction to UML Activity Diagrams
- UML 2.5 diagram taxonomy (Structure vs. Behavior diagrams)
- Activity and Activity node concepts
- Types of activity nodes: Action node, Object node, Structured Activity node, Control nodes
- Activity edges (edges and connectors)
- Action types: Action, Call Behaviour Action, Send Signal Action, Accept Event Action, Time Event
- Structured Activity nodes: Structured activity, Conditional node, Loop node
- Object nodes and Pins
- Expansion Region
- Control nodes: Initial node, Activity Final, Flow Final
- Control nodes: Decision, Merge, Guard
- Control nodes: Fork, Join
- Swimlanes (partitions)
- Object states on activity diagrams
- Requirements-phase activity diagram examples
- Correct and incorrect usage patterns (recommendations)

---

## Slide 1 — IS Development Process (Used Process)

**Title:** Naudojamas PĮ kūrimo procesas
*(Used Software Development Process)*

> [Diagram: UML Activity Diagram showing the full IS development process flow. The process flows top to bottom with decision diamonds between phases. The "Requirements Specification" (Reikalavimų specifikavimas) phase is highlighted with a blue oval. Each phase produces one or more artefacts listed to the right.]

**Phases and their artefacts:**

- **Initial Requirements Description** (Pradinis reikalavimų aprašymas)
  - : Interface Prototype (Sąsajos prototipas)
  - : Initial System Description (Pradinis sistemos aprašas)

- **Requirements Specification** (Reikalavimų specifikavimas) ← *[highlighted — current focus]*
  - Functional Requirements: Use Case Diagram (Funkciniai reikalavimai: Panaudojimo atvejų diagrama)
  - Scenario for each use case: Activity Diagram (Kiekvieno panaudojimo atvejo scenarijus: Veiklos diagrama)
  - Domain entities: Class Diagram (Dalykinės srities esybės: Klasių diagrama)
  - Entity states: State Machine Diagram (Esybių būsenos: Būsenų diagrama)

- **Design** (Projektavimas)
  - Logical architecture: Package Diagram (Loginė architektūra: Paketų diagrama)
  - Scenario for each use case: Sequence Diagram (Kiekvieno panaudojimo atvejo scenarijus: Sekų diagrama)
  - Project classes: Class Diagram (Projekto klasės: Klasių diagrama)

- **Implementation** (Realizavimas)
  - : Component Diagram (Komponentų diagrama)
  - : Deployment Diagram (Diegimo diagrama)
  - : Program Code (Programos kodas)

- **Testing** (Testavimas)
  - : Test Plan (Testavimo planas)
  - : Test Report (Testavimo ataskaita)

---

## Slide 2 — Section Title: Activity Diagram

**Title (Lithuanian):** Veiklos diagrama

**Subtitle:** ACTIVITY DIAGRAM

*(This is the section title slide introducing the Activity Diagram topic.)*

---

## Slide 3 — UML 2.5 Diagrams

**Title:** UML 2.5 diagramos *(UML 2.5 Diagrams)*

> [Diagram: UML 2.5 diagram taxonomy tree. Root node: "Diagram". Two main branches: "Structure Diagram" and "Behavior Diagram". The Activity Diagram is highlighted with a green box (current topic). The Use Case Diagram is marked with a green checkmark (covered previously).]

**Structure Diagram** subtypes:
- Class Diagram
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram
- Profile Diagram

**Behavior Diagram** subtypes:
- **Activity Diagram** ← *[highlighted — current topic]*
- **Use Case Diagram** ← *[checkmark — previously covered]*
- State Machine Diagram
- Interaction Diagram
  - Sequence Diagram
  - Interaction Overview Diagram
  - Communication Diagram
  - Timing Diagram

---

## Slide 4 — Activity (Veikla)

**Title:** Veikla (Activity)

The Activity Diagram is used to visualize processes.
- We will use it to model the scenario of each Use Case (PA — Panaudojimo atvejis).

**Activity** — parameterized behavior, represented as a coordinated flow of actions.
*(Veikla – parametrizuota elgsena, vaizduojama kaip koordinuotas veiksmų srautas.)*

An activity consists of **activity nodes**, which can be:
- Action (Veiksmas)
- Structured activity (Struktūrinė veikla)
- Object (Objektas)
- Control node (Valdymo mazgas)

> [Diagram: Simple activity diagram example labeled `activity [ Valdyti užsakymus ]` (Manage Orders). Flow: Initial node → sukurti_užsakymą (create order) → patvirtinti_užsakymą (confirm order) → pristatyti_užsakymą (deliver order) → Activity Final node.]

---

## Slide 5 — Types of Activity Nodes (Veiklos mazgų tipai)

**Title:** Veiklos mazgų tipai (Activity nodes)

*(Source: UML 2.5 specification)*

> [Diagram: Visual notation reference showing the graphical symbols for each node type:]

| Node Type | Symbol Description |
|---|---|
| **Action node** | Rounded rectangle (soft corners) |
| **Object node** | Plain rectangle (sharp corners) |
| **Control nodes** | Diamond (Decision/Merge), thick vertical bar (Fork/Join), filled circle (Initial node), circle with inner filled circle (Activity Final), circle with X (Flow Final) |
| **Structured Activity node** | Dashed rounded rectangle with `«structured»` stereotype label |

---

## Slide 6 — Representing Activity Edges (Veiklos briaunų vaizdavimas)

**Title:** Veiklos briaunų vaizdavimas *(Representing Activity Edges)*

> [Diagram: Three notation examples for edges:]

- **Activity Edge** (Veiklos briauna) — solid arrow with arrowhead
  - Two parallel solid arrows (thick blue) indicate equivalence between notations
- **Connector** (Jungtis) — arrow leading to a circle labeled `n`, and a matching circle labeled `n` with an arrow leaving it (used to connect distant parts of a diagram without crossing lines)
- **Named Edge** (Briauna su vardu) — arrow labeled with `name` above it

---

## Slide 7 — Action (Veiksmas)

**Title:** Veiksmas (Action)

An action corresponds to a single atomic step in an activity.
*(Veiksmas atitinka vieną atominį žingsnį veikloje.)*

Actions can be of many types:
- **Action**
- **Call Behaviour Action**
- **Send Signal Action**
- **Accept Event Action**
- **Time Event**
- **...** (and many more)

> [Diagram: Several notation examples for different action types:
> - Regular action: rounded rectangle labeled "Pažymėti varnele perskaitytą knygą" (Check off a read book)
> - Call Behaviour Action: rounded rectangle with a rake/fork symbol inside — ": Įvertinti knygą" (Evaluate book)
> - Send Signal Action: pentagon (convex arrow shape) — "Išsiųsti užsakymą" (Send order)
> - Accept Event Action: concave pentagon shape — "Priimti užsakymą" (Accept order) → "Apdoroti užsakymą" (Process order) — "Pranešti klientui" (Notify client)
> - Time Event: hourglass shape labeled "at (kas valandą)" (at [every hour]) → "Atnaujinti informaciją" (Update information)]

> [Screenshot: "Select Action Metaclass" dialog from a CASE tool showing 42 action metaclass types, including: Accept Call Action, Accept Event Action, Add Structural Feature Value Action, Add Variable Value Action, Broadcast Signal Action, Call Behavior Action, Call Operation Action, Clear Association Action, Clear Structural Feature Action, Clear Variable Action, Conditional Node, Create Link Action, Create Link Object Action, Create Object Action, Destroy Link Action, Destroy Object Action, Expansion Region, Loop Node, Opaque Action, Raise Exception Action, Read Extent Action, Read Is Classified Object Action, Read Link Action, Read Link Object End Action, Read Link Object End Qualifier Action, and more.]

---

## Slide 8 — Structured Activity Node (Struktūrinė veikla)

**Title:** Struktūrinė veikla (Structured Activity Node)

**Structured activity** (Struktūrinė veikla)

> [Diagram: Example of a Structured Activity node labeled `«structured» Order`. Contains: Receive Order → Decision diamond → [Order accepted] → Fill Order; or → Close Order. The entire sub-activity is enclosed in a dashed rounded rectangle.]

**Conditional Structured Activity** (Sąlyginė struktūrinė veikla — Conditional node)

> [Diagram: Conditional node with two sections — `test` section containing "Check if reading item is reserved", and `body` section containing "Recalculate possible loan date and e-mail notifications" → "E-mail notifications".]

**Loop** (Ciklas — Loop node)

> [Diagram: Loop node with three sections — `setup` containing "Select the reading item to remove"; `test` containing "Check if there are more copies" → "Decrease the number of reading items by one"; `body` containing "E-mail notifications".]

---

## Slide 9 — Object Node and Pin (Objektas / Veiksmo argumentas)

**Title:** Objektas (Object node) / Veiksmo argumentas (Pin)

> [Diagram (top): Two equivalent notations shown side by side with a "=" sign:
> - Left notation: "Fill Order" and "Ship Order" action nodes both connected to a shared "Order" object node (rectangle).
> - Right (Pin) notation: "Fill Order" action node with an output pin labeled "Order" connected to "Ship Order" action node with an input pin labeled "Order". Pins are small squares attached to the action node boundary.]

> [Diagram (bottom): More complex example showing an order assembly flow with pins:
> - "Accept Order" (output pin: Order) → "Assemble Order" (input pins: Order [accepted], Materials [picked], PC designs)
> - "Pick Materials for Order" (output pin: Materials [picked]) → "Assemble Order"
> - "Produce Designs" (output pin: PC designs {stream}) → "Assemble Order"
> - "Assemble Order" output pins: Order [assembled], PC designs]

---

## Slide 10 — Expansion Region (Išplėtimo regionas)

**Title:** Išplėtimo regionas (Expansion Region)

Represents actions performed on sets of objects.
*(Vaizduoja veiksmus, atliekamus su aibėmis.)*

- Input and output are sets of objects (įėjimas, išėjimas — objektų aibė).

> [Diagram: Expansion Region example for article review process.
> - Input expansion node (multi-bar bracket) labeled "Pateikti straipsniai" (Submit articles) feeds into an `«iterative»` Expansion Region.
> - Inside the region: "Recenzuoti straipsnį" (Review article) → Decision diamond → [atmestas] (rejected) → Flow Final (circle with X); or → [priimtas] (accepted) → output expansion node.
> - Output expansion node labeled "Priimti straipsniai" (Accepted articles).]

---

## Slide 11 — Control Nodes: Start, End (Valdymo mazgai: pradžia, pabaiga)

**Title:** Valdymo mazgai: pradžia, pabaiga *(Control Nodes: start, end)*

> [Diagram: Simple linear activity showing:
> - **Initial node** (filled black circle) — start of the activity, indicated with a blue arrow label "Initial node"
> - → Veiksmas1 (Action1)
> - → Veiksmas2 (Action2)
> - → **Activity Final** node (circle containing a filled circle) — end of the activity, indicated with a blue arrow label "Activity Final"]

---

## Slide 12 — Which End Node to Use? (Kurią pabaigą naudoti?)

**Title:** Kurią pabaigą naudoti? *(Which end to use?)*

**Activity Final** (Pabaigos viršūnė)
- Ends the entire activity (visos veiklos pabaiga)
- Symbol: circle with inner filled circle

**Flow Final** (Išėjimo viršūnė)
- Ends one of the parallel flows (vieno iš lygiagrečių srautų pabaiga)
- Symbol: circle with X inside

> [Diagram: Example showing both end node types in use:
> - "Pull Order Item from Stock" → Fork bar → upper branch: "Prepare Item for Delivery" → "Ship Order" (continues to Activity Final)
> - Fork bar → lower branch: Decision diamond → [true] → "Reorder Goods"; [false] → Flow Final (circle with X)
> - Decision node has a note attached: `«decisionInput» inventoryLevel < reorderPoint`]

---

## Slide 13 — Control Nodes: Decision, Merge (Valdymo mazgai: Decision, Merge)

**Title:** Valdymo mazgai: Decision, Merge

- **Decision point** (Sprendimo taškas — decision) — diamond with one incoming and multiple outgoing edges
- **Merge** (Suliejimas — merge) — diamond with multiple incoming and one outgoing edge
- **Guard** (Sąlyga — guard) — condition in square brackets on outgoing edges

> [Diagram (top right): Order processing example:
> - "Receive Order" → Decision → [Order rejected] (loop back to top); [Order accepted] → "Fill Order" → "Close Order"]

> [Diagram (middle right): Merge example:
> - "Buy Item" and "Make Item" both connect to a Merge diamond → "Ship Item"]

> [Diagram (bottom left, with annotations): Decision with guards [x>0] and [else], leading to two separate action nodes, which then merge back via a Merge diamond. Blue arrows point to: Sprendimo taškas (decision), Suliejimas (merge), Sąlyga (guard).]

> [Diagram (bottom right — alternative notation): Decision shown as a diamond labeled "Ar x>0?" with outgoing edges labeled "Taip" (Yes) and "Ne" (No); caption reads "Kitas vaizdavimo variantas:" (Another notation variant).]

---

## Slide 14 — Control Nodes: Fork, Join (Valdymo mazgai: Fork, Join)

**Title:** Valdymo mazgai: Fork, Join

**Fork** (Išsišakojimas)
- Outgoing actions can start simultaneously (Išeinantys veiksmai gali prasidėti vienu metu)

**Join** (Sujungimas)
- All incoming actions must have completed before continuing (turi būti pasibaigę visi įeinantys veiksmai)

> [Diagram: Fork and Join example for order fulfillment:
> - "Užpildyti užsakymą" (Fill order) → Fork bar (thick horizontal line)
> - Fork → "Išsiųsti užsakymą" (Send order) [parallel branch 1]
> - Fork → "Siųsti sąskaitą" (Send invoice) [parallel branch 2]
> - Both branches → Join bar (thick horizontal line)
> - Join → "Užbaigti užsakymą" (Complete order)
> Blue arrows indicate the Fork bar and the Join bar.]

---

## Slide 15 — Swimlanes (Juostos)

**Title:** Juostos (swimlanes)

The activity diagram can be partitioned to indicate who is responsible for each action.
*(Galima veiklos diagramą padalinti, nurodant, kas atsakingas už veiksmus.)*

> [Diagram: Order processing activity diagram with three horizontal swimlanes:
>
> **Swimlane 1 — Order Department** (performingDept):
> - Initial node → "Receive Order" → Decision → [order accepted] → "Fill Order" → Fork → "Ship Order" → Join → Decision → "Close Order" → Activity Final
>
> **Swimlane 2 — Accounting Department** (Acctg Department, performingDept):
> - Fork output → "Send Invoice" → "Invoice" (object node)
> - "Invoice" (object node) → "Accept Payment"
> - "Accept Payment" → Join input
>
> **Swimlane 3 — Customer** («external»):
> - "Invoice" (object node) → "Make Payment"
> - "Make Payment" → "Accept Payment"]

---

## Slide 16 — Object States (Objektų būsenos)

**Title:** Objektų būsenos *(Object States)*

> [Diagram (main — swimlane activity diagram): Order fulfillment process with three swimlanes:
>
> **Swimlane — Buyer (Pirkėjas):**
> - Initial node → "Pateikti užsakymą" (Submit order) → ": Užsakymas [Pateiktas]" (Order [Submitted]) object node
> - Later: "Apmokėti" (Pay) → ": SąskaitaFaktūra [Apmokėta]" (Invoice [Paid]) object node
> - Later: "Gauti prekes" (Receive goods)
>
> **Swimlane — Sales Manager (Pardavimų vadybininkas):**
> - ": Užsakymas [Pateiktas]" → "Priimti užsakymą" (Accept order) → ": Užsakymas [Priimtas]" (Order [Accepted])
> - → "Išrašyti sąskaitą faktūrą" (Issue invoice) → ": SąskaitaFaktūra [Išrašyta]" (Invoice [Issued])
> - Fork bar (synchronization)
> - Later: "Užbaigti užsakymą" (Complete order) → ": Užsakymas [Užbaigtas]" (Order [Completed]) → Activity Final
>
> **Swimlane — Warehouse Worker (Sandėlininkas):**
> - ": Užsakymas [Priimtas]" (after fork) → "Supakuoti prekes" (Pack goods) → ": Užsakymas [Supakuotas]" (Order [Packed])
> - Join bar
> - → "Pristatyti" (Deliver) → ": Užsakymas [Pristatytas]" (Order [Delivered])
> - Join bar → feeds into "Užbaigti užsakymą"]

> [Diagram (right side — object state machines):
>
> **Užsakymas** (Order) state sequence:
> Initial → Pateiktas (Submitted) → Priimtas (Accepted) → Supakuotas (Packed) → Pristatytas (Delivered) → Užbaigtas (Completed) → Final
>
> **SąskaitaFaktūra** (Invoice) state sequence:
> Initial → Išrašyta (Issued) → Apmokėta (Paid) → Final]

---

## Slide 17 — Requirements-Phase Activity Diagram Examples (Reikalavimų etapo veiklos diagramų pavyzdžiai)

**Title:** Reikalavimų etapo veiklos diagramų pavyzdžiai *(Requirements-Phase Activity Diagram Examples)*

> [Diagram (left): Two-swimlane activity diagram for a task initiation use case:
>
> **Swimlane — Specialist (Specialistas):**
> - Initial node → "Paspausti iniciavimo mygtuką" (Press initiation button)
> - → "Pasirinkti procesą" (Select process)
> - → "Įvesti pradžios duomenis" (Enter initial data)
> - → Decision → [duomenys teisingi] (data correct) → "Spausti starto mygtuką" (Press start button)
> - [else] → no action from Specialist side
>
> **Swimlane — Task List Subsystem (Užduočių sąrašo posistemė):**
> - "Atidaryti proceso iniciavimo formą" (Open process initiation form)
> - → "Atidaryti proceso reikšmių langą" (Open process parameter window)
> - → "Patikrinti įvestus duomenis" (Validate entered data)
> - [duomenys teisingi] → "Starto mygtukas aktyvuojamas" (Start button activated)
> - [else] → "Pateikiamas klaidos pranešimas" (Error message displayed)
> - → Merge → ": Inicijuoti užduoties vykdymą" (: Initiate task execution) [Call Behaviour Action] → Activity Final
>
> Note (precondition): "Specialistas yra prisijungęs" (Specialist is logged in)]

> [Diagram (right): Two-swimlane activity diagram for a data migration tool use case:
>
> **Swimlane — Developer (Programuotojas):**
> - Initial node → "Paleisti migravimo įrankį" (Launch migration tool)
> - Later: ": Pakeisti nustatymus" (: Change settings) [Call Behaviour Action]
> - Later: ": Įvesti lauko apjungimo nustatymą" (: Enter field merge setting) [Call Behaviour Action]
> - Later: "Paleisti migravimo skriptą" (Run migration script)
>
> **Swimlane — Data Migration Tool (Duomenų migravimo įrankis):**
> - "Atidaryti duomenų migravimo pagrindinį langą" (Open main data migration window)
> - → ": Apjungti laukus" (: Merge fields) [Call Behaviour Action]
> - → Decision → [yra neapjungtų laukų] (there are unmerged fields) → "Informuoti vartotoją apie neapjungtus laukus" (Notify user about unmerged fields) → back to ": Įvesti lauko apjungimo nustatymą"
> - [else] → ": Sugeneruoti migravimo skriptą" (: Generate migration script) [Call Behaviour Action]
> - → Activity Final]

---

## Slide 18 — In What Order Will Actions Occur? (Kokia seka vyks veiksmai?)

**Title:** Kokia seka vyks veiksmai? *(In what order will actions occur?)*

> [Diagram (left): Decision (exclusive choice) pattern:
> - Incoming flow → Decision diamond: [x=true] → Action A; [else] → Action B
> - Both A and B → Join bar → Action C → continues
> - Semantics: either A or B executes (not both), then C executes after whichever one finishes.]

> [Diagram (right): Fork (parallel split) pattern:
> - Incoming flow → Fork bar → Action A (parallel) and Action B (parallel)
> - Both A and B → Merge diamond → Action C → continues
> - Semantics: A and B both execute concurrently; C executes after the first one to finish (Merge does NOT wait for both — that is Join's role).]

*(Note: This slide illustrates the semantic difference between Decision+Join vs. Fork+Merge, which is a common source of confusion.)*

---

## Slide 19 — Recommendations (Rekomendacijos)

**Title:** Rekomendacijos *(Recommendations)*

> [Diagram set — showing incorrect and correct patterns:]

**Pattern 1 — Multiple outgoing edges from Initial node:**

- **Incorrect** (nekorektiškai): Initial node with two outgoing edges directly to two action nodes (without a Decision or Fork node).
- **Correct option 1** (teisingai): Initial node → Decision diamond → two outgoing guarded edges → two action nodes (exclusive choice).
- **Correct option 2** (teisingai — "arba" / "or"): Initial node → Fork bar → two outgoing edges → two action nodes (parallel).

**Pattern 2 — Loop with guard on the wrong edge:**

- **Incorrect** (nekorektiškai): Initial node → Action node → outgoing edge guarded with [x=false] loops back; Decision diamond with guard [x=true] points down but the initial node feeds into the action directly (missing the decision before first execution).
- **Correct** (teisingai): Initial node → Decision diamond → [x=false] → Action node → [x=true] → Decision diamond (loop back). The Decision node must appear before the action in a loop so the condition is checked before executing.

---

## Slide 20 — UML 2.5 Diagrams (revisited)

**Title:** UML 2.5 diagramos *(UML 2.5 Diagrams)*

> [Diagram: Same UML 2.5 diagram taxonomy tree as Slide 3. This time both the Activity Diagram and the Use Case Diagram are marked with green checkmarks, indicating both have now been covered in the course.]

**Structure Diagram** subtypes:
- Class Diagram
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram
- Profile Diagram

**Behavior Diagram** subtypes:
- **Activity Diagram** ← *[checkmark — covered this lecture]*
- **Use Case Diagram** ← *[checkmark — covered previously]*
- State Machine Diagram
- Interaction Diagram
  - Sequence Diagram
  - Interaction Overview Diagram
  - Communication Diagram
  - Timing Diagram
