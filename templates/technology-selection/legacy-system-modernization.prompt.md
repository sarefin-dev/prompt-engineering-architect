Act as a Principal Architect designing a legacy system modernization.

Current state:
[REQUIRED: Legacy system description — technology, age, known limitations]
[REQUIRED: Why modernization is required — specific pain points or business drivers]
[REQUIRED: Team capability — what the team can build and operate]

Constraints:
[REQUIRED: Cannot replace all at once — must be incremental]
[REQUIRED: Cannot take extended downtime]
[REQUIRED: Business operations that must continue throughout migration]

Target state:
[REQUIRED: Target technology, architecture, or capability]

Task:
Design an incremental modernization strategy.

Evaluate the three primary modernization approaches:

1. Rewrite (high risk):
   Build the new system alongside the old, migrate traffic, decommission old.
   Risk: two systems in production simultaneously, coordination overhead.
   Suitable when: the old system is too constrained to extend further.

2. Refactor (medium risk):
   Incrementally improve the existing system without full replacement.
   Risk: legacy constraints persist; improvement is slow.
   Suitable when: the core data model and domain logic are sound.

3. Strangler fig (lower risk):
   Add new capabilities in modern technology; route old capabilities
   through a facade that gradually migrates to the new system.
   Risk: facade complexity; two systems for extended period.
   Suitable when: the legacy system can be incrementally hollowed out.

Output:
Recommend the modernization approach with explicit rationale.
Design the incremental plan — no step should take longer than one sprint
to complete and verify.
For each step: state the deliverable, the success criteria, the rollback procedure.
Identify the highest-risk step in the migration — typically the data model migration.
State the decommissioning criteria: what must be true before the legacy
system can be shut down?
Enumerate the capabilities that cannot be incrementally migrated —
these require a cutover plan.
Do not recommend a full rewrite without evidence that refactoring is not viable —
rewrites consistently underestimate the knowledge embedded in legacy code.
