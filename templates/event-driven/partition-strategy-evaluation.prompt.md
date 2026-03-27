Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Kafka/streaming topic configuration — partition count, partition key]
[REQUIRED: Consumer group configuration — consumer count per group]
[REQUIRED: Message throughput and ordering requirements]

Task:
Evaluate the partition strategy for scalability and correctness.

Assess:
1. Partition count vs. consumer count: can enough consumers be added
   to match throughput at peak load? (Max parallelism = partition count)
2. Partition key selection: does the key distribute load uniformly?
   Are there hot partitions?
3. Ordering requirements: where is ordering required — by partition key only,
   or globally? Does the current design satisfy this?
4. Rebalancing impact: when consumers join or leave, what happens to
   in-flight messages during rebalancing?
5. Future partition count: if the topic needs more partitions later,
   what is the migration procedure and its impact on ordering?

Output:
State whether the current partition count supports target parallelism.
Identify any hot partition risk with the current partition key.
Enumerate the ordering guarantees the current design provides and does not provide.
State the rebalancing impact on in-flight message processing.
Provide the partition count recommendation with throughput calculation.
Explicitly state whether the partition key change is a breaking change
for downstream consumers.
