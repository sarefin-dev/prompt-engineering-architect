Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: System that requires a message broker]

Requirements:
[REQUIRED: Throughput — messages per second]
[REQUIRED: Ordering guarantees required — per-key, global, or none]
[REQUIRED: Delivery guarantee — at-least-once, exactly-once, at-most-once]
[REQUIRED: Retention — how long messages must be retained]
[REQUIRED: Consumer patterns — streaming, queue, fan-out, or mixed]
[REQUIRED: Operational constraints — team expertise, cloud provider, self-hosted or managed]

Options to evaluate:
Apache Kafka | RabbitMQ | AWS SQS/SNS | Google Pub/Sub | Azure Service Bus

Task:
Evaluate the message broker options against the stated requirements.

For each option:
1. Throughput ceiling: what is the practical throughput limit for this system?
2. Ordering: does it provide the required ordering guarantee?
3. Delivery: does it support the required delivery guarantee natively?
4. Retention: does it support the required retention period and replay?
5. Consumer model: does it support the required consumer patterns?
6. Operational overhead: managed service vs. self-hosted, expertise required
7. Cost at target throughput

Output:
Tabulate the evaluation across all seven dimensions per option.
Eliminate options with Disqualifying ratings before making a recommendation.
Provide the recommendation with the specific configuration requirements
for the chosen broker that satisfy the stated guarantees.
State the configuration changes required to meet the delivery and
ordering requirements — default configurations rarely provide the
strongest guarantees available.
Do not recommend Kafka for use cases where RabbitMQ or a managed queue
is more appropriate — Kafka's operational complexity is not justified for
low-throughput, simple queue patterns.
