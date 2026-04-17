# Travel System P2 Architecture Design

## Problem and Goal

For P2, the project needs a coherent logical architecture package diagram, sequence diagrams per use case, and a working CRUD-capable prototype that matches UML and BCE/MVC rules.

The current use case model is split by actor subsystems (Guest, User, Admin). This design keeps that split for requirements/UI perspective, but defines a cleaner implementation architecture for backend and sequence modeling.

## Chosen Approach

**Recommended and selected:** React frontend + Python FastAPI backend + PostgreSQL, implemented as a **modular monolith** with strict BCE/layered dependencies.

This is the lowest-risk option for same-day delivery while keeping strong alignment with P2 grading criteria.

## Architecture Overview

### 1. Frontend (Boundary layer)

Frontend is organized by user-facing areas:
- `GuestViews`
- `TravelerViews`
- `AdminViews`

These are boundary elements that collect input, render output, and call backend API endpoints. No business rules are implemented here.

### 2. Backend API (Boundary layer)

Backend boundary is split by access context:
- `GuestApi`
- `TravelerApi`
- `AdminApi`

API packages validate input, check auth/role constraints, and delegate to application controllers/services.

### 3. Application (Control layer)

Control logic is split by feature/domain:
- `Auth`
- `Trips`
- `Deals`
- `Places`
- `Food`
- `Users`

This is where use case orchestration, business rules, and transaction flow live.

### 4. Domain (Entity layer)

Shared entities and value objects:
- `User`, `Admin`, `Traveler`
- `Trip`, `Route`, `RouteAttraction`, `RouteFoodPlace`
- `Deal`, `FoodPlan`, `Preferences`, `Menu`, `Dish`, `VisitedPlace`, `Group`

Entities are reused across admin/traveler/guest scenarios, avoiding duplication by role.

### 5. Infrastructure

Technical adapters:
- `Persistence` (PostgreSQL repositories)
- `GoogleMapsGateway`
- `EmailGateway`

Application controllers depend on interfaces/ports and call infrastructure through those contracts.

## Package Diagram Rules (for Magic)

1. Keep **Requirements model** subsystem split (Guest/User/Admin) in use case model.
2. In **Project model**, show architecture packages by implementation responsibility (Boundary/Control/Entity/Infrastructure), not by role-only backend folders.
3. Dependency direction:
   - Frontend Boundary -> Backend API Boundary
   - Backend API Boundary -> Application Control
   - Application Control -> Domain Entity
   - Application Control -> Infrastructure
   - Infrastructure -> Domain Entity (mapping/persistence only)
4. Do not allow:
   - Boundary -> Entity direct calls
   - Actor -> Control direct calls
   - Boundary -> Boundary chaining for business flow
5. Ensure the package diagram structure and the actual Magic model tree are identical (same packages, same class placement), because this is checked in defense.

## Magic Transition Rules (Requirements -> Design)

1. Run model transformation from requirements model to design model.
2. Keep transformed use cases, actors, entity classes, and packages; remove transformed activity/state/signal artifacts not needed in design.
3. Keep the auto-generated `«edition»` traceability package (do not delete it).
4. Convert transformed use cases into **collaborations** so sequence diagrams are created under the correct collaboration elements with maintained trace links.
5. Use English names in design model classes/attributes/operations (aligned with implementation naming).

## Sequence Diagram Pattern (for all use cases)

Canonical flow:
1. `Actor -> FrontendView <<boundary>>`
2. `FrontendView -> ApiController <<boundary>>`
3. `ApiController -> UseCaseController <<control>>`
4. `UseCaseController -> Entity/Repository/Gateway <<entity/infrastructure>>`
5. Replies return in reverse order (except allowed UI-navigation exception from lecture notes)

Mandatory consistency:
- Every operation called in sequence must exist in class diagram.
- Every sender/receiver class pair in sequence must have a class relationship.
- Include/extend from use cases must appear as `ref` / `opt` / `alt` in sequence.
- Combined fragments must include covered lifelines ("Covered By" in Magic).

Additional sequence constraints from lecture rules:
- Actors do not get operations; actor-facing messages can be free-text labels.
- Reply messages are required for all synchronous calls except UI navigation between windows/views.
- `alt` should include an `[else]` branch for complete logic coverage.
- `loop` should use either a guard condition or iteration count (not both together).
- Recommended lifeline order: actor -> boundary -> control -> entity -> external actor (far right).

## Mapping Existing Subsystems to Feature Split

- **Guest subsystem use cases** mostly map to `Auth`, `Deals`.
- **Traveler subsystem use cases** mostly map to `Trips`, `Route/Places`, `Food`, `Deals`, `Users`.
- **Admin subsystem use cases** mostly map to `AdminApi` boundary + same feature modules (`Deals`, `Places`, `Food`, `Trips`, `Users`) with admin permissions.

This keeps traceability to existing diagrams while producing cleaner implementation architecture.

## Error Handling Design

- API boundary returns explicit error responses (validation/auth/not-found/conflict).
- Control layer raises domain/application errors with clear cause.
- Infrastructure errors are surfaced to control layer and translated to API-level errors.
- No silent failures and no swallowed errors.

## Testing Strategy (P2-focused)

- Prioritize CRUD paths agreed with instructor.
- For each implemented use case:
  - verify activity -> sequence -> class operation -> code traceability
  - verify boundary/control/entity rule compliance
- Validate role access (guest/traveler/admin) on API boundary level.

## Out of Scope for P2

- Microservice decomposition
- Event-driven distributed architecture
- Multi-service deployment optimization

These can be considered after P3 if needed.

## Deliverables Alignment

This design directly supports:
- P2 logical architecture package diagram
- Sequence diagram per use case
- System class diagram with boundary/control/entity stereotypes
- Fast prototype implementation path with React + FastAPI + PostgreSQL
