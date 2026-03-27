Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: System description with data model and operations]

Business requirements:
[REQUIRED: For each major operation — what staleness is acceptable?]
[REQUIRED: What are the consequences of serving stale data per operation?]

Task:
Select the appropriate consistency model for each operation category.
Work through this for each category:
1. Strong consistency / linearizability: required when stale reads cause
   financial loss, security violation, or user-visible corruption
2. Read-your-writes: required when a user must see their own actions immediately
3. Causal consistency: required when operations have causal dependencies
   that must be visible to all observers
4. Eventual consistency: acceptable when temporary staleness is tolerable
   and the eventual convergence window is defined

For each operation in the system: state the required consistency level
and the consequence of using a weaker model than required.

Output:
Tabulate: Operation | Required consistency model | Consequence of weaker model.
Group operations by required consistency level.
Identify the operations that require strong consistency — these drive
the infrastructure requirements and performance implications.
Enumerate the consistency anomalies that the chosen models must prevent:
lost updates, dirty reads, phantom reads, stale reads.
Do not recommend eventual consistency for operations with financial,
security, or user-safety consequences without explicit business sign-off.
