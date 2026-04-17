# Lecture 6 — Logical Architecture, Package Diagrams, and Transitioning from Requirements to Design

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Iterative nature of software development: going back and correcting earlier work
- Upcoming midterm exam format (hand-drawn sketches on paper)
- Transition from the requirements model to the design model
- Logical vs. physical architecture
- Package diagram: notation, namespace, dependency relationships, visualization options
- Architectural patterns: MVC, layered architecture, microservices overview
- ROBUSTNESS stereotypes: Boundary, Controller, Entity — and the interaction rules between them
- Model transformation (requirements model → design model) using the modeling tool
- Converting use cases to collaborations for sequence diagrams
- Placing classes into architectural packages
- Sequence diagrams: how they generate operations on classes automatically
- Planning class diagrams per subsystem/package

---

## Course Logistics and Assessment Reminders

So, let us pause for a moment and recap what we are talking about. We are currently in the design phase — this is what you need for the second lab assignment. If today you present and defend your first lab, then everything there will be fine, though I do have some bad news regarding the first lab, in case you are not already upset.

It is very rare in practice to get everything right on the first try. In a well-ordered sequence of steps where you carefully think through each element and everything builds properly on top of it. When I show you the process, you can see there are many arrows pointing backwards — indicating things you will need to go back and fix. If you are in the design phase and suddenly realize you need to add a function differently or change something, what do you have to do? Go back and fix it.

Going back and fixing things will be, shall we say, the expletive of this module. If everything is connected at one end, you cannot just do something, set it aside, and relax. Nothing in this project is an isolated, self-contained piece. Even if you have defended the first lab, almost certainly you forgot about some aspect — nearly guaranteed. For instance, you may have forgotten an important attribute in the class diagram that seemed unnecessary at the time, but then while implementing things you suddenly realized that without it you cannot proceed. That is a natural, normal state of affairs. It is how things should work in practice — rarely does everything go according to a strict waterfall process.

In a perfect world you have requirements first, then design, and so on. In reality, you often have to swim against the current, even in a waterfall model. So what is needed is to step back to an earlier stage. While working on the second lab you will likely need to go back and fix things from the first lab. While working on the third lab you will likely need to go back and fix both the first and second. And any comments you receive after defending the first lab — if something is wrong — you will have to fix those as well. You cannot simply move forward with errors in earlier work.

Yes, you can start banging your head on the table — I have said enough bad things to cause some stress. Should I add a bit more? I also want to remind you, since I am already causing stress, that the midterm exam is coming up. Do you remember? I mentioned it before. I think that truly will make some people want to bang their heads on the table.

### Midterm Exam Format

The reason I am preparing you psychologically is that the exam will work a little differently than the lab assignments. In the labs you defend your work using the modeling tool, but in the midterm exam you will be drawing on paper.

That means drawing diagrams roughly the way I draw them for you during lectures — to quickly illustrate things. The goal of the exam is to assess how quickly you are able to sketch a diagram from a given description. UML diagrams serve multiple purposes: they can be used as detailed specification tools, as aids for thinking through things you would not otherwise think about, and as communication tools.

As a communication tool, you very often just need to quickly sketch something on a whiteboard — or if working remotely, on a digital board — just to make it easier to communicate an idea. That is what you will be doing on paper in the exam. There is no need for a ruler, no need for colored pencils. I have seen students arrive for the exam with sets of colored markers, rulers, erasers, and nearly a compass for drawing use case ovals — please do not do that.

The goal is simply to see how quickly you can sketch a diagram from a description. There will be enough work to fill the entire class period. If you have not practiced the diagrams that will appear on the exam through the lab work, it will be difficult. I strongly recommend not procrastinating — defend the first lab and immediately start the second, because the most complex diagrams are class diagrams and sequence diagrams, especially sequence diagrams. There is a risk that students who have only drawn basic sequence diagrams — where it is just a user interacting with a system — will think they already know how to do them.

The two hardest diagram types for students in this module are, in my experience: state machine diagrams and sequence diagrams. You have already worked on state machines, so hopefully you felt how difficult it is to shift your mindset — because it is not a process but a set of states. You do not think in terms of endings; you think in terms of triggers and guards, and it does not come out right on the first attempt.

Regarding sequence diagrams: if you have been drawing them at a level where there is just a user and a system, now imagine that you will need to expand that system — to show which classes exist, which methods each class has, and who calls whom until the user receives a response. If you drew basic sequence diagrams in earlier courses and think you already know them, think again. The sequence diagrams in this module will be significantly more complex.

They are also worth a meaningful share of the exam grade precisely because they are a complex diagram type. The control test is expected to be before the Easter break — around the 30th, I believe, but please check the schedule. I recorded the date, so I should not have it confused. The idea is for you to write it before the Easter holiday and then go on vacation with a lighter heart. Do not relax, though — use that vacation week to work on more lab assignments.

---

## Today's Agenda: Moving from Requirements to Design

Now let us get back to what we need to discuss today. We have finished covering diagrams for the requirements phase, and today we will transition from requirements to the design phase. This will not be as simple — we will perform a transformation and I will show you how, in the design phase, we first need to establish the logical architecture.

### What Is Architecture?

I took the definition from a classic textbook. Architecture, broadly speaking, is both logical and physical. Whenever we talk about architecture we should specify which kind we mean.

**Physical architecture** is easier to understand: it is about how we arrange hardware — where we run network cables, where we place routers, where we put servers. It is the deployment of software components onto physical devices and their interconnections.

**Logical architecture**, to put it simply in everyday terms (I intentionally left the formal definition in English so you could see the original): it is the organization of a system into layers, packages, and the like. Very simply: how we divide the system into parts.

Into what parts, and how we make that division — this matters enormously for how we work going forward. Those parts should ideally be as independent as possible from each other, or at least divided in a way that makes the system more convenient to build, work with, or deploy. All of these are valid goals. Logical architecture is, roughly speaking, the division of the system into parts.

Many of you have already attempted to divide systems into parts when drawing use case diagrams and trying to put architecture in them — with subsystem boxes labeled "this subsystem" and "that subsystem." I remind you: the use case diagram is completely unsuitable for representing architecture. However you grouped things in those diagrams, that is not your architecture. Your architecture is what we will create today — we will draw a package diagram showing how the system is divided into parts.

So let us look at how many diagrams we have covered. We have covered quite a few behavioral diagrams. Today we will also talk about class diagrams and learn about one more structural diagram type — the package diagram. After this, the remaining structural diagrams we have yet to cover are the deployment diagram and the component diagram. And from the interaction diagrams — sequence diagrams. Once we cover those, you will know everything I wanted to teach you in this module.

---

## Package Diagrams

### Basic Concepts

A package diagram — its basic element is the package. If you have opened the modeling tool you have seen it many times and understand what it is. Every time you create a new project, it will always contain at least one package.

The primary purpose of a package is simply grouping elements — like a folder in a file system. You need somewhere to put things, and a package is that container.

According to the UML specification, a package is a **namespace**. I am not sure of the Lithuanian translation — if you know one, let me know. A namespace means that the names of elements within the same package cannot be duplicated. If you try to create an element with the same name inside the same package, your modeling tool will complain. You can show the same element on multiple diagrams under the same name, but that is the same element. If you try to create a new, separate element with the same name in the same package, the tool will not allow it.

In different packages, you can have elements with the same name. The reason is that the fully qualified name of an element is not just its local name but the entire path to it through all containing packages. So I can name a class the same thing in two different packages and they will be two different elements, because the full name of each class includes its entire path plus its local name.

A package has a name, and it can contain internal elements or not, can have relationships with external elements or not. When it does have relationships, the options are more numerous than you might expect — not just the **dependency** relationship you may have seen, which applies to any element, but also import, merge, and access. However, these more specific relationship types are relevant for more advanced uses of package diagrams. Since we are using the package diagram primarily in the simplest way — to show architecture — we will only discuss the **dependency** relationship, which essentially means: this package needs that one. How exactly it needs it, and why, the dependency relationship leaves open. UML is a Unified Modeling Language — the more universal you make something, the more freedom of interpretation you must leave. Here that freedom is left deliberately. Dependency simply says: this one depends on that one.

### Visualization Options

There are several ways to display packages in a diagram.

**Option 1:** Show the package with its contents directly inside it — displaying the classes along with their relationships, attributes, etc. This gives maximum visual information but takes up a lot of space.

**Option 2:** Show the elements inside a package as a list. This saves space but loses visual richness — you cannot see relationships or attributes between elements.

The list-style display is useful when a package contains many elements but you still want to show the overall picture. You will likely need separate diagrams to show the details of relationships and attributes within those packages.

There is also the containment relationship (shown with a circle-and-cross connector), which explicitly shows that an element belongs to a package. If you have elements nested in the model tree and bring them into a diagram asking to show their relationship, the tool will draw the containment connector automatically.

All of these visualization options are valid — the choice depends on what you want to communicate with a particular diagram.

---

## Logical Architecture: Architectural Patterns

We use the package diagram to construct the project model's architecture. The simplest example that all students love and immediately want to copy: the classic **Model–View–Controller (MVC)** architecture. You all know what MVC is — what do the letters stand for?

Model, View, Controller. What other architectural patterns do you know?

- MVP (Model–View–Presenter)
- MVVM (Model–View–ViewModel)

These are variations — specific adaptations for particular frameworks, platforms, or implementation technologies. The classic MVC may not always fit, but in this module we are guiding you to work along MVC lines to avoid needing to break too many patterns. Start from the classic variant — separate the view (presentation), logic (controller), and data (model). That is the starting point.

### Warning: Do Not Copy the Example Blindly

The worst possible answer to the question "Why does your diagram look like this?" is: "Because that is what the example looked like," or "Because that is what the lecturer drew." I cannot stress this enough. The same solution that works perfectly in one system may be complete nonsense in another, depending on the context and domain. You always need to know why you made a given decision.

When I draw a diagram for my example coffee vending machine system, it does not necessarily apply to your system. Do not blindly copy it. First, think about why — think about where and how you will apply it. The classical architecture separates presentation, logic, and data — that is the starting point, but your architecture may look different.

### Examples of Package Diagram Architectures

**Example 1 (basic MVC):** Three packages at the top level: controllers, views (boundary), models. Simple and clean.

**Example 2 (controllers subdivided):** Controllers and models kept separate, but controllers are further subdivided into packages by functional area for easier navigation when there are many classes.

**Example 3 (subsystem-based):** Large functional packages (e.g., for orders, for reporting) where each subsystem contains its own views and controllers, and all share a common model package. All subsystems access a shared models package.

**Example 4 (fully separated subsystems):** Each major subsystem (e.g., user management, machine management) is completely separate and has its own views, controllers, and models. This approaches a microservices-style split — but note: you are not required to build a microservices architecture. That approach makes sense when you truly want to make parts of the system as independent as possible from each other.

You can also have a mix: a frontend and a backend as the two large parts, and within each, further subdivision into packages. If you are planning a separate frontend and backend in different technologies, your architecture will reflect that naturally.

The package structure you design should match the model element tree in the tool. That is: if you have controller, view, and model packages, those actual packages should exist in the tool's project tree with the corresponding classes placed inside them. I have often seen students create a nice-looking package diagram while the actual classes in the model tree are thrown in randomly — chaotic, duplicated, misplaced. During your defense we check both the diagrams and the model tree. If the model tree is a mess with garbage elements, wrong types, or classes not placed in the correct packages, your lecturer will tell you that is an error.

---

## ROBUSTNESS Stereotypes and Interaction Rules

When we work according to proper principles — specifically the modified Rational Unified Process that I have adapted for this module so that you learn as many diagram types as possible — there are so-called ROBUSTNESS stereotypes.

These define three types of classes:

- **Boundary** — the interface between the system and the outside world (screens, external APIs)
- **Controller** — contains business logic
- **Entity** — passive data classes (models)

After defining these stereotypes, interaction rules specify what is allowed to communicate with what, and what is not.

### Interaction Rules

- **Actors** (external users or systems) can only communicate with **boundary** elements. They cannot directly call a controller or an entity class.
- **Boundary** elements cannot communicate with each other directly.
- **Boundary** elements cannot communicate directly with **entity** classes.
- **Controllers** can communicate with boundary elements, with each other, and with entity (model) classes.
- **Entity** classes are passive — if they need something done, they call a controller; they cannot call other entities directly without going through a controller.

### Why These Rules Matter: A Practical Example

Why can a controller not directly call an external actor (e.g., an external API) without a boundary class in between?

Imagine you make a direct call to an external API from your controller. At first it works fine. Then you realize you need that same external call in another controller. So you write it again there. Then in a third place. Eventually you have five places in your code that call the same external API. Everything works — no principle violations, no obvious problems.

Then the external API changes. You need to update the way you call it. Now you search through the codebase to find all five places, fix the ones you find, and inevitably miss at least one. Debugging begins.

But if you had created a **boundary class** as the single point of communication with that external API, and all internal controllers communicated with the external world only through that boundary class — then when the API changes, you fix exactly **one place**. That is the core logic: minimize the number of exit points to the outside world. When something external changes, you only need to update one class rather than hunting through the entire codebase.

Similarly, actor access through boundaries: an actor sees the system only from the outside, meaning they see only the boundary layer. They cannot directly reach a controller or a model class — everything has to go through a boundary element.

---

## Transforming the Requirements Model into the Design Model

### When to Do the Transformation

Perform the transformation after you have finalized your requirements model. If during your defense you receive feedback that something is wrong in the requirements model, fix it first, then perform the transformation. I will explain why shortly.

### How to Perform the Transformation in the Tool

1. Go to **Model Transformations** and select **Transformation Edition**.
2. The first time, it will ask you to set up a profile — accept all defaults and it will not ask again.
3. **Select the source**: the requirements model (or the specific packages from it you want to transform).
4. **Select the target**: the design model package you have created.
5. The tool will import everything from the requirements model, but you do not need everything. Remove what you do not need:
   - Remove the use case diagrams themselves (you do not need the diagrams, only the use case elements)
   - Remove activity diagrams (use case descriptions)
   - Remove state machine diagrams
   - Remove signal elements
   - **Keep**: use cases themselves, actors, entity classes (from the domain model / class diagram), and packages.
6. Do not accidentally click "remove all" when you have nearly finished selecting — that would reset your selections and you would have to start over.
7. After selecting what to keep, specify the target location and click **Finish**.

The worst mistake: accidentally deleting the auto-generated `«edition»` package that the tool creates. This package maintains **traceability** — it records what was transformed from what. Even if your elements are renamed (e.g., a Lithuanian entity class "Žinutė" becomes an English class "Message"), the tool records "transformed from: Žinutė in the requirements model." This lets you trace every element in the design model back to its source in the requirements model, and later trace forward to the implementation model. Never delete this package, even if it contains many things you do not recognize — expand it carefully, but do not delete it.

### What to Keep and Reorganize

After the transformation, the design model will contain:
- The use case packages and their use cases (now converted to **collaboration** elements)
- The actor classes
- The entity classes from the domain model

You will typically want to place actors in a dedicated actors package to keep things organized. Move all actor elements there.

### Converting Use Cases to Collaborations

For the sequence diagrams you will draw in the next lecture, use cases need to be converted to **collaborations** in the design model. Here is why: in the tool, sequence diagrams live inside collaboration elements. If you convert your use cases to collaborations now, then when you create a sequence diagram, the tool will automatically:
- Place the sequence diagram under the correct collaboration
- Name the diagram after the use case
- Maintain the traceability link back to the original use case in the requirements model

To convert use cases to collaborations:
1. Select the use case elements (you can select per package; selecting all at once across packages can cause issues).
2. Right-click → **Refactor** → **Convert** → select **Collaboration** as the target type.
3. Confirm. The tool asks "are you sure?" — confirm.

After conversion, all your use cases will appear as collaboration elements with dashed-border icons. Opening the specification of any one will show it is a collaboration and display its "transformed from" traceability.

### Language: Lithuanian vs. English

While you were working in the requirements model, most of you named your elements in Lithuanian. Your entity classes (the domain model) will have Lithuanian names. When you transition to the design phase, now is the time to decide: will you code in Lithuanian or in English?

If you plan to code in English (which is overwhelmingly standard), then transition your entity class names and attribute names to English in the design model. The classes in the design model should be as close as possible to the classes you will actually have in your code (or database tables). Go through all your classes and rename attributes to English — it is actually easier to do this via the model tree than in a diagram.

If someone truly intends to code in Lithuanian — that is technically possible, though unusual. In that case, your entity model can stay as-is, though you will still need to clean up names (e.g., remove spaces from names, add camelCase notation, etc.).

---

## Building the Architectural Package Diagram

Once the transformation is done and the design model is set up, create the **architecture package diagram**.

### Steps

1. Inside your design model package, create a new diagram of type **Package Diagram**.
2. Decide on your architecture. Think about which packages make sense for your system. Do not copy the example architecture blindly — reason about what fits your project and your chosen technology stack.

### Architecture Options

**Option A — Pure MVC:** Three packages: `controllers`, `views` (boundary), `models`. Simple, but may become hard to navigate if you have many classes.

**Option B — MVC with subdivided controllers:** Separate `controllers` and `models` packages, with controllers further subdivided by functional area (e.g., `controllers::client`, `controllers::admin`). More organized for larger systems.

**Option C — Subsystem-based:** Large packages representing major system subsystems (e.g., `client`, `machineManagement`, `main`), each containing their own controllers and views, with a shared `models` package. All subsystems depend on `models`.

**Option D — Frontend / Backend split:** If you plan a separate frontend and backend in different technologies, represent this at the top level as two large packages, each containing further subdivisions.

The key principle: your package structure in the diagram **must match** the package structure in the model element tree. Classes must actually be placed in the correct packages in the tool — not just shown in a nice diagram while the actual model tree is disorganized.

### Showing Package Contents

You can display package contents in several ways:
- **Show classes inside the package graphically** (full class boxes with attributes and operations visible) — shows everything but uses a lot of space.
- **Show elements as a list** inside the package — saves space, good for an overview diagram.
- **Hide elements entirely** and just show the package names with dependency arrows — the highest-level architectural view.

A good strategy: have one high-level overview diagram showing only packages and their dependency relationships, plus separate detailed diagrams per package showing the classes and their relationships.

### Dependency Relationships Between Packages

Use the **dependency** relationship (dashed arrow) to show that one package needs another. For example:
- `client` depends on `models`
- `machineManagement` depends on `models`
- `client` and `machineManagement` both depend on `main` (for shared login logic)

The direction of the arrow is: the package that depends on another points toward the package it depends on.

---

## Placing Classes in Packages and Organizing the Model

After creating the architectural package structure, you need to populate the packages with classes.

### From Entities to Model Classes

Your entity classes from the requirements model (transformed over) are your **model** (entity) classes in the design model. They carry the `«entity»` stereotype. Place them in the `models` package.

### Creating Boundary and Controller Classes

As you draw sequence diagrams (next lecture), you will naturally discover which boundary and controller classes you need. However, you can begin creating them now based on your architectural decisions.

**Boundary classes** represent user interface elements or external system interfaces. For each screen or external integration point, create a boundary class. Place it in the views (or boundary) sub-package of the relevant subsystem.

**Controller classes** contain business logic. Create one or more controllers per subsystem. The number of controllers is a design decision — neither one controller for everything nor one controller per method is ideal. The right granularity depends on your architecture and your framework.

To illustrate: suppose you need a screen showing a list of vending machines (for a maintenance officer). Create a boundary class `MachineList` with stereotype `«boundary»`. Place it in the appropriate package (e.g., `machineManagement::views`). Then this boundary class needs a controller to handle the logic of fetching and displaying that list. Create a controller class, e.g., `MachineListController` with stereotype `«control»`, placed in `machineManagement::controllers`.

The question of how many controllers to create is a philosophical one. At one extreme: one controller per use case. At the other extreme: everything in one controller (which is technically possible but a maintenance nightmare — there is a real story of a student team that tried this and ended up deeply regretting it by the end of the project). The right answer depends on your architecture.

---

## Sequence Diagrams: Introduction and Connection to Class Diagrams

### Overview

For each use case, you need to create a sequence diagram (similar to how you created an activity diagram for each use case in the requirements phase). The sequence diagram will show how the use case is realized inside the system — which classes are involved, what methods are called, in what order.

### How Sequence Diagrams Generate Operations Automatically

This is a key feature of the modeling tool: when you draw a sequence diagram and add a message call from one lifeline to another (i.e., you specify that class A calls a method on class B), the tool will automatically create that operation on the target class.

So when you place a controller on the sequence diagram and draw a message to it from a boundary class, then specify the method name — the tool records that this controller must have that operation. If you then look at the controller class in your class diagram, that operation will be there.

This is how your class diagrams gain their operations: by working through the sequence diagrams. Start with the architecture and the entities (which give you attributes from the domain model), then draw sequence diagrams which give you operations on the controllers and boundary classes. The class diagrams then reflect the full picture.

### Layout Convention for Sequence Diagrams

Standard layout guidance:
- Place the **primary actor** on the far left.
- Next: **boundary classes** (the interface elements the actor interacts with).
- Then: **controller classes**.
- Then: **entity (model) classes**.
- If there are **secondary actors** (external systems the primary system interacts with), place them on the far right, with their associated boundary class just to their left.

Following this convention makes the sequence diagram much easier to read and review.

---

## Closing Remarks

That is as far as we will go today. Next lecture we will discuss sequence diagrams in detail. For now — prepare your requirements models for transformation, decide on your architectural pattern, set up your package structure in the tool, and make sure the model element tree matches your architecture diagram.

Thank you for your patience.
