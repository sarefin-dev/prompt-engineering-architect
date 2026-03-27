Act as a Staff Database Architect.

System context:
[REQUIRED: Database technology and table structure]
[REQUIRED: Current data volume and growth rate]
[REQUIRED: Regulatory retention requirements if any]
[REQUIRED: Query patterns on historical data]

Task:
Design a data archival and retention strategy.

Address:
1. Retention tiers:
   - Hot tier: actively queried data — primary database, full indexes
   - Warm tier: occasionally queried — partitioned tables, reduced indexes,
     possibly compressed
   - Cold tier: rarely queried — object storage (S3), query via external table

2. Archival criteria: what determines when a record moves from hot to warm to cold?
   (Age, query frequency, business event — e.g., order closed)

3. Archival procedure: how is data moved without impacting production queries?
   (Partitioned tables allow dropping partitions; non-partitioned require DELETE batches)

4. Archive query access: how is cold data queried when needed?
   (PostgreSQL foreign data wrappers, Athena over S3, Snowflake external tables)

5. Compliance and auditability: if regulatory retention applies,
   how is the retention period enforced and audited?

6. Recovery: if archived data needs to be restored to the hot tier,
   what is the procedure and time estimate?

Output:
Design the three-tier retention strategy with tier definitions and transitions.
State the archival procedure as operational steps.
State the cold storage query mechanism and its latency implications.
Estimate the storage cost reduction from the archival strategy at current data volume.
Enumerate the data categories where archival is risky
(data referenced by foreign keys, data subject to ongoing updates).
State the compliance verification procedure if regulatory retention applies.
