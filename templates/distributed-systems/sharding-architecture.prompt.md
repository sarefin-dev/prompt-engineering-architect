Act as a Staff Database Architect specializing in large-scale systems.

System context:
[REQUIRED: Database technology, current data volume, growth projection]
[REQUIRED: Current query patterns — read/write ratio, key access patterns]

Sharding objective:
[REQUIRED: Target data volume or write throughput requiring sharding]

Task:
Design a sharding architecture for the stated database.
Cover:
1. Shard key selection — rationale, distribution analysis, hot shard risk
2. Shard count — initial and projected, with resharding strategy
3. Cross-shard query handling — which queries span shards and at what cost
4. Routing layer design — how clients locate the correct shard
5. Rebalancing strategy — how data moves when shards are added
6. Failure isolation — what happens when one shard is unavailable

Output:
Provide a structured design covering all six areas.
Explicitly state the queries that become cross-shard after sharding
and the performance impact of each.
State the resharding approach (consistent hashing / range-based / directory-based)
and the operational procedure for adding a shard.
Enumerate the three highest-risk operational events in the sharded architecture
and the mitigation for each.
Do not recommend a sharding strategy without assessing the resharding cost.
