# Lecture 3 — UML Activity Diagrams: Theory and Practical Modeling

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- The role of Activity Diagrams in the requirements specification phase
- Core Activity Diagram concepts: activity, action, structured activity, object node, control node
- Action types: basic action, call behavior action, signal sending, signal receipt, time event
- Structured activities: conditional (if), loop — and their equivalents using decision/merge nodes
- Control flow nodes: initial node, activity final node, flow final node, fork, join, decision (split), merge
- Guard conditions and their notation in square brackets
- Swimlanes (partitions) and their use to represent responsible actors/subsystems
- Showing objects and object states in activity diagrams (dependency on class and state machine diagrams)
- Relationship between activity diagram steps and use case diagram include/extend relationships
- Practical live modeling: drawing activity diagrams in MagicDraw/Cameo for two use cases — "View Messages" and "Poll Vending Machines"
- Common diagramming errors and how to avoid them: ambiguous parallelism, incorrect use of join vs. merge, incorrect terminal node usage, crossing flow lines
- Diagram readability and layout best practices
- Handling tool-specific issues (MagicDraw/Cameo bugs and workarounds)
- Modeling external actors (mobile network operator) and signal semantics
- Iterating over a collection of objects and deciding when to send SMS notifications

---

## Introduction and Context

**Lina Čeponienė:** This process — which should already be boring you to tears by the time I finish telling you about it — is still at the requirements specification stage. Last time we covered use case diagrams, and today we will talk about activity diagrams. These are the means by which we describe each individual use case in more detail.

So in order — activity diagrams. I would very much like my remote to work in just a moment. Well, an activity diagram is what it is called.

## What Is an Activity Diagram?

The activity diagram is yet another behavioral-type diagram, which belongs to that same UML branch. We have already ticked off the use case diagram, and after this lecture we will tick off the activity diagram as well — you will know everything about it perfectly. First, what is an activity, and what is the difference between the concepts of activity and action?

An active activity — an action, a step, right? In general, an activity or an activity diagram — which is the diagram — is a means of describing a process, and it can be used in many different ways. It can even be used to describe things that are not computerized — to describe processes that happen in general life, to explain them to others, or to describe some algorithm.

In that sense, it is simply a tool for describing a process, and which process we choose is our own business. In this module we will use it to describe the scenario of each individual use case. Each one — let me remind you once more so there are no misunderstandings later, with someone saying "I thought only one diagram was needed" — no, you need to describe every use case that you have drawn. This is also an excellent tool for checking whether you have drawn the right use cases, because when you start thinking "wait, there is nothing to show in the activity diagram for this use case," it is very likely that the use case itself does not exist, and this is the moment you realize that you can correct things.

An activity is, in principle, some kind of behavior that is represented as a flow of actions — which is a full analogy to a flowchart, right? Everything you see on the side there is an activity. At the top it even says that it is an activity. It has a beginning, an end, and some sequence of actions.

## Node Types Inside an Activity

Now, what kinds of activity nodes can there be? There can simply be an action — any action — or there can be a structured activity, an object node, and a control node. Let us talk about each one in more detail.

### Action Types

Actions — there are very many different types. If I opened the action type selection in the tool, which I do not recommend, it found forty-two variants. We will definitely not use all thirty-two — we do not need them.

But the basic ones that you will most often need — I would like you to know those. The first is simply an **action**: you see the action shape and inside it is text describing what is done. The next variant is a **call behavior action**, which is a reference to another behavior, another activity. In our case it will be a reference to another activity diagram. How to recognize that it is a call behavior action: either you see the rake symbol (fork icon), or the colon in the name, or both.

Either of those two symbols tells you that this is a reference, meaning that if you click on this action, another diagram will be hidden underneath it.

Next, there can be a **signal sending** action — we are handing something to someone as a signal, rather than simply performing an action. And there can be a **signal receipt** event — some signal arrives to us. There can also be a **time event**, shown by a clock icon, which can be either at a specific point in time (an absolute time event) or an "after" event — a relative time event after some duration.

For further variants, do not go deeper — just know that there are many different types, but you truly do not need to use them all.

### Structured Activities

**Structured activity** — you should not overuse it, but it simply contains other actions inside it. We place actions inside it, because you cannot place one action inside another unless it is a structured activity.

A structured activity can be **conditional** — that is, if we want to show an if-branch. We declare it as a structured activity with a conditional type, but the same result can be achieved using a decision node and a merge node. The latter is often preferred in practice and looks nicer in some ways, but the structured activity has one problem: if the conditional branch needs to cross multiple swimlanes (I will explain swimlanes later), it cannot be done with the structured node. Then you must use decision and merge nodes. For that reason the decision/merge approach is more commonly used in practice, as it has fewer restrictions.

The same applies to a **loop**: you can represent it as a structured activity, or you can achieve exactly the same result with a decision node and a merge/join node. In practice the latter is more common.

### Object Nodes

There is one more thing I would like you to see so that you are not surprised when you encounter it: the **object node**. In order to place an object node in a diagram, I first need to have a class in my model whose instance I will place there. If I do not have a class yet, I can still place the object, but it will just be meaningless text.

You can pass that object from action to action. You can show this directly with a flow line, or you can show it through **pins** — small squares on the side of the action shape — which also represent the same thing. Both representations mean exactly the same thing.

There is also a variant called an **expansion region**, which shows a structured activity where we pass in a collection of objects, execute actions on each object, and produce an output collection. The input collection comes in, the actions execute on each element, and the output collection exits. In practice this means we have a loop over a collection.

## Control Flow Nodes

### Initial and Final Nodes

The most basic control flow is this: there is always exactly one initial node (solid filled circle) at the top. Then there are two types of final node.

The first type is the **activity final node** (solid circle inside a circle, like a bull's-eye). When any flow in the diagram reaches this node, everything in the diagram terminates — whatever parallel flows may still be running, they all stop.

The second type is the **flow final node** (circle with an X, like a light bulb in an electrical schematic). This only terminates the one flow that reaches it; all other parallel flows can continue running normally.

I have seen many times that students, seeing two end node variants, choose based on aesthetics. Know that they have completely different meanings. If you have no parallelism in your diagram, always use the activity final node — no question. If you have parallelism, think about which one you need at which moment. You can have multiple final nodes in a diagram, but the general recommendation is to converge to a single one. When you have parallel flows that you want to terminate differently, you may use different node types, but always use them deliberately.

### Fork and Join

A **fork** (a thick horizontal or vertical bar with one incoming flow and multiple outgoing flows) launches as many concurrent parallel flows as there are outgoing edges. You can launch ten if you want; launching fewer than two probably does not make sense. There is no waiting at the fork — execution simply reaches that point and all the parallel flows start. UML does not specify whether they start simultaneously or in sequence; it only states that they may all start.

A **join** (the same thick bar shape, but with multiple incoming flows and one outgoing flow) does the opposite — it does not let execution pass until all incoming flows have arrived. If one flow completes but another never does, execution will stall at the join forever.

### Decision and Merge

A **decision node** (diamond shape) is a branch point. It is not an action — nothing happens there. Execution simply passes through and is directed either this way or that way depending on the guard condition on each outgoing edge. You must not put any action logic inside the decision node itself; place an action before the decision node if something must happen.

Guard conditions are written in square brackets on each outgoing edge. This is the recommended style. An alternative style is to write a question at the decision node and write the answers on the branches, but that style is more appropriate for non-computerized processes. For our work, always use guards in square brackets — one on each branch, clearly stating what must be true for that branch to be taken. Do not write just "yes" or "no" — write a meaningful condition so anyone reading it immediately understands what must hold.

A **merge node** (same diamond shape) merges multiple incoming control flows: any flow that arrives simply passes through, regardless of how many flows arrive and regardless of which one arrives first. Note that a decision node and a merge node look identical in standard UML notation (only the tool may color them differently as a display aid, which is not part of the standard).

A decision node can also function simultaneously as a merge node if it has both multiple incoming and multiple outgoing flows — that is a valid combination and is useful when you want to both merge and branch at the same point.

## Guard Conditions

Guards are placed in square brackets on the outgoing edges of a decision node. The guard must evaluate to true for flow to proceed along that edge. Make sure that the set of guards covers all possible outcomes — at minimum, include an "else" branch to catch any case not covered by the other guards. A well-formed guard reads clearly: a reader looking at the condition should immediately understand what state or value must hold.

## Parallelism — Common Errors

### Ambiguous Fan-out / Fan-in

If multiple edges leave a single action node without a fork, or multiple edges enter a single action without a join, this is called **poorly defined parallelism** and is treated as a modeling error. The diagram reader cannot tell whether the flows are parallel or conditional.

- If you intend **parallel** flows, use a **fork**.
- If you intend **alternative** flows (one or the other), use a **decision node**.
- Never leave multiple outgoing or incoming edges on an action without an explicit fork/join or decision/merge.

An action that has two incoming edges and no join before it is also an error: it will never execute because both flows must arrive, but since no fork produced them, they never both arrive. This is a deadlock by construction.

## Swimlanes (Partitions)

**Swimlanes** (also called partitions) are vertical or horizontal regions of the diagram that show who is responsible for the actions placed inside them. We will use swimlanes to show the participating actors and the system. Swimlanes can be vertical or horizontal — even stepped — but the principle is always the same: actions are placed inside the lane of the party responsible for them.

## Objects and Object States in Activity Diagrams

Another thing you may need in an activity diagram — but which you cannot do yet because you do not have a class diagram — is showing objects and their states as they pass between actions. To do this properly, you need both a class diagram (to have the class) and a state machine diagram for that class. After the next lecture on class diagrams, and the one after that on state machine diagrams, this diagram type will be clearer. For now, just note that it is possible to annotate flows with an object of class "Order" in state "Submitted," for example.

## Relationship Between Activity Diagrams and Use Case Diagrams

Activity diagrams and use case diagrams are tightly coupled. When you draw an action in an activity diagram using a call behavior action (with the rake icon or colon), it means that action is linked to another activity diagram — it is essentially a reference to a use case. This corresponds directly to an include or extend relationship in the use case diagram.

The relationship is bidirectional: if you have an include or extend in the use case diagram, that means somewhere in the activity diagram there must be a call behavior action pointing to the included/extended use case. You cannot add such a call behavior action if there is no corresponding include/extend in the use case diagram, and conversely, if there is such a relationship in the use case diagram it must be visible in the activity diagram. One reflects the other.

## Practical Demonstration: Modeling in MagicDraw/Cameo

### General Workflow

When creating activity diagrams, I do not create new packages or extra elements in the model tree. Since I already have a use case model with all its elements, I simply navigate to the relevant use case and create an activity diagram for it. I right-click on the use case in the model tree and create an activity diagram (Activity diagram type).

I recommend keeping the fork icon indicator visible on call behavior actions — it helps you see which use cases already have a diagram created and which do not. Once all diagrams are created, you can select all use case elements at once via the menu and toggle off the indicator.

To navigate between diagrams conveniently, use the back and forward buttons in the top navigation bar of the tool.

When resizing the frame of a diagram, always try to make it as compact as possible while still fitting the content. Diagrams that are too large waste space in reports.

**Key naming principle:** Name actions in general, implementation-neutral terms. Do not say "click the Message Inbox button" — say "select message inbox" instead. The implementation may use a button, or it may use a menu; you do not need to commit to that now. Abstract naming gives the implementers freedom and means you will not need to come back and revise.

### Example 1: "View Messages" Use Case

The use case is connected to actors including the Buyer. The swimlanes will include the Buyer and the system (represented by the User subsystem).

**Flow:**
1. The Buyer selects message inbox (in the Buyer swimlane).
2. The system displays the message inbox window (in the System swimlane).
3. A decision node: does the Buyer want to do anything?
   - If yes (guard: `[wants to view a message]`): the Buyer selects a message; the system displays the message window.
   - A merge node combines the "viewed" path with the "nothing selected" path.
4. Another decision node: does the Buyer want to delete messages?
   - If yes (guard: `[wants to delete]`): this is handled by the "Delete Messages" use case, which is shown as a call behavior action (rake icon).
   - If no (guard: `[else]`): flow skips that step.
5. Activity ends with an activity final node.

**Note on the extend relationship:** Because there is an extend relationship on "Delete Messages," the call behavior action for deletion must appear in this activity diagram. If you include such a call behavior action here, there must be a corresponding include or extend in the use case diagram.

The "Delete Messages" use case was described by the customer as a bulk operation: the user marks multiple messages with checkboxes and then confirms deletion. So the flow of "Delete Messages" is:
1. Buyer selects the deletion mode.
2. System displays the message list with checkboxes (marking list).
3. Buyer marks messages for deletion.
4. Buyer confirms deletion (a separate action, or it can be merged into the marking step if the step is named to encompass both).
5. System deletes the marked messages.
6. System refreshes and shows the updated message list (without the deleted ones).
7. Activity final node.

**Diagram layout advice:** When positioning elements, make sure flow lines do not cross each other. Crossing lines make the diagram very hard to read. If you are placing it in a bachelor's thesis report, reviewers who see a clean diagram will pass over it without stopping; those who see a messy one will stop and scrutinize every detail — often finding functional errors. Lay things out cleanly so your diagram passes the eye test as well as the correctness test.

Use the alignment and centering tools in the toolbar (center vertically, align to edge, make same size) to tidy up your elements once the structure is in place.

If a validation warning (red highlight) appears on an element, it usually means the element is visually overlapping a swimlane boundary without actually belonging to it. Fix this by dragging the element fully inside its correct lane. Avoid using the "ignore" option — fix the underlying layout issue instead.

### Example 2: "Poll Vending Machines" Use Case

This use case is more complex: there are multiple actors (the Supervisor, the system itself, and the vending machines as external entities), an extend relationship, and a periodic system-triggered flow.

**Swimlanes:** Supervisor, System (Vending Machine Maintenance Subsystem), Vending Machine.

**Trigger:** The poll can be initiated in two ways:
- Manually by the Supervisor (the Supervisor selects "Start poll" in the vending machine list view).
- Automatically by the system after a configured polling period (a time event: `after [configured polling period]`).

Both triggers are modeled as separate incoming flows into the main query loop, connected through a merge node.

**Precondition (shown as a note on the initial transition):** The Supervisor must be viewing the vending machine list (applicable to the manual trigger).

**Flow after trigger:**

If manually triggered:
1. The Supervisor selects "Start poll."
2. The system notifies: "Poll started" (so the user knows the process has begun, since the vending machines respond slowly — the list goes grey while awaiting results).

If system-triggered (time event):
- No notification needed — no human initiated it. Flow skips the notification step.

Both flows merge, then the core polling loop begins:

**Loop (using decision + merge nodes):**
- Decision: `[not all vending machines polled]` → proceed to query loop body.
- `[all vending machines polled]` → exit loop.

**Loop body (in the Vending Machine swimlane / System swimlane):**
1. System queries vending machine status (sends a request to the vending machine).
2. Vending machine provides status information (signal or call behavior action back to system).
3. If manually triggered: System updates the vending machine's status in the on-screen list (so the row changes from grey to its real status indicator — green, red, etc.).
   - If system-triggered: No screen update needed (no one is watching the list). Decision: `[supervisor initiated]` → update list; `[else]` → skip.
4. System checks whether maintenance is required.
   - Decision: `[maintenance required]` → add to maintenance-needed list; `[else]` → skip.
5. Loop back to check whether all machines have been polled.

**After the loop (all machines polled):**
1. Decision: `[maintenance-needed list is not empty]` → send SMS notification to Supervisor; `[else]` → do not send.

**Send SMS sub-process** (shown as a separate activity diagram, accessible via call behavior action):

Actors: System (Vending Machine Maintenance Subsystem), Mobile Network Operator.

1. System compiles the SMS text (formats the list of machines needing maintenance, retrieves Supervisor's phone number).
2. System sends the SMS via the Mobile Network Operator (shown as a signal send action towards the Mobile Network Operator swimlane).
3. Mobile Network Operator transmits the SMS (their internal processing is not modeled — we only care that they return a result).
4. Mobile Network Operator provides a delivery result.
5. System checks the delivery result:
   - Decision: `[sent successfully]` → proceed to end; `[else]` → retry logic.
   - Retry: the number of retries needs to be agreed upon (e.g., three attempts before escalating). If all retries fail: notify the Administrator (which requires a separate use case "View Failed SMS Notifications" in the use case diagram, and a corresponding additional actor — an email recipient or administrator).

**After SMS sub-process:** If manually triggered, the system notifies: "Poll complete." If system-triggered, no notification is needed. Decision: `[supervisor initiated]` → send notification; `[else]` → end.

**Activity final node.**

**Important note on the Mobile Network Operator lane:** Do not model the internals of the mobile network operator's process — we do not implement that side. The only thing we show from their side is that they provide a delivery result back to us. This is the boundary of our system responsibility.

**Important design note on SMS sending:** The business decision was that one poll should produce at most one SMS, not one SMS per vending machine. If there are thirty machines and we send one SMS per machine, the cost to the mobile operator will be enormous. Therefore: collect all machines needing service into a single list during the loop, and send one consolidated SMS after the loop completes.

## General Best Practices and Common Mistakes

### When to Use Fork/Join vs. Decision/Merge

- Use **fork** when you intend two or more flows to happen concurrently (in parallel).
- Use **decision** when you intend exactly one of several alternative flows to happen.
- Use **join** when you need all parallel flows to complete before proceeding.
- Use **merge** when any one of several flows arriving is sufficient to proceed.
- A decision node can double as a merge node (multiple inputs, multiple outputs) — this is valid and avoids adding an extra element.
- Never leave multiple edges entering or leaving an action without an explicit fork/join or decision/merge.

### Deadlock Patterns to Avoid

A join that waits for two incoming flows, where those flows were not produced by a fork (so they can never both arrive), will deadlock forever. This is a modeling error. Always trace your flows: if two edges enter a join, make sure a fork upstream produced them both.

### Activity Final vs. Flow Final

- Use **activity final** (`⊙`) when reaching this node should terminate the entire activity, including any parallel flows still running.
- Use **flow final** (`⊗`) when reaching this node only terminates the one flow that reached it; other parallel flows continue.
- If there is no parallelism, use activity final exclusively.
- If there is parallelism, choose consciously which termination behavior you need at each endpoint.

### Diagram Completeness and Consistency

- Every use case that you drew in the use case diagram needs its own activity diagram.
- If an activity diagram contains a call behavior action (rake symbol), the corresponding use case diagram must have an include or extend relationship pointing to that sub-use case. The two diagrams must stay in sync.
- You can check whether all use cases have been given an activity diagram by looking at the model tree: each use case should have a child activity diagram beneath it in the tree.

### Naming Actions

- Write action names at a conceptual level — not UI-implementation level.
- "Select message inbox" is better than "click the Message Inbox button."
- This avoids locking down implementation details prematurely and avoids the need to revise diagrams if the UI design changes.

### Layout and Readability

- Minimize crossing flow lines.
- Use the tool's alignment, centering, and equal-size features.
- Imagine your diagram placed on a page in a final report — if it looks messy, reviewers will scrutinize every detail. If it looks clean, they will accept it and move on.
- Every element you add must belong fully inside the correct swimlane (not straddling a boundary), or the tool's validator will flag it.

### Tool Tips (MagicDraw/Cameo)

- When dragging an element onto an existing flow line, the tool will ask whether to insert it before or after the edge. If the edge has no label or guard, placement does not matter.
- To wrap long text inside an action shape, go to the element's Properties → Display and check the wrap option.
- Decision and merge nodes look identical in standard UML. The tool may display them differently (filled vs. unfilled diamond) depending on a display option. That colored rendering is a tool convenience, not part of the UML standard.
- To re-type an element (e.g., change a merge into a decision), use right-click → Refactor → Convert To.
- If the tool prevents you from connecting more than a certain number of arrows into a single element (a known bug in some versions), refactor the element through a merge node and back, and the connection limit usually resets.
- If validation errors (red highlights) appear because actions sit on a swimlane boundary rather than inside it, drag them fully inside the correct swimlane. The red color will disappear once the tool recognizes the proper containment.
- Use back/forward navigation buttons to move between diagrams quickly.

### On Copying Examples

Never use "because that's what the example showed" as a justification for a modeling decision during a lab defense. What is correct in one domain or system scenario may be completely wrong in another. You must be able to justify each choice based on your own system's logic and domain. The example is a guide, not a template. Giving "it was an example" as an answer will cost you marks.

## Closing Remarks

That covers all the theoretical content about activity diagrams. You can now put a checkmark next to "activity diagrams" — you know them well. The next steps are to draw the remaining diagrams for your own project. Draw several different ones to get variety — some simple, some more complex, involving parallel flows, time events, and call behavior actions. The next lectures will cover class diagrams and then state machine diagrams, after which the object and state node features of activity diagrams will also make full sense.
