Act as a Staff Database Architect specializing in large-scale systems.

System context:
[REQUIRED: Write workload characteristics — writes/second, data model, access patterns]
[REQUIRED: Consistency requirements — what must be transactionally consistent]
[REQUIRED: Read patterns — what must be queryable and at what latency]

Task:
Design a data model optimized for the stated high-scale write workload.

Address the fundamental tensions:
1. Normalization vs. write amplification:
   highly normalized schemas require writes to multiple tables per operation —
   evaluate whether this is acceptable at the stated write throughput
2. Consistency scope: what data must be written atomically?
   What can be written eventually?
3. Hot row contention: do multiple concurrent writers contend on the same rows?
   (e.g., a counter column updated by every transaction) — design around this
4. Index maintenance overhead: every index adds write cost —
   evaluate which indexes are justified by read query requirements
5. Partitioning: does the write pattern distribute across partitions uniformly?
   Monotonically increasing keys (timestamps, sequences) create hot partitions.

Output:
Provide the data model design with explicit trade-off justification.
For each design decision: state the write throughput implication and
the read query implication.
Enumerate the hot row contention risks and the mitigation
(optimistic locking, partitioning, event sourcing, counter sharding).
State the partitioning recommendation if the write volume requires it.
Do not recommend a fully normalized schema for a write-heavy workload
without assessing the write amplification at target throughput.
