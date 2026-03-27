Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Pipeline with ordering requirements]
[REQUIRED: Current partition key and consumer parallelism]

Business requirements:
[REQUIRED: Which events must be processed in order — and for what business reason]

Task:
Design an ordering strategy that satisfies the business requirements.

Work through:
1. Identify the ordering unit: per-entity ordering (e.g., all events for
   order-123 must be in order) vs. global ordering (all events in order)
2. For per-entity ordering: map the ordering unit to a partition key —
   events for the same entity must route to the same partition
3. Evaluate whether the current partition count limits parallelism too severely
4. Identify where ordering requirements conflict with parallelism requirements
5. Design the out-of-order event handling: how are late-arriving or
   out-of-order events detected and handled?

Output:
State the ordering guarantee the current design provides vs. what is required.
Specify the partition key that satisfies per-entity ordering requirements.
Enumerate the trade-off between ordering granularity and parallelism:
   a single partition provides global ordering but limits parallelism to one consumer.
State how the system detects and handles out-of-order events.
Identify the business consequences of relaxing the ordering requirement —
where eventual ordering (rather than strict ordering) is acceptable.
