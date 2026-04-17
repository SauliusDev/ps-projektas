# Lecture 5 — UML State Machine Diagrams

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Overview of UML behavioral diagrams and where state machines fit
- State machine (statechart) diagram fundamentals: states, transitions, triggers, guards, actions
- Pseudo-states: initial, final, terminate, choice, junction, history (H, H*)
- Composite and orthogonal (parallel) states
- Entry/exit points on composite states
- Submachine states
- Practical worked examples: conference paper lifecycle, door states, ATM, SMS message, coffee-machine vending automaton
- How to derive state diagrams from entity class attributes
- Consistency between state diagrams and other UML diagrams (use cases, activity diagrams, class diagrams)
- Lab 1 guidance: how many state diagrams are needed and common student mistakes

---

## Introduction and Context

**Lina Čeponienė:** This is the last topic I need to explain before your first laboratory session. We have already covered use case diagrams, class diagrams, and activity diagrams; what remains is state diagrams, and after this you will be fully ready to defend Lab 1 next week. Do not forget to consult with the lecturer beforehand — state diagrams are probably the hardest diagrams for students to produce independently. In my experience, students usually get them wrong. I suspect most of you have never drawn one before. You have seen class diagrams and activity diagrams to some extent, but state diagrams will be completely new. They are a very useful type of diagram, so let us examine them in detail.

Let us start by situating state machines within UML. We have already covered a good portion of the behavioral diagrams. On the structural side, so far we have only looked at class diagrams (packages come next lecture), but from the behavioral side we have covered quite a bit already. State diagrams are one more behavioral diagram.

---

## What Is a State Machine?

**Lina Čeponienė:** A state machine — you may be more familiar with the term *finite automaton* — is exactly that kind of automaton. It describes states and transitions between them. In principle a state machine can describe many different kinds of things: not only a class, but other model elements as well. That only makes things more complicated, though, and the diagram is already complex enough on its own. So we will take the simplest and clearest approach, which is: we will model the states of a class — specifically, the states of an entity class.

In UML there are two kinds of state machines: **behavioral state machines** and **protocol state machines**. The protocol state machine is a trimmed-down version of the behavioral one. If you master the behavioral variant, understanding the protocol state machine later will be very easy. That is why I will only explain the behavioral variant here; you just need to know that two versions exist, so if you ever need the protocol variant you can orient yourself quickly.

---

## States

**Lina Čeponienė:** A state represents the situation of an object — in our case, a class instance — when it satisfies some condition, is waiting for an event, or is executing some action.

The distinction between these scenarios matters. *Satisfying a condition* is more characteristic of a **passive class** — entities in our model will behave this way. For example, "as long as balance is below zero" or "as long as such-and-such value holds", the object is in a given state. *Executing an action* or *waiting for an event* is more characteristic of an **active class**, such as a controller: the object is doing something, finishes, and then moves on to do something else.

We will focus on passive classes — entity classes — so the "satisfies a condition" interpretation will be most relevant. In essence, a state is a snapshot of an object's attribute values. Given the concrete attributes of a class, the set of attribute values at a particular moment should determine the state. This is one of the first questions we ask: how do you identify which state an object is in from its attribute values?

A state must have a name; everything else is optional. Possible internal activities are **entry** (`entry /`), **exit** (`exit /`), and **do** (`do /`), plus any custom activity labels. For the kinds of states you will be drawing in the lab, these internal activities are rarely needed — I am showing them mainly so you can read a diagram drawn by someone else.

An example of an active-style state: imagine a class in state *Typing Password*. On entry, the input is hidden (masked); on exit, input is shown again; while in the state, if any key is pressed a `do` action runs; if `help` is pressed, a specific handler fires. All of these are optional; the only mandatory element is the name.

---

## Transitions

**Lina Čeponienė:** A transition between states does not have to carry any label at all — you can have two states with an unlabeled arrow between them. However, a transition can have:

- **Trigger** — the event that causes the transition
- **Guard** — a condition (in square brackets) that must be true for the transition to fire
- **Effect/Action** — an action executed during the transition (after a `/`)

The syntax on a transition is: `trigger [guard] / effect`

The semantics: if we are in state S1 and event *e* arrives *and* guard condition *c* is true, we execute action *a* and move to state S2. If the event arrives but the guard is false, nothing happens. If the guard is true but the event has not arrived, nothing happens either. The effect is executed only when the transition actually fires.

---

## Event / Trigger Types

**Lina Čeponienė:** Triggers that cause transitions include several types:

- **Call event** — an operation call on the object
- **Signal event** — receipt of an asynchronous signal
- **Change event** (`when`) — fires whenever a condition becomes true (e.g., balance drops to zero)
- **Time event** — either `after(duration)` (relative) or `at(time-expression)` (absolute), analogous to the `after` and `at` events in activity diagrams

For most of your work, time events and call events are the most likely to be relevant.

---

## Pseudo-States

**Lina Čeponienė:** In addition to real states, state diagrams contain **pseudo-states** — they are not true states; the object cannot reside in them for any duration.

**Initial pseudo-state** looks exactly like the start of an activity diagram (a filled black circle). In a state diagram it marks the initial pseudo-state. A newly created object cannot stay there for even an instant; the tool automatically creates an initial pseudo-state plus a transition to the first real state when you create a new state machine. The transition out of the initial pseudo-state to the first real state must have no guard and no branch — it fires unconditionally the moment the object is created.

**Final state** (a circle with a filled dot inside) indicates that the object has finished its lifecycle — it ceases to exist. If the lifecycle ends normally, this is a final state. If it ends abnormally, UML also provides a **terminate pseudo-state** (an X symbol).

**Choice pseudo-state** (a diamond) is purely a visual convenience — it lets you draw one transition in and multiple transitions out. Logically it is identical to simply drawing multiple outgoing transitions from the source state with different guards. Use a choice node when it makes the diagram tidier. In activity diagrams we tended to use choice nodes as default; in state diagrams you add them only when they genuinely improve readability.

There is also a **junction** (a small filled circle — it looks like a finish node but smaller), which passes through any incoming combination. You can arrive from different sources and leave toward different targets in any combination.

---

## Composite and Orthogonal States

**Lina Čeponienė:** A **composite state** contains nested states inside it. There are two variants:

- **Simple composite state** — one region inside, with its own nested state machine.
- **Orthogonal (parallel) composite state** — multiple regions separated by dashed lines. The object is simultaneously in one state from each region. For example, if there are two regions, the object is in some state from region 1 *and* in some state from region 2 at the same time.

When you have a simple composite state and the transition from outside enters it without specifying an entry point, flow enters at the composite state's own initial pseudo-state. Alternatively, you can use **entry points** (small open circles on the border of the composite state) to enter at a non-default inner state, or **exit points** (similarly, circles with an X) to leave at a non-default inner exit.

A transition into a composite state that targets a nested state directly (rather than the composite's initial pseudo-state) uses an entry point on the boundary.

If you want to reuse the same nested state machine in multiple places, use a **submachine state** — a state whose name is followed by a colon and the name of the referenced state machine (e.g., `StateName : SubMachineName`), or a colon with a special icon. Otherwise, if you just want to show that the state has inner states, it is cleaner to draw the nested states directly inside the composite state, unless reuse across diagrams is needed.

---

## History Pseudo-States

**Lina Čeponienė:** History pseudo-states are relevant inside composite states. They are used when, after leaving and re-entering a composite state, the object should resume in the inner state it was in last time (rather than starting over from the beginning).

**Shallow history (H)** — remembers the most recent active substate at one level of nesting inside the composite state.

**Deep history (H\*)** — remembers the most recent active substate at any depth of nesting.

Example: imagine a washing machine class. Without history, every time you open and close the door, the machine restarts from the *Washing* sub-state regardless of how far through the cycle it was. With a shallow history pseudo-state, when you close the door the machine resumes in whichever sub-state (washing, rinsing, spinning) it was in when the door was opened. With deep history it remembers all the way down through nested levels.

When you use a bare H symbol in the corner of a composite state, you must also show a default transition out of H (to a specific inner state) for the first time the composite state is entered, when there is no history yet. Using `H →` to an inner state specifies "on first entry (no history yet), go here." The H with an outgoing arrow to a specific state combines both: it handles the no-history case.

---

## Practical Example: Conference Paper Lifecycle

**Lina Čeponienė:** Consider a class `ConferencePaper`. This looks similar to an activity diagram but it is not — it has states, not actions.

When a paper object is first created, it is in state **Submitted**. If the trigger *Assign reviewers* arrives, the paper transitions to state **Under Review**. It stays there until the trigger *Calculate rating* arrives. If the rating is acceptable, it transitions to **Accepted**; if not, to **Rejected**. Notice the choice element (a diamond) that could be drawn here instead of two separate arrows — either approach is equivalent.

If the paper object is never deleted or archived, it will simply remain in state *Rejected* or *Accepted* indefinitely — no final state is necessary. However, suppose that when the paper is in state *Accepted* and a time event fires (*after the payment deadline*) and the guard `paid = false` is satisfied, the paper becomes **Not Paid** and lingers there — no one will print it. We can always retrieve it to check. If before that time event fires another trigger arrives — payment is received — the paper transitions from *Accepted* to **Paid** and waits there.

This demonstrates a key point: in a state diagram there is no top-to-bottom sequential process. There are states and transitions between them triggered by events.

---

## Practical Example: Door States (Live Drawing)

**Lina Čeponienė:** Let us build a state diagram for a door, so you can see the process. A door can be in three states: **Open**, **Closed**, and **Locked**.

Step 1: Draw all the states first, without any transitions. Think about what states are possible.

Step 2: Add the initial pseudo-state. When a new door object is created, it is most natural to say it is **Closed**. So the initial pseudo-state points to *Closed*.

Step 3: Work through every possible pair of states and ask whether a transition exists.

- *Closed* → *Open*? Yes. Trigger: **open**. Guard: `locked = false`.
- *Closed* → *Locked*? Yes. Trigger: **lock**.
- *Locked* → *Closed*? Yes. Trigger: **unlock**.
- *Locked* → *Open*? This is not really possible — you cannot open a locked door by simply turning the handle; the model excludes this.
- *Open* → *Locked*? Also excluded — you cannot lock a door while it is open.
- *Open* → *Closed*? Yes. Trigger: **close**.

So we end up with four transitions. A door is never destroyed in this model, so there is no final state. A door is always in one of these three states. That is perfectly valid — a final state in a state diagram is not obligatory.

---

## Practical Example: ATM States (from uml-diagrams.org)

**Lina Čeponienė:** The ATM example is probably the most overused example in UML, but it is very clear. Here is how the ATM state machine works:

When an ATM object is first created, it is in state **Off**. There is no guard on the initial transition (guards on the initial transition are not allowed). When the trigger *Turn on* fires, the action `start` is executed and the ATM transitions to state **Self Test**. From *Self Test* there are two possible exits:

- At any moment during self-test, if the event *Fail* occurs, the ATM immediately transitions to **Out of Service**.
- If self-test completes successfully (no trigger, just the state ending naturally — denoted by a completion transition), the ATM transitions to **Idle**.

From *Out of Service*, if the trigger *Serviced* arrives the ATM transitions to **Maintenance**; if the trigger *Turn off* arrives it returns to **Off**. From *Maintenance*, if everything is successful the ATM goes back to **Idle**; if *Fail* occurs at any time, it returns to *Out of Service*.

From **Idle**, if a card is inserted the ATM transitions to **Serving Customer**. On entering *Serving Customer*, the entry action is *Read card*; on exiting, the exit action is *Eject card*. At any time while in *Serving Customer*, if *Cancel* is received the ATM immediately returns to *Idle* (the exit action still fires, ejecting the card). Once all transactions complete normally (completion transition), it also returns to *Idle*. If a *Fail* event occurs while *Serving Customer*, the ATM goes to *Out of Service*.

Notice: this is not a sequential top-to-bottom process. There are states and you move between them in response to events. This distinction from activity diagrams is crucial.

---

## Key Principle: State Diagrams vs. Activity Diagrams

**Lina Čeponienė:** I am emphasizing this because students commonly confuse them. An activity diagram shows a sequential (or parallel) flow of actions, top to bottom. A state diagram shows states and how an object moves between them in response to external triggers. They look superficially similar but represent completely different things. A state diagram for a passive entity class is not an activity diagram.

---

## Composite State with History: Washing Machine Example

**Lina Čeponienė:** Now let us look at a composite state with history in more detail. Suppose we have an old-style washing machine (the kind where you can open the door at any moment). When the machine is running, it is in either *Washing*, *Rinsing*, or *Spinning*. If at any moment you open the door, the machine pauses; when you close the door again, it starts over from *Washing* — because there is no history.

If we want a smarter machine that resumes where it left off, we use the history pseudo-state (H). When the door is closed, the machine returns to whichever inner state it was in. Note: "return to rinsing" still means starting the rinsing stage fresh (from its beginning), not continuing from some point mid-rinse. But at least it knows it was in *Rinsing*, not *Washing*.

---

## Exam-Style Exercise: Tracing a State Sequence

**Lina Čeponienė:** You will almost certainly get a question like this on the test. I usually vary the details — different state names, different event sequences — but the principle is always the same. Here is the structure of the question: given this state diagram (with a composite state and a shallow history pseudo-state), and given that you start in state S11, and the following sequence of events arrives — tell me which state you end up in.

Example trace:
- Start in S11. Event E1 fires → transition to S12 (inside the composite state S1). ✓
- Now in S12. Event E2 fires → the composite state S1 has a transition on E2 to outer state S2. The composite-level transition overrides any inner-state behavior, so regardless of which inner state we were in, we leave to S2.
- Now in S2. Event E2 fires again → S2 has a transition on E2 back to the composite state. Because there is a history pseudo-state (H), we return to the last inner state, which was S12.
- Now in S12. Event E1 fires → transition to S13.

Correct final state: **S13**. Without history, re-entering the composite state would always go to S11 (the default initial), not S12. With history it goes to the most recently active inner state.

Questions like this will be on the test. Understand this mechanism and you will be able to answer them.

---

## Connecting State Diagrams to the Rest of the Model

**Lina Čeponienė:** I would like you to notice one important point before the first lab. All the diagrams you are drawing are strongly interrelated.

- Actors connected to use cases appear in the use case diagram.
- Includes and extends are visible in the activity diagrams.
- A class that appears in an activity diagram can also have a state diagram.
- If a state diagram is drawn for a class, the states in it must be consistent with the class's attributes.
- States that appear in a state diagram cannot appear out of nowhere — they must be expressible in terms of the class's attribute values.
- Triggers on state transitions must correspond to events that actually occur somewhere in your model — a use case step, an activity diagram action, or something else you can point to.

Objects cannot appear in diagrams if they are not in the class diagram. State diagrams cannot contain states that are not documented. Activity diagrams cannot contain scenarios that do not have a use case. Objects in activity diagrams cannot be attached to unlisted actors. In short: if you change something in one diagram, check whether it has broken consistency with all the others.

You should also be able to show an object node in an activity diagram with a state label in the square brackets. However, you are not required to do this everywhere — only use it when it genuinely clarifies something. Adding object-with-state notation everywhere just clutters the diagram.

---

## Common Mistakes and Lab Guidance

**Lina Čeponienė:** The worst mistake I have ever seen is students drawing a state diagram for the **User** class. States like *Logged in* / *Logged out* seem very useful at first glance, but consider: do you have an attribute in your database (entity) that stores, at any given moment, whether that user is currently logged in? Very rarely. Most typical systems do not need to track live session state at the entity level — that is usually handled by sessions or tokens, not a persistent attribute on the User entity. If your system *does* store such a flag and poll it, then the states are justified. If not, they are not.

The principle is: for a passive entity class, the set of attribute values must be sufficient to determine which state the object is in at any given moment. If you cannot distinguish states from the attribute values, you either need additional attributes or those states are not valid.

The opposite mistake is also common: drawing a state diagram with all the transitions, but without triggers. For entity (passive) classes, every transition must be caused by an external trigger. Entities cannot cause their own state changes. If you cannot name the trigger — some event that occurs somewhere in your system — the transition either does not exist or you have modeled something incorrectly.

**How many state diagrams are needed for Lab 1?** You must produce at least one. If only one entity in your system meaningfully has distinct states, one diagram is fine. If multiple entities clearly have states, you should include diagrams for each of them. During the lab defense, if I see that a class obviously needs a state diagram but you have not drawn one, that is a problem. If you are uncertain, come and consult — we can almost always find a class that warrants one.

---

## Worked Example: SMS Message State Diagram

**Lina Čeponienė:** Let us work through the SMS message entity from our coffee-machine monitoring system. Looking at the activity diagram for "Send SMS", the message goes through the following lifecycle: it is first composed, then handed to the operator for sending, then we receive a result.

Proposed states:
1. **Composed** — the message text has been created.
2. **Handed for Sending** — transferred to the operator.
3. **Sent** — operator confirmed successful delivery.
4. **Send Failed** — operator returned a failure result.

Now, how do we determine state from attribute values? Suppose the class currently only has a `text` attribute. That is not enough to distinguish all four states. We need more attributes.

Let us add:
- `transferredToOperatorAt: DateTime` — set when we hand the message to the operator.
- `isSent: Boolean` — set by the result from the operator.
- `operatorResponseAt: DateTime` — set when we receive the operator's response.

With these attributes:

| State | `text` | `transferredToOperatorAt` | `operatorResponseAt` | `isSent` |
|---|---|---|---|---|
| Composed | not null | null | null | false |
| Handed for Sending | not null | not null | null | false |
| Sent | not null | not null | not null | true |
| Send Failed | not null | not null | not null | false |

The key point: using only `transferredToOperatorAt` and `isSent`, the states *Handed for Sending* and *Send Failed* would have identical attribute value combinations (both: `transferredToOperatorAt` not null, `isSent` false). That is why we need `operatorResponseAt` — once the operator responds (whether success or failure), that field is set, distinguishing the two states.

Adding a plain `status` enum attribute (with values for each state) is simpler but less informative — it only tells you the state, but nothing else. When you use real attribute values, you also capture timestamps and other useful data. A `status` enum is valid and sometimes appropriate; just be aware that it carries less information.

**Transitions:**

- *Composed* → *Handed for Sending*: trigger `hand to operator`. This trigger must be findable somewhere in your model — in the activity diagram, that specific step.
- *Handed for Sending* → *Sent* or *Send Failed*: trigger `check send result`. Which branch? Use a guard: `[isSent = true]` → *Sent*; `[isSent = false]` → *Send Failed*. You can use a choice pseudo-state here for clarity.
- From *Sent* or *Send Failed*: if there is no deletion use case, the objects simply remain in those terminal states indefinitely — no final state needed.
- If there is a cleanup use case (e.g., delete messages older than 3 months): you would need a trigger, such as a time event `after(3 months) / delete`. This requires a corresponding use case or process in your model that causes the deletion. Without that, you cannot put the trigger in the state diagram.

Example of a time event trigger notation: `after(3 months) / delete` on the transition to the final state. The tool will typically autocomplete event type recognition when you type `after`.

---

## Worked Example: Vending Machine (Automaton) State Diagram

**Lina Čeponienė:** Now let us draw a state diagram for the *Automaton* (vending machine) entity, which clearly has states: **New**, **Operating**, **Not Operating**, **Turned Off**. It can also be in a sub-state: *Operating but needs servicing* vs. *Operating, no service needed*.

The states *New*, *Operating*, *Not Operating*, and *Turned Off* reflect the physical device's condition as reported to our system.

Transitions:
- *New* → *Operating*, *Not Operating*, or *Turned Off*: triggered by `get status information` (we poll the device for the first time). Depending on the guard (what the device reports), we branch to the appropriate state.
- *Operating* → *Turned Off*: trigger `get status information` with guard `[status = off]`.
- *Operating* → *Not Operating*: trigger `get status information` with guard `[status = not operating]`.
- *Turned Off* → *Operating* or *Not Operating*: trigger `get status information`, with respective guards.
- *Not Operating* → *Operating* or *Turned Off*: same pattern.

All these transitions share the same trigger but have different guards — this is a natural use case for a choice pseudo-state.

Within *Operating*, there is a composite state with two sub-states:
- **Needs Servicing** — supplies are running low.
- **No Service Needed** — all stocked, everything fine.

The machine can switch between these sub-states via the same `get status information` trigger (with guard `serviceRequired = true` or `false`). When the composite *Operating* state is first entered, we need to specify the default sub-state. Since we cannot put a guard on the initial pseudo-state inside the composite, we use an **entry point**: the default entry into *Operating* goes to *No Service Needed*, but there is also a non-default entry point that leads directly to *Needs Servicing* (used when we know at the point of transition that servicing is needed).

A **common student error** in this example: after seeing the automaton example from the slides, students start putting `get status information` as a trigger on every single state diagram they draw, regardless of whether their system actually polls device status. Your triggers must reflect what actually happens in your system. For the SMS entity, no status polling occurs — the relevant event is handing the message to the operator and receiving a response. Keep your triggers grounded in your own model's use cases and activity diagrams.

---

## Final Remarks

**Lina Čeponienė:** That is everything I wanted to cover today. A few closing points:

- A state diagram without triggers on transitions for a passive entity class is almost always wrong. Every transition on a passive class must be caused by an external event.
- A final state in a state diagram is not mandatory. If your entity objects are never deleted or destroyed, there is simply no final state.
- If you do include a final state, you must be able to point to somewhere in your model — a use case, an activity diagram step — where the triggering event occurs.
- Think carefully about whether a `status` enum attribute or a richer set of typed attributes best suits your model. Both are valid but have different trade-offs.
- When working on your state diagrams during lab sessions, come and consult — it always seems obvious until you try to actually draw it, and then it gets complicated. Get feedback early.

Thank you.

*(Post-lecture student question — answered)*

**Lina Čeponienė:** Regarding the automaton — if it is never deleted from the system (you want to keep historical records indefinitely), then there is no final state, no deletion trigger, and no end transition. This is not an activity diagram where a process ends. If you have a deletion use case and can point to where that happens in your model, then you add a final state and the corresponding trigger. If you delete the object, you need a final state. If you do not delete it, you do not. And if you do have a final state, you must be able to show where in your model the deletion event originates.

It will all seem clear until you start drawing — then it will get hard. Work on your state diagrams during lab sessions so you can get advice in the moment.
