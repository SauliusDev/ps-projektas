# Lecture 06 — Architecture, Package Diagram, and Design Model Construction

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Topics covered:**
- The software project development process and the role of the Design phase
- Logical and physical architecture concepts
- UML 2.5 diagram taxonomy (with emphasis on Package Diagram)
- Package Diagram: definition, notation, and representation styles
- Constructing the project model architecture in Magic tool
- RUP Robustness Analysis class stereotypes (boundary, control, entity)
- Robustness Analysis principles — allowed and disallowed relationships
- Key transition points from requirements to design

---

## Slide 1 — Software Project Development Process (PS Development Process Used)

> [Diagram: Activity diagram showing the full software project (PS) development process as a sequential flow with decision diamonds between phases. Each phase box has arrows pointing to artifact boxes on the right. The "Design" (Projektavimas) phase is highlighted with a blue ellipse.]

**Phase: Initial Requirements Description (Pradinis reikalavimų aprašymas)**
- : Interface Prototype (Sąsajos prototipas)
- : Initial System Description (Pradinis sistemos aprašas)

**Phase: Requirements Specification (Reikalavimų specifikavimas)**
- Functional requirements: Use Case Diagram (Funkciniai reikalavimai: Panaudojimo atvejų diagrama)
- Scenario for each use case: Activity Diagram (Kiekvieno panaudojimo atvejo scenarijus: Veiklos diagrama)
- Domain entities: Class Diagram (Dalykinės srities esybės: Klasių diagrama)
- Entity states: State Machine Diagram (Esybių būsenos: Būsenų diagrama)

**Phase: Design (Projektavimas)** ← *highlighted as the current focus*
- Logical architecture: Package Diagram (Loginė architektūra: Paketų diagrama)
- Scenario for each use case: Sequence Diagram (Kiekvieno panaudojimo atvejo scenarijus: Sekų diagrama)
- Project classes: Class Diagram (Projekto klasės: Klasių diagrama)

**Phase: Implementation (Realizavimas)**
- : Component Diagram (Komponentų diagrama)
- : Deployment Diagram (Diegimo diagrama)
- : Program Code (Programos kodas)

**Phase: Testing (Testavimas)**
- : Test Plan (Testavimo planas)
- : Test Report (Testavimo ataskaita)

---

## Slide 2 — Architecture

**Logical (Loginė)**
- *Logical Architecture – conceptual organization of system in layers, packages, major frameworks, classes, interfaces and subsystems\**

**Physical (Fizinė)**
- *Deployment Architecture – allocation of processes to processing units and network configuration\**

**Logical architecture will be represented with a Package Diagram**

\*C.Larman, Applying UML and Patterns

---

## Slide 3 — UML 2.5 Diagrams

> [Diagram: UML 2.5 diagram taxonomy tree. Root node: Diagram. Two child branches: Structure Diagram and Behavior Diagram. Structure Diagram children: Class Diagram (checkmark), Component Diagram, Object Diagram, Composite Structure Diagram, Deployment Diagram, Package Diagram (highlighted with green border/box). Behavior Diagram children: Activity Diagram (checkmark), Use Case Diagram (checkmark), State Machine Diagram (checkmark), Interaction Diagram. Interaction Diagram children: Sequence Diagram, Interaction Overview Diagram, Communication Diagram, Timing Diagram. Profile Diagram is a child of Class Diagram. Checkmarks indicate diagrams already covered. Package Diagram is highlighted as the new diagram being introduced this lecture.]

---

## Slide 4 — Package Diagram (Section Title Slide)

# Paketu diagrama

**PACKAGE DIAGRAM**

---

## Slide 5 — Package (Package)

Intended for grouping model elements.

*A Package is a **namespace** for its members\**

- Has a name
- Can have internal elements
- Can have relationships with external elements:
  - ***dependency***
  - *implementation*
  - *import, access*
  - *merge*

> [Diagram: Two package symbols (folder-shaped boxes). Package A on the left connected to Package B on the right by a dashed arrow (dependency relationship).]

\*OMG UML 2.5 specification

---

## Slide 6 — Representation Styles (Vaizdavimo budai)

> [Diagram: Three equivalent representations of the same package structure shown side by side, connected by "equals" signs (blue bars).
>
> **Left — Nested containment style:** A large package box labeled "Paketas1" containing: Klase1, Klase2, Klase3 (class boxes), and a nested sub-package box "Paketas11".
>
> **Top right — Tree/hierarchy style:** "Paketas1" at the top connected via lines with plus-circle connectors to: Paketas11 (sub-package), Klase2, Klase1, Klase3 (all as children shown spread out horizontally).
>
> **Bottom right — List style (tool view):** A package box labeled "Paketas1" with a contents list: Paketas11 (folder icon), Klase1, Klase2, Klase3 (class icons).]

All three notations represent the same package structure.

---

## Slide 7 — Project Model Construction (Section Title Slide)

# Projekto modelio sudarymas

*(Project Model Construction)*

---

## Slide 8 — Representing Project Architecture with a Package Diagram — Example

> [Diagram: Three packages connected in a left-to-right chain by dashed dependency arrows.
>
> - Package 1: "Naudotojų sąsajos modelis" (User Interface Model)
> - Package 2: "Veiklos logikos modelis" (Business Logic Model)
> - Package 3: "Duomenų modelis" (Data Model)
>
> Dependency arrows: User Interface Model → Business Logic Model → Data Model.]

---

## Slide 9 — Architecture Representation with Package Diagram — Example (Real-World)

*(Slide title: Architektūros vaizdavimo paketu diagrama pavyzdys)*

> [Diagram: A detailed real-world package diagram sourced from uml-diagrams.org showing a layered web application architecture with four main packages and external components:
>
> **Package: web** (top layer)
> - Contains sub-packages: servlets, transformers, exceptions, config
> - Depends on (dashed arrow to): logging (external package, top right)
>
> **Package: business** (second layer)
> - Contains sub-packages: orders, exceptions
> - Note attached: "Provides business and data access logic with distributed transactions support, if needed."
> - Has a provided interface connector (circle on right side)
>
> **Package: plsql** (third layer)
> - Contains sub-packages: datasources, sql_pkgs, helpers, exceptions, config
> - Internal dependency arrows: datasources ← sql_pkgs → helpers → exceptions; config has incoming arrows
> - Depends on (dashed arrow to): ojdbc14.jar, orai18n.jar (external)
> - External: "Oracle 10g JDBC driver" note connected to ojdbc14.jar, orai18n.jar package
>
> **Package: data** (bottom layer)
> - Contains sub-packages: dto, exceptions, types, values
>
> Dependency arrows flow from web → business → plsql, and all layers reference data. The web, business, and plsql packages all have dependency arrows into data.]

---

## Slide 10 — Project Architecture Example (Projekto architekturos pavyzdys) — MVC Example 1

> [Diagram: Package diagram showing an MVC-style architecture with three top-level packages:
>
> **Package: Views** (left)
> - Contains classes (shown with boundary-style icons): CommentFormModal, ConditionForm, Confirmation, Dashboard, DoctorIndex, DoctorShow, Home, LoginForm, MedicamentForm, PatientShow, PostForm, PostIndex, PostShow, RecommendationForm, RecordForm, Statistics, UserForm, UserIndex, UserRegistrationForm
>
> **Package: Controllers** (center, with two nested sub-packages)
> - Sub-package: Admin
>   - Contains: «control» UserController, «control» HomeController (with inheritance arrow between them)
> - Sub-package: Main
>   - Contains: CommentController, ConditionController, DoctorController, MedicamentController, PatientController, PostController, RecommendationController, RecordController
>
> **Package: Models** (right)
> - Contains classes (entity-style icons): Category, Comment, Condition, Doctor, Food, Medicament, Patient, Post, PostComment, Recommendation, Record, User
>
> Relationships: Views --«use»--> Controllers (dashed arrow), Controllers --«use»--> Models (dashed arrow).]

---

## Slide 11 — Project Architecture Example (Projekto architekturos pavyzdys) — MVC Example 2

> [Diagram: Package diagram showing a more complex modular architecture with four functional packages and one model package:
>
> **Package: Core**
> - Sub-package: Pages — contains: MainPage
> - Sub-package: Controls — contains: MainPageControl
> - Pages → Controls (dependency arrow inside package)
>
> **Package: Drive**
> - Sub-package: Pages — contains: DrivePage, TestDriveFormPage
> - Sub-package: Controls — contains: DriveControl, TestDriveFormControl, UserControl
> - Dependency arrow from Pages to Controls
> - Dependency from Core → Drive (dashed)
>
> **Package: User**
> - Sub-package: Pages — contains: EditAccountPage, LoginPage, RegisterPage
> - Sub-package: Controls — contains: EditAccountControl, LoginControl, LogoutControl, RegisterControl
> - Dependency from Pages to Controls
>
> **Package: Vehicle**
> - Sub-package: Pages — contains: AttributeAdministrationPage, AttributeForm, CarAdministrationPage, CarForm, CarListPage, MyCarList, MyCarServiceStatus
> - Sub-package: Controls — contains: AttributeControl, CarControl, CarListControl, MyCarListControl
> - Dependency from Pages to Controls
>
> **Package: Model** (right, standalone)
> - Contains: Attribute, Car, Comment, Image, Issue, IssueType, Manufacturer, Model, New, Part, Payment, Purchase, Reaction, RegisteredUser, Repairmen, SearchCriterion, Service, TestDrive, Upgrade
>
> Dependency arrows: Core → Drive; User and Vehicle depend on Model (dashed arrows right). Core, User, Vehicle, Drive all connect downward/rightward showing layered dependencies.]

---

## Slide 12 — Project Architecture Example (Projekto architekturos pavyzdys) — MVC Example 3

> [Diagram: Package diagram showing two high-level domain packages, each internally structured with MVC sub-packages:
>
> **Package: BookManagement** (left)
> - Sub-package: Views
> - Sub-package: Controllers
> - Sub-package: Models
> - Internal dependencies: Views → Controllers (dependency arrow), Controllers → Models (dependency arrow)
>
> **Package: UserManagement** (right)
> - Sub-package: Views
> - Sub-package: Controllers
> - Sub-package: Models
> - Internal dependencies: Views → Controllers, Controllers → Models
>
> Relationship between packages: BookManagement --→ UserManagement (dashed dependency arrow).]

---

## Slide 13 — Model Structure in the Magic Tool (Modelio struktura Magic irankyje)

> [Diagram: Three side-by-side tree views showing how models from the three project architecture examples above are structured in the Magic (MagicDraw/Cameo) modeling tool's model browser panel:
>
> **Tree 1 — "Projekto modelis"** (corresponding to Example 1 / MVC):
> - Projekto modelis
>   - Controllers
>     - Admin
>     - Main
>   - Models
>   - Views
>   - Architektura (diagram icon)
>   - Projekto klasiu diagrama (diagram icon)
>
> **Tree 2 — "2 Projekto modelis"** (corresponding to Example 2 / modular):
> - 2 Projekto modelis
>   - Core
>   - Drive
>     - Controls
>     - Pages
>     - Drive (diagram icon)
>   - Model
>   - User
>   - Vehicle
>   - Projekto modelis (diagram icon)
>
> **Tree 3 — "Projektas"** (corresponding to Example 3 / domain-partitioned):
> - Projektas
>   - BookManagement
>     - Controllers
>     - Models
>     - Views
>     - BookManagement (diagram icon)
>   - UserManagement
>     - Controllers
>     - Models
>     - Views
>     - UserManagement (diagram icon)
>   - Projektas (diagram icon)]

---

## Slide 14 — RUP Robustness (Robustness) Analysis Class Stereotypes

*(Slide title: RUP robastiskumo (Robustness) analizes klasiu stereotipai)*

> [Diagram: Three UML class stereotypes shown with their graphical icons:
>
> 1. «boundary» — Boundary Class (Ribine klase): shown as a circle with a vertical line on the left side (boundary icon), colored blue/purple
> 2. «control» — Controller (Valdiklis): shown as a circle with a small arrow/line (control icon), colored pink/rose
> 3. «Entity» — Entity (Esybe): shown as a circle with a horizontal line underneath (entity icon), colored orange/brown]

---

## Slide 15 — Robustness Analysis Principles (Robastiskumo analizės principai)

> [Diagram: Two side-by-side groups of allowed and disallowed relationship rules, illustrated with the three robustness stereotypes (actor stick figure, boundary circle, control circle, entity circle):
>
> **ALLOWED RELATIONSHIPS (LEISTINI RYŠIAI)** — shown with green double-headed arrows:
> - Actor ↔ Boundary class
> - Boundary class ↔ Control class
> - Control class ↔ Control class
> - Control class ↔ Entity class
>
> **DISALLOWED RELATIONSHIPS (NELEISTINI RYŠIAI)** — shown with red arrows:
> - Actor → Control class (direct, bypassing boundary) — NOT ALLOWED
> - Actor → Entity class (direct, bypassing boundary and control) — NOT ALLOWED
> - Boundary class → Boundary class — NOT ALLOWED
> - Boundary class → Entity class (direct, bypassing control) — NOT ALLOWED
> - Entity class ↔ Entity class — NOT ALLOWED]

---

## Slide 16 — Key Emphases When Transitioning from Requirements to Design

*(Slide title: Svarbūs akcentai pereinant nuo reikalavimu prie projekto)*

- Transform the required elements of the requirements model into the design model (Tools / Model Transformations / Any to Any)
- Construct the architecture of your own project model
- Create a Sequence Diagram for each Use Case (UC)
  - In the Class Diagram, create the classes that implement that UC (their operations are defined in the Sequence Diagrams)
- Decide on the language — in the design model, the names of classes, attributes, and operations must match those used in the program code

---

## Slide 17 — UML 2.5 Diagrams (Updated — Package Diagram Now Checked)

> [Diagram: Same UML 2.5 diagram taxonomy tree as shown on Slide 3, but now the Package Diagram node also has a green checkmark, indicating it has been covered in this lecture. Diagrams now marked with checkmarks: Class Diagram, Activity Diagram, Use Case Diagram, State Machine Diagram, and Package Diagram. All other diagram types remain unchecked.]
