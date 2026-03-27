Act as a Staff Database Architect.

System context:
[REQUIRED: Table schema, existing indexes, and the high-frequency queries
  that are currently performing heap fetches after index scans]

Task:
Design covering indexes to eliminate heap fetches for the stated queries.

For each target query:
1. Identify the columns in the WHERE clause (index scan columns)
2. Identify the columns in the SELECT clause (columns needed in the output)
3. Identify the columns in the ORDER BY clause (sort columns)
4. Design the covering index: scan columns (higher selectivity first),
   then INCLUDE columns (from the SELECT clause not already in the index key)
5. Assess the write overhead: how many rows are written per second
   to this table? Estimate the covering index maintenance cost.
6. Assess the storage cost: estimate the index size relative to table size.

Output:
For each covering index: provide the CREATE INDEX DDL with column order
and INCLUDE columns.
State the query it eliminates heap fetches for and the expected
performance improvement (index-only scan vs. index + heap fetch).
State the write overhead added by the covering index.
Identify the covering indexes that are worth the write overhead vs.
those where the read benefit does not justify the write cost.
Do not recommend covering indexes on tables with very high write rates
without explicitly evaluating the write amplification trade-off.
