Act as a Staff Database Architect specializing in PostgreSQL.

System context:
[REQUIRED: PostgreSQL schema with problem queries]
[REQUIRED: Table size, approximate row counts, and current pg_stat_user_indexes data
  if available]

Task:
Optimize the PostgreSQL indexing strategy for the stated queries.

Evaluate PostgreSQL-specific index capabilities:

1. Partial indexes: can a WHERE clause on the index reduce size significantly?
   (e.g., CREATE INDEX ON orders (created_at) WHERE status = 'pending')

2. Expression indexes: are there queries filtering on a function of a column?
   (e.g., CREATE INDEX ON users (lower(email)) for case-insensitive email lookups)

3. GIN indexes: are there JSONB, array, or full-text search queries?
   Standard B-tree indexes cannot accelerate these.

4. BRIN indexes: are there range queries on monotonically increasing columns
   (timestamps, sequential IDs) on very large tables?
   BRIN is dramatically smaller than B-tree for this pattern.

5. Index bloat: have the indexes been vacuumed recently?
   High-update tables accumulate dead index entries.

6. Visibility map and index-only scans: are visibility map pages up to date?
   Stale visibility maps force heap fetches even for covering indexes.

Output:
For each applicable PostgreSQL index type: evaluate whether it applies
to the stated query patterns and recommend specific indexes.
Provide CREATE INDEX DDL for each recommendation.
State the expected query plan change for each recommendation
(from sequential scan to index scan, from index scan to index-only scan).
Include the EXPLAIN ANALYZE output format expected after the index is created.
Do not recommend a B-tree index for JSONB containment queries —
these require GIN.
