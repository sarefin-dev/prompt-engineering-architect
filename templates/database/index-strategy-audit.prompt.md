Act as a Staff Database Architect.

System context:
[REQUIRED: Database technology]
[REQUIRED: Table schema with existing indexes]
[REQUIRED: Query patterns — the most frequent and most critical queries,
  with approximate execution frequency and criticality]

Task:
Audit the indexing strategy against the stated query patterns.

For each query pattern:
1. Identify which index (if any) the query uses
2. Evaluate whether the index fully satisfies the query or whether
   a table heap fetch is still required (index scan vs. index-only scan)
3. Identify whether the column order in composite indexes matches
   the query's filter and sort order (higher selectivity columns first)

For each existing index:
1. Identify the queries it serves
2. Assess whether it is used — or whether it is write overhead with no read benefit
3. Evaluate for redundancy — is it a prefix of another index?

Output:
Tabulate the query-to-index mapping: Query | Index used | Scan type | Heap fetch required.
For each index: classify as essential, useful, redundant, or unused.
Recommend unused and redundant indexes for removal — with the write
cost reduction calculation.
Recommend missing indexes for high-frequency queries missing index coverage.
For each recommended new index: specify the exact column order and
the query it serves.
Do not recommend an index without naming the query it serves.
Do not recommend composite index column orders without stating the
selectivity rationale.
