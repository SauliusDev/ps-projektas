# Lecture 01 — Modelling and UML

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Lecturer:** L. Čeponienė
**Institution:** Kaunas University of Technology (KTU)

**Topics covered:**
- What is a model and why modelling is needed
- Techniques for managing problem complexity (abstraction, decomposition, projection, structuring)
- UML — definition, purpose, and scope
- UML 2.5 diagram taxonomy (Structure Diagrams vs. Behaviour Diagrams)
- When UML is and is not appropriate (Hello World and CORAL examples)
- Software development process types (Waterfall, Iterative, Agile, RUP/UP)
- Course project process structure and deliverables (3 project submissions)
- Example system introduction: Coffee Vending Machine Information System

---

## Slide 1 — Modelling and UML (Title Slide)

**Modeliavimas ir UML**
*(Modelling and UML)*

Lecturer: L. Čeponienė

KTU

---

## Slide 2 — Paysera Example

> [Diagram: Left side — a UML State Machine Diagram showing transaction/payment states: **waiting** → (Accepted on web page) → decision "Is enough funds?"; No branch → **waiting_funds** (incoming funds); Yes branch → decision "Are all beneficiaries registered?"; No branch → **waiting_registration** (Beneficiary registered); Yes branch → decision "Is some password pending?"; Yes branch → **waiting_password** (Password provided); No branch → **reserved**. Blue arrows indicate state changes initiated by using the API. Note: **done** and **canceled** statuses are available only for payments. Up to these states, all payments in the same transaction have the same status as the transaction itself.]

> [Diagram: Right side — Two combined diagrams. (1) A UML State Machine Diagram titled "Transaction and payment statuses" with states: **create** → (API: create transaction) → **new** → (after 1 month) → **deleted**; **new** → (Accept payment) → states for **waiting**, **waiting_funds**, **waiting_registration**, **waiting_password**, **reserved**, **confirmed**, **freezeUntil**, **done**, **canceled**; API: delete payment leads to **canceled**. (2) A UML Class Diagram with the following classes and attributes:]

**Class: Transaction**
- transaction_key: string
- created_at: int
- status: string
- type: string
- wallet: int
- confirmed_at: int
- correlation_key: string
- payments: Payment[]
- allowance: TransactionAllowance
- reserve_for: int
- reserve_until: int
- use_allowance: bool
- suggest_allowance: bool
- auto_confirm: bool
- redirect_uri: string
- callback_uri: string
- user: UserInformation

**Class: UserInformation**
- email: string

**Class: Password**
- type: string
- value: string
- status: string

**Class: Wallet**
- id: int
- owner: int

**Class: TransactionAllowance**
- id: int
- data: Allowance
- optional: bool

**Class: WalletIdentifier**
- id: int
- email: string
- phone: string

**Class: Allowance**
- id: int
- transaction_key: string
- created_at: int
- status: string
- wallet: int
- *(additional attributes partially visible)*

**Class: Limit**
- max_price: int
- period: int

**Class: Payment**
- id: int
- transaction_key: string
- created_at: int
- status: string
- price: int
- currency: string
- cashback: int
- wallet: int
- confirmed_at: int
- freeze_for: int
- freeze_until: int
- description: string
- items: Item[]
- beneficiary: WalletIdentifier
- password: Password
- parameters: mixed

**Class: Item**
- title: string
- description: string
- image_uri: string
- price: int
- currency: string
- quantity: int
- parameters: mixed

Relationships shown:
- Transaction has association `user` → UserInformation
- Transaction has association `payments` → Payment (1 to many)
- Transaction has association `allowance` → TransactionAllowance
- TransactionAllowance `<< related to >>` Allowance
- Allowance `<< related to >>` WalletIdentifier
- Payment has association `password` → Password
- Payment has association `beneficiary` → WalletIdentifier
- Payment has association `items` → Item
- Wallet has association `allowance` ← Allowance
- Allowance has association `limits` → Limit
- Transaction `rejects` → Allowance

**Info notes from slide:**
- Blue arrows indicate state changes initiated by using API
- `done` and `canceled` statuses are available only for payments. Up to these states, all payments in the same transaction have the same status as the transaction itself

---

## Slide 3 — Why Is Modelling Needed?

**Model — a simplification of reality**

**Modelling helps to:**
- Understand what questions need to be asked
- Discover problems
- Make key design decisions
- Demonstrate important decisions without superfluous detail
- Document decisions that have been made

**Key question: What matters more — the modelling process, or the result of that process?**

---

## Slide 4 — Problem Complexity and Modelling

**Abstraction** — we ignore details in order to see the big picture
- But... every abstraction is a choice between what is important and what is not

**Decomposition** — we break the problem into smaller, independent parts
- But... very rarely will the separate parts truly be independent

**Projection** — we separate different projections and describe each one individually
- But... different projections will frequently be mutually inconsistent

**Structuring** — we form a stable structure in order to localise changes
- But... any given structure will make some changes easier and others harder

---

## Slide 5 — UML

**A language intended for software system artifact:**
- Visualisation
- Specification
- Construction
- Documentation

> "The objective of UML is to provide system architects, software engineers, and software developers with tools for analysis, design, and implementation of software-based systems"
> [OMG UML 2.5 specification]

---

## Slide 6 — UML 2.5 Diagrams

> [Diagram: UML 2.5 diagram taxonomy — a hierarchy tree with the following structure:]

```
Diagram
├── Structure Diagram
│   ├── Class Diagram
│   ├── Component Diagram
│   ├── Object Diagram
│   ├── Composite Structure Diagram
│   │   └── Profile Diagram
│   ├── Deployment Diagram
│   └── Package Diagram
└── Behavior Diagram
    ├── Activity Diagram
    ├── Use Case Diagram
    ├── State Machine Diagram
    └── Interaction Diagram
        ├── Sequence Diagram
        ├── Interaction Overview Diagram
        ├── Communication Diagram
        └── Timing Diagram
```

---

## Slide 7 — When Is UML Needed? Hello, World!

Source: http://umlguide2.uw.hu/

**Java source code shown:**
```java
import java.awt.Graphics;

class HelloWorld extends java.applet.Applet {

  public void paint (Graphics g) {

    g.drawString("Hello, World!", 10, 10);

  }
}
```

> [Diagram: Multiple UML diagrams are shown for the HelloWorld applet, illustrating that even a trivial program can be described with many diagram types:]

> [Diagram 1 — Class Diagram (Object Diagram): Shows class `HelloWorld` with method `paint()`, linked by a dashed arrow to a note element `g.drawString("Hello, World!", 10, 10)`. Also shows `Applet` ← (inheritance) `HelloWorld` with `paint()`, linked by dashed arrow to `Graphics`.]

> [Diagram 2 — Package Diagram: Shows packages: `java` containing `applet`, which is linked by dashed dependency to `awt`, which is linked to `lang`. `HelloWorld` has a dashed dependency to `applet`.]

> [Diagram 3 — Class/Inheritance Diagram: Shows inheritance chain: `Object` → `Component` → `Container` → `Panel` → `Applet` → `HelloWorld`. Also shows `ImageObserver` interface connected with a lollipop to `Component`.]

> [Diagram 4 — Sequence Diagram: Shows lifelines `root : Thread`, `: Toolkit`, `: ComponentPeer`, `target : HelloWorld`. Messages: `run` from `root` to itself (activation bar), then `run` to `: Toolkit`; `: Toolkit` calls `callbackLoop` on itself, then `handleExpose` to `: ComponentPeer`, then `paint` to `target : HelloWorld`.]

> [Diagram 5 — Deployment/Artifact Diagram: Shows `HelloWorld` class with `«manifest»` relationship to artifact `«artifact» HelloWorld.class`; `HelloWorld.class` has `«manifest»` relationship to `hello.java` (source file). Also shown: `hello.html` (document icon) with dashed arrows to `HelloWorld.class` and `hello.jpg` (image icon).]

---

## Slide 8 — When Is UML Needed? CORAL

**CORAL** (COmmon Relational Abstraction Layer) — one of the software infrastructure components used for data storage and retrieval at the Large Hadron Collider (CERN).

Source: http://home.cern/

> [Diagram: An extremely large and detailed UML Class Diagram for the CORAL system. It shows dozens of interfaces and classes with their attributes and methods, and numerous associations between them. Key elements visible include:]

**Selected classes/interfaces visible in diagram:**
- `IRelationalDomain` — availableTechnologies(): vector\<string\>, ..., implementationOf(technologyName: string): IRelationalDomain, ..., domainName: string, implementationName: string, ...
- `IRelationalService`
- `IConnectionService` (facade object)
- `IConnection` — canJoinPhysicalConnection(): bool, ..., serverVersion: string, ..., newSession(schemaName: string, mode: AccessMode): ISession
- `ITransaction` — startUserSession(): bool, startTableSession(schema: ISchema), isActive(): bool, ..., rollback()
- `ISession` — nominalSchema(): ISchema, ..., startUserSession(): string, password: string, ...
- `ITypeConverter`
- `IConnectionServiceConfiguration`
- `IWebCache`
- `IMonitoringService`
- `IMonitoringReporter`
- `IMsgCache`
- `ITableCacheServiceSet`
- `INegotiationAlgorithm`
- `ITableServiceDescription`
- `ISchema` — tableList(): set, ..., createTable(tableName: string, description: ITableDescription): ITable, dropTable(tableName: string): bool, ..., existsTable(tableName: string): bool
- `ITableEditor` — insertRow(buffer: AttributeList, newCacheSize: int, IbulkOperation), dropTable(tableName: string), ..., getRows(condition: string, inputData: AttributeList, dataTypes: ..., IbulkOperation), setRowsCondition(string, coordinates: AttributeList()), bulkOperation(): IbulkOperation
- `IView`
- `IPrivilegeManager`
- `IQuery` — defineOutput(typedAttributeName: string, aliasTypeName: string), execute(): ICursor
- `ICursor` — next(): bool, currentRow(): AttributeList
- `IQueryDefinition` — addToTableList(string, alias: string), setCondition(string, alias), setDistinct(string), ..., limitReturnedRows(maxRows: int)
- `IOperationWithQuery`
- `IBulkOperation`
- `ITable` — description(): ITableDescription, dataEditor(): ITableEditor, ..., numberOfRows(): int, numberOfOffsetting(): int, ..., foreignKeys: IForeignKey[], primaryKey: IKey, indices: Index[]
- `ITableDescription` — name(): string, type(): string, ..., tableSpaceName(): string, ..., columnDescription(columnName: string): IColumn, numberOfColumns(): int, numberOfPrimaryKeyColumns(): int, hasPrimaryKey(): bool, ..., numberOfForeignKeyConstraints(): int, numberOfUniqueConstraints(): int, addConstraint(constraint: IUniqueConstraint)
- `TableDescription` — setName(tableName: string), setTableSpaceType(string), ...
- `IColumn` — name(): string, tableName(): string, columnType(): string, isNotNull(): bool, isNullable(): bool, tableSpaceName(): string
- `IPrimaryKey` / `IForeignKey` — columnNames(): vector\<string\>, ...
- `Index` — columnNames(): vector\<string\>, ...

*(Note: The diagram is dense and contains many more attributes and methods than can be fully enumerated here. It represents a real-world production-scale UML Class Diagram.)*

---

## Slide 9 — Development Processes

> [Diagram: Top-right — Waterfall cascade diagram with phases in descending steps: **Definition (Apibrėžimas)** → **Specification (Specifikavimas)** → **Design (Projektavimas)** → **Implementation (Realizavimas)** → **Testing (Testavimas)** → **Deployment (Diegimas)** → **Maintenance (Priežiūra)**]

> [Diagram: Bottom-left — RUP (Rational Unified Process) diagram showing disciplines (Business Modeling, Requirements, Analysis & Design, Implementation, Test, Deployment, Configuration & Change Management, Project Management, Environment) plotted over time across phases (Inception, Elaboration, Construction, Transition) and iterations (Preliminary Iteration(s), Iter. #1, Iter. #2, Iter. #n+1, Iter. #n+2, Iter. #m, Iter. #m+1), with the intensity of each discipline shown as a bell-curve-shaped band.]

> [Diagram: Bottom-right — Scrum process diagram showing: Product Backlog (Stories: Create account, Book reservation, Print report, Login, Search) → Sprint Backlog (Sprint Backlog cards: Create Permit, Approve Permit, Cancel Permit) → 2-week Sprint cycle (24 hrs / Daily Scrum loop) → Potentially Shippable Product Increment (represented by gold bar icon)]

**Development process types:**
- **Waterfall**
- **Iterative** (evolutionary, incremental, ...)
- **Agile-type processes:** XP, Scrum, Kanban, ...
- **RUP (UP)**
- **...**

Sources:
- http://www.agilenutshell.com/scrum
- https://www.ibm.com/developerworks/rational/library/4763.html

---

## Slide 10 — Which Process Will We Use?

> [Diagram: An activity diagram (flowchart) showing the course project process with three coloured groupings corresponding to the three project submissions:]

**Project Submission No. 1** (blue outline):

- Activity: **Initial requirements description (Pradinis reikalavimų aprašas)**
  - Output: `: Interface prototype (Sąsajos prototipas)`
  - Output: `: Initial system description (Pradinis sistemos aprašas)`
- Decision point →
- Activity: **Requirements specification (Reikalavimų specifikavimas)**
  - Output: `Functional requirements : Use Case Diagram (Panaudojimo atvejų diagrama)`
  - Output: `Each use case scenario : Activity Diagram (Veiklos diagrama)`
  - Output: `Domain entities : Class Diagram (Klasių diagrama)`
  - Output: `Entity states : State Machine Diagram (Būsenų diagrama)`

**Project Submission No. 2** (red outline):

- Activity: **Design (Projektavimas)**
  - Output: `Logical architecture : Package Diagram (Paketų diagrama)`
  - Output: `Each use case scenario : Sequence Diagram (Sekų diagrama)`
  - Output: `Project classes : Class Diagram (Klasių diagrama)`

**Project Submission No. 3** (green outline):

- Activity: **Implementation (Realizavimas)**
  - Output: `: Component Diagram (Komponentų diagrama)`
  - Output: `: Deployment Diagram (Diegimo diagrama)`
  - Output: `: Program code (Programos kodas)` *(highlighted in red as required)*
- Activity: **Testing (Testavimas)**
  - Output: `: Test plan (Testavimo planas)`
  - Output: `: Test report (Testavimo ataskaita)`

*(Diagram ends with a final end node.)*

---

## Slide 11 — Example System

During lectures, we will create Magic diagrams specifying the example system.

---

## Slide 12 — Coffee Vending Machine Information System — Description 1

In the coffee vending machine online information system, a buyer can view vending machine installation locations on a map. Having selected a specific machine, they can view more detailed information about its location. The buyer can register in the online information system and, once logged in, view a list of received messages. A registered buyer receives a discount code via message, which, when entered into the machine when buying coffee, will give a discount. Unnecessary messages can be deleted.

A vending machine network supervisor can connect to the online information system. The supervisor sees the general list of machines assigned to them. They can add a new machine (the created machine is assigned to the supervisor who created it), edit machine information, and remove a machine from the list.

In the general list it is possible to see the machine status: a new machine whose status has not been read; an operating machine; operating but requiring service; not operating because service is required; switched off.

---

## Slide 13 — Coffee Vending Machine Information System — Description 2

The information system periodically updates the machine status in the list by polling the machines (at a set time). If during the periodic poll information is received that a machine requires service, an SMS message is sent to the supervisor.

The supervisor can also connect at any time and poll the machines (refresh the general machine list) to get the most up-to-date information. Machine service is required: when the remaining stock of any required product is running out; when the stock of required denominations of coins for change is running out; when a scheduled maintenance deadline is approaching; when the machine's cash box is full; when a fault has occurred.

Having selected a specific machine, the supervisor can view detailed information about its status: the stock percentage of all products, the percentage of remaining coins of each denomination available, the scheduled maintenance time, the cash box fill percentage, the fault code (if any).

---

## Slide 14 — Coffee Vending Machine Information System — Description 3

The vending machine network administrator, upon logging into the system, creates login credentials for supervisors. The administrator can also view the general list of all machines, their status, and detailed information. The administrator can not only create, edit, and remove machines, but also assign machines to supervisors. The administrator sets the periodic machine polling times.

The administrator can view reports on vending machine sales.

Having selected one or more machines from the machine list, the administrator can create a discount for them, specifying the discount percentage and the period of application. Information about the discount is sent by message to registered buyers, in which a unique discount code generated for each buyer is provided.
