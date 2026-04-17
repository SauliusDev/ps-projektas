# Lecture 04 — Class Diagram

**Course:** Software Systems Analysis and Design Tools (T120B029)

**Topics covered:**
- Overview of the class diagram in the IS development process
- UML 2.5 diagram taxonomy — position of the Class Diagram
- Classes: definition, attributes, operations, and notation
- Relationships between classes: dependency, association, generalization, aggregation, composition
- Association details: cardinality, role names, navigability, dot notation, association class
- Attribute notation: visibility, type, multiplicity, default value, modifiers, derived attributes
- Operation notation: visibility, parameters, direction, return type, properties
- Interface: definition, provided and required interfaces, notation
- When to use a class diagram (requirements, design, implementation phases)
- Domain model (entity classes, <<entity>> stereotype)
- Domain model example (fragment of a quiz/game system)
- Coffee machine information system description (running example)

---

## Slide 1 — Class Diagram (Title Slide)

# KLASIŲ DIAGRAMA

**Class diagram**

---

## Slide 2 — The IS Development Process Being Used

> [Diagram: Activity diagram showing the full IS development process with phases and their artefacts]

**Naudojamas PĮ kūrimo procesas** — The IS Development Process Being Used

Phases and artefacts:

- **Initial requirements description (Pradinis reikalavimų aprašymas)**
  - : Interface prototype (: Sąsajos prototipas)
  - : Initial system description (: Pradinis sistemos aprašas)

- **Requirements specification (Reikalavimų specifikavimas)** ← *highlighted/circled — current focus*
  - Functional requirements : Use Case Diagram (Funkciniai reikalavimai : Panaudojimo atvejų diagrama)
  - Each use case scenario : Activity Diagram (Kiekvieno panaudojimo atvejo scenarijus : Veiklos diagrama)
  - **Domain entities : Class Diagram (Dalykinės srities esybės : Klasių diagrama)** ← *this lecture*
  - Entity states : State Machine Diagram (Esybių būsenos : Būsenų diagrama)

- **Design (Projektavimas)**
  - Logical architecture : Package Diagram (Loginė architektūra : Paketų diagrama)
  - Each use case scenario : Sequence Diagram (Kiekvieno panaudojimo atvejo scenarijus : Sekų diagrama)
  - Project classes : Class Diagram (Projekto klasės : Klasių diagrama)

- **Implementation (Realizavimas)**
  - : Component Diagram (: Komponentų diagrama)
  - : Deployment Diagram (: Diegimo diagrama)
  - : Program code (: Programos kodas)

- **Testing (Testavimas)**
  - : Test plan (: Testavimo planas)
  - : Test report (: Testavimo ataskaita)

---

## Slide 3 — UML 2.5 Diagrams

> [Diagram: UML 2.5 diagram taxonomy tree. Root node: Diagram. Two branches: Structure Diagram and Behavior Diagram. Class Diagram is highlighted with a green border. Activity Diagram and Use Case Diagram are marked with green checkmarks (already covered).]

**UML 2.5 diagramos** — UML 2.5 Diagrams

**Structure Diagram** subtypes:
- **Class Diagram** ← *highlighted (this lecture)*
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram
- Profile Diagram

**Behavior Diagram** subtypes:
- Activity Diagram ✓ *(already covered)*
- Use Case Diagram ✓ *(already covered)*
- State Machine Diagram
- Interaction Diagram (abstract)
  - Sequence Diagram
  - Communication Diagram
  - Interaction Overview Diagram
  - Timing Diagram

---

## Slide 4 — Classes

**Klasės** — Classes

- A class diagram describes the types of objects (classes) in the system and the relationships between them, class attributes, operations, and relationship constraints.

- The purpose of a **Class** is to specify **a classification of objects** and to specify the **Features** that characterize the structure and behavior of those objects.*

- Class features (Features):
  - attributes
  - operations

*[OMG UML 2.5 specification]

---

## Slide 5 — Class Notation

**Klasės vaizdavimas** — Class Notation

> [Diagram: Standard UML class box with three compartments: class name (bold, centred), attributes section, operations section.]

**Standard class notation:**

```
         Klasės vardas
    ─────────────────────────
           attributes
  -atributas : Tipas
    ─────────────────────────
           operations
  +operacija( parametras1 : Tipas, parametras2 : Tipas ) : Tipas
```

**Possible representation styles (Galimi vaizdavimo būdai):**

| Minimal | Partial | Full |
|---------|---------|------|
| Class name only | Name + some attributes/operations | All compartments filled |

Example — minimal:
```
   Window
```

Example — partial (attributes only):
```
         Window
  ───────────────────
  size: Area
  visibility: Boolean
  ───────────────────
  display()
  hide()
```

Example — full:
```
              Window
  ──────────────────────────────
            attributes
  +size: Area = (100, 100)
  #visibility: Boolean = true
  +defaultSize: Rectangle
  -xWin: XWindow
  ──────────────────────────────
            operations
  display()
  hide()
  -attachX(xWin: XWindow)
```

**Class and class object (Klasė ir klasės objektas):**

```
        Asmuo                     jonasj : Asmuo
  ──────────────────        ──────────────────────────
       attributes            gimimoData = "2000.01.01"
  -vardas : String           pavardė = "Jonaitis"
  -pavardė : String          vardas = "Jonas"
  -gimimoData : date
```

*(Object name is underlined; attribute values are shown instead of types)*

---

## Slide 6 — Relationships Between Classes

**Ryšiai tarp klasių** — Relationships Between Classes

- **Dependency (Priklausomybė)**
  - When one object uses the information and/or services of another object.
  - Example: one class uses objects or attributes of another class as arguments of its operations.
  - Notation: dashed arrow `- - - - →`

- **Association (Asociacija)**
  - Notation: solid line `────────────`

- **Generalization (Apibendrinimas)**
  - Notation: solid line with open (hollow) arrowhead `──────▷`

- **Aggregation (Agregavimas)**
  - Notation: solid line with open diamond `──────◇`

- **Composition (Kompozicija)**
  - Notation: solid line with filled diamond `──────◆`

---

## Slide 7 — Association

**Asociacija (association)**

- A class association means that there is a relationship between instances of the classes.
- Association ends have names that indicate the role the corresponding object plays in that relationship.

> [Diagram: Association between class Asmuo (Person) and class Organizacija (Organisation). The association is named "dirba" (works at), with a direction indicator arrow. Role names: "darbuotojas" (employee) on the Asmuo end, "darbovietė" (workplace) on the Organizacija end. Cardinality: 0..* on the Asmuo side, 1 on the Organizacija side.]

Labels explained:
- **Asociacijos vardas** — Association name: `dirba` (works at)
- **Asociacijos kryptis** — Association direction (filled triangle showing reading direction)
- **kardinalumas** — cardinality: `0..*`
- **vaidmuo** — role name: `darbuotojas` / `darbovietė`

---

## Slide 8 — Cardinality (Multiplicity)

**Kardinalumas** — Cardinality

- The cardinality of an association end — the number of relationship instances that an object of one class can have with objects of another class.
- Each A object has a relationship with B object(s):

| Cardinality | Meaning | Type |
|-------------|---------|------|
| `1` | exactly one (one and only one) | mandatory relationship |
| `1..*` | one or more | mandatory relationship |
| `0..1` | no more than one | optional relationship |
| `*` | zero or more | optional relationship |

> [Diagram: Four UML association diagrams between class A and class B showing the four cardinality cases above, each with the multiplicity value circled in red at the B end.]

---

## Slide 9 — Which Diagram Satisfies All These Conditions?

**Kuriai diagramai galioja visos šios sąlygos?** — Which diagram satisfies all of these conditions?

Conditions:
- A subordinate (pavaldinys) may have no more than one manager (vadovas)
- A manager may have no subordinates
- A department (padalinys) may have any number of employees
- A department may be empty
- An employee must necessarily belong to a department

> [Diagram: Three candidate class diagrams (a), (b), (c) showing different cardinality combinations between classes Darbuotojas (Employee) and Padalinys (Department), with a self-association on Darbuotojas for the manager/subordinate relationship.]

**Diagram (a):**
- Darbuotojas self-association: `pavaldinys 0..*` — `vadovas 1` and `* — 0..1` to Padalinys
  - Darbuotojas → Padalinys: `* — 0..1`

**Diagram (b):**
- Darbuotojas self-association: `pavaldinys 0..*` — `vadovas 0..1`
- Darbuotojas → Padalinys: `1..* — 0..1`

**Diagram (c):**
- Darbuotojas self-association: `pavaldinys 0..*` — `vadovas 0..1`
- Darbuotojas → Padalinys: `0..* — 1`

*(Correct answer: **c** — employee must belong to exactly 1 department [1 on Padalinys end], manager is optional [0..1], department may be empty [0..* employees])*

---

## Slide 10 — Association Role Names

**Asociacijos vaidmenų vardai** — Association Role Names

- Recommended to specify so that the meaning of the association is clear.
- **Required** when there is more than one association between the same pair of classes.

> [Diagram (before): Asmuo — Organizacija with no role names, two associations: multiplicities 1—0..* and 0..1—1]

> [Diagram (after): The same Asmuo — Organizacija model with role names added. Two named associations:
> - `direktorius 1 — 0..* darbuotojas` (director — employee)
> - `valdomaĮmonė 0..1 — 1 darbovietė` (managed company — workplace)
> Asmuo attributes: asmensKodas, vardas, pavarde. Organizacija attributes: imonesKodas, ikurimoData.]

---

## Slide 11 — Associations — Examples

**Asociacijos — pavyzdžiai** — Associations — Examples

**Question: What if a company can have many directors?**

> [Diagram (before): Asmuo — Organizacija with `direktorius 1 — 0..* darbuotojas` and `valdomaĮmonė 0..1 — 1 darbovietė`]

> [Diagram (after): Changed to `direktorius 1..* — 0..* darbuotojas` (one-or-more directors per company). The `valdomaĮmonė 0..1 — 1 darbovietė` association remains unchanged.]

*(Changing the cardinality from `1` to `1..*` on the direktorius end models the case where a company may have multiple directors.)*

---

## Slide 12 — Associations — Examples (continued)

**Asociacijos — pavyzdžiai** — Associations — Examples

**Question: What if a company can have many directors, and a director can manage many companies?**

> [Diagram (before): Asmuo — Organizacija with `direktorius 1 — 0..* darbuotojas` and `valdomaĮmonė 0..1 — 1 darbovietė`]

> [Diagram (after): The many-to-many relationship between Asmuo (as director) and Organizacija (as managed company) is resolved by introducing an association class **ValdomaĮmonė** (ManagedCompany). ValdomaĮmonė connects:
> - Asmuo (role: direktorius) with multiplicity `1` on the ValdomaĮmonė side `*`
> - Organizacija (role: valdomaĮmonė) with multiplicity `1` on the ValdomaĮmonė side `*`
> The `darbuotojas 0..* — 1 darbovietė` association between Asmuo and Organizacija remains.]

---

## Slide 13 — Association Class

**Asociacijos klasė** — Association Class

**When there is a many-to-many relationship between classes ("many to many")**

> [Diagram (left): Three-class model with association class ValdomaIlmone linking Asmuo (direktorius, 1) and Organizacija (valdomaĮmonė, 1), both ends with `*`. Separate association `darbuotojas 0..* — 1 darbovietė` between Asmuo and Organizacija.]

> [Diagram (right, equivalent): The ValdomaIlmone association class shown using the dashed-line notation. ValdomaIlmone floats as a class attached by a dashed line to the many-to-many association line between Asmuo (`direktorius *`) and Organizacija (`valdomaĮmonė *`). The `darbuotojas 0..* — 1 darbovietė` link remains. Both forms are semantically equivalent (shown with `=` symbol).]

*(An association class is used when the association itself carries attributes or must be uniquely identified per pair of linked objects.)*

---

## Slide 14 — Attribute

**Atributas** — Attribute

> [Diagram: UML class box named "Klasės vardas" with annotated attributes showing all notation elements]

**Attribute notation elements:**

- **Attribute visibility (Atributo matomumas / visibility):**
  - `private (-)` — private
  - `public (+)` — public
  - `protected (#)` — protected
  - `package (~)` — package

- **Derived attribute (Išvestinis atributas / derived):** prefix `/`

- **Attribute type (Atributo tipas / Type)**

- **Multiplicity of attribute value collection (Atributo reikšmių kolekcijos dydis / multiplicity)**

- **Default value (Reikšmė pagal nutylėjimą / default value)**

- **Modifier (Modifikatorius / modifier):**
  - `id`, `readOnly`, `ordered`, `sequence`, `unique`, `nonunique`, `union`, `redefines`, `subsets`, constraint text

**Example attribute declarations in the class:**

```
         Klasės vardas
  ────────────────────────────────────
              attributes
  -privateAttrib : String
  -/derivedAttrib : Integer
  +publicAttrib : Date{readOnly}
  #protectedAttrib : String [1..*]
  ~packageAttrib : Integer = 5
```

---

## Slide 15 — Attribute vs. Association

**Atributas — asociacija** — Attribute vs. Association

- It is possible to choose how to represent the same relationship:

> [Diagram (left — attribute form): Class Asmuo with attribute `-darbovietė : Organizacija` in the attributes compartment.]

> [Diagram (right — association form): Class Asmuo and class Organizacija connected by a navigable association arrow, with role name `darbovietė` at the Organizacija end.]

Both representations are semantically equivalent (shown with `=` symbol). The choice is a matter of presentation preference.

---

## Slide 16 — Navigability

**Navigability**

> [Diagram: Three rows of equivalent representations — association notation (left) and attribute notation (right).]

**Row 1 — Bidirectional (no arrowheads):**
- Association: `K1 -r1 ──────── -r2 K2`
- Equivalent to: K1 has attribute `-r2 : K2` AND K2 has attribute `-r1 : K1`

**Row 2 — Unidirectional (arrow from K3 to K4):**
- Association: `K3 -r1 ──────→ -r2 K4`
- Equivalent to: K3 has attribute `-r2 : K4`; K4 has no back-reference attribute

**Row 3 — Non-navigable both ends (crossed arrowheads):**
- Association: `K5 -r1 ─×──×─ -r2 K6`
- Equivalent to: K5 and K6 have no navigability attributes defined (navigability explicitly denied in both directions)

---

## Slide 17 — "Dot" Notation

**"Dot" notacija** — "Dot" Notation

- A dot at the association end marks that the end attribute belongs to the class (i.e., is owned by the class at that end).
- If there is no dot — the attribute belongs to the association itself.
- Rarely used.

> [Diagram: Classes G and H connected by an association. Role name `g` with multiplicity `1..4` on the G side (with a dot at G), and role name `h` with multiplicity `2..5` on the H side (with a dot at H). Both ends have dots, indicating both role attributes are owned by their respective classes.]

---

## Slide 18 — Aggregation

**Agregavimas (aggregation)**

- Aggregation means that the "whole" has "part" objects.
  - An aggregation relationship can be replaced by an association where the role names would be, e.g., "composed of" and "belongs to".
- Parts can exist without the whole.
- Parts can belong to several wholes.
- The whole can exist without its parts.

> [Diagram: Class Automobilis (Car) connected to class Ratas (Wheel) with an open diamond (aggregation) at the Automobilis end. Labels: "Visuma" (Whole) pointing to Automobilis, "Agregavimas" (Aggregation) pointing to the diamond, "Dalis" (Part) pointing to Ratas.]

---

## Slide 19 — Composition

**Kompozicija (composition)**

- Composition is a form of aggregation where the part strictly belongs to the whole and its lifecycle is completely dependent on the whole.

> [Diagram 1: Class Pastatas (Building) connected to class Kambarys (Room) with a filled diamond (composition) at the Pastatas end. A room cannot exist without the building.]

> [Diagram 2: Three-class chain — Universitetas (University) ◆→ Padalinys (Department) ◇→ Dėstytojas (Lecturer). University–Department is composition (filled diamond); Department–Lecturer is aggregation (open diamond). A department cannot exist without the university, but a lecturer can exist without a department.]

---

## Slide 20 — Generalization / Inheritance

**Apibendrinimas / paveldėjimas (generalization)**

- The relationship between a specific class (subclass) and a generalized class (superclass), where the subclass inherits all features of the superclass (attributes, relationships, and operations), and has its own additional features.

> [Diagram: Superclass Asmuo (Person) with attributes `-vardas` and `-pavardė`. Two subclasses inherit from Asmuo via generalization (hollow triangle arrowhead pointing to Asmuo):
> - Studentas (Student) with attributes `-vidurkis` and `-kursas`
> - Dėstytojas (Lecturer) with attribute `-atlyginimas`
> Labels: "superklasė" pointing to Asmuo, "apibendrinimas" pointing to the generalization arrow, "subklasė" pointing to the subclasses.]

---

## Slide 21 — Example

**Pavyzdys** — Example

- Let us create a class diagram for the game of draughts (checkers).

> [Image: Photograph of a draughts (checkers) board with pieces in play, placed on a wooden bench.]

---

## Slide 22 — Operation

**Operacija** — Operation

- **Operation** is a behavioral **feature** that may be **owned by** an interface, data type, or **class**.
  - An operation may be directly **invoked** on instances of its featuring classifiers.
  - The operation specifies the **name, type, parameters, and constraints** for such invocations.*

*[OMG UML 2.5 specification]

---

## Slide 23 — Operation Notation

**Operacija** — Operation Notation

> [Diagram: UML class box named "Klasė" with annotated operations showing all notation elements]

**Operation notation elements:**

- **Operation visibility (Operacijos matomumas / visibility)**
- **Operation parameter (Operacijos parametras / parameter)**
- **Parameter type (Parametro tipas)**
- **Parameter default value (Parametro reikšmė pagal nutylėjimą / default value)**
- **Return parameter (Grąžinamas parametras / return)**
- **Parameter direction (Parametro kryptis / direction):** `in`, `out`, `inout`, `return`
- **Multiplicity**
- **Properties (Savybės / properties):** `redefines`, `query`, `ordered`, `unique`, `apribojimas (constraint)`

**Example operation declarations in the class:**

```
              Klasė
  ───────────────────────────────────────────────────────────
                        operations
  +publicOperation( param1 : String, inout param2 : Integer=1 )
  -privateOperation() : Boolean [0..*]
  #protectedOperation( array : Asmuo [1..*], out parameter : date )
  ~packageOperation(){query}
```

---

## Slide 24 — Interface

**Interfeisas** — Interface

- An Interface represents a declaration of a set of public features and obligations.
  - An Interface specifies a contract; any instance of a Classifier that realizes the Interface shall fulfill that contract.*

*[UML 2.5 specification]

> [Diagram (lollipop notation): Circle labelled "Interfeisas" (ball/lollipop icon)]

> [Diagram (expanded notation — equivalent forms):
> Left: Interface shown as a class box with stereotype, named "Interfeisas", operations compartment with `+operacija()`
> Right: Full example interface `«interface» Pageable`:
> - `+ UNKNOWN_N_OF_PAGES: int = -1`
> - `+ getNumberOfPages(): int`
> - `+ getPageFormat(int): PageFormat`
> - `+ getPrintable(int): Printable`
> ]

---

## Slide 25 — Interface Notation

**Interfeiso vaizdavimas** — Interface Notation

> [Diagram (top): Class Klasė connected via a lollipop interface "Interfeisas" to Class Klasė2 — showing the ball-and-socket notation for provided/required interfaces between two classes.]

Classes can have:

**Provided interfaces (teikiami interfeisai):**
- Connected via **interface realization** relationship
- Notation (lollipop): `Klasė ──○ Interfeisas`
- Equivalent expanded notation: `Klasė ─ ─ ▷ Interfeisas ○` (dashed arrow with open arrowhead toward the interface box)

**Required interfaces (reikalaujami interfeisai):**
- Connected via **dependency** relationship
- Notation (socket): `Klasė ──( Interfeisas2`
- Equivalent expanded notation: `Klasė ─ ─ «use» ─→ Interfeisas2 ○` (dashed arrow with `«use»` stereotype toward the interface box)

---

## Slide 26 — When Is a Class Diagram Used?

**Kada naudojama klasių diagrama?** — When Is a Class Diagram Used?

- **Requirements phase** — to model the subject domain (*domain*).
- **In the design (project)** — to describe high-level software classes and components (data entity classes, business logic classes, interface classes…).
- **Implementation phase** — to describe software classes in maximum detail, from which code can be generated.
- ….

---

## Slide 27 — Domain Model

**Dalykinės srities modelis** — Domain Model

- For domain model classes (entities) we will use the `<<entity>>` stereotype.
- Entities are also called passive classes, because they themselves do not initiate the execution of actions.
- We can identify entities by analysing use case descriptions.
  - Nouns frequently become entities or attributes.
- There must be mutual consistency between the use case descriptions and the entity class model.

---

## Slide 28 — Domain Model Example (Fragment)

**Dalykinės srities modelio pavyzdys (fragmentas)** — Domain Model Example (Fragment)

> [Diagram: A comprehensive UML class diagram (domain model fragment) for what appears to be a children's educational game/quiz system. All classes use the <<entity>> stereotype (orange circle icon). Full diagram contents below.]

**Classes and their attributes:**

**«enumeration» Žaidimo būsenos** (Game States)
- enumeration literals: juodraštis (draft), aktyvus (active), nenaudojamas (inactive)

**Klausimas** (Question) — entity
- `-tekstas : String`
- `-paveiksliukas : String`

**Atsakymas** (Answer) — entity
- `-tekstas : String`
- `-pirmas_paveiksliukas : String`
- `-antras_paveiksliukas : String`
- `-ar_teisingas : Boolean`
- `-paveiksliuko aprašymas : String`

**Žaidimas** (Game) — entity
- `-pavadinimas : String`
- `-aprašymas : String`
- `-sukūrimo_data : date`
- `-redagavimo_data : date`
- `-būsena : Žaidimo būsenos`

**Šablonas** (Template) — entity
- `-pavadinimas : String`

**Žaidimo rezultatas** (Game Result) — entity
- `-žaidimo_vertė : Integer`
- `-žaidimo_rezultatas : Integer`
- `-žaidimo_data : date`

**Vaiko žaidimai** (Child's Games) — association class (dashed link)

**Pacientas** (Patient) — entity *(no attributes shown)*

**Tėvai** (Parents) — entity *(no attributes shown)*

**Vaikas** (Child) — entity
- `-vardas : String`
- `-pavardė : String`
- `-lytis : String`
- `-gimimo_data : date`
- `-nuotrauka : String`
- `-sukūrimo_data : date`

**Komentaras** (Comment) — entity
- `-komentaro_tekstas : String`
- `-data : date`

**Specialistas** (Specialist) — entity *(no attributes shown)*

**Vartotojas** (User) — entity
- `-vardas : String`
- `-pavardė : String`
- `-slaptažodis : String`
- `-el_pastas : String`
- `-paskutinis_prisijungimas : date`
- `-nuotrauka : String`

**Relationships (associations and compositions):**
- Klausimas `1` — `-žaidimo klausimas 1..*` — Žaidimas (a game has 1..* questions, a question belongs to 1 game)
- Klausimas `1` — `-klausimo atsakymo variantas 1..*` — Atsakymas (a question has 1..* answer options)
- Žaidimas `0..*` — `-žaidimo šablonas 1` — Šablonas (a game is created from 1 template; a template can be used for 0..* games): `kuriamas pagal ►`
- Žaidimas `0..*` — `-specialisto sukurtas žaidimas` — Specialistas (a specialist creates 0..* games): `kuria ►`
- Žaidimo rezultatas `0..*` — `-vaiko žaidimo rezultatas ◄ turi` — Vaiko žaidimai
- Vaiko žaidimai — association class connecting Žaidimas `0..*` and Vaikas `0..*` via dashed line: `priklauso ◄`
- Vaikas `-vaikas 0..1` — Vaiko žaidimai `1`
- Specialistas `1` — `-žaidimo kūrėjas / -specialistas 1` — Vartotojas (specialist is a user): generalization down-arrow
- Specialistas `1..*` — `-vaikui priskirtas specialistas` — Pacientas
- Specialistas `0..*` — `-priskiria ►` — Vaiko žaidimai
- Pacientas `1` — Tėvai `1` — `-tėvo vaikas 1..*` — Vaikas
- Vaikas `-vaiko žaidimo komentaras 0..*` — Komentaras
- Vartotojas — Vaikas: `rašo ►` (`-vartotojo parašytas komentaras 0..*` — Komentaras)

---

## Slide 29 — UML 2.5 Diagrams (Progress Update)

> [Diagram: Same UML 2.5 diagram taxonomy tree as Slide 3, now with Class Diagram also marked with a green checkmark, in addition to Activity Diagram and Use Case Diagram.]

**UML 2.5 diagramos** — UML 2.5 Diagrams — Progress

Diagrams covered so far (marked with ✓):
- **Class Diagram** ✓ *(this lecture)*
- **Activity Diagram** ✓ *(previous lecture)*
- **Use Case Diagram** ✓ *(previous lecture)*

Remaining to cover:
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram
- Profile Diagram
- State Machine Diagram
- Sequence Diagram
- Communication Diagram
- Interaction Overview Diagram
- Timing Diagram

---

## Slide 30 — Coffee Machine Information System Description

**Kavos automatų informacinės sistemos aprašas** — Coffee Machine Information System Description

*(This is a running case study used throughout the course for practical exercises.)*

In the coffee vending machine online information system, a **buyer** (pirkėjas) can view the locations of machines on a map. By selecting a specific **machine** (automatas), they can view detailed information about its installation location. A buyer can register in the online information system and, after logging in, view a list of received **messages** (žinutės). A registered buyer receives a discount code via message, which when entered into the machine when buying coffee, will give a discount. Unnecessary messages can be deleted.

A **supervisor** (prižiūrėtojas) of the machine network can connect to the online information system. The supervisor sees a general list of machines assigned to them. They can add a new machine (a created machine is assigned to the supervisor who created it), edit machine information, and remove a machine from the list.

In the general list, the **machine status** (automato būklė) can be seen: new machine whose status has not yet been read; working machine; working, but maintenance required; not working, maintenance required; switched off.

The information system updates the machine status list periodically by polling the machines (at a set time). If during the periodic poll information is received about required maintenance for a machine, an **SMS message** is sent to the supervisor.

The supervisor can also connect at any time to poll the machines (update the general machine list) to get the latest information. Machine maintenance is required when: any required product stock runs out; required change coin count runs out; scheduled maintenance time approaches; machine cash box fills up; a fault occurs.

By selecting a specific machine, the supervisor can view **detailed information about its status**: percentages of all product stocks, percentages of each coin denomination remaining, scheduled maintenance time, percentage of cash box fill, fault code (if any).

The machine network **administrator** (valdytojas), upon connecting to the system, creates login credentials for supervisors. The administrator can also view the general list of all machines, their status, and detailed information. The administrator can not only create, edit, and delete machines, but also assign machines to supervisors. The administrator sets the periodic machine **polling times** (apklausos laikų).

The administrator can view reports on machine sales.

From the machine list, by selecting one or more machines, the administrator can create a **discount** (nuolaidą) for them, specifying the discount percentage and the period of application. Information about the discount is sent via message to registered buyers, in which a unique discount code generated for each buyer is provided.
