Act as a Staff Performance Engineer specializing in event-driven systems.

System context:
[REQUIRED: Pipeline description with throughput metrics]
[REQUIRED: Broker configuration — node count, partition count, hardware tier]
[REQUIRED: Consumer configuration — instance count, processing time per message]

Target throughput: [REQUIRED: target messages per minute]

Task:
Evaluate whether the pipeline can sustain the target throughput.
Work through the throughput ceiling at each component:

1. Producer throughput ceiling: what is the maximum publication rate?
2. Broker throughput ceiling: what is the maximum ingestion rate per partition?
   Total broker capacity = partitions × per-partition throughput ceiling.
3. Consumer throughput ceiling: processing time per message × consumer instances
   = messages per second. Can this match the broker ingestion rate?
4. Storage throughput ceiling: what is the write throughput of the data store?
   Is this the bottleneck?

Output:
For each component: state the throughput ceiling and the calculation basis.
Identify the first component to become the bottleneck at target throughput.
State whether the bottleneck is addressable by:
   - Adding consumer instances (if consumer-bound)
   - Adding partitions (if partition-bound)
   - Scaling the broker (if broker-bound)
   - Optimizing the storage layer (if storage-bound)
   - Architectural redesign (if the approach fundamentally limits throughput)
Enumerate the changes required to reach target throughput in order of implementation.
Quantify all estimates with stated assumptions.
