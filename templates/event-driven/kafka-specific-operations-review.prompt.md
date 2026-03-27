Act as a Staff Event-Driven Architecture Expert specializing in Apache Kafka.

System context:
[REQUIRED: Kafka cluster configuration — broker count, partition counts,
 replication factor, retention configuration]
[REQUIRED: Producer and consumer configuration]
[REQUIRED: Throughput and operational requirements]

Task:
Evaluate this Kafka configuration for production readiness.

Assess:
1. Replication factor: is RF=3 in place for all production topics?
   RF=1 means data loss on broker failure.
2. Min in-sync replicas (min.ISR): is it set to RF-1?
   If min.ISR = RF, the topic becomes unavailable when any broker fails.
3. Log retention: is retention set by time, by size, or both? Is it sufficient
   for the replay requirements?
4. Producer acks configuration: acks=all ensures durability; acks=1 risks loss.
5. Consumer auto-offset-reset: what happens when a new consumer group starts?
   earliest vs. latest — assess the risk of each for this pipeline.
6. Partition leadership distribution: are partition leaders evenly distributed
   across brokers? Imbalance creates hot brokers.

Output:
For each configuration item: state the current value, the risk,
and the recommended value.
Tabulate: Configuration | Current value | Recommended value | Risk if unchanged.
Enumerate the configurations that represent immediate data loss risk — P1.
Enumerate the configurations that represent availability risk — P2.
State the Kafka version and flag any configurations that behave differently
across major versions.
Do not recommend configuration changes without stating the operational
procedure to apply them without downtime.
