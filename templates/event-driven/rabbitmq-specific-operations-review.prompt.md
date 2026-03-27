Act as a Staff Event-Driven Architecture Expert specializing in RabbitMQ.

System context:
[REQUIRED: RabbitMQ configuration — clustering state, exchange types,
 queue durability, persistence mode]
[REQUIRED: Producer publish confirm configuration]
[REQUIRED: Consumer prefetch count and acknowledgement mode]

Task:
Evaluate this RabbitMQ configuration for production readiness.

Assess:
1. Queue durability: are queues declared durable? Non-durable queues lose
   all messages on broker restart.
2. Message persistence: are messages published with delivery-mode=2?
   Non-persistent messages are lost on broker restart even in durable queues.
3. Publisher confirms: are publish confirms enabled? Without them,
   the producer has no delivery guarantee.
4. Consumer prefetch count: is it set appropriately? prefetch=0 (unlimited)
   causes all messages to be delivered to one consumer before acknowledgement.
5. Manual acknowledgement: are consumers using manual ack (not auto-ack)?
   Auto-ack removes the message before it is processed.
6. Clustering and quorum queues: is the cluster configured with quorum queues
   for durability? Classic mirrored queues are deprecated.

Output:
For each configuration item: state the current configuration, the risk,
and the recommended configuration.
Tabulate: Configuration | Current | Recommended | Risk if unchanged.
Enumerate the data loss scenarios in the current configuration under:
   - Broker restart
   - Consumer crash during processing
   - Network partition between cluster nodes
State the migration procedure from classic mirrored queues to quorum queues
if the current configuration uses the deprecated approach.
