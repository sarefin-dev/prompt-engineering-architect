Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Consumer group, partition count, current instance count]
[REQUIRED: Current throughput, target throughput, processing time per message]

Task:
Design a consumer scaling strategy to meet target throughput.

Address:
1. Maximum parallelism ceiling: partition count limits the number of
   active consumer instances — evaluate whether partition count is sufficient
2. Autoscaling trigger: what metric triggers scale-out?
   Consumer lag (in messages) is preferable to CPU/memory for event pipelines.
3. Scale-out speed: how quickly can new consumer instances join and begin processing?
   What is the rebalancing impact?
4. Scale-in safety: how are in-flight messages handled when a consumer
   instance is removed?
5. Stateful consumer scaling: if the consumer maintains local state
   (aggregations, deduplication cache), how does that state scale?

Output:
Provide the complete scaling strategy covering all five areas.
State the autoscaling trigger metric, threshold, and cooldown period.
Enumerate the sequence of events during scale-out:
   trigger → new instance joins → rebalancing → normal processing.
Identify whether stateful consumer scaling requires state redistribution
and how that is implemented.
State the maximum consumer instance count supported by the current
partition configuration.
