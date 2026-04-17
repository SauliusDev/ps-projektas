# Lecture 4 — UML Class Diagrams: Structure, Relationships, and Domain Modelling

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Overview of the software development process and where we are in it
- Introduction to structural (static) UML diagrams vs. behavioural diagrams
- What is a class, and how it differs from an object
- Class diagram notation: attributes, operations, visibility
- Association relationships: naming, role names, navigability, multiplicity/cardinality
- Many-to-many associations: intermediate classes and association classes
- Dependency (dashed arrow) relationship
- Aggregation vs. Composition ("consists of" relationships)
- Inheritance (Generalisation)
- Interface notation and realisation relationships
- When to use which diagram element (requirements phase vs. design phase)
- Entity stereotype and domain model class diagrams
- Live modelling exercise: checkers (draughts) game class diagram
- Live modelling exercise: vending machine monitoring system class diagram
- Tool tips: working in MagicDraw/a UML modelling tool
- Assessment information: midterm exam coverage

---

## Course Progress Reminder

**Lina Čeponienė:** I will remind you of the same process we are already working with — you already know it well, but I will go over it again. We have a whole stack of things here, some of which we have already done. That is: the Use Case Diagram — you already know how to draw it and everyone in the labs has at least started. Or I really hope that you have drawn it. The Activity Diagram should also already be sufficiently done for your use cases. So today we will talk about the Class Diagram, and in the next lecture we will talk about the State Diagram, and we will have covered the requirements phase.

After that we will move on to design. So for now we are still talking about requirements, and we have arrived at the Class Diagram — which you already know everything about, right? Well, perhaps you have drawn more of them somewhere else in other modules. Most likely, so now we will only review and clarify certain nuances, and perhaps something new will emerge.

---

## Introduction to Structural Diagrams and Classes

**Lina Čeponienė:** The Class Diagram is one of the branch of diagrams we have not yet touched. Up to now we have been talking about diagrams that describe behaviour — Use Cases and Activity Diagrams are on that side. Now we will talk about structural diagrams — those that describe not how a system behaves, but what its structure is. These are more static in nature.

So let us start with a bit of a digression: since we are talking about the Class Diagram, what is a class? Well, you are probably already in your third year and have already written quite a few classes in code, haven't you?

So, what is a class? An object template — yes, that is a reasonable definition. I call it almost the same thing — I call it an object type. To put it very simply: it is some higher-level type that can have many objects, right? So, that is how we define a class. Our Class Diagram describes those object types, it describes the relationships between them, and what belongs to the class as properties — those are attributes and operations, as well as constraints.

From the UML specification, the formal definition sounds quite similar to what I said. They formally define it the same way. They call it a "classifier" — in English, because it does not translate well into Lithuanian, I intentionally leave it in English so I do not distort the original meaning. The idea is that a class, as an object of attention, can have properties, and those properties are called "features" and features can be of two types: either attributes or operations.

A class can look different ways. The fullest view — when talking about the material — is when we have the class name, then a section where the attributes are listed and labelled as attributes, and a section where the operations are listed and labelled as operations. But the maximum is rarely needed; more often some combination is used.

You can indicate only the class name — that is also sufficient. Or you can show separate sections without the labels, where we distinguish an attribute from an operation by its appearance. And you can show things in more or less detail. We will talk more about what is inside those sections shortly.

---

## Classes vs. Objects

**Lina Čeponienė:** One thing I always want you to be able to distinguish — the difference between a class and an object. As you yourselves said, a class is like an object type. There is also something called an Object Diagram. We will not draw it — we will only draw Class Diagrams — but even in other diagrams a class instance (object) can appear, so how do we tell them apart when they are both shown as rectangles?

The key visual difference: if there is a colon in the name compartment — the colon can even be at the very beginning, meaning I can omit the object name — I will have just `:Person` — regardless of whether a name is given or not, if there is a colon in the name part, I am no longer talking about a class but about its instance. That is the primary indicator.

Then, secondarily, if an attribute was, say, of some type, here it will no longer be a type but a concrete value.

In summary: a colon in the name means it is an object. No colon means it is a class.

---

## Relationships in Class Diagrams

**Lina Čeponienė:** Now, in Class Diagrams there can also be relationships. We will quickly go through and clarify those relationships so that everyone understands them consistently.

The first relationship is probably the one that is applicable to any UML diagram — the most loosely interpreted one — and it simply indicates dependency.

### Dependency

In a Class Diagram, an example of when we use the dependency relationship: for instance, if one class uses another class as a parameter for one of its operations. There is no direct structural relationship, but that class is dependent on the other class — so we place a dependency. This is a dashed arrow line. As I say, it is a very loosely interpreted relationship. We can also use it in other ways. The stricter relationships follow.

### Association

The stricter relationships are: Association — which you have probably drawn most often — Inheritance (Generalisation), then Aggregation and Composition, which are essentially variants of Association, and I will explain them to you now. Then I will explain in detail when to use which.

Let us start with Association, because this is what you will encounter most often. In principle, an association between classes means that there is a relationship between the objects (instances) of those classes. What kind of relationship? That brings us to the parameters that can be annotated on a relationship.

**Association name and reading direction:** This simply states which direction to read it in and what it means — for example "Person works-for Organisation."

**Role names (end names):** I would recommend using role names, because each end of an association is actually an attribute. If that attribute has no name, it remains nameless. By adding a role name to the relationship end, you give it an attribute name — these are the role names.

Role names are required in some cases and recommended in others. Sometimes you choose whether to show the association's overall name or the end names. This is a matter of preference, but adding the end name provides additional benefit. For example, it generates additional information. Multiplicity (cardinality) is specified at each end of the relationship.

**Multiplicity/Cardinality:** Multiplicity specifies how many instances of one class are related to instances of the other class. The standard typical variants are:
- **1** — exactly one: cannot be zero — there must always be exactly one.
- **1..**** — one or more: at least one must exist, but there can be more.
- **0..1** — zero or one: optional, at most one.
- **\*** (or **0..*) — zero or more: optional, any number. Note: `*` means the same as `0..*`. You choose which notation you prefer to display — both are completely equivalent.
- **1..\*** — one to many: at least one required.

I always get asked why there is a star and not `0..*`. The asterisk means the same as `0..*`. If I want from one to N, I show the `1..*` variant.

---

### Cardinality Exercise: Choosing the Right Diagram Variant

**Lina Čeponienė:** Since you all already know this, tell me: there are three variants of a class diagram and some rules that should apply — for which variant do all the rules apply?

Rules given:
1. A department can have at most one head (supervisor).
2. A supervisor can have no subordinates.
3. A department can have any number of employees.
4. An employee must belong to a department.

Working through this: "at most one" means it can be zero — so all three variants could match the first rule. "A supervisor can have no subordinates" — all variants have the subordinate end starting from zero, so all variants still match. "A department can have any number of employees" — "any number" is ambiguous: does it mean from zero, or from one? The third statement says "at least one must be in the department." That eliminates one variant because there it said the department cannot be empty. Then "an employee must belong to a department" — this eliminates any variant that says an employee can belong to zero departments.

The answer is variant C, which most of you were suggesting.

---

### Role Names — Mandatory and Recommended Use

**Lina Čeponienė:** Continuing with associations — let us discuss role names a bit more. It is generally recommended to specify them, because they simply help read the diagram and understand what the association means. The role name says what role that class plays in that association. But if there is more than one association between two classes — and exactly that situation occurs here, where this class has two association ends coming into it — then if we do not specify role names, it will be completely unclear. Likewise, in a situation where there are two associations with different cardinalities — one zero-to-one, the other one-to-many — without role names it would be read as an error, because we would not understand what is happening.

When we see that in one association the organisation is a "managed company" and the person is a "director", and in another association the organisation is a "workplace" and the person is an "employee", then we can interpret what the diagram means.

In short: where there is more than one relationship, role names are mandatory. Where there is only one and it seems obvious — you may omit them. But whenever adding an end name adds clarity to the diagram, it is always recommended to include it.

---

### Many-to-Many Associations and Intermediate Classes

**Lina Čeponienė:** You can put a star at both ends and then you have a many-to-many relationship. You can also use an intermediate class. The question then is: when do you need an intermediate class? It is not always needed when the relationship is many-to-many.

If later you would generate a database schema from this, then a tool will generate an intermediate table for you. But when is it explicitly needed in the diagram? If the intermediate class has attributes — which are also relationships — then you must show it, because otherwise we simply will not know where to put that attribute; it is the only place where it can go.

There is also a nuance with many-to-many relationships: they can be shown as I just showed, or they can be shown as an association class. An association class is drawn like a relationship but shown as if a class sits on that relationship. The same principle applies: you show the association class when it has additional attributes and you want to make that explicit, or for some other reason it is important to show it. These two representations mean the same thing and you should be able to do both in the tool.

One practical note: if you are generating a database schema from this, the tool may not recognise the association class notation and will leave it untransformed — that is a limitation of the tool, not a problem with your model.

---

## Attribute Notation (Full Syntax)

**Lina Čeponienė:** The maximum of what can be described for a class attribute looks like this. First there is **visibility**: either public (`+`), private (`-`), protected (`#`), or package (`~`). Who can see what?

- **Private** (`-`): visible only to that class.
- **Public** (`+`): visible to all.
- **Protected** (`#`): visible only to inheriting classes (visible to this class and its subclasses).
- **Package** (`~`): UML-specific — visible only to classes inside the same package.

Next can come a **derived attribute** indicator (`/`). Then the **attribute name**. The **attribute type** is always written after a colon. Standard UML types are: `String`, `Integer`, `Boolean`. They are capitalised; if you write them in lowercase, the tool may treat them as custom class names and create a new class — be careful.

After the attribute type, in curly braces (`{}`), there can be a **property string** called a "modifier," which specifies, for example, whether it is an `id`, whether it is `unique`, or a constraint (e.g., a numeric value no greater than ten). There you would write a specific constraint text.

Finally, if you have an array and want to show it is not just a String but an array of Strings, you can specify the **multiplicity** in square brackets next to the attribute type.

The last element is the **default value**: write `=` followed by the value, and that is the default. This is the maximum of what can be written for an attribute. This does not mean every attribute will be written this way — it means you should be able to read it: if you see `=` followed by something, that is the default; if you see brackets, that is an array; and so on.

---

## Navigability and Association Direction

**Lina Čeponienė:** Here is an important nuance that I want to emphasise — and I think many of you may not have internalised it despite drawing class diagrams before: an attribute and an association have a direct equivalence. If I show an association with a directed arrow from Class A to Class B, that means Class A has an attribute whose name is the role name at end B, and whose type is Class B — because Class A "knows about" Class B and reaches it through that attribute. Analogously, if the association is bidirectional (both ends are navigable), then both classes have corresponding attributes for each other.

The worst mistake I have seen is someone creating both an attribute and a relationship for the same thing — because in UML terms, that creates two attributes: one nameless (from the association end without a role name) and one named (from the explicit attribute). Never do both. Choose: either show it as an attribute or as a relationship — they mean the same thing. Most often in diagrams we show it as a relationship because it is easier to understand visually.

If there is a direction arrow on the association, it means the class from which the arrow originates knows about the class the arrow points to, but not vice versa. Class K3 has an attribute of type K4, but K4 has nothing — it does not know about K3.

**The mysterious "no-navigation" case:** You can also have a situation where both ends are explicitly marked as non-navigable (with an X). That means the relationship exists, but neither side navigates through it. The one example I found that justifies why this was invented is anonymous voting: if we have a `Person` and a `Ballot`, we need to know the person voted only once — so we need a relationship — but because voting is anonymous we must not know which person cast which ballot. So the relationship exists (to verify a person has voted) but is not stored (so the ballot cannot be traced back to a person). This is the only sensible use case I found for that notation.

**Ownership dots:** UML 2.5 introduced a notation where the ends of associations should technically have small dots to indicate the end belongs to the class as an attribute. Nobody uses it, tools do not apply it by default. But if you ever encounter it, know that it conforms to the standard and means exactly a normal association where the ends are attributes — you can safely ignore the dots.

---

## Aggregation

**Lina Čeponienė:** Now let us talk about Aggregation. Aggregation, like Composition which we will discuss next, is a specific type of association that is appropriate only when you are talking about a relationship that you could name "consists of."

For example: a lamp consists of a stand, a shade, a bulb, a switch, and a cord. Those are components — what something is made of. At that point you decide whether to use aggregation or composition.

**Aggregation is the looser relationship.** Example: a car consists of (among other things) wheels. Because I can take a wheel off and put it on another car, this is an aggregation. The wheel can exist independently even without the car. If I leave a wheel somewhere, it sits there perfectly fine. Also, the same wheel can belong to one car and later be moved to another.

A car without wheels is still a car — you might put it on bricks, but looking at it you would still say "that is probably a car, even if it does not drive." The part can exist independently of the whole and can be transferred.

---

## Composition

**Lina Čeponienė:** Composition is also a "consists of" relationship, but it is stricter. The rule: if you destroy the whole, you destroy the part.

Example: a building consists of rooms. A room cannot float in the air or exist independently without the building. If we demolish the building, the rooms are gone too.

Better example: a university consists of departments (faculties). If we eliminate the university, we eliminate its departments — they cannot exist independently. But a department consists of lecturers: if we eliminate the department, we do not kill the lecturers. They can still exist and go work somewhere else. So department–lecturer is aggregation; university–department is composition.

**The most common student mistake:** After seeing these examples, students start putting aggregation or composition on absolutely every relationship. Never do that. The first step is to ask: is this relationship a "consists of" relationship? Only if yes do you then decide whether destroying the whole destroys the part (composition, shown with a filled diamond) or the part can be transferred/survive independently (aggregation, shown with an open diamond). If the relationship is not a "consists of" relationship at all, then no aggregation or composition — it is simply a plain association with cardinality, role names, and everything else.

---

## Inheritance (Generalisation)

**Lina Čeponienė:** Let us talk about inheritance. Inheritance — as you probably know very well — is when a subclass inherits the elements of a higher-level superclass, and the subclass can have its own additional attributes or operations. This is shown as an inheritance (generalisation) relationship. Now we have practiced cardinalities and various relationships.

---

## Live Modelling: Checkers (Draughts) Game

**Lina Čeponienė:** I would like to draw a diagram together with you — a class diagram for a checkers game where we use as many different relationship types and cardinalities as possible. Tell me: from which classes could such a diagram be made?

We need: a `Checker` (piece), a `Board`, a `Square` (cell on the board), a `Player`, a `Game`, and `Rules`.

**Board — Square (Composition):** The board consists of squares — that is clearly a "consists of" relationship. If I were to name it I would call it "consists of," so we can use aggregation or composition. Recall: composition is stricter — if the board is destroyed the squares are gone. So this is composition. A standard 8×8 board has 64 squares. Cardinality on the square side: exactly 64. On the board side: a square belongs to exactly one board (it cannot exist without the board), so cardinality is 1.

**Checker — Square (Association):** A checker stands on a square — it does not "consist of" a square, so this is a plain association. Cardinality on the square side: a checker stands on 0 or 1 squares (it might be taken off the board). Cardinality on the checker side: at most 1 checker per square. But note: checkers only stand on black squares, not white squares. To model that properly, we should distinguish Black Square and White Square and draw the relationship only to Black Square. This leads us to inheritance.

**Square inheritance:** We can have `Square` as a parent class with `BlackSquare` and `WhiteSquare` as children via inheritance. Then the checker-stands-on relationship goes from `Checker` to `BlackSquare` specifically.

**Checker colours and inheritance:** Checkers come in two colours — black and white. We can model this as: (a) a single `Checker` class with a boolean attribute `isWhite`, (b) an enumeration (if there are only two values), or (c) two separate subclasses `WhiteChecker` and `BlackChecker` inheriting from `Checker`. Option (c) is best when the two colours behave differently and we want to model that explicitly. In that case, the player relationship should go from `Player` to `BlackChecker` and separately to `WhiteChecker`, with cardinality 12 on each side (a standard game has 12 pieces per player) and 1 on the player side — a checker belongs to exactly one player.

**Player — Game (Aggregation):** A game consists of players, boards, and pieces. If we delete/end a game record, we do not delete the players, the board, or the pieces — they can all exist independently. So this is aggregation (open diamond on the game side). A game has exactly 2 players. A player can participate in many games.

**Game — Board (Aggregation):** A game consists of one board. The board can be reused in multiple games. Aggregation. One board per game; a board can be in many games.

**Game — Checkers (Aggregation):** A game has exactly 24 checkers; a checker can belong to many games. Aggregation.

**Domain model note:** Any domain information that adds value for a person reading the diagram — and helps them understand how things work — is good to include. That is why we need role names, association names, cardinalities, and careful thought about how to represent things as richly as possible.

---

## Returning to Slides: Operations

**Lina Čeponienė:** Returning to the slides, let me also explain operations and a few more nuances about the class diagram.

### Operation Notation

From the UML specification: an operation is a property of a class that can be invoked on objects of that class. It can have a name, a type, and parameters. The maximum notation for an operation is:

- **Visibility** (`+`, `-`, `#`, `~`): same as for attributes.
- **Operation name**
- **Parameters** in parentheses: each parameter has a name, then a colon and a type. Parameters can also have a default value, just like attributes.
- **Return type**: after the closing parenthesis, a colon and the return type. This is optional — an operation may return nothing.
- **Direction**: each parameter can have a direction: `in`, `out`, `inout`, `return`. The default is `in`.
- **Multiplicity** on return type: e.g., if the return type is an array of `Person`.
- **Property modifier** (in `{}`): for instance `{query}` to indicate the operation is read-only.

---

## Interfaces

**Lina Čeponienė:** Another element that can appear in class diagrams is the interface.

An interface is like a contract — I am not sure how to say it better — that classes must implement. We describe what is offered, but the interface itself does nothing until a class realises it.

An interface is displayed either as a small circle (lollipop notation) or as a rectangle that looks exactly like a class, except it must have either the lollipop circle or the `«interface»` stereotype in the name compartment. If neither is present, it is a class. If either or both are present, it is an interface. An interface can have both operations and attributes.

Each class can have **provided interfaces** — those it implements/realises. The connection notation is a dashed line with a closed arrowhead (the realisation relationship). This can also be shown with the lollipop notation where the class is connected to the circle.

A class can also have **required interfaces** — those that it needs in order to work. This is shown with a socket (half-circle) connector or with a dependency arrow (`«use»`). The "ball and socket" notation shows at a glance which class provides an interface and which one requires it.

---

## When to Use What in a Class Diagram

**Lina Čeponienė:** We have now covered everything that can be in a class diagram. But what we use depends on where we are applying the diagram.

**In the requirements phase** (which is where we currently are), we use the class diagram to model the **domain**. The most intuitive thing to model is a domain entity class diagram, which can later become a database schema. At this stage:
- We do **not** need operations — they do not exist yet.
- We do **not** need interfaces — they do not exist yet either.
- We only need classes, their relationships, and their attributes.

We will use the **`«entity»` stereotype** to mark our classes. Entity classes are passive — they do not initiate anything on their own; they wait to be called and provide data.

**In the design phase** (later), we will use the same class diagram to model the software structure — where controllers are, where views are, where model classes are, and so on.

A class diagram can ultimately be used to generate code or even to describe non-computerised things. But right now, let us start from the requirements phase and build a domain model.

### Identifying Entities from Requirements

If there are concepts mentioned in your use case diagram or activity diagrams, those will most likely become entities or become attributes of those entities. You should look carefully at what you have and ask: from the other direction, if we describe an entity in our system, should there be use cases or activity diagram steps where that entity is actually used? If you described an entity but never use it anywhere, that is also wrong.

---

## Live Modelling: Vending Machine Monitoring System

**Lina Čeponienė:** We have the full requirements text — let me copy it here. I have highlighted the nouns in the text to make them easier to model. Let us start by creating a class diagram, and I will build it live. Since this is a domain model, I create a separate model called the domain model (rather than mixing it into the requirements model where the use cases and activity diagrams live). The class diagram and the state diagram I will create later both go here.

Let us build the class diagram.

### Buyer (Customer) Class

Looking at the system, I have a `Buyer`. A buyer can log in — so what attributes does a login require?
- `name`: String
- `email`: String
- `password`: String

**Tool tip — attribute types:** When I type the attribute type, if I type "String" with an initial capital, the tool recognises it as a String primitive type. If I type it in lowercase or make a typo, it will create a new class called `string` and add it to the model. That spurious class will linger in your model elements even after you fix the type. Model cleanliness is one of the things we evaluate at the defence, so clean up any junk classes you accidentally create.

### Discount (Nuolaida) Class

I can see from the requirements that there is a Discount entity. It probably has:
- `startDate`: Date
- `endDate`: Date
- `percentage`: Integer (or Double — let us use Integer, discounts probably do not have decimals)

### Message (Žinutė) Class

The buyer receives messages (discount notification messages). So we need a `Message` class. A message has:
- `text`: String

**Association: Message — Buyer**

A message is sent to exactly one buyer (a message cannot exist without being assigned to a specific buyer when it is created — we must specify who to send it to). So the cardinality on the Buyer side is **1**. A buyer can receive zero or more messages, so the cardinality on the Message side is **\*** (or `0..*`).

When I add the role name at the Buyer end: the buyer in this relationship is the `recipient` (gavėjas). Now in the Message class specification you can see it has a `text` attribute and also a `recipient` association end attribute.

**Association: Message — Discount**

A message reports about a discount. We will have many messages for the same discount (one per buyer who receives it). So the cardinality on the Message side is `0..*` (a new discount starts with no messages yet). A message reports about exactly one discount, so the cardinality on the Discount side is **1**. Association name: "notifies about discount."

### Vending Machine (Automatas) Class

**Automatas** attributes:
- `status` (būklė): enumeration. Enum values: `new` (newly entered in the system, never polled), `operational` (working), `needsMaintenance` (operational but maintenance required), `offline` (maintenance in progress), `disabled` (switched off).
- `needsMaintenance`: Boolean (default: `false`) — indicates whether maintenance is needed.
- `location`: String (address)
- `model`: String

**Tool tip — enumerations:** For the `status` attribute, use an enumeration type (not just a string). In UML you specify the enumeration type as a classifier — literally a `«enumeration»` element — not a plain attribute. The attribute type then refers to that enumeration class.

**Tool tip — default values:** You can set the default value for an attribute in the diagram notation. The tool shows it in a different colour once recognised correctly.

**Tool tip — showing attributes as association ends:** If an attribute's type is another class, you can "unfold" it into a visible association in the diagram. The attribute then disappears from the attribute compartment and appears as an association line — they represent the same information, just presented differently. To show the association end as an attribute, use "Show Association End as Attribute."

**Association: VendingMachine — Technician (Prižiūrėtojas)**

A technician monitors vending machines. Role name at the machine end: `monitoredMachine`. A technician can have zero or more monitored machines (they may have just been hired and not yet assigned). A vending machine can have zero or one assigned technician (it may not yet be assigned). Cardinality: `0..*` on the machine side, `0..1` on the technician side. (Using exactly 1 would mean a machine cannot exist in the system without an assigned technician — we prefer the more flexible option.)

### User (Naudotojas) Parent Class

Both `Technician` and `Administrator` (valdytojas) share common attributes: `name`, `email`, `password`. So we create a parent class `User` with those attributes, and both `Technician` and `Administrator` inherit from it.

**Tool tip — drawing inheritance:** When drawing inheritance in the tool, aim to connect the arrow directly to the parent class body so the tool draws it neatly and it is clear which classes belong to that inheritance hierarchy.

- `Buyer` has no additional attributes beyond the user ones, but it has the additional `Message` relationship.
- `Technician` has: `phone` attribute, and the association to VendingMachine.
- `Administrator` — we will see what attributes are needed when we get there.

**Note on inheritance and relationships:** If `Buyer` were to inherit from `User`, and `Technician` also inherits from `User`, and `User` had the `Message` relationship, then both would inherit it — but `Technician` does not receive discount messages. Therefore the `Message` relationship stays on `Buyer`, not moved up to `User`.

### Inspection Result (Apklausos rezultatas) Class

The system periodically polls each vending machine and updates its status. When it polls, it knows the detailed current state: coffee level, sugar level, cup level, coin levels, error code, next maintenance date. If I store these as attributes directly on the `VendingMachine`, I only know the current snapshot — no history. If I need to generate reports on how consumption changed over time, I need a separate entity to store each polling result.

**InspectionResult** attributes:
- `coffeeLevel`: Integer (percentage)
- `sugarLevel`: Integer
- `coinLevel`: Integer
- `errorCode`: String
- `nextMaintenanceDate`: Date
- `timestamp`: DateTime (each inspection result is unique per timestamp)

**Association: InspectionResult — VendingMachine**

An inspection result belongs to exactly one machine — cardinality on machine side: **1**. A machine can have zero or many inspection results (zero if it is brand new and has never been polled). Cardinality on inspection result side: `0..*`.

### SMS / Service Notification (Esamas / Pranešimas apie aptarnavimą)

The system sends notifications to technicians when machines need servicing. So we have a `ServiceNotification` class:
- `text`: String

**Association: ServiceNotification — Technician**

A service notification is sent to exactly one technician (the `recipient`). A technician can receive zero or many notifications.

**Association: ServiceNotification — InspectionResult (or VendingMachine)**

The notification is about which machines need servicing. Whether we link it to the machine directly or via the inspection result depends on access patterns. If we frequently need to know which machine a notification is about, link directly to the machine. If the link is to a specific inspection event, link to the inspection result. Either way we can navigate to the machine through the inspection result. The association name can be "notification about machines to service."

**Tool tip — wrapping long association labels:** In the tool, you can enable word wrap for association names via the symbol properties. This allows multi-line labels and a more compact diagram view.

---

## Entity Stereotypes on All Classes

**Lina Čeponienė:** Since we are building a domain entity class diagram, I should add the `«entity»` stereotype to all classes. You can select all classes at once, then apply the stereotype to all of them simultaneously via "Select connected → Select all of the same type" (or via Ctrl+click), then apply the stereotype. After that, if the diagram looks cluttered because of the stereotype label display, go into Symbol Properties and uncheck "Show stereotype" — the stereotype is still applied, but not visually shown on each box.

---

## Assessment and Exam Reminder

**Lina Čeponienė:** I would like to add a note about assessment. We will ask you to draw sketches in the midterm exam. A sketch does not need to be beautiful — I drew it freehand now specifically to show you what a sketch looks like. A sketch is not done with a ruler in coloured pencils with perfect lettering. It just needs to be readable at the moment so we can discuss and figure out the best approach.

In the exam (kontrolinis), you will have one-and-a-half hours. You will receive a fairly detailed text description, and from it you need to draw the diagrams — what is written in the text is what needs to be drawn.

Basically, all the diagrams we will cover together will be in the exam:
- Use Case Diagram
- Activity Diagram
- Class Diagram
- State Diagram
- Sequence Diagram
- Package Diagram

(If I forgot any, I can check later.) All the theory I explain to you and that we draw together — all those diagrams will be in the exam with different questions. The exam will have enough questions and different diagrams. You will not know in advance which ones you get — each person gets them as a task.

Depending on how we structure it, there may be all of them, since we try to include as many diagrams as possible so we can verify that you understand all of them. Some maybe in more detail, some more superficially, but all of them.

---

## Closing

**Lina Čeponienė:** From the class diagram theory side, I have more or less told you everything, and you now know a bit more than you did before — I hope. I will finish putting together the class diagram on my own to add a few more classes, and if possible use a few more varied relationship types. There will definitely be more elements: more inspection timestamps, the discount will need to be connected more, so the diagram will grow a little. But do you have any remaining questions from this?

I think I showed you most of the technical side — except the dependency relationship, which I mentioned briefly: in any UML diagram, in the relationships palette, you can always find the dependency relationship (dashed arrow), which you can draw whenever needed; in this case it is not needed, but just so you have seen how to draw it.

If you have no more questions, thank you for your attention today, and I hope you will very successfully draw these class diagrams in the labs this week.
