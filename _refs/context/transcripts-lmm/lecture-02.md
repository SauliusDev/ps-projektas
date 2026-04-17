# Lecture 2 — Use Case Diagrams: Elements, Relationships, and Practical Modeling

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Overview of the requirements specification phase and the UML diagram roadmap
- Use Case diagram elements: actors and use cases
- Correct Lithuanian terminology: "panaudojimo atvejis" (use case), not "panauda"
- Association relationship: rules and multiplicity (cardinality)
- Inheritance (generalization) between actors and between use cases
- «include» relationship: mandatory shared behavior
- «extend» relationship: conditional optional behavior and extension points
- Common student mistakes in use case diagrams
- Grouping use cases into packages (subsystems)
- Specifying use cases using tables (pre/post-conditions, scenarios)
- Live modeling walkthrough: Coffee Vending Machine Management System
- Tool tips: profile settings, element numbering, compact view of extension points, packaging

---

## Introduction: Where We Are in the Course

Today we are discussing the diagram I am showing here, and I will refer back to it throughout the semester so you always know where we are. We will be spending quite a long time in the requirements specification section.

As you can see, in the requirements specification phase we have quite a lot of things to do and describe: use case diagrams, activity diagrams, class diagrams, and a state diagram, building on the initial description from the previous step. You have already, or will soon, agreed on a topic during your lab sessions. I will briefly show you the interface prototype at the end of this lecture. Today we are talking about the requirements specification stage and the first diagram we will study: the **Use Case Diagram**.

You already know how to draw this from previous courses, right? You have already drawn them. I will just do a recap, since it is not particularly difficult. We will figure out what you know, what you do not know, go over the grammar, and I will show you some of the wonders students who "know everything" produce. To make it more interesting, I have some examples. I collect exotic diagrams drawn by students — my own, and ones sent to me by colleagues when they spot something interesting. I will show you what can be drawn.

From the UML diagram tree you can see here, we will be covering various diagrams — not all of them. Today we start with use cases, which are a **behavioral** type of diagram. There are structural diagrams and behavioral diagrams. Use cases belong to the behavioral category. This diagram is one of the simplest — it has a little stick figure, some ellipses (use cases), and that is essentially it.

---

## Terminology: "Use Case" — Why Not "Panauda"?

A quick terminology note. We say **panaudojimo atvejis** ("use case"), not "panauda" ("use"). You may have heard the short form — it is fashionable to say it, presumably because it is shorter.

However, as lawyers have clarified to us, "panauda" is actually a specific type of rental arrangement in Lithuanian law — lending property under a usufruct right. It has nothing to do with software. That is why the correct term is **panaudojimo atvejis**.

---

## Elements of the Use Case Diagram

### Actors

An actor is either a person or a system. It does not have to be a person. The actor exists outside the boundaries of the system, but interacts with the system we are building. An actor can be many things: a user of some kind, a company, an organization, a device, and so on.

**Can you show your own system as an actor?**

If you think about it informally, an actor is something whose internals we do not know — it is not part of our system. We do not know what is inside; we only know what we pass to it and what we receive from it. That applies to a human actor as well: we are not interested in their organs or brain activity. The same applies to any external system — we know what we send and what we get back.

If you start talking about **your own system**, it can never be an actor. The only case where it might make a marginal amount of sense to show your own system as an actor is when you are modeling it in subsystems: you temporarily treat one part as if it is external because you are only modeling another part right now. But the system you are currently modeling can never appear as an actor in its own use case diagram. You would show it as the system boundary (a rectangle), and its own functionality would be use cases inside that boundary.

One more point from the human side: an actor is a **role**, not a person. The same physical person can have multiple roles in a system. For example, in an e-commerce system, I might be an admin with rights to manage products, and I might also want to make purchases. Those would be two separate actors: **Administrator** and **Buyer**. It is not good practice to give the administrator all possible permissions — it is better from a security standpoint to keep roles separate and create separate user accounts.

### Use Cases

A **use case** is roughly a unit of functional requirements — what can be done in the system. It describes what the actor connected to it can do.

**An important rule:** a use case must deliver a meaningful, observable result. You should be able to say "I did this function, and I can now go for a coffee" — meaning something actually happened. A common mistake is splitting use cases into tiny steps: "enter data," "select an attribute," "select another attribute," "save." Those are not separate use cases — they are steps in a scenario. If you cannot name a meaningful result, it is not a use case.

Use cases describe **what** the system should do, not **how** it is implemented. There are no technologies, no servers, no architecture in a use case diagram. If you add subsystems (packages) to the diagram, they are not architectural subsystems — they are only there to improve readability.

**Naming conventions:** Keep names short. It is strongly recommended to use a consistent form — either noun form ("Login") or verb form ("Log in"), but do not mix them. Do not write a use case name that spans four lines. Single word like "Delete" alone is also too vague — delete what? There is always a balance between too detailed and too vague. The name must carry enough meaning for the reader.

---

## Relationships in Use Case Diagrams

### Association

The simplest relationship. A line between an actor and a use case means one thing only: **this actor can perform this function in the system**. Nothing more.

**Rules:**
- Association can only exist between an actor and a use case.
- It cannot connect two actors.
- It cannot connect two use cases.

The relationship can carry **multiplicity (cardinality)** at either end, though you will rarely use it. For example, a multiplicity of `2..*` on the actor end means: "this use case requires at least two actors simultaneously." An example: "Play game" — this can only happen when at least two players are present. You can also express this by connecting two separate actors (Player 1, Player 2) to the same use case. But if the number is variable and unbounded, the cardinality notation is the only way to express it cleanly.

Do not start placing multiplicities everywhere just because you can. Use them only when they are genuinely needed. Know that they exist and what they mean, so when you encounter them you understand them.

**Convention — primary vs. secondary actors:** When multiple actors are connected to the same use case, there is an unwritten UML convention that primary actors (those who initiate the interaction) go on the left side of the diagram, and secondary actors (those who are called upon) go on the right side. This is not a formal grammar rule, but people expect it — it makes diagrams easier to read.

### Inheritance (Generalization)

Generalization **between actors** is clear and useful: an inheriting actor has all the use cases of the parent actor, plus potentially some of its own. This is the most common scenario — for example, a Supervisor inheriting from a basic User. Use this — it is recommended.

Generalization **between use cases** is a different matter. It exists in the spec, but it is very ambiguous and hard to interpret consistently. In theory, the child use case inherits the scenario of the parent and can extend or override it. But because this is so loosely defined and everyone can interpret it differently, I would advise you **not to use it**. It is formally valid, but it adds no clarity. If you see it somewhere, you will know what it means — but avoid using it yourself.

About 80% of students tend to add actor inheritance automatically. I am not saying it is wrong — it depends on the system, the number of different actors, security requirements, etc. But be aware: it is not always appropriate, and having an admin who can do literally everything can be problematic from a security standpoint.

**The one rule that is strictly forbidden:** You cannot connect two use cases with an association. That is completely off-limits. Everything else is a matter of judgment.

### «include» Relationship

The «include» relationship connects two use cases. The arrow goes **from the including (parent) use case to the included (child) use case**.

This means: when the parent use case executes, the child use case **always and unconditionally** executes as part of it. You cannot run the parent without running the included child.

The original reason «include» was invented: **factoring out repeated behavior**. If a set of steps appears in several different use cases, instead of writing those steps out every time, you extract them into a separate use case and all the others include it. This avoids duplication.

Later, «include» came to be used for decomposition — breaking a large use case into smaller ones for clarity. That is also valid, but use judgment. If you chain too many includes you will get a spider web that nobody can read.

**If you see «include» applied to a chain of sequential steps** (browse list → open item → edit item → edit category), that is usually a sign of misuse. Stop and reconsider. The use case diagram reads no better for having a web of relationships — clarity is the entire point.

### «extend» Relationship

The «extend» relationship also connects two use cases, but the arrow direction is **reversed**: the arrow goes from the extending (child) use case **toward** the use case it extends (the parent).

The notation says: "B extends A" — meaning B **may** occur inside A, but only if a specified condition is met at a defined **extension point**.

Key difference from «include»:
- «include»: the child **always** executes when the parent executes.
- «extend»: the child **may or may not** execute — it is conditional.

**Extension points are mandatory.** Every «extend» relationship must have an extension point defined — a named location in the parent use case scenario where, if the condition is met, the extending behavior kicks in. If there is no extension point, there is no way to know under what circumstances the extension occurs, which makes the diagram meaningless.

Summary in plain terms:
- If A **includes** B: A cannot occur without B also occurring.
- If B **extends** A: A can run perfectly well without B, but B can optionally trigger at the named extension point if the condition holds.

**Warning:** When students see both «include» and «extend» after learning them, they often start connecting everything in chains. A chain of «extend» after «extend» is almost always a sign that you are trying to model navigation flow or a sequence of steps — neither of which belongs in a use case diagram. The use case diagram shows **what** the system does, not step-by-step **how** the user navigates through it.

---

## Common Mistakes — Examples

### Mistake 1: Oversized, chained relationships
Students who are excited about «include» and «extend» create a web of connections showing browsing a list → viewing a list item → editing → editing a category — essentially trying to model UI navigation. This is incorrect. The diagram should not describe screen-to-screen flow.

### Mistake 2: Actor names that are states, not roles
A common mistake: "Logged-in User" and "Guest (not logged in)" as actors. **An actor is a role, not a state.** Whether the user is currently logged in or not does not change their role. If I am a warehouse manager, I can log in, log out, and log back in — and I am still a warehouse manager with the same permissions. There is no such actor as "logged-in user." What you have are two roles: **Guest** (an unregistered user) and **User** (a registered user). These are the correct actors. The login/logout themselves become use cases.

### Mistake 3: Inflated actor figures
If the diagram feels too sparse, some students enlarge actor figures to fill space. Do not do this — all elements should be a standard size. Inflating figures just makes the diagram look odd.

### Mistake 4: Starting with packages instead of use cases
Never design a use case diagram by first creating packages/subsystems. First draw all the actors and use cases, see how they relate, and only then — if the diagram becomes hard to read — group elements into packages.

---

## Grouping Use Cases into Packages (Subsystems)

There is only one valid reason to group use cases into packages: **to improve readability**. Not architecture. Not system design.

**Process:**
1. First draw all actors and use cases.
2. Connect them with relationships.
3. If the diagram becomes hard to read, only then start grouping into packages.

Never start by drawing packages. The most common natural grouping is by actor: all use cases for Actor A in one package, all for Actor B in another. This is usually the clearest.

**Guideline:** Aim for roughly 5–10 use cases per package. Do not create packages with only one use case — that defeats the purpose.

If the diagram is very large, you can do a two-level presentation: a high-level diagram showing only packages, and then detailed diagrams for each package. But overusing this approach makes reading harder, not easier — you have to jump back and forth.

---

## Specifying Use Cases: Tables

Each use case can be further specified using a structured table (pre-conditions, post-conditions, main scenario, alternative scenarios). You have probably filled out such tables by hand before.

In the modeling tool we are using (Enterprise Architect), if you set up the correct profile, the tool can **generate these tables automatically** into a Word report — provided you fill in the data fields in the model. I will show you how to do this in the tool. I strongly recommend using this generated output rather than writing tables manually — it is much easier to maintain consistency, and if something changes you can regenerate.

---

## Live Modeling: Coffee Vending Machine Management System

### System Description (recap from Lecture 1)

The system manages a network of coffee vending machines. The problems the system solves:
- Maintenance supervisors do not know when they need to travel to a machine — they waste trips, or miss necessary ones.
- The company wants to attract customers: show machine locations on a map, send discount codes.

The system should:
- Allow querying the machines for their current status.
- Send a notification (SMS) when a machine needs attention.
- Let customers view machine locations on a map and view discount messages.
- Let supervisors manage the machines (add, edit, delete, query status).

### Actors Identified

**Buyer (Customer / Purchaser):**
Can perform:
- View vending machine locations (on a map via an external map service such as Google Maps)
- View detailed information about a specific machine (extend of the above, triggered when user drills in from the map)
- Register
- Log in
- Log out
- Edit profile
- Reset password ("forgot password") — triggered as an extend off the "Log in" use case, requiring an external email service actor
- View messages (discount notifications)
- Delete messages

**Guest (Unregistered user):**
Can perform:
- View vending machine locations (map — same as above)
- Register

Note: A guest cannot log in (they are not yet registered), cannot log out, cannot edit a profile, and cannot view messages. The correct modeling approach is to use actor inheritance: create a base **User** actor with common use cases (Log in, Log out, Edit profile), and then have **Buyer** inherit from User. The Guest only gets the map and Register use cases. This avoids the anti-pattern of modeling "Logged-in user" vs "Guest" as different states of the same actor.

**Supervisor (Maintenance Technician):**
Inherits login/logout/profile from the base User actor.
Additionally can:
- View list of assigned machines
- Add a new machine
- Edit machine details
- Delete a machine
- Query machine statuses (manually triggered)
- Receive SMS notification when maintenance is required

**System-triggered use case (no human actor):**
The system itself periodically queries all machines (e.g., every hour) and sends an SMS if any machine needs servicing. This can be modeled as a "floating" use case (no actor connected) — which by convention we interpret as system-triggered — or by adding a **Timer / Scheduler** actor representing the time-based trigger. Either approach is acceptable.

**External system actors:**
- **Map Service** (e.g., Google Maps / OpenStreetMap) — needed for the "View machine locations on map" use case.
- **Vending Machine** — an external actor (a device) that responds to status queries.
- **Mobile Network Operator / SMS Gateway** — needed for the "Send SMS notification" use case.
- **Email Service** — needed for the "Reset password" use case (sends a reset link/token).

### Modeling Notes from the Live Demo

**«extend» with extension points:**
When a user views machine locations on the map and drills into a specific machine for details ("View detailed machine info"), this is modeled as an «extend» with an extension point named something like "User selects machine on map." The extension only fires when that condition is true — browsing the map without drilling in does not trigger the extended use case.

**Multiple «extend» from the same extension point:**
If two different extending use cases share the same extension point, they will both fire when that condition is met. If they have separate conditions, create separate extension points — one per extending use case.

**Deleting from diagram vs. deleting from model:**
In Enterprise Architect, pressing Delete on an element removes it from the diagram but leaves it in the model tree. To remove it from the model entirely, use Ctrl+Delete. Keep your model clean — do not leave orphan elements floating in the model tree.

**Element numbering:**
To enable automatic numbering of use cases and actors (e.g., UC-1, A-1), change the active **profile** in Enterprise Architect (File → Profile). With the correct profile enabled, a numbering menu appears, allowing you to add prefixes to element names.

**Compact view of «extend» extension points:**
When extension points are shown inline in the use case ellipse, the element becomes very large and hard to read. Click the small minus/collapse button to collapse the extension point display — the connection label still shows the extension point name, so readability is preserved while saving space.

**Packages / subsystems:**
Once you have all use cases drawn, if the diagram is getting crowded, drag related use cases into a package. In Enterprise Architect, drag the elements into the package shape on the canvas — this also moves them into the package in the model tree. For example:
- Package "User Subsystem" — contains all buyer/guest related use cases.
- Package "Supervisor Subsystem" — contains all maintenance-related use cases.

Actors remain outside the package boundaries (they are external to the system boundary by definition).

---

## Summary: Key Principles

- A use case diagram shows **what** the system does and **who** can do it — not how it is implemented, not navigation flow, not architecture.
- Every use case must deliver a **meaningful, observable result**.
- **«include»**: mandatory — always runs when the parent runs. Arrow points from parent to included child.
- **«extend»**: conditional — only runs if an extension point condition is met. Arrow points from extending child toward the parent. **Always define an extension point.**
- **Actors are roles, not states.** Never use "logged-in user" as an actor.
- **Do not start with packages.** Draw use cases and actors first; structure second.
- **UML is not a perfect language.** Know when it is appropriate to bend a rule, and when a rule is strict (e.g., you must never draw an association between two use cases).
- In modeling, there is rarely a single correct answer. The goal is to make the best informed trade-off, not to seek a perfect solution.

I have now covered everything I wanted to tell you today. Thank you for your patience. If you have questions, you are welcome to stay and ask.
