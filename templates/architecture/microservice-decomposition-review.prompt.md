Act as a Principal Microservices Architect.

Current system:
[REQUIRED: Description of the current monolith or service landscape]

Proposed decomposition:
[REQUIRED: The proposed service boundaries and their responsibilities]

Business domain:
[REQUIRED: Brief description of the business domain and its core concepts]

Constraints:
[OPTIONAL: Team topology, technology constraints, migration constraints]

Focus areas:
- Service boundary correctness: alignment with domain bounded contexts
- Coupling and cohesion: appropriate dependency direction
- Data ownership: each service owns its data, no shared databases
- API contract quality: interface design and backward compatibility
- Operational complexity: deployment, debugging, distributed transaction risk

Task:
Evaluate the proposed decomposition against domain-driven design principles.
Identify boundaries that are too coarse (services doing too much) or too fine
(services that are always deployed together and share data).
Diagnose shared database anti-patterns and propose data ownership resolution.
Assess the communication pattern at each service boundary.
Identify missing services implied by the domain model.

Output:
Provide a structured analysis with one section per focus area.
For each service boundary: state whether it is correctly scoped,
over-scoped, or under-scoped, with rationale.
Enumerate all shared database violations — these are blocking issues.
Tabulate recommended communication pattern per service boundary:
synchronous REST | asynchronous event | event with reply | none.
Do not recommend decompositions that would require distributed transactions
across more than two services without explicit justification.
