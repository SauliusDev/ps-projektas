# Lecture 02 — Use Case Diagram (Use-case diagram)

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Institution:** Kaunas University of Technology (KTU)

**Topics covered:**
- The IS (Information System) development process and the role of Requirements Specification
- Overview of UML 2.5 diagram types
- Use Case (UC) diagram — elements, notation, and purpose
- Actor: definition, types, representation
- Use Case: definition, naming conventions
- Relationships: association, generalization, <<include>>, <<extend>>
- Association multiplicity on both the UseCase and Actor end
- Generalization between actors and between use cases
- <<include>> vs <<extend>>: comparison and correct usage
- Common mistakes in UC diagrams (CRUD-type UCs, navigation chains, overcrowded diagrams)
- UC grouping with packages/subsystems
- UC specification: table format, fields, examples
- Generating UC specification reports in Magic Systems of Systems Architect
- Interface window sketches (UI mockups) linked to use cases
- Extended example: Coffee Vending Machine Information System

---

## Slide 1 — IS Development Process (Used Process)

> [Diagram: Activity diagram showing the IS (Information System) development process. Highlighted stage: Requirements Specification (circled in blue).]

**Naudojamas PI kūrimo procesas** — The IS Development Process in Use

Phases and their corresponding artefacts:

| Phase | Artefacts |
|---|---|
| **Pradinis reikalavimų aprašymas** (Initial Requirements Description) | : Sąsajos prototipas (Interface Prototype) |
| | : Pradinis sistemos aprašas (Initial System Description) |
| **Reikalavimų specifikavimas** (Requirements Specification) ← *highlighted* | Funkciniai reikalavimai : Panaudojimo atvejų diagrama (Functional requirements : Use Case Diagram) |
| | Kiekvieno panaudojimo atvejo scenarijus : Veiklos diagrama (Each use case scenario : Activity Diagram) |
| | Dalykinės srities esybės : Klasių diagrama (Domain entities : Class Diagram) |
| | Esybių būsenos : Būsenų diagrama (Entity states : State Machine Diagram) |
| **Projektavimas** (Design) | Loginė architektūra : Paketų diagrama (Logical architecture : Package Diagram) |
| | Kiekvieno panaudojimo atvejo scenarijus : Sekų diagrama (Each use case scenario : Sequence Diagram) |
| | Projekto klasės : Klasių diagrama (Design classes : Class Diagram) |
| **Realizavimas** (Implementation) | : Komponentų diagrama (Component Diagram) |
| | : Diegimo diagrama (Deployment Diagram) |
| | : Programos kodas (Program Code) |
| **Testavimas** (Testing) | : Testavimo planas (Test Plan) |
| | : Testavimo ataskaita (Test Report) |

---

## Slide 2 — Section Title: Use Case Diagram

# Panaudojimo atvejų (PA) diagrama

**Use-case diagram**

---

## Slide 3 — UML 2.5 Diagrams

> [Diagram: Taxonomy tree of UML 2.5 diagram types. The Use Case Diagram (highlighted with a green border) is a Behavior Diagram.]

**UML 2.5 diagramos** — UML 2.5 Diagrams

```
Diagram
├── Structure Diagram
│   ├── Class Diagram
│   ├── Component Diagram
│   ├── Object Diagram
│   ├── Composite Structure Diagram
│   ├── Deployment Diagram
│   ├── Package Diagram
│   └── Profile Diagram
└── Behavior Diagram
    ├── Activity Diagram
    ├── Use Case Diagram   ← [highlighted]
    ├── State Machine Diagram
    └── Interaction Diagram
        ├── Sequence Diagram
        ├── Interaction Overview Diagram
        ├── Communication Diagram
        └── Timing Diagram
```

---

## Slide 4 — Basic Elements (Pagrindiniai elementai)

> [Diagram: UML use case diagram showing stick-figure actors, use case ellipses, generalization arrows between actors, and dashed arrows labelled <<extend>> and <<include>> between use cases.]

**Pagrindiniai elementai** — Basic Elements

- **Aktorius** (Actor)
- **Panaudojimo atvejis** (Use case)

- **Ryšiai** (Relationships):
  - **association** — ryšys tarp aktoriaus ir panaudojimo atvejo (relationship between an actor and a use case)
  - **generalization** — apibendrinimas tarp dviejų aktorių/PA (generalization between two actors / use cases)
  - **include** — tarp dviejų PA (between two use cases)
  - **extend** — tarp dviejų PA (between two use cases)

---

## Slide 5 — Actor (Aktorius)

> [Diagram: Stick-figure icon representing an Actor.]

**Aktorius** — Actor

- An actor can be a person or a system.
- Located outside the boundaries of the system being developed; interacts with the system being developed.
- An actor can represent:
  - a system user,
  - an organisational unit,
  - a company,
  - an external software system,
  - an automated device,
  - ...
- The same person can use the system as several different actors.

---

## Slide 6 — Use Case (Panaudojimo atvejis)

> [Diagram: Ellipse icon representing a Use Case.]

**Panaudojimo atvejis** — Use Case

- A UC is a unit of functional requirements — a specific system function that a specific actor can use.
- It is a set of interactions between the user and the system that gives the user a meaningful result.
- Use cases describe the behaviour of the system being developed, but not how that behaviour will be implemented.
- UC name — as short as possible, describing an action.
  - recommendation: use an infinitive verb form

---

## Slide 7 — Relationship Between Actor and UC (Association)

**Ryšys tarp aktoriaus ir PA (Association)** — Relationship Between Actor and UC (Association)

> [Diagram: Actor (stick figure) labelled "Registratorius" connected by a solid line to a use case ellipse labelled "Registruoti užsakymą" (Register order).]

**Registratorius gali Registruoti užsakymą**
The Registrar **can** Register an order.

---

## Slide 8 — Association Multiplicity on the UC End

**Ryšio kardinalumas PA pusėje** — Association Multiplicity on the UseCase End

When an Actor has an **association** to a UseCase with a multiplicity that is **greater than one at the UseCase end**, it means that a given Actor can be involved **in multiple UseCases** of that type.*

> [Diagram: Actor (stick figure) labelled "Bankas" (Bank) connected with multiplicity "0..*" to a use case ellipse labelled "Pervesti lėšas" (Transfer funds).]

*OMG UML 2.5 specification

---

## Slide 9 — Association Multiplicity on the Actor End

**Ryšio kardinalumas aktoriaus pusėje** — Association Multiplicity on the Actor End

When a UseCase has an association to an Actor with a multiplicity that **is greater than one at the Actor end**, it means that **more than one Actor instance** is involved in the UseCase.*

> [Diagram: Actor (stick figure) labelled "Žaidėjas" (Player) connected with multiplicity "2..*" on the actor side and "1" on the use case side to a use case ellipse labelled "Žaisti žaidimą" (Play game).]

*OMG UML 2.5 specification

---

## Slide 10 — Generalization (Generalization) Relationship

**Paveldėjimo (Generalization) ryšys** — Generalization Relationship

> [Diagram — left side: Between use cases:]
> Parent use case "Apmokėti" (Pay) with two child use cases "Apmokėti su Paypal" (Pay with Paypal) and "Apmokėti kreditine kortele" (Pay with credit card), connected by generalization (hollow arrowhead) arrows pointing up to the parent.

> [Diagram — right side: Between actors:]
> Parent actor "Registruotas vartotojas" (Registered user) with two child actors "Administratorius" (Administrator) and "Skyriaus vadovas" (Department head); "Administratorius" has a further child actor "Redaktorius" (Editor). All connected by generalization arrows pointing upward.

**Tarp panaudojimo atvejų:** — Between use cases:
**Tarp aktorių:** — Between actors:

---

## Slide 11 — <<include>> Relationship (1)

**<<include>> ryšys** — <<include>> Relationship

Include is a DirectedRelationship between two UseCases, indicating that the behavior of the **included UseCase is inserted into** the behavior of the **including UseCase**.*

> [Diagram — left: Actor "Registratorius" (Registrar) connected to use case "Registruoti užsakymą" (Register order). From "Registruoti užsakymą", two dashed arrows labelled «include» point down to "Rezervuoti viešbutį" (Reserve hotel) and "Informuoti klientą" (Notify client).]

> [Diagram — right: Conceptual bubble showing "Registruoti užsakymą" as a large oval containing two sub-ovals "Rezervuoti viešbutį" and "Informuoti klientą", with blue arrows showing the insertion.]

*OMG UML 2.5 specification

---

## Slide 12 — <<include>> Relationship (2)

**<<include>> ryšys** — <<include>> Relationship

- The including UC cannot occur without the included UC.
- All included UCs must be executed when the including UC is executed.
- A suitable mechanism for specifying reusable behaviour:

> [Diagram: Two use cases "Padėti pinigus į sąskaitą" (Deposit money to account) and "Išimti pinigus iš sąskaitos" (Withdraw money from account) both point via «include» dashed arrows to "Autentifikuoti vartotoją" (Authenticate user).]

---

## Slide 13 — <<extend>> Relationship (1)

**<<extend>> ryšys** — <<extend>> Relationship

An Extend is a relationship that specifies **how and when** the behavior defined in the **extending UseCase can be inserted into** the behavior defined in the **extended UseCase**. The extension takes place at one or more specific **extension points** defined in the extended UseCase.*

> [Diagram: Actor "Registratorius" (Registrar) connected to use case "Registruoti užsakymą" (Register order). The use case has a compartment showing extension points: "jei paprašo papildomos informacijos" (if additional information is requested). A dashed arrow labelled «extend» comes from "Nusiųsti informaciją apie paslaugas" (Send information about services) pointing to "Registruoti užsakymą". From "Registruoti užsakymą", «include» arrows point to "Rezervuoti viešbutį" (Reserve hotel) and "Informuoti klientą" (Notify client).]

*OMG UML 2.5 specification

---

## Slide 14 — <<extend>> Relationship (2)

**<<extend>> ryšys** — <<extend>> Relationship

- It is necessary to specify the extension point (extension points) — the condition under which the extending (extending) UC occurs.
- The extending UC is independent of the extended (extended) UC.

---

## Slide 15 — <<include>> or <<extend>>?

**<<include>> ar <<extend>>?** — <<include>> or <<extend>>?

> [Diagram — left column: A --«include»--> B]
> [Diagram — right column: A <--«extend»-- B]

| <<include>> | <<extend>> |
|---|---|
| Read as: A includes B | Read as: B extends A |
| A encompasses B | B extends A |
| A is incomplete without B | A is complete without B |
| When A is executed, B is always executed | A can occur without B |
| | When A is executed, B may occur at a specific point if a specified condition holds |

---

## Slide 16 — UC Diagram Is NOT Meant to Show Navigation

**PA diagrama nėra skirta navigavimui rodyti** — The UC Diagram Is NOT Meant to Show Navigation

- include/extend "chains" — most often **wrong**

> [Diagram (marked as bad example — red border): A diagram showing a chain of include/extend relationships acting as navigation steps: "Naudotojas" (User) → "Peržiūrėti sąrašą" (View list) → «extend» → "Peržiūrėti sąrašo elementą" (View list item) → «extend» → "Redaguoti" (Edit); also «extend» → (if no confirmation) "Patvirtinti" (Confirm) → «include» → "Patikrinti" (Check); "Peržiūrėti sąrašo elementą" → «extend» (if wants to edit) → "Redaguoti"; "Redaguoti" → «extend» (if required category does not exist) → "Sukurti kategoriją" (Create category). All labelled with conditions.]

---

## Slide 17 — Do You Understand Anything Here?

**Ar čia ką nors suprantate?** — Do You Understand Anything Here?

> [Diagram: Extremely complex, overcrowded use case diagram for a game called "Isle-Breakout" with 41 numbered use cases, one actor (Player), one subsystem (Data System), and dozens of <<include>> and <<extend>> relationships with extension points. Use cases include: Select main menu option, Play game, Show game settings, Exit game, Select character, Create character, Delete character, Initialize game world, Spawn player, Spawn enemies, Control player, Move player, Fight enemies, Select weapon, Craft items, Increase stats, Open profile, Use item, Equip item, Consume item, Unequip item, Cast spell, Select target, Deselect target, Land weapon attack, Interact with NPC, Get quest, Finish quest, Get XP, Learn spell, Tame pet, Open menu, Resume game, Save game, Main menu, and others.]

This slide is shown as an example of a use case diagram that has become unreadable and unmanageable due to overuse of include/extend relationships and too many use cases.

---

## Slide 18 — When Multiple Actors Are Associated with the Same UC

**Kai keli aktoriai susiejami su tuo pačiu PA** — When Multiple Actors Are Associated with the Same UC

- If both actors participate in the UC simultaneously:

> [Diagram: «Subsystem» boundary labelled "Bankomatas" (ATM) contains three use cases: "Patikrinti likutį" (Check balance), "Išsiimti grynujų pinigų" (Withdraw cash), "Įnešti grynujų į sąskaitą" (Deposit cash). Actor "Banko klientas" (Bank client) on the left is connected to all three UCs. Actor "Bankas" (Bank) on the right is connected to "Išsiimti grynujų pinigų" and "Įnešti grynujų į sąskaitą".]

---

## Slide 19 — How to Fix When Not Both Actors Participate in a UC

**Kaip pataisyti, jei ne abu aktoriai dalyvauja PA?** — How to Fix When Not Both Actors Participate in a UC

> [Diagram — left (wrong, marked with red "?"): «Subsystem» "Viešbučių rezervavimo sistema" (Hotel reservation system). Two actors: "Registratorius" (Registrar) and "Viešbučio informacijos administratorius" (Hotel information administrator). Both connected to "Registruoti užsakymą" (Register order) and "Įvesti viešbučio informaciją" (Enter hotel information) — incorrectly implying joint participation.]

> [Diagram — right (correct): Same system. "Registratorius" connected only to "Registruoti užsakymą". "Viešbučio informacijos administratorius" connected only to "Įvesti viešbučio informaciją". Additionally, "Viešbučio informacijos administratorius" has a generalization arrow to "Registratorius" (it inherits from Registratorius).]

---

## Slide 20 — Another Example of How NOT to Do It

**Dar vienas pavyzdys, kaip nedaryti** — Another Example of How NOT to Do It

> [Diagram (marked as bad example): A use case diagram for a gaming-related social system with actors "Prisijungęs naudotojas" (Logged-in user) and "Neprisijungęs naudotojas" (Guest user). Contains use cases including: "Patalpinti įrašą" (Post entry), "Pasidalinti žaidimo pasiekimu" (Share game achievement), "Pasidalinti 'Warzone' paskutinio žaisto žaidimo informacija" (Share last Warzone game info), "Pasidalinti 'LeagueOfLegends' paskyros TOP 3 čempionais" (Share LoL top 3 champions), "Redaguoti įrašą" (Edit entry), "Atnaujinti įrašo patiktukų kiekį" (Update entry likes count), "Peržiūrėti įrašą" (View entry), "Komentuoti įrašą" (Comment on entry), "Pridėti 'Steam' žaidimus" (Add Steam games), "Palyginti žaidimo pasiekimus" (Compare game achievements), "Redaguoti profilį" (Edit profile), "Naudotojų paieška sistemoje" (User search in system), "Prisiregistruoti sistemoje" (Register in system), "Prisijungti sistemoje" (Log in to system). Various misused include relationships shown.]

This diagram illustrates how overly specific, technology-referencing use case names (e.g., naming specific games) and navigation chains using <<include>> are incorrect.

---

## Slide 21 — CRUD-Type Use Cases

**CRUD tipo PA** — CRUD-Type Use Cases

> [Diagram — top-left (acceptable): Actor "Naudotojas" (User) connected to "Valdyti" (Manage) use case; from "Peržiūrėti" (View) three «extend» arrows go to "Kurti" (Create), "Redaguoti" (Edit), "Naikinti" (Delete).]

> [Diagram — top-right (acceptable/correct): Actor "Naudotojas" directly connected to four separate use cases: "Kurti" (Create), "Naikinti" (Delete), "Peržiūrėti" (View), "Redaguoti" (Edit).]

> [Diagram — bottom-left (WRONG — red X): Actor "Naudotojas" connected to "Valdyti" (Manage), which then has four «extend» arrows to "Kurti", "Peržiūrėti", "Redaguoti", "Naikinti". Marked as incorrect.]

> [Diagram — bottom-right (WRONG — red X): Actor "Naudotojas" connected to "Valdyti" (Manage), which has four «include» arrows to "Kurti", "Redaguoti", "Naikinti" (and implied View). Marked as incorrect.]

---

## Slide 22 — UC Grouping (PA grupavimas)

**PA grupavimas** — UC Grouping

- Packages (packages) can be used to group UCs.
  - recommendation: no more than 5–10 UCs in one package
  - another recommendation: do not create packages with only 1–2 UCs
  - easiest to group by actor

> [Diagram: Use case diagram of a book library system with three packages/subsystems grouped by actor:
> - **Svečio posistemė** (Guest subsystem): Register, Search book, View book information, Filter books by price
> - **Nario duomenų valdymo posistemė** (Member data management subsystem): Log in, Log out, Change registration data
> - **Nario posistemė** (Member subsystem): Manage book shelf, Rate book, Mark book as read (included by Rate book via «include»), Write comment
> Actors: "Svečias" (Guest) connected to Guest subsystem; "Narys" (Member) connected to all three, with generalization from Narys to Svečias.]

---

## Slide 23 — Use Case Diagram with Packages

**Panaudojimo atvejų diagrama su paketais** — Use Case Diagram with Packages

- When a UC diagram is too large, an overview view can be shown.
- Each package can then be detailed separately.

> [Diagram — left (overview): Actors "Svečias" (Guest), "Narys" (Member, inherits from Svečias), "Administratorius" (Administrator). Dashed lines from each actor to their respective packages: Svečio posistemė, Nario duomenų valdymo posistemė, Nario posistemė, Administratoriaus posistemė.]

> [Diagram — right (detail of one package): "Svečio posistemė" expanded to show: Register, Search book, View book information, Filter books by price. Actor "Svečias" connected to all four.]

---

## Slide 24 — UC Specification (PA specifikavimas)

**PA specifikavimas** — UC Specification

- Every UC must have a specification.
- A detailed UC specification can include:
  - A document describing UC properties
  - Activity/sequence diagram(s) illustrating UC scenario(s)

---

## Slide 25 — Specification Table. Example 1

**Specifikavimas lentele. Pavyzdys 1** — Specification Table. Example 1

| Field | Value |
|---|---|
| **UC.** | Mark book as read (Pažymėti perskaitytą knygą) |
| **Goal.** | To give a member the ability to mark books as read (Suteikti galimybę nariui žymėti perskaitytas knygas) |
| **Description.** | A member can select any book from the list and mark it as read. Then in the book list, next to this book a mark will be visible indicating that the book has been read. (Narys gali pasirinkti iš sąrašo bet kurią knygą ir pažymėti ją kaip perskaitytą. Tuomet knygų sąraše prie šios knygos bus matoma žymė, rodanti, kad knyga yra perskaityta.) |
| **Pre-condition** | Member is logged in (Narys yra prisijungęs) |
| **Actor** | Member (Narys) |
| **Related use cases** — **Extending UCs** | |
| **Related use cases** — **Included UCs** | |
| **Related use cases** — **Specializing UCs** | |
| **Post-condition:** | The book in the member's shelf is marked as read (Nario lentynoje knyga yra pažymėta kaip perskaityta) |

---

## Slide 26 — Specification Table. Example 2

**Specifikavimas lentele. Pavyzdys 2** — Specification Table. Example 2

| Field | Value |
|---|---|
| **UC.** | View medical history (Peržiūrėti ligos istoriją) |
| **Goal.** | To allow a doctor to view a patient's medical history (Leisti gydytojui peržiūrėti paciento ligos istoriją) |
| **Description.** | A doctor, having selected a patient, sees the patient's medical history in a new window. (Gydytojas, pasirinkęs pacientą, naujame lange mato jo ligos istoriją.) |
| **Pre-condition** | Doctor is logged in to the system (Gydytojas prisijungęs prie sistemos) |
| **Actor** | Doctor (Gydytojas) |
| **Related use cases** — **Extending UCs** | UC Manage diagnosis (PA Valdyti diagnozę); UC Manage treatment plan (PA Valdyti gydymo planą) |
| **Related use cases** — **Included UCs** | UC View patient list (PA Peržiūrėti pacientų sąrašą) |
| **Related use cases** — **Specializing UCs** | |
| **Post-condition:** | Patient's medical history has been viewed (Paciento ligos istorija peržiūrėta) |

---

## Slide 27 — Generating Magic Reports (Magic ataskaitos generavimas)

**Magic ataskaitos generavimas** — Generating Magic Reports

- If we correctly describe all UC properties in the Magic Systems of Systems Architect tool, we can generate a UC specification document.
- When describing a UC you must fill in the following fields in its Specification:
  - **Documentation** (description / aprašymas)
  - **Goal** (goal / tikslas)
  - **Pre Condition** (pre-condition / prieš sąlyga)
  - **Post Condition** (post-condition / po sąlyga)
  - **Author** (responsible student's initials / atsakingo studento inicialai)
- Instructions for generating the UC specification report and the report template file can be found on Moodle.

---

## Slide 28 — UML 2.5 Diagrams (Recap — Use Case Diagram checked off)

> [Diagram: Same UML 2.5 taxonomy tree as Slide 3. This time the Use Case Diagram box has a green checkmark, indicating it has been covered.]

**UML 2.5 diagramos** — UML 2.5 Diagrams (Use Case Diagram — completed)

```
Diagram
├── Structure Diagram
│   ├── Class Diagram
│   ├── Component Diagram
│   ├── Object Diagram
│   ├── Composite Structure Diagram
│   ├── Deployment Diagram
│   ├── Package Diagram
│   └── Profile Diagram
└── Behavior Diagram
    ├── Activity Diagram
    ├── Use Case Diagram   ← [checked off with green tick]
    ├── State Machine Diagram
    └── Interaction Diagram
        ├── Sequence Diagram
        ├── Interaction Overview Diagram
        ├── Communication Diagram
        └── Timing Diagram
```

---

## Slide 29 — Interface Window Sketches (Sąsajos langų eskizai)

**Sąsajos langų eskizai** — Interface Window Sketches

- You can draw them with any tool.
- If you use Magic to create sketches, the created UIM (User Interface Modeling) diagram can be linked to use cases.

> [Diagram: Screenshot of Magic Systems of Systems Architect's "Create Diagram" dialog showing available diagram types. "User Interface Modeling Diagram" is highlighted in blue under the "Other Diagrams" category. Also visible: Interaction Overview Diagram, Profile Diagram; Analysis Diagrams: Dependency Matrix, Relation Map Diagram, Robustness Diagram; Other Diagrams: Generic Table, Instance Table, Metric Table, Glossary Table, User Interface Modeling Diagram, Content Diagram.]

---

## Slide 30 — Coffee Vending Machine Information System — Description 1

**Kavos pardavimo automatų informacinė sistema – aprašas 1** — Coffee Vending Machine Information System — Description 1

In the online information system of coffee vending machines, a **buyer** can **view vending machine locations** on a map. Having selected a specific machine, they can **view detailed information** about its location. A buyer can **register** in the online information system and when **logged in**, view a **list of received messages**. A registered buyer receives a discount code via a message, which when entered into the machine when buying coffee, will give a discount. Unnecessary **messages can be deleted**.

The vending machine network **supervisor** can **log in** to the online information system. The supervisor sees a **general list of machines assigned** to him. He can **add a new machine** (the created machine is assigned to the supervisor who created it), **edit** machine information, **remove** a machine from the list.

In the general list it is possible to see the machine's status: a new machine whose status has not been read; a working machine; a working machine but requiring servicing; a non-working machine because it needs servicing; switched off.

---

## Slide 31 — Coffee Vending Machine Information System — Description 2

**Kavos pardavimo automatų informacinė sistema – aprašas 2** — Coffee Vending Machine Information System — Description 2

In the machine status list, the **information system** periodically updates by **polling machines** (at a set time). If during the periodic polling information is received that a machine requires servicing, an **SMS message is sent** to the supervisor.

The supervisor can also at any time when logged in **poll machines** (refresh the general machine list) to get the latest information. Machine servicing is needed: when any required product is running low, when the required number of change coins is running low, when the preventive maintenance deadline is approaching, when the machine's cash box is full, when a malfunction occurs.

Having selected a specific machine, the supervisor can **view detailed status information**: the percentage of remaining stock for all products, the percentage of remaining coins of each denomination, the scheduled maintenance time, the cash box fill percentage, the malfunction code (if one exists).

---

## Slide 32 — Coffee Vending Machine Information System — Description 3

**Kavos pardavimo automatų informacinė sistema – aprašas 3** — Coffee Vending Machine Information System — Description 3

The vending machine network **manager**, having **logged in** to the system, **creates login credentials for supervisors**. The manager can also **view the general list of all machines**, their statuses and **detailed information**. The manager can not only **create**, **edit**, and **remove machines**, but also **assign machines to supervisors**. The manager **sets the periodic machine polling times**.

The manager can **view reports** about machine sales.

In the machine list, having selected one or more machines, the manager can **create a discount** for them, specifying the discount percentage and the period of validity. Information about the discount is **sent via message** to registered buyers, in which each buyer is given a uniquely generated discount code.
