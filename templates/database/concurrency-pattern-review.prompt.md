Act as a Staff Database Architect.

System context:
[REQUIRED: All tables involved in concurrent access patterns]
[REQUIRED: The concurrent operations — which transactions touch which tables]
[REQUIRED: Current locking strategy if any]

Task:
Review the concurrency design for correctness and performance.

Work through each concurrency pattern:

1. Lock contention analysis:
   For each table with concurrent writes: identify the rows that are
   contended and the transaction duration holding the lock.
   Contention = long transaction duration × high concurrent writers × narrow row range.

2. Deadlock risk assessment:
   Identify any pair of transactions that acquire locks in different orders —
   these are deadlock candidates. State the lock acquisition order for each
   transaction and identify any intersecting lock sets.

3. Long transaction risk:
   Identify any transaction that holds locks for > 100ms under normal load.
   Long transactions block VACUUM, cause index bloat, and hold shared locks
   that prevent DDL changes.

4. MVCC bloat assessment:
   Identify tables with high UPDATE/DELETE rates — these accumulate dead tuples
   if VACUUM cannot keep pace with the write rate.
   State the autovacuum configuration and whether it is sufficient for the
   write rate.

Output:
Enumerate contention hotspots by table and operation type.
For each deadlock risk: state the lock order inversion and the prevention fix
(standardize lock acquisition order, or reduce transaction scope).
Identify any transaction that should be decomposed to reduce lock duration.
State the autovacuum configuration requirements for high-write tables.
Do not recommend row-level locking (SELECT FOR UPDATE) without quantifying
the throughput impact at the stated concurrent transaction volume.
