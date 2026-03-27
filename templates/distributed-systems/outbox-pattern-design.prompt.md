Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Service that writes to a database and must publish events reliably]
[REQUIRED: Database technology, message broker, current transaction approach]

Problem:
[REQUIRED: Describe the dual-write problem being solved — what events
 must be guaranteed to be published after a database transaction commits]

Decision:
Before designing the implementation, choose the outbox publication mechanism:

Option A — Polling-based outbox:
The outbox publisher polls the outbox table on a scheduled interval,
reads unprocessed entries, publishes to the broker, marks as processed.
Trade-offs:
- Minimum latency = polling interval (typically 100ms–5s)
- Adds read load to the primary database at polling frequency
- Simple to implement; no additional infrastructure
- Correct for: lower-throughput systems, teams without CDC infrastructure

Option B — CDC-based outbox (Debezium / logical replication):
A CDC connector reads the PostgreSQL write-ahead log (WAL) via logical
replication. Every INSERT into the outbox table is captured and published
to the broker without polling.
Trade-offs:
- Near-zero latency (milliseconds from commit to publish)
- No polling load on the primary database
- Requires logical replication enabled (wal_level=logical), a replication slot,
  and a CDC connector (Debezium, AWS DMS, or pgoutput consumer)
- Replication slots accumulate WAL if the consumer falls behind — monitor
  pg_replication_slots for slot lag; an unbounded slot is a disk-fill risk
- Correct for: high-throughput systems, sub-second publication latency required,
  or when database polling load is a concern

Recommend one option with explicit rationale against the stated throughput
and latency requirements.

Task:
Design the transactional outbox pattern implementation for the chosen option.
Cover:
1. Outbox table schema — what fields are required for reliable publishing
2. Transaction scope — what database operations are atomic with the outbox insert
3. Publication mechanism implementation — polling interval + batch size (Option A)
   OR CDC connector configuration + replication slot monitoring (Option B)
4. Message deduplication — how consumers handle duplicate publications
   (at-least-once is standard; idempotency key required on the consumer side)
5. Outbox cleanup — how processed entries are archived or deleted
6. Failure handling — publisher crash mid-batch (Option A) or
   CDC connector restart + replication slot lag (Option B)

Output:
Provide the complete outbox design including the outbox table DDL.
State the delivery guarantee: at-least-once (standard for both options);
state the consumer-side deduplication strategy.
Enumerate the failure scenarios and how each is handled.
State the maximum latency from database commit to message publication
and what determines that bound (polling interval for A; WAL propagation
latency for B, typically under 100ms).
For Option B: state the replication slot monitoring requirement —
pg_replication_slots.confirmed_flush_lsn must be monitored; alert if
slot lag exceeds the defined threshold.
Explicitly distinguish the outbox pattern from direct event publishing
and state why the outbox is required for this use case.
