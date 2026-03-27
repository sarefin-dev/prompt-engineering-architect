Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Domain with separate read and write requirements]
[REQUIRED: Current unified model causing problems — describe the pain]

Requirements:
[REQUIRED: Write throughput and consistency requirements]
[REQUIRED: Read throughput, query patterns, and staleness tolerance]

Task:
Design a CQRS implementation for the stated system.
Address:
1. Command model: the write-optimized domain model and its consistency guarantees
2. Query model: the read-optimized projections and their derivation from commands
3. Synchronization: how the query model is kept up to date from the command model
4. Consistency window: the acceptable lag between command and query model
5. Query model rebuild: how the query model is rebuilt from event history
6. Operational complexity: what increases in complexity CQRS introduces

Output:
Design the command and query models for the stated domain.
State the synchronization mechanism (synchronous projection, event-driven
projection, CDC) and its latency characteristics.
Enumerate the queries that require the command model (strong consistency)
vs. the query model (eventual consistency).
Explicitly state whether event sourcing is required — CQRS does not require
event sourcing, and recommending them together requires explicit justification.
Enumerate the operational changes CQRS introduces: separate deployment,
separate monitoring, projection replay procedure.
Do not recommend CQRS without stating the problem it solves for this
specific system — it is not appropriate for simple CRUD systems.
