Act as a Principal Architect designing a migration strategy.

Current state:
[REQUIRED: Current architecture, technology, and data model]

Target state:
[REQUIRED: Target architecture, technology, or deployment model]

Constraints:
[REQUIRED: Non-negotiables — downtime tolerance, team size,
 timeline, compatibility requirements]

Business continuity requirements:
[REQUIRED: What must keep working throughout the migration]
[REQUIRED: Rollback requirements — what constitutes a rollback trigger]

Task:
Design a migration strategy from current to target state.
Decompose the migration into phases — each phase must be:
- Independently deployable without completing subsequent phases
- Reversible — each phase can be rolled back without data loss
- Testable — success criteria are verifiable before proceeding

For each phase:
1. Define the scope of change
2. Define the deployment approach (strangler fig | feature flag | parallel run | cutover)
3. Define the success criteria before proceeding to the next phase
4. Define the rollback procedure and rollback trigger conditions
5. Estimate the team effort and elapsed time

Output:
Produce a phased migration plan.
Tabulate phases: Phase | Scope | Approach | Success criteria | Rollback trigger | Effort.
After the table, provide implementation notes for the two highest-risk phases.
Identify the point of no return — the phase after which rollback to the
original state is no longer practical — and state this explicitly.
Enumerate the top three risks to the migration and their mitigations.
Do not propose a big-bang migration if an incremental approach is feasible.
Do not recommend phases that violate the stated business continuity requirements.
