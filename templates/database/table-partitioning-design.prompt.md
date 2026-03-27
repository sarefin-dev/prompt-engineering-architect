Act as a Staff Database Architect specializing in large-scale PostgreSQL systems.

System context:
[REQUIRED: Table to be partitioned — schema, current size, growth rate]
[REQUIRED: Query patterns — how the table is queried, common filter columns]
[REQUIRED: Retention requirements — how long data must be retained]

Task:
Design a partitioning strategy for the stated table.

Evaluate the three partitioning approaches:

1. Range partitioning (most common for time-series data):
   - Partition by a date or timestamp column
   - Assess: does every query include the partition key in its WHERE clause?
     Queries without the partition key scan all partitions.
   - Design the partition interval: daily, weekly, monthly — based on
     data volume and query granularity
   - Design the partition management: pg_partman for automated creation
     and retention-based dropping

2. List partitioning:
   - Partition by a discrete value (e.g., tenant_id, region, status)
   - Assess: is the cardinality of the partition key bounded and stable?
     Unbounded cardinality produces unmanageable partition counts.

3. Hash partitioning:
   - Partition by hash of the partition key
   - Assess: are range queries on the partition key required?
     Hash partitioning makes range queries inefficient.

Output:
Recommend the partitioning approach with rationale specific to this table.
For the recommended approach: specify the partition key, the partition
interval or list values, and the partition count.
Design the partition management procedure:
  how are new partitions created, and how are old partitions dropped?
Enumerate the queries that will NOT benefit from partition pruning —
these still scan all partitions and may perform worse than an unpartitioned table.
State the index strategy for the partitioned table:
  indexes must be created per partition (PostgreSQL automatically propagates
  indexes created on the parent table to partitions).
Do not recommend partitioning without assessing the partition pruning
coverage of the stated query patterns.
