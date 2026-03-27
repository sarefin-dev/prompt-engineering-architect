Act as a Staff Database Architect.

System context:
[REQUIRED: Database technology and version]
[REQUIRED: The concurrent transaction patterns — what operations run simultaneously]
[REQUIRED: The business consequences of data anomalies — what happens if two
 concurrent transactions see inconsistent data]

Task:
Analyze the transaction isolation requirements for this system.

Work through each isolation level in order against the stated concurrent patterns:

Level 1 — Read Committed (PostgreSQL default):
- Anomalies possible: non-repeatable reads, phantom reads, write skew
- Safe for: single-statement operations, read-heavy workloads with no
  concurrent updates to the same rows
- Unsafe for: any multi-statement transaction that reads and then updates
  based on those reads (write skew possible)

Level 2 — Repeatable Read:
- Anomalies prevented: non-repeatable reads
- Anomalies still possible: phantom reads (range queries), write skew
- Safe for: reports and aggregations that must see a consistent snapshot
- Unsafe for: check-then-act patterns (check balance, then debit)

Level 3 — Serializable:
- All anomalies prevented including write skew and phantom reads
- Implementation: Serializable Snapshot Isolation (SSI) in PostgreSQL
- Cost: serialization failures (transactions abort and must retry)
- Required for: financial transactions, inventory reservation, any pattern
  where two transactions read overlapping data and one updates based on
  the read result

For each concurrent transaction pattern in the system:
1. Identify the anomaly class it is vulnerable to at Read Committed
2. State the minimum isolation level that prevents the anomaly
3. State the performance impact of the required isolation level

Output:
State the required isolation level per transaction pattern — not a single
level for the whole database.
Enumerate every check-then-act pattern in the system — these require at
minimum Repeatable Read and typically Serializable.
For any pattern requiring Serializable: design the retry logic for
serialization failures (PostgreSQL error code 40001).
Quantify the expected serialization failure rate under the stated
concurrent transaction volume.
Do not recommend Read Committed for any transaction that reads and
then updates based on that read — this pattern is vulnerable to write skew
regardless of application-level locking.
