# Lecture 7 — Sequence Diagrams: Elements, Combined Fragments, and Live Modeling

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Overview of UML interaction diagram types (sequence, communication, timing, interaction overview)
- Sequence diagram elements: lifelines, activation bars, messages
- Message types: synchronous, asynchronous, reply, create, destroy, self-call, recursive
- Combined fragments: alt, opt, loop, par, ref (interaction use)
- Constraint on reply messages (a reply can only go back to the caller)
- Navigation between UI windows and why it breaks the standard reply model
- Consistency between sequence diagrams and class diagrams (operations must exist)
- MVC/BCE architecture rules in sequence diagrams (boundary, controller, entity)
- Live modeling demo: "Poll Machines" use case — start poll, query each machine, save results, send SMS notification
- Live modeling demo: "Browse Messages" use case — navigation pattern

---

## Introduction and Course Context

**Lina Čeponienė:** Today we are covering one more diagram type that belongs to the project phase — the sequence diagram. You can see here what you will need for the test: use case diagrams, activity diagrams, class diagrams, state diagrams, package diagrams, sequence diagrams, and again class diagrams (though you already know what those are about). Component and deployment diagrams will be on the exam. So for now we stop here. After this test, the lecturer will take over the rest of the teaching — except that I will still have one more lecture on component and deployment diagrams, and everything else will be his. The exam will cover his portion. For the last test, the relevant diagram is the sequence diagram, which is what we will talk about today.

---

## Interaction Diagrams — Overview

**Lina Čeponienė:** The sequence diagram belongs to a family of UML diagrams called interaction diagrams. All of them describe interaction. Interaction is, broadly speaking, a set of messages exchanged between objects. The difference is just in how they are shown.

The types of interaction diagrams are:

- **Sequence diagram** — the one we will study in depth. It is the most commonly used.
- **Communication diagram** (also called collaboration diagram) — shows the same things but in a completely different visual layout. There is no top-to-bottom time axis; objects send messages to each other in a general network view. It is used much less frequently.
- **Timing diagram** — looks visually similar to a sequence diagram but adds time-related constraints. It is used mainly for modeling real-time systems where the exact duration between actions matters (e.g., fractions of a second). The visual form is different.
- **Interaction overview diagram** — think of it as a hybrid of an activity diagram and sequence diagrams. Each node in an activity diagram would be a small sequence diagram. It is a way of composing sequence diagrams into a larger process overview.

Of these, the sequence diagram is used most often. The others are good to know exist; if you ever need them in practice, knowing they exist is enough to go and figure them out.

---

## Sequence Diagram — Basic Elements

**Lina Čeponienė:** You have already drawn sequence diagrams — very, very simplified ones, just to get a first look. Do not be fooled into thinking they are always that simple. They are in reality much more complex than what you did in Fundamentals of Information Systems. The basic elements are lifelines and messages.

Roughly speaking: there are the vertical sticks with rectangles at the top, and there are messages (arrows) that travel between them.

There are also what are called interaction fragments — more on those shortly. These can be a message send/receive event, an activation bar (when an object is doing something), or state variants. And then there are combined fragments — the big rectangles — where we draw conditions, loops, and interaction uses (references to other sequence diagrams).

### Lifelines

A lifeline represents an object. We show what class that object belongs to. Most often we do not give the object a name — the part before the colon in the label is the object name, and it is usually left blank. However, to include a lifeline in a sequence diagram, that class must exist somewhere in the class diagram. To be more precise, UML uses the term *classifier* (which is broader than class — it can also be an actor, etc.). The element you bring in as a lifeline should exist elsewhere in the model.

By default, a lifeline is considered to always be alive throughout the diagram. However, there are messages that create or destroy an object, which we will discuss shortly.

### Activation Bar

The activation bar is a thin rectangle drawn on top of a lifeline's dashed line. It shows that the object is currently doing something. For example, one object is active (executing) while another is waiting — because it sent a message and is now waiting for the return. Both ends can be active at the same time when execution is nested.

There is a practical tool issue where activation bars may appear split between messages. You do not need to worry about this — in reality, activation should be continuous. You can stretch the bars to merge them, or simply ignore the visual gap. It is purely a tooling artifact.

---

## Messages — Types and Rules

**Lina Čeponienė:** A message is a send event and a receive event. That is the whole specification — nothing more. It defines how the lifelines communicate.

### Message Types

| Type | Description |
|---|---|
| **Synchronous call** | Filled arrowhead. Waits for a response. |
| **Asynchronous call / signal** | Open arrowhead. Does not wait for a response. |
| **Reply** | Dashed line with open arrowhead. Can only appear after a synchronous call; returns to the caller. |
| **Create** | Looks like an asynchronous call, but always points to the top of the target's lifeline box — it creates a new object. |
| **Destroy** | Points to a large X at the end of a lifeline — the object is destroyed at that point. |
| **Self-call** | A message that loops back to the same lifeline — the object calls one of its own operations. |
| **Recursive call** | Looks similar to a self-call but includes an additional nested activation rectangle. Use only where actual recursion is intended. |

### Reply Message — Strict Grammar

A reply message can only return to the object that made the original synchronous call. It is impossible to send a reply to an object that never called you. Think of it like code: a method's `return` can only go back to the caller. There is no way to return to someone who did not call you. In standard object-oriented languages, this is simply not how it works.

Therefore: a reply always follows a call, and always goes back to the caller. It can never go sideways or to a random third party.

### Asynchronous vs. Synchronous — When to Use Which

If we implement a technology where a call means we wait for the result, we show a synchronous call. Most common programming languages work this way. If we are launching parallel tasks and we do not care about waiting — for example, firing multiple requests simultaneously — then we show an asynchronous call.

Create and destroy messages are used less often. Destruction is mainly relevant when you explicitly manage memory. In modern frameworks, garbage collectors and other mechanisms usually handle this automatically.

### Found and Lost Messages

These are exotic but worth knowing:

- **Found message** (found end): We do not know who sent it, but we know who received it.
- **Lost message** (lost end): We know who sent it, but we do not know who received it.

The logic is: the message arrived from somewhere we do not model, or it was sent out to somewhere we do not model. Be aware of these; they exist.

### Recursive Message

A recursive message looks very similar to a self-call but has an additional activation rectangle nested inside it. Students sometimes confuse self-calls with recursion — be careful. Use recursion only where actual recursion exists in the logic. Do not place it randomly.

---

## Reply Messages and Synchronous Calls — Practical Note

**Lina Čeponienė:** There are different conventions. Some people say: since all synchronous calls implicitly have a reply, we do not need to draw replies at all — just assume they are there. We will not follow that convention. In this course, we always show replies explicitly, except for one problematic situation involving navigation, which I will explain shortly. The reason is: until you have learned to draw diagrams fully and correctly, it is better to practice showing everything. Once you understand the full picture, you can make informed decisions about what to omit.

The rule is: if you have a synchronous operation call, and no reply message comes back, that is an error — unless it is navigation between windows (see below).

---

## Sequence Diagram and Class Diagram Consistency

**Lina Čeponienė:** When a message goes from one lifeline to another and the name has parentheses, that means it is an operation call. This has implications for the class diagram: the receiving class must have that operation. If you call an operation on class B, but class B does not have that operation, that is a mistake.

This is easily fixed: when you draw a sequence diagram and type in a message name with parentheses (an operation call), the tool will create that operation in the corresponding class automatically if you press the green "create" button. Be careful not to do this carelessly and end up with duplicate operations (multiple operations with the same name but no distinguishing parameters). It is best to either use the autocomplete from existing operations, or be deliberate when creating new ones.

Also: actors cannot have operations. When we send a message to an actor (e.g., showing a pop-up to a human user), we do not create an operation on the actor. We just label it with free text describing what happens (e.g., "display success message to user").

Furthermore: if class A calls an operation on class B, then class A must know about class B — there must be an association (relationship) between them in the class diagram. If you draw a message from one lifeline to another, a navigable association must exist between those two classes in the class diagram. The tool may create this automatically; make sure it is actually there.

---

## Combined Fragments

**Lina Čeponienė:** Combined fragments are the large rectangles drawn over sequence diagrams. They show various control structures. The operator in the top-left corner of the rectangle says what kind of fragment it is.

Each fragment has:
- An **operator** (e.g., `alt`, `opt`, `loop`, `par`, `ref`)
- An **operand condition** — written in square brackets — which specifies when the fragment applies
- **Coverage circles (bullets)** at the top of each lifeline that is involved — these indicate which lifelines participate in the fragment

The coverage circles must be drawn. You can do this by right-clicking the fragment in the tool and selecting the "Covered By" (or equivalent) option.

### Operators

**`alt` (alternative):**
The equivalent of an `if/else`. It always has at least two operands, separated by a dashed horizontal line. Each operand has a guard condition in square brackets. You can have as many branches as needed. It is good practice to always include an `else` branch to cover all cases — otherwise, if none of the conditions is true, the diagram has an undefined state. This is similar to how you handle decision nodes in an activity diagram (you always need to cover all branches).

**`opt` (optional):**
Has only one operand. If the guard condition is true, the contents of the fragment are executed. If the condition is false, the entire fragment is skipped as if it were not there. It cannot have multiple operands separated by dashed lines — that would be `alt`, not `opt`.

**`loop`:**
A loop. If drawn without a guard or count, it implies an infinite loop. To avoid an infinite loop, choose one of two approaches:
- Write a **guard condition** in square brackets — this gives you a `while` loop.
- Write a **repetition count** (a number or variable) in brackets — this gives you a `for` loop.

Note: UML formally allows combining a count and a condition in the same loop, but there is no clearly defined precedence rule for what happens when both are specified simultaneously. It is best practice not to combine them. Use either a condition (while) or a count (for), not both.

**`par` (parallel):**
Shows parallel execution. Separate operands within the fragment run concurrently. You can add as many parallel sections as needed.

**`ref` (interaction use):**
A reference to another sequence diagram. Instead of drawing everything inline, you place a `ref` fragment and name the diagram it refers to. The coverage circles mark which lifelines in the current diagram are also present in the referenced diagram.

---

## Combined Fragments — Practical Example (Cinderella)

**Lina Čeponienė:** I found a fun example to make this less scary. Recall the fairy tale of Cinderella — the prince lost a glass slipper, and had to go around trying it on every girl until he found the right one.

Imagine: the prince is an actor, and there is a class `Girl`. The prince finds a girl and calls `getName()` on her. The return value `n` is the name she tells him. If `n` equals "Cinderella", then the `Girl` object is destroyed and a new `Princess` object is created (though in the full story it should probably be "Queen" — but anyway).

This example uses many sequence diagram elements: a loop, an `opt` fragment (if the name is not the right one, skip and call the next girl), object destruction, and object creation.

If you wanted to show the full loop in the same diagram (iterating through all girls until the right one is found), you would need a `loop` with a `break` when the match is found. However, for simplicity, a single sequence diagram usually just shows what happens when one encounter occurs — we do not model the outer iteration inside the same diagram.

---

## `alt` vs. `opt` — Key Distinction

**Lina Čeponienė:** The difference is:

- `alt` always has at least two sections separated by a dashed line. Each section has a guard condition. One of the sections is selected based on which condition is true.
- `opt` has only one section. If the condition is true, it executes. If false, nothing happens. There are no alternative sections.

---

## Loop Fragment — Detailed Notes

**Lina Čeponienė:** An empty loop with no guard or count is an infinite loop. When asked how many times the loop in a given diagram runs, the answer is: infinitely, if there is no guard or count.

To write a condition, you write it in square brackets next to the `loop` keyword. To write a count, you write the number. For example, `loop [counter > 0]` means "while counter is greater than zero." Or you can write a variable that evaluates to a number.

Do not combine a count and a condition in the same loop, because UML does not formally define which one takes precedence. Use one or the other. You can enter both technically in some tools, but you will end up with a diagram where you cannot tell which wins — 10 iterations, or the condition becoming false earlier.

---

## Interaction Use (ref Fragment)

**Lina Čeponienė:** The `ref` operator is used when one sequence diagram calls out to another sequence diagram. It works analogously to the include relationship in a use case diagram. If a use case A includes use case B, and you are drawing the sequence diagram for use case A, you place a `ref` fragment at the appropriate point. Inside that fragment, you write the name of the sequence diagram it refers to.

For an `extend` relationship (conditional extension), you would place the `ref` inside an `opt` or `alt` fragment to show the condition under which the extension is triggered.

Coverage circles apply to `ref` fragments too: mark the lifelines in the current diagram that also appear in the referenced diagram. You do not need to redraw the internal lifelines of the referenced diagram inside the `ref` box — just note which lifelines from the current diagram are shared.

---

## Navigation Between UI Windows — A Special Problem

**Lina Čeponienė:** A common source of confusion is how to show navigation between UI windows (screens) in a sequence diagram.

When you are on a single screen and no navigation occurs, all messages can have proper replies following normal rules. This is straightforward.

However, when you navigate from one window to another, the original window closes (or becomes inactive). This breaks the standard reply model in two ways:

1. The old window/boundary object no longer exists (or is no longer active), so it cannot receive a reply.
2. The new window was just opened and never sent any call — so there is nothing for the controller to return to.

Concretely: if a controller navigates to a new boundary object (a new window), that new boundary object was never called by anyone. You cannot send it a reply message because it did not call anyone first. It was freshly opened.

This is a known limitation of sequence diagrams when applied to UI navigation. The diagram is not really designed to show window-by-window navigation — it is designed to show how classes communicate internally (messages, interactions). When an actor and a boundary enter the picture with a new window, the strict reply grammar breaks down.

**Practical compromise:** For navigation steps, we omit the reply message. It is the one accepted exception. Everywhere else in the diagram (non-navigation messages), replies are required. So:

- If a message in your sequence diagram is not navigation-related and has no reply — that is an error.
- If a message is navigation (opening a new window) — skip the reply; it is accepted.

If you have ideas on how to represent this better, feel free to suggest them.

---

## Sequence Diagrams and Operations in the Class Diagram

**Lina Čeponienė:** As you draw sequence diagrams for all your use cases, operations accumulate in your class diagrams — in boundaries, controllers, and models. After drawing your sequence diagrams, you must verify that the operations appearing in the sequence diagrams match the operations in your class diagram.

**Practical tip:** When you start typing a message name in the tool, it will suggest existing operations. If it suggests the operation, you are reusing the same one — no duplicate. If you type freely without using the suggestion, you risk creating duplicate operations with the same name. Always check if the tool is offering an autocomplete for an operation you have already created elsewhere.

---

## BCE (Boundary–Controller–Entity) Architecture Rules

**Lina Čeponienė:** In a classical MVC or BCE architecture, there is a strict communication rule:

- A controller may not communicate directly with an external actor or external system — it must go through a boundary.
- The boundary is the system's interface to the outside world.
- A boundary cannot contain business logic — it is just a dumb I/O component. All logic is in the controller.

This principle exists for maintainability. If the external interface changes (e.g., the protocol with an external machine changes), you only need to update the one boundary class, not every controller that uses it. If controllers talked directly to external entities in ten different places, a change would require updating all ten places.

So: when a controller needs to call an external device (e.g., a vending machine), it must go through a boundary class. If there is no boundary class for that external system yet, you must create one.

---

## Live Modeling Demo — "Poll Machines" Use Case

**Lina Čeponienė:** Let us now draw a sequence diagram for the "Start Machine Poll" use case. Last time we created a general architecture overview and started the class diagram. Let me show you how to proceed.

**Starting point:** The Supervisor (actor) is on the machine list screen. They press the "Start Poll" button.

**Step 1 — Entry and trigger:**

The poll can be started in two ways: manually by the supervisor, or automatically by a timer event (e.g., every 30 minutes). These are two alternative triggers. We model this with an `alt` fragment:

- Branch 1: `[started by user]` — the supervisor presses the button
- Branch 2: `[timer event]` — the system clock fires the event

Because we have a timer-based case (found message — we do not know where the timer came from, it just fires), we can model it as a "found message" starting the controller directly.

**Step 2 — Notifying the supervisor:**

After pressing "Start", the supervisor should see a notification that the poll has begun. However, we cannot just send a reply immediately because the system has not finished yet — the poll is still running. Options:

- Have the boundary call a method like `showPollStarted()` asynchronously so that the notification is shown without blocking continued execution.
- Or model it as an asynchronous call so that the boundary displays the message and the controller continues processing in parallel.

We do not close the activation prematurely — we show the message as a self-contained display call to the boundary (using an asynchronous message to it), so that we can continue the rest of the diagram.

**Step 3 — Getting the list of machines:**

The controller does not know which machines to poll. It must first retrieve the list of machines. We add a method like `getAll()` (or `get...()` — consistent naming is important: always use the same prefix pattern such as `get`, `find`, `fetch`, or `select` throughout your project).

Note on language: requirements-phase models were in Lithuanian, but the design model uses English names. All class and method names in the project model should be in English. The lecturer notes that she translates entity names into English for the design model, and that is perfectly acceptable.

The controller calls `getAll()` on the model (e.g., `MachineModel`), and gets back a list of machines (`machineList`).

**Step 4 — Loop over all machines:**

We need to query each machine in turn. This is modeled with a `loop` fragment. The repetition count is the number of machines — e.g., `loop [m]` where `m = machineList.count()` — giving a `for` loop over all machines.

Inside the loop:

1. The controller asks the machine's boundary element (`MachineBoundary`) for its status. Since the controller cannot talk directly to an external machine (BCE rule), it must go through a boundary class.
2. `MachineBoundary` calls `getStatus()` on the actual machine (external actor). Since the machine is an actor, we cannot create an operation on it — we label the message with free text.
3. The machine returns its status information (e.g., how much coffee, sugar, coins remain, and whether it needs service).
4. The controller receives this data and saves a new record in `PollResult` model with a `create()` (or `add()`) call.
5. The controller then checks if the machine needs servicing. This logic can either be hidden inside the main method, or explicitly shown as a separate `checkNeedsService()` self-call on the controller. Both are acceptable.
6. If service is needed (`opt [needsService]`), the controller appends the machine to a service list — modeled as a self-call `appendToServiceList()` (or similar).
7. If the supervisor was the one who started this poll, the UI is updated asynchronously to reflect the updated machine status (the boundary is notified to refresh that machine's row).

**Step 5 — After the loop:**

Once all machines have been polled, the system needs to send an SMS notification to service staff and notify the supervisor that the poll is complete.

For the SMS, we reference a separate sequence diagram using a `ref` fragment for the "Send SMS" interaction. This keeps the current diagram manageable.

The controller then returns a result to the supervisor (via the boundary), confirming the poll completed successfully.

---

## Live Modeling Demo — "Browse Messages" Use Case

**Lina Čeponienė:** Let me briefly show how navigation looks. Consider the "Browse Messages" use case. The activity diagram says: the user selects the "Browse Messages" option, the system shows the message list window, then the user selects a message, and the system shows the message detail window.

For the sequence diagram, we need:
- Actor: Customer (or Buyer)
- Boundary: currently active window (e.g., main menu)
- Controller: handles navigation
- New boundary: message list window (`MessageListBoundary`)
- Another controller: handles message list data
- Model: message data

**Flow:**

1. The customer interacts with the main window boundary. They select "Browse Messages."
2. The main window boundary sends a message to its controller — no operation name, just free text (it is a boundary, it cannot think for itself).
3. The controller decides it needs to navigate to the message list. It tells the new boundary (`MessageListBoundary`) to open. This is a navigation step — no reply is expected back.
4. Meanwhile, the new boundary needs data. It calls its own controller, which retrieves messages from the model.
5. The model returns the message list to the controller, which passes it to the boundary for display.
6. The customer is now at the message list. A lot happened, but from the customer's perspective they just ended up at the new screen.

**The navigation problem again:** Steps 1–3 involve opening a new window. These messages have no reply. All subsequent messages (4 onward) that happen within the same window do have replies. This is the consistent pattern to follow.

**Important:** Do not draw a reply from the new window boundary back to the old controller. That old controller's activation has ended. The new window was not called by anything — it was opened fresh. No reply is possible there. This is the accepted compromise.

---

## Key Takeaways

**Lina Čeponienė:** To summarize what you need to know:

1. The sequence diagram is the most important interaction diagram. The others (communication, timing, interaction overview) are good to know about.
2. Every lifeline corresponds to an element (class, actor) defined elsewhere in the model.
3. A reply message can only return to whoever made the call. Never to a random third party.
4. All synchronous calls must have a reply — except navigation steps (opening a new window), which are the accepted exception.
5. Every operation name shown in a sequence diagram must exist in the corresponding class in the class diagram. Use autocomplete to avoid duplicates.
6. Combined fragments: `alt` for branching, `opt` for single optional block, `loop` for repetition, `par` for parallelism, `ref` for referencing another diagram.
7. Coverage circles on combined fragments must be drawn.
8. In BCE/MVC architecture, controllers may not call external actors directly — always go through a boundary class.
9. Sequence diagrams will show more internal system logic than activity diagrams — steps that were not visible in the activity diagrams (because they are purely internal) will appear here.
10. After drawing all sequence diagrams, verify that the operations in the sequence diagrams are consistent with the operations in the class diagram.

We will see each other next week for the test.
