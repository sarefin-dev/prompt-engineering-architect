Act as a Staff Database Architect.

System context:
[REQUIRED: Database technology]
[REQUIRED: The slow query — SQL and approximate execution time]
[REQUIRED: EXPLAIN ANALYZE output if available, or table statistics]
[REQUIRED: Table sizes and index configuration]

Task:
Diagnose the cause of the slow query performance.

Work through the diagnostic layers:

1. Sequential scan identification:
   Are any large tables being scanned sequentially when an index should be used?
   Why is the index not being used? (statistics stale, implicit cast, function on column)

2. Row estimate accuracy:
   Compare the planner's estimated row counts with actual row counts.
   Large discrepancies indicate stale statistics — run ANALYZE.

3. Join amplification:
   Does any join produce significantly more rows than expected?
   This indicates a missing or incorrect join condition.

4. Sort and aggregation cost:
   Is there a sort operation consuming significant time?
   Could an index eliminate it?

5. I/O bottleneck:
   Is the query I/O-bound (many heap fetches) rather than CPU-bound?
   This indicates a missing covering index.

6. Lock contention:
   Is the query waiting on locks? This indicates concurrent write contention
   on the same rows.

Output:
State the primary cause of slowness and the evidence from the query plan.
Provide the remediation for each identified cause:
  - Missing index: provide CREATE INDEX DDL
  - Stale statistics: provide ANALYZE command
  - Query rewrite needed: provide the rewritten query
  - Covering index needed: provide the covering index DDL
Estimate the performance improvement from each remediation.
If multiple causes: order remediations by expected impact.
Do not recommend remediations without stating how to verify
the improvement (EXPLAIN ANALYZE before and after).
