Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Event-driven system with event types and current schema management]

Task:
Design an event schema strategy that supports long-term evolution.

Address:
1. Schema format selection: JSON vs. Avro vs. Protobuf — trade-offs for this system
2. Schema registry: whether a schema registry is required and which
3. Versioning strategy: how schema versions are numbered and communicated
4. Backward compatibility: which changes are backward compatible?
   (add optional field: safe; remove field: unsafe; change type: unsafe)
5. Forward compatibility: can old consumers read new schemas?
6. Consumer upgrade sequencing: which upgrades must happen first —
   producers or consumers — for each type of schema change

Output:
Recommend the schema format and versioning strategy with rationale.
Enumerate the schema change types and their compatibility classification:
compatible / breaking / compatible with care.
Provide the consumer upgrade sequencing rule: state which must be upgraded
first for each change category.
Identify the events in the current system that would be most expensive
to change (high fan-out, many consumers) — these require the most conservative
versioning strategy.
Do not recommend schema changes that break existing consumers without
a defined migration path.
