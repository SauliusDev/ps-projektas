# Lecture 1 — Introduction to UML, Modelling, and the Course

**Course:** Software Systems Analysis and Design Tools (T120B029)
**Speaker(s):** Lina Čeponienė
**Topics covered:**
- Course structure, grading, and key deadlines
- Project requirements and team formation
- The modelling tool (MagicDraw/Cameo) and its role
- Why UML exists and what problems it solves
- Fundamental modelling concepts: abstraction, decomposition, projection
- Overview of UML diagram types (structural vs. behavioural)
- Development processes: Waterfall, Scrum/Agile, Unified Process
- The adapted course process and lab assignment structure
- Introduction to the example system (coffee vending machine management)

---

## Course Introduction and Teaching Staff

I will be one of the lecturers teaching you the module Software Systems Analysis and Design Tools this semester. In addition to me there is lecturer Andrejus Sacharovas, who will cover approximately the second half of the semester — he takes the latter part of the module while I cover the first. There is also Karolis Ryselis, who will deliver one theory lecture. You probably already know Andrejus from the Concurrent Programming module; if not, you will get to know him. There are also a number of other lecturers who will run the laboratory sessions.

You can contact any lecturer by email if you need to consult on something. The email format for everyone is firstname.lastname@ktu.lt. You can also write to me through Teams — I use both channels equally.

---

## Grading and Assessment Structure

Let me now explain how this module will be assessed. The grade is made up of several components.

Fifty percent of your grade comes from the project, which you will complete during the laboratory sessions. Out of this, the project will have three defence sessions, and the grade is distributed proportionally across them.

Twenty percent comes from a written test covering the theory portion that I will deliver. I will teach the theory first, then there will be the test, after which I will cover a few remaining topics needed for the lab work, and then lecturer Andrejus Sacharovas will take over.

The remaining thirty percent comes from an exam covering Sacharovas's part of the module.

Additionally, you can earn one bonus point towards your exam grade if you present your completed laboratory project during the last week of the semester (week 16), according to the requirements that will be announced later.

---

## Key Deadlines and Schedule

The key assessment milestones for the semester are as follows:

- **Week 1 (this week):** Form your teams and agree on a project topic with your lab lecturer. This must be done before the second laboratory session.
- **Week 7:** First laboratory project defence.
- **Week 9:** Written theory test (from the portion I deliver).
- **Week 11:** Second laboratory project defence.
- **Week 15:** Third (final) laboratory project defence.
- **Week 16:** Optional project presentation for a bonus exam point.

Note that public holidays shift some weeks each year, so always refer to the dates posted on Moodle rather than week numbers alone.

The test in week 9 will be written on paper. Everyone writes at the same time and draws UML diagrams by hand from various diagram types used at different stages of development. The reason for a hand-drawn test is that one of the skills I want to develop in you is the ability to quickly sketch a diagram on paper during a meeting or conversation — UML as a communication tool, not just a documentation artefact. During the test I will assess how well you can use UML as a communication tool: given a description, you will need to draw the appropriate diagram.

---

## Team Formation and Project Scope

**Teams** should be approximately four people. Variations in size are possible but must be agreed individually with your lecturer. Be aware: if you increase team size, the project scope expectations increase as well. If you decrease team size, the scope does not decrease. So if you work in three people, you are still expected to deliver a four-person project. I would strongly recommend working in full teams of four.

The classic question always arises — why work in teams at all? Why not just sit down alone and do it quietly? The main reason is that to experience what it is like to work on a large project, a single person's scope is not enough. We want to show you what it looks like to work on a reasonably large project. A four-person project is still relatively small, but it is much better than a one-person mini-project, where you would never encounter the full range of problems and situations that arise when working with other people.

Choose your teammates carefully, because you will work with them for the whole semester. Do not end up in a situation where you find that only you are doing the work. Since nobody forces you into a team, find people you would work well with and whose work ethic matches yours.

Also make sure your teammates are in the same laboratory time slot as you. It does not work well if your teammates attend a different session. If you want to migrate to a different time slot to work with friends, register for the same lab time.

---

## Project Requirements

**You must agree your project topic with your lecturer** — you cannot simply show up and announce "I am doing a car service system" and leave. It is an iterative process: you discuss the idea together, figure out where complexity can be added, and refine it until the scope and difficulty are sufficient.

The project must be more than a simple CRUD application. It needs to include:
- A **database-backed information system** with a server and client component
- At least **two distinct user types** (naturally, it often ends up being more)
- At least **one external integration** — the system should not be entirely self-contained
- At least **one non-trivial algorithm** or more complex logic — something that involves real computation, not just storing and retrieving records

An example of a non-trivial algorithm: implementing a shortest-path algorithm in a graph. That involves loops, conditionals, calculations — the kind of thing that must be drawn out in diagrams. In contrast, simple validate-and-save logic is what was considered complex in your Information Systems Fundamentals course, but in this module that is baseline material. Here the baseline is that, and the expectation is something more sophisticated on top of it.

For example, a warehouse management system could be done two ways: the trivial version just adds, views, and removes stock. But the version done in this course included an algorithm for optimal item placement on shelves based on dimensions and frequency, plus a forecasting algorithm for restocking decisions. The topic name alone does not determine complexity — the depth of the solution does.

The **third lab session** will also require partial implementation. During the first defence, you are modelling only. During the second and third, you add implementation. The parts to implement are chosen by your lecturer, not by you — otherwise every team would implement just the login screen. Make sure to agree in advance on what will be implemented so there are no surprises at the defence.

Project reports must be submitted to Moodle in advance so lecturers can review and comment before the defence session. Do not submit at the last minute: if you submit right before the defence with no time for review, you will not be allowed to defend. Lecturers need time to read and annotate.

The defence itself is individual: each team member must answer questions individually. The lecturer will ask you to demonstrate something live in the modelling tool — for example, "add a dependency relationship here" or "show me the cardinality on this association." If you cannot answer, one mark is deducted per unanswered question. After three unanswered questions, the defence is failed. Questions can come from both the model and the implementation, and "my colleague did that part" is not an accepted answer. You are responsible for the entire project.

---

## Tooling

The primary modelling tool for this course is **MagicDraw** (also known as Cameo). You already know it from previous modules and have varying opinions about it. Yes, the interface is not the most elegant among modelling tools. But none of the modelling tools I have encountered have a truly elegant interface — they all have things buried deep in menus. Some tools have a slightly prettier interface, but are equally or more frustrating to use.

The key distinction to understand is the difference between **drawing a picture** and **building a model**. If you use draw.io, PowerPoint, Word, or any generic drawing tool, you are drawing a picture. Each element exists only on that diagram. If you rename a class, you rename it only in one place.

If you use a modelling tool like MagicDraw, every element is part of a shared model. A class used in five different diagrams is the same object — change its name once and it updates everywhere. You can validate consistency: does this element relate correctly to that one? You can also generate code from the model.

The conclusion is: when you need a one-time sketch to communicate an idea, a whiteboard or paper is actually the best tool. When you need a persistent, consistent, reusable model that can be evolved, validated, and used for code generation — use a modelling tool. Both have legitimate uses.

**For implementation**, you may use any object-oriented programming language, but confirm this with your lecturer. The course assumes an object-oriented approach because we are working with UML, which is tightly aligned with OO design. Using a non-OO language is possible but creates an awkward mismatch that will require a lot of discussion with your lecturer.

MagicDraw can generate code stubs — primarily Java/C++ style. You are not required to use generated code for your implementation, but you should try the feature at least once so you understand what code generation from a model looks like.

**For collaborative work**, you will use the cloud-based version of MagicDraw (Teamwork Cloud), which you have already used in previous modules. Multiple team members can work on the same model simultaneously — one person locks a section, edits it, commits, and so on.

**UML version:** we will work strictly with **UML 2.5.1**. UML has changed significantly over its history. Version 1.4 was in use for a long time and many online examples are drawn according to those older rules, where some relationships pointed in opposite directions or were notated differently. If you find a diagram online that contradicts what I teach, it may simply be drawn according to an older version. We follow UML 2.5.1 rules.

Lectures will be recorded and broadcast on Teams, and the MagicDraw model file from each lecture will be uploaded to Moodle after each session. However, recording availability is not a reason to skip lectures. When I draw diagrams live, I draw them in conversation with the audience — the discussion shapes the result. The same system can legitimately be modelled in five or more different valid ways depending on what you emphasise, and that is something that only emerges in a two-way class. I will not monitor the remote Teams stream and will not respond to comments there. Please attend in person.

---

## Recommended Resources

The primary reference for this module is the **UML 2.5.1 specification** — a formal document describing the complete structure, rules, and semantics of UML. It is approximately 700 pages of dense text, diagrams, and formal rules, which I will describe as having a soporific effect. You do not need to read it. I will quote the relevant portions when explaining each diagram type.

The main source you should rely on is what I explain in lectures. Online resources can vary widely in quality and may reflect older UML versions or incorrect usage. Rather than navigating that, use the lecture material as your primary reference.

There is also a gamified practice course which I will share a link to on Moodle before the written test. It lets you solve quiz-style exercises, collect points, and self-assess your knowledge. I will remind you about it closer to the test date.

---

## What is UML and Why Do We Use It?

Now let's move on to the actual theoretical content.

One of the most common comments I receive is some version of: "Why do we have to use this clunky tool? We could just use draw.io and draw nice pictures, no suffering required." And honestly — who here agrees with that? Nobody? Really? You have all fallen in love with MagicDraw after two modules? Or you are just afraid to say it.

Let me be clear: MagicDraw is not the most comfortable of the modelling tools I have used. Some have prettier interfaces. But every single one of them is unpleasant to use. The depth in the menus, the complexity — that is inherent to what modelling tools do. And the reason we do not just use draw.io is precisely the difference between a picture and a model, which I described above.

To illustrate why a shared notation matters, consider this: a real Lithuanian payment processing company (similar to "Paysera") publishes technical documentation with diagrams so that developers can integrate with their API. When they tried using plain text, developers didn't understand everything. So they added diagrams. But the diagrams they drew were invented by themselves — custom colours, shapes, and relationships — with a legend trying to explain what each one meant. When I show those diagrams in class, nobody can tell what type of diagram it is, what the relationships mean, or what the rectangles versus ellipses signify. They tried adding a legend to explain it, but it barely helped.

The reason is simple: if you invent your own visual language, only you understand it. But if you use a **standard language** that everyone either knows already or can look up, you eliminate the overhead of explaining what every colour and shape means. That is why UML exists.

---

## Why Model at All?

Modelling is useful for several interconnected reasons.

**Understanding what you don't know.** When you start drawing a model, you immediately begin asking questions you hadn't asked before. Should there be a distance label here? What happens at the end of this corridor? Does this step apply to all users or just some? Modelling forces you to confront gaps in your understanding before you start building. The earlier you discover those gaps, the cheaper they are to fix.

**Communicating with others.** Rather than narrating a full description of a room in absurd detail ("the floor is linoleum, the ceiling has panels, the door handle is metal and turns at a 5-degree angle before the door opens outward"), you sketch a floor plan. The sketch is not perfect — but it conveys the essential structure without the noise. A diagram on a whiteboard is always more effective than a verbal description, even if it is rough. Any diagram is better than no diagram, and any diagram is better than a page of text.

**Documenting for the future.** Real software systems live for years, require maintenance, get extended, and get handed off to new developers. The original developers rarely remember the details after a year. I once spoke with a company that initially believed that "the best documentation is the code." A few years later, after significant growth, they said they probably needed to write some descriptions after all. By then they had as many analysts as developers, modelling and documenting everything. Long-term, it does not pay to build things that nobody will be able to understand or maintain a year later.

**Choosing how much detail to include.** This is the hard part. Modelling involves **abstraction**: you choose which details to keep and which to drop. Too much detail and your model is as noisy as the original. Too little and it communicates nothing. I have seen a perfectly formally correct use case diagram with one actor connected by one use case labelled "Use the system." Formally valid. No errors in notation. Completely useless because the abstraction level was too high — every detail of the system was hidden behind a single label. Getting the abstraction level right is a skill that comes from iteration and practice: draw it, look at it, realise something is missing or something is excessive, adjust.

The same applies to the written test: when you draw a diagram by hand, the goal is to sketch the structure quickly and communicate the essential idea. It does not need to be perfect or beautiful — it needs to be correct and readable. You do not need rulers, compasses, or coloured pencils. A hand-drawn sketch communicates the idea, and that is the point.

---

## Core Modelling Concepts

### Abstraction

Abstraction means deliberately dropping details that are not relevant to the question at hand, in order to highlight the parts that are. When I draw a rough map to explain how to exit the building, I omit the ceiling height, the floor material, the door handle design — none of that matters. What matters is the spatial structure: this room connects to that corridor, the exit is at the end.

Choosing the right level of abstraction is central to good modelling. Too abstract and the model conveys nothing; too detailed and it is harder to understand than the thing it models. This is almost never correct on the first try. Expect to draw, review, adjust, and redraw — that is the normal process.

### Decomposition

Decomposition means breaking a complex problem into smaller independent parts that can be worked on separately. Like "eating an elephant one bite at a time." In theory, decomposed parts are independent. In practice, complete independence is rare: if you change one part, something in another part may break. The goal is to minimise those dependencies through good design decisions, which is itself something that modelling helps you think through.

### Projection

A model is a shared entity. A diagram is one **projection** of that model from a particular angle, showing particular aspects. Consider engineering drawings: a table is described with a top view, a side view, and a front view — three projections that together allow you to reconstruct the full 3D object. Similarly, in UML:

- A **class diagram** is a structural projection of the model.
- A **sequence diagram** is a behavioural projection showing how objects interact over time.
- A **use case diagram** shows the functional scope from the user's perspective.

The same underlying model element appears in multiple diagrams. In MagicDraw, the element tree on the side panel *is* the model. The diagrams are views into it. This is why consistency matters: if you update a class name in one diagram but not another, you now have contradictory projections of the same model, which is worse than having no model at all.

---

## UML Diagram Types

UML 2.5.1 contains a large number of diagram types, divided into two broad categories:

**Structural diagrams** describe the static structure of a system — what it is made of:
- **Class diagram** — classes, attributes, methods, relationships
- **Component diagram** — high-level software components and their interfaces
- **Deployment diagram** — hardware/software deployment topology
- **Package diagram** — organisation of model elements into packages

**Behavioural diagrams** describe how a system behaves — what it does over time:
- **Use case diagram** — actors and the functional use cases they interact with
- **Activity diagram** — workflow and process flows (similar to flowcharts)
- **State machine diagram** (state diagram) — states and transitions of an object over its lifecycle
- **Sequence diagram** — messages exchanged between objects in time order (a subtype of interaction diagram)

In this course we will focus on: **class, component, deployment, and package diagrams** from the structural group, and **use case, activity, state machine, and sequence diagrams** from the behavioural group. Sequence diagrams belong to the interaction diagram subgroup. Once you understand these, the remaining diagram types are accessible on your own.

You may not have encountered **state machine diagrams** (state diagrams) before. All the others you should have seen at least briefly in previous modules.

---

## When Should You Use UML?

UML is not appropriate for every situation. Consider the example of a "Hello World" program: technically you could draw a class diagram, show the inheritance hierarchy, add a package diagram, a sequence diagram for the print operation, and a deployment diagram. That would be absurd over-engineering for three lines of code.

UML becomes valuable when:
- The system is complex enough that one person cannot hold it all in their head
- Multiple people need to understand and work on the same codebase
- You need documentation that will be read by newcomers in the future
- You are making architectural decisions that affect many downstream components
- The cost of misunderstanding is high

As a vivid example: the Large Hadron Collider (LHC) at CERN generates billions of data points per second that must be stored, processed, and structured. Even a small fragment of the class diagram for the LHC's data management subsystem fills an entire screen with dozens of classes and relationships. For systems of that scale, diagrams are not a bureaucratic exercise — they are a survival tool. You cannot navigate that codebase without them.

For small projects, though? The modelling overhead may genuinely not be worth it. The lesson is: **use the right tool for the right situation**. Sketches and full models both have their place.

---

## Development Processes and UML

UML is just a language — it does not prescribe a development process. It does not tell you which diagram to draw first, in what order, or when. That is the job of a development process methodology.

You all know at least two processes:

**Waterfall (sequential):** requirements are fixed, then design, then implementation, then testing — in strict sequence. Going back to a previous phase is like swimming upstream against a waterfall. Theoretically rigid, practically inflexible. Nobody uses pure waterfall on large projects for this reason.

**Scrum (agile, iterative):** work is organised in sprints. During each sprint, a fixed set of requirements from the backlog is committed to and cannot be changed mid-sprint. This is important: within the sprint, requirements are locked. If a client wants to change a feature from blue to red on Tuesday and to sunset-gradient-green by Thursday, the sprint boundary enforces stability. What you committed to on Monday is what you deliver at the sprint review. The client's new wishes go into the backlog for the next sprint.

Here is an insight worth noticing: within a single sprint, with requirements fixed and implemented sequentially, you are running a mini-waterfall. The criticism of waterfall is not the sequentiality itself — it is applying sequentiality to the entire multi-year project at once. Small waterfalls (sprints) are exactly what agile frameworks rely on.

There are also other process frameworks. The one most relevant to UML is the **Unified Process (UP)** — a methodology that prescribes how to use UML throughout the development lifecycle, organising work into phases (inception, elaboration, construction, transition) with iterative cycles. In its pure form, UP requires creating hundreds of formal documents and is notoriously heavy. Nobody uses pure UP either. However, a **tailored (scaled-down) UP** is what I have adapted for this course.

The adapted process we will follow looks approximately like this:

1. Initial requirements → Requirements specification (use case, activity, class, state diagrams)
2. Design → (above diagrams updated) + partial implementation (sequence diagrams added; component and deployment diagrams added)
3. Realisation → Remaining implementation + final diagrams

Notice that back-arrows exist at every step: if something changes, you go back and update. If a late-stage change requires revising the first diagram, you go all the way back and correct it. Models that contradict each other are worse than no model at all.

---

## Lab Assignment Breakdown

The three lab defence sessions correspond to three phases:

- **First defence (week 7):** Modelling only. Deliverables: use case diagram, activity diagrams, class diagram, state machine diagrams.
- **Second defence (week 11):** Updated modelling from phase 1 + partial implementation. Deliverables: sequence diagrams added, component and deployment diagrams added, initial code.
- **Third defence (week 15):** Remaining implementation + final diagram set complete.

Important note: when the assignment lists a diagram type (e.g., "activity diagram"), that does not mean one diagram. If you have ten use cases, you need ten activity diagrams — one per use case. If you have ten use cases you also need ten sequence diagrams. There will be many diagrams. Based on the experience of previous student cohorts: **this cannot be done in one night, or even two nights.** The diagrams are tightly interconnected. If your first diagram (e.g., the use case diagram) has a fundamental error, everything that follows it is also wrong, and it all needs to be redone from scratch.

Use your laboratory sessions as consultation time. Come in, show what you have done so far, get feedback, adjust, come back. Do not arrive at the defence with thirty diagrams that were all drawn in three days without any intermediate review.

---

## Example System: Coffee Vending Machine Management

From the next lecture onwards, I will model a demonstration system in MagicDraw during each theory session, live, while explaining the corresponding diagram type. The system I will use throughout the course is a **coffee vending machine management system**.

The scenario is as follows: a company operates a fleet of coffee vending machines deployed across various locations. Each machine must be periodically restocked with coffee, sugar, cups, and change. Currently, a technician simply drives a fixed route once a week, checks each machine, and refills as needed. Problems with this approach:

- A machine might run out of coffee three days before the visit — nobody knows until the technician arrives.
- Conversely, the technician might arrive at a machine that barely needs anything — a wasted trip.

The machines are passive devices: they do not push status updates. They only respond when queried.

The company needs a system with two parts:
1. **Customer-facing component:** shows where machines are located on a map, displays promotions and discounts, possibly allows some interaction.
2. **Technician/admin component:** allows technicians to log in, view machine statuses, query each machine for current inventory levels, determine which machines need attention and when, schedule visits efficiently. Also needs a higher-level admin user who can create technician accounts, manage promotions, and configure the system.

The system must periodically poll each machine automatically as well as respond to on-demand queries. It must track inventory levels, maintenance history, and servicing schedules.

Next lecture we will begin drawing a **use case diagram** for this system based on this description.

---

## Closing Remarks

Thank you for your patience. If you have questions — about organisational matters or anything else — please ask now, or contact me by email or Teams.

A few final reminders:
- Form your team and agree on a project topic before the second lab session this week.
- Attend theory lectures in person — live modelling is interactive and the recording does not substitute for that.
- Start early on your lab work. Each defence builds on the previous one, and the diagrams are deeply interconnected.

See you at the next lecture.
