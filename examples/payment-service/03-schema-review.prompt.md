Act as a Staff Database Architect specializing in large-scale systems.

[REQUIRED: Paste the previously generated outbox table schema here]
[REQUIRED: State the expected peak throughput of the Payment Service per second]

Task: Based on the outbox table schema generated in the previous step, calculate the disk I/O requirements for polling and deletion.

Identify before recommending: Analyze the cost of indexing the `published` boolean flag versus using a partial index on `published = false`. Will the table bloat due to MVCC if we delete published events rapidly? 

Evaluate the schema for scale. Synthesize a recommendation for partition key selection if this table needs to be partitioned later. Provide the exact recommended DDL changes. Prohibit application code.
