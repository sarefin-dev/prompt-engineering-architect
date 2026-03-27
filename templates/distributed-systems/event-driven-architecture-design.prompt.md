Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Business domain and the events that drive it]
[REQUIRED: Current synchronous communication that is being replaced or augmented]

Requirements:
[REQUIRED: Throughput, ordering guarantees, delivery guarantees]
[REQUIRED: Consumer types — real-time, near-real-time, batch]

Task:
Design an event-driven architecture for the stated system.
Address:
1. Event taxonomy: what events exist, their schema, and their semantic meaning
2. Topic/queue design: how events are organized for routing and parallelism
3. Producer design: idempotent publication, schema versioning
4. Consumer design: consumer groups, parallelism, idempotency
5. Event ordering: where ordering is required and how it is guaranteed
6. Schema evolution: how consumer and producer schemas can evolve independently

Output:
Provide the event-driven design covering all six areas.
For each event type: name, trigger, schema (key fields), ordering requirement,
consumer types, and retention requirement.
Tabulate: Event | Topic | Partition key | Ordering guarantee | Delivery guarantee.
Enumerate the cases where events must be consumed in order — these constrain
parallelism and must be explicitly designed for.
State the schema evolution strategy: backward compatible only, or forward
compatible too — with the implication for consumer upgrade sequencing.
