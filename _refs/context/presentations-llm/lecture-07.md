# Lecture 07 — Sequence Diagram

**Course:** Software Systems Analysis and Design Tools (T120B029)

**Topics covered:**
- The software development process context and the role of the Design phase
- Interaction (Interaction) diagrams — types and concepts
- Sequence Diagram — definition and purpose
- Main elements of a sequence diagram: Lifeline, Message, Interaction fragment
- Lifeline and Execution (activation bar)
- Message types: synchronous call, reply, asynchronous, create, delete, lost, found, message to self, recursive
- SynchCall message in detail — relationship to class diagrams
- Combined fragment — operator, operand, guard condition
- Combined fragment operator types: alt, opt, loop, par, and others
- Interaction use fragment (ref operator)
- Worked examples: Cancel Flight, Remove User, Remove Article
- UML 2.5 diagram taxonomy (progress overview — diagrams covered so far)
- Conventions for laboratory work (when to show/omit reply messages)
- Project class diagram — relationship between sequence diagrams and class operations

---

## Slide 1 — Software Development Process in Use

> [Diagram: Activity diagram showing the IS (Information System) development process. The flow proceeds through the following stages, each with associated artefacts:]

**Pradinis reikalavimų aprašymas** (Initial Requirements Description)
- : Sąsajos prototipas (: Interface Prototype)
- : Pradinis sistemos aprašas (: Initial System Description)

**Reikalavimų specifikavimas** (Requirements Specification)
- Funkciniai reikalavimai : Panaudojimo atvejų diagrama (Functional requirements : Use Case Diagram)
- Kiekvieno panaudojimo atvejo scenarijus : Veiklos diagrama (Each use case scenario : Activity Diagram)
- Dalykinės srities esybės : Klasių diagrama (Domain entities : Class Diagram)
- Esybių būsenos : Būsenų diagrama (Entity states : State Machine Diagram)

**Projektavimas** (Design) — *highlighted with a blue circle*
- Loginė architektūra : Paketų diagrama (Logical architecture : Package Diagram)
- Kiekvieno panaudojimo atvejo scenarijus : Sekų diagrama (Each use case scenario : Sequence Diagram)
- Projekto klasės : Klasių diagrama (Project classes : Class Diagram)

**Realizavimas** (Implementation)
- : Komponentų diagrama (: Component Diagram)
- : Diegimo diagrama (: Deployment Diagram)
- : Programos kodas (: Program Code)

**Testavimas** (Testing)
- : Testavimo planas (: Test Plan)
- : Testavimo ataskaita (: Test Report)

---

## Slide 2 — Section Title: Sequence Diagram

**Sekų diagrama**

SEQUENCE DIAGRAM

---

## Slide 3 — Interaction Diagrams

**Interaction** — behaviour composed of a set of messages exchanged between objects playing particular roles in order to achieve a particular goal.

Types of Interaction diagrams:
- **Sequence diagrams** (*Sequence diagrams*) — most commonly used
- Communication diagrams (*Communication diagrams*)
- Timing diagrams (*Timing diagrams*)
- Interaction overview diagrams (*Interaction overview diagrams*)

---

## Slide 4 — Main Elements of a Sequence Diagram

Lifeline (*Lifeline*)

Message (*Message*)

Interaction fragment (*Interaction fragment*):
- *occurrence* — event of sending or receiving a message
- *execution* — activation, when an object is executing an action
- *state invariant* — state invariant
- *combined fragment* — fragment that has a control operator
- *interaction use* — use of another interaction diagram

---

## Slide 5 — Lifeline (*Lifeline*) and Execution Bar (*Execution*)

A Lifeline represents a participant in the interaction (object: Class).

Most often objects live for the entire duration of the interaction, but they can be created and destroyed.

An Execution bar (activation bar) means that the object is in an active state — it is executing an action or waiting for an event.

> [Diagram: Left side shows two lifelines — `: Aktorius` (: Actor, with stick-figure icon) and `: Klasė` (: Class) — displayed as boxes with dashed vertical lines below them (basic lifeline notation with no messages). Right side shows the same two lifelines (`: Aktorius` and `: Klasė`) with a synchronous message labelled `1:` sent from the Actor to the Class, accompanied by a narrow activation bar (rectangle) on each lifeline indicating execution. A blue arrow highlights the activation bar on the receiving lifeline.]

---

## Slide 6 — Message (*Message*)

*The semantics of a complete Message is simply the trace \<sendEvent, receiveEvent\> \**

A Message defines the communication between lifelines.

A Message can be:
- synchronous (the caller waits for a reply)
- asynchronous (the caller does not wait for a reply)
- an operation call or reply
- a signal send
- creation or destruction of a lifeline object

*\*OMG UML 2.5 specification*

---

## Slide 7 — Message Types

> [Diagram: Four UML sequence diagram fragments illustrating different message types:]

**Synchronous call** — shown between `: Aktorius` (: Actor) and `: Klasė` (: Class):
- Solid arrow with filled arrowhead: `pranešimas()` (message()) — **synchronous call**
- Dashed arrow returning: `atsakymas` (reply) — **reply**
- Note: *The calling class waits for a reply only after a SynchCall type message!*

**Asynchronous call / asynchronous signal** — shown between `: Aktorius` and `: Klasė`:
- Open arrow: `asinchroninis pranešimas` (asynchronous message) — **asynchronous call / asynchronous signal**

**Create** — shown for `: Klasė` creating `: Klasė2`:
- Dashed arrow pointing to a new lifeline head: `sukūrimo pranešimas` (creation message) — **create**

**Delete** — shown for a lifeline ending with an X:
- Solid arrow: `sunaikinimo pranešimas` (destruction message) — **delete** (lifeline ends with ×)

---

## Slide 8 — Message Types (continued)

> [Diagram: Three UML sequence diagram fragments illustrating additional message types on `: Klasė` lifelines:]

**Lost message** — a message sent with no receiving end (ends with a filled circle on the lifeline, no target):
- Label: `pranešimas be adresato` (message without a recipient)

**Found message** — a message that arrives from an unknown sender (originates from a filled circle):
- Label: `pranešimas be siuntėjo` (message without a sender)

**Message to self** — a message sent back to the same lifeline object:
- Label: `1: pranešimas()` — arrow loops from the lifeline back to itself — **message to self**

**Recursive message** — a nested self-call on the same activation bar:
- Label: `1: pranešimas()` — arrow loops inward on the same activation box — **recursive message**

---

## Slide 9 — SynchCall Message

Denotes an operation call, after which the calling lifeline waits for a reply message (*Reply*).
- We follow the rule that a reply message must be shown whenever possible, and it is mandatory to indicate what is returned in that message.

If an operation call message is shown in a sequence diagram:
- the class (message receiver) must have such an operation
- there must be a relationship between the classes

> [Diagram left: Sequence diagram showing `: Klasė1` and `: Klasė2` lifelines. Message `1: pranešimas()` (synchronous call) is sent from Klasė1 to Klasė2. Reply `2: atsakymas` (reply) is returned from Klasė2 to Klasė1, shown as a dashed arrow.]

> [Diagram right: Class diagram showing `Klasė1` linked to `Klasė2` with an association. `Klasė2` has a section labelled `operations` containing `+pranešimas()`, confirming the operation exists on the receiver class.]

---

## Slide 10 — Combined Fragment (*Combined fragment*)

Every combined fragment has a control operator and at least one operand with a guard condition (*guard*).

A combined fragment used in a sequence diagram applies to the lifelines it covers.

> [Diagram: Sequence diagram with three lifelines — `: Klasė1`, `: Klasė2`, `: Klasė3`. The flow shows:]
> - `1: pranešimas()` sent from Klasė1 to Klasė2 (synchronous call, activation bar on both)
> - `2: atsakymas` reply returned from Klasė2 to Klasė1
> - A combined fragment box labelled **`opt`** (operator) begins, covering Klasė1 and Klasė2 (operand-covered lifelines — annotated as "Operando apimamos gyvavimo linijos" / Lifelines covered by the operand)
> - Guard condition: `[x>0]` (annotated as "Operando sąlyga" / Operand condition)
> - Inside the opt fragment: `3: pranešimas1()` sent from Klasė1 to Klasė3

Labels in diagram:
- **Operatorius** (Operator) — points to `opt` label in top-left corner of fragment
- **Operando sąlyga** (Operand condition / guard) — points to `[x>0]`
- **Operando apimamos gyvavimo linijos** (Lifelines covered by the operand) — points to the lifelines enclosed in the fragment

---

## Slide 11 — Combined Fragment Operator Types

Most commonly used:
- **alt** — alternative: one of the operands is executed
- **opt** — optional: operand is executed if the guard condition holds
- **loop** — loop / cycle
- **par** — operands execute in parallel

Other operators: break, strict, seq, critical, ignore, consider, assert, neg

---

## Slide 12 — Example (opt with create and delete)

> [Diagram: Sequence diagram with lifelines `: Prince Charming` (Actor, stick-figure icon) and `: Girl`.]
>
> Flow:
> - `1: getName()` — synchronous call from Prince Charming to Girl
> - `2: n=getName()` — reply, the name is returned as `n`
> - **opt** combined fragment begins, guard: `[n=Cinderella]`
>   - Inside opt:
>     - `3:` — delete message sent to Girl (lifeline ends with ×, meaning the Girl object is destroyed)
>     - `4: new Princess(n)` — create message (dashed arrow) to a new lifeline `: Princess`
>
> (The opt block executes only if the name returned equals "Cinderella")

---

## Slide 13 — Operators alt and opt

The **alt** (*alternative*) operator can have more than two operands.

The **opt** (*optional*) operator always has exactly one operand.

> [Diagram left: alt combined fragment showing two lifelines.]
> - Guard `[sąlyga]` (condition): `pranešimas()` call, then `atsakymas` reply
> - Guard `[else]`: `signalas` (signal) sent
>
> [Diagram right: opt combined fragment showing two lifelines.]
> - Guard `[sąlyga]` (condition): `pranešimas()` call, then `atsakymas` reply
> - (Only one operand — executes if condition holds, otherwise nothing)

---

## Slide 14 — Operator loop

> [Diagram: Three variants of the loop combined fragment, each showing two lifelines with `pranešimas()` (call) and `atsakymas` (reply):]

**Variant 1 — Infinite loop:**
- `loop` with guard `[ ]` (empty) — **amžinas ciklas** (infinite loop / eternal cycle)

**Variant 2 — Conditional loop:**
- `loop` with guard `[x>0]` — **ciklo sąlyga** (loop condition): executes while x > 0

**Variant 3 — Fixed repetition count:**
- `loop (10)` with guard `[ ]` — **ciklo kartojimų skaičius** (number of loop repetitions): executes exactly 10 times

---

## Slide 15 — Interaction use Fragment

In a sequence diagram it is possible to use (invoke) another interaction diagram; for this the **ref** operator is used.

> [Diagram: Sequence diagram with lifelines `: Klasė1` and `: Klasė2`.]
> - `1: pranešimas()` — synchronous call from Klasė1 to Klasė2
> - `2: ok` — reply
> - **ref** fragment box (yellow background) labelled **sekų diagrama 1** (sequence diagram 1) — references another sequence diagram
> - `3: pranešimas1()` — continuation message after the ref
> - `4:` — reply

Side note (blue text):
> If in the use case diagram there is an `<<include>>` or `<<extend>>` relationship between use cases, where in sequence diagrams should you use the *ref* operator?

---

## Slide 16 — Examples (Cancel Flight / Remove User)

> [Diagram left: Sequence diagram titled `interaction Atšaukti skrydį` (Cancel Flight) with lifelines:]
> - `: FlightAdministrator` (Actor)
> - `«boundary» : FlightsPage`
> - `«control» : FlightController`
> - `«Entity» : Flight`
>
> Flow:
> 1. `handleCancel()` — FlightAdministrator → FlightsPage
> 2. `cancelation confirmation dialog` — FlightsPage → FlightAdministrator (reply, show dialog)
> - **alt** combined fragment:
>   - `[wants to cancel]`:
>     - 3. `handleConfirmCancel()` — FlightAdministrator → FlightsPage
>     - 4. `cancelFlight()` — FlightsPage → FlightController
>     - 5. `cancelFlightAsync()` — FlightController → Flight
>     - 6. `ok` — Flight → FlightController (reply)
>     - 7. `flight canceled` — FlightController → FlightsPage (reply)
>     - 8. `closed dialog` — FlightsPage → FlightAdministrator (reply)
>   - `[else]`:
>     - 9. `handleCancelCancelation()` — FlightAdministrator → FlightsPage
>     - 10. `closed dialog` — FlightsPage → FlightAdministrator (reply)

> [Diagram right: Sequence diagram titled `interaction Pašalinti naudotoją` (Remove User) with lifelines:]
> - `«Actor» : Admin`
> - `«boundary» : UserDetailedPage`
> - `«control» : UserController`
> - `«Entity» : User`
>
> Flow:
> 1. `clickDelete()` — Admin → UserDetailedPage
> 2. `provideConfirmationPopup()` — UserDetailedPage → UserController
> 3. `serve confirmation` — UserController → UserDetailedPage (reply)
> 4. `serve confirmation popup` — UserDetailedPage → Admin (reply)
> - **opt** combined fragment, guard `[delete user]`:
>   - 5. `clickConfirm()` — Admin → UserDetailedPage
>   - 6. `update()` — UserDetailedPage → UserController
>   - 7. `update()` — UserController → User
>   - 8. `success` — User → UserController (reply)
>   - 9. `user set to deleted` — UserController → UserDetailedPage (reply)
>   - 10. `user set to deleted` — UserDetailedPage → Admin (reply)

---

## Slide 17 — Example: Remove Article (Pašalinti straipsnį)

> [Diagram: Full sequence diagram for use case **Pašalinti straipsnį** (Remove Article) with lifelines:]
> - `: Author` (Actor)
> - `«boundary» : MainView`
> - `«boundary» : UserArticleListView`
> - `«control» : ArticlesController`
> - `«control» : CommentsController`
> - `«Entity» : Article`
> - `«Entity» : Comment`
>
> Flow:
> 1. `openUserArticleWindow()` — Author → MainView
> 2. `openUserArticles()` — MainView → UserArticleListView
> 3. `select()` — UserArticleListView → ArticlesController
> 4. `user's articles` — ArticlesController → UserArticleListView (reply)
> 5. `open()` — UserArticleListView → MainView (reply, opens view)
> 6. `startArticleDeletion()` — Author → MainView
> 7. `confirmation popup` — MainView → Author (reply)
> 8. `deleteArticle()` — Author → MainView
> 9. `delete()` — MainView → ArticlesController
> 10. `deleteRelatedComments()` — ArticlesController → CommentsController
> 11. `delete()` — CommentsController → Comment
> 12. `related comments deleted` — Comment → CommentsController (reply)
> 13. `success` — CommentsController → ArticlesController (reply)
> 14. `delete()` — ArticlesController → Article
> 15. `success` — Article → ArticlesController (reply)
> 16. `select()` — ArticlesController → Article
> 17. `user's articles` — Article → ArticlesController (reply)
> 18. `article list` — ArticlesController → UserArticleListView (reply)
> 19. `refreshed article list` — UserArticleListView → Author (reply)

---

## Slide 18 — UML 2.5 Diagrams (Progress Overview)

> [Diagram: UML 2.5 diagram taxonomy tree. Root node: `Diagram`, split into two branches:]

**Structure Diagram** branch:
- Class Diagram ✓ (covered)
- Component Diagram
- Object Diagram
- Composite Structure Diagram
- Deployment Diagram
- Package Diagram ✓ (covered)
- Profile Diagram

**Behavior Diagram** branch:
- Activity Diagram ✓ (covered)
- Use Case Diagram ✓ (covered)
- State Machine Diagram ✓ (covered)
- Interaction Diagram (sub-branch):
  - Sequence Diagram ✓ (covered — this lecture)
  - Interaction Overview Diagram
  - Communication Diagram
  - Timing Diagram

(Green checkmarks indicate diagrams that have been covered in the course so far.)

---

## Slide 19 — Conventions (for Laboratory Work)

> [Diagram: Two-part sequence diagram showing the "Remove Article" scenario, annotated with conventions:]

**Top part — navigation between views:**
- `: Author` → `«boundary» : MainView` — `1: openUserArticleWindow()`
- `MainView` → `«boundary» : UserArticleListView` — `2: openUserArticles()`
- `UserArticleListView` → `MainView` — `5: open()` (reply)
- `Author` → `MainView` — `6: startArticleDeletion()`

Annotation (blue text and arrow pointing to the dashed reply after `openUserArticles()`):
> **Rodydami navigaciją tarp langų, atsakymo pranešimų nerodome**
> (When showing navigation between views/windows, we do not show the reply messages)

**Bottom part — all other calls:**
- `8: deleteArticle()`, `9: delete()`, `10: deleteRelatedComments()`, `11: delete()`, `12: related comments deleted`, `13: success`, `14: delete()`, `15: success`, `16: select()`, `17: user's articles`, `18: article list`, `19: refreshed article list`

Annotation (blue text and double-headed arrow):
> **Visais kitais atvejais, atsakymo pranešimus privaloma rodyti kiekvienam *SynchCall***
> (In all other cases, reply messages are mandatory for every SynchCall)

---

## Slide 20 — Project Class Diagram

By creating sequence diagrams, we define operations for classes.

> Note (blue text):
> - Are all operations from the class diagram used in the sequence diagrams?
> - Are all operations shown in the sequence diagrams visible in the class diagram?

> [Diagram: Project class diagram with the following classes and their operations:]

**SportView**
- operations:
  - +setEditMode()
  - +modifyVal()
  - +toggleCreateModal()
  - +toggleDeleteModal()
  - +createSport()
  - +deleteSport()
  - +editSport()
  - +renderSports()

**FlagView**
- operations:
  - +setEditMode()
  - +modifyVal()
  - +toggleCreateModal()
  - +toggleDeleteModal()
  - +createFlag()
  - +deleteFlag()
  - +editFlag()
  - +renderFlags()

**DashboardView**
- operations:
  - +selectFlagTab()
  - +selectSportTab()

**DashboardController**
- operations:
  - +openDashboard()
  - +openFlagView()
  - +renderFlag()
  - +renderFlags()
  - +renderSports()

**SportController**
- operations:
  - +GetSports()
  - +PostSport()
  - +PutSport()
  - +DeleteSport()

**FlagController**
- operations:
  - +GetFlags()
  - +PostFlag()
  - +PutFlag()
  - +DeleteFlag()
  - +PutFlag()

**Sport**
- operations:
  - +ToListAsync()
  - +Add()
  - +Entry()
  - +Remove()
  - +FirstOrDefault()

**Flag**
- operations:
  - +ToListAsync()
  - +Add()
  - +Entry()
  - +Remove()

> Associations shown: SportView → DashboardController, FlagView → DashboardController, DashboardView → DashboardController, DashboardController → SportController, DashboardController → FlagController, SportController → Sport, FlagController → Flag.
