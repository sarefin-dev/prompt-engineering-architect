Act as a Principal Microservices Architect.

Current state:
[REQUIRED: Description of the monolith — size, technology, team structure]
[REQUIRED: What problems the migration is intended to solve]
[REQUIRED: Scale requirements that the monolith cannot meet]

Constraints:
[REQUIRED: Team size and microservices experience]
[REQUIRED: Downtime tolerance]
[REQUIRED: Timeline and business milestones that cannot be interrupted]

Target architecture:
[REQUIRED: Target service decomposition, if known]

Task:
Design an incremental migration from monolith to microservices.
Apply the strangler fig pattern — extract services at the edges
while the monolith continues to serve traffic.

Design the migration in phases:
Phase 1 — Identify extraction candidates:
  Which functionality is highest-value to extract first?
  Criteria: high change rate, independent scalability need, team boundary alignment.

Phase 2 — Establish the extraction pattern:
  API gateway in front of the monolith to enable traffic splitting.
  New service deployed alongside the monolith, not replacing it immediately.
  Gradual traffic migration from monolith endpoint to new service.

Phase 3 — Data ownership migration:
  The extracted service must own its data — not share the monolith's database.
  Design the data migration: dual-write period, cutover, cleanup.

Phase 4 — Monolith shrinkage:
  Remove the extracted functionality from the monolith after the service is stable.

Output:
Provide the phased migration plan with the extraction sequence.
For each phase: define the entry criteria, the exit criteria, and the rollback procedure.
Identify the data ownership migrations — these are the highest-risk steps.
State the point of no return: after which phase does rolling back to a
full monolith become impractical?
Enumerate the anti-patterns to avoid:
  distributed monolith (services that cannot be deployed independently),
  shared database (multiple services sharing a database),
  synchronous chains (services that form a request chain with high coupling).
State the team topology changes required — Conway's Law applies.
Do not propose extracting all services simultaneously —
sequence by extraction value and risk.
