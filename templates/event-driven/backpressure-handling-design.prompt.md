Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Pipeline with identified consumer lag or slow consumer risk]
[REQUIRED: Upstream producer rate, consumer processing rate, queue depth limits]

Task:
Design a backpressure handling strategy for the pipeline.

Address:
1. Consumer lag monitoring: at what queue depth does backpressure need to apply?
2. Backpressure mechanism: how does slow consumer signal to producer?
   (For Kafka: no native backpressure — evaluate load shedding alternatives)
   (For RabbitMQ: prefetch count controls, flow control mechanism)
3. Load shedding: if the queue fills faster than it drains, what messages
   are shed and how?
4. Producer rate limiting: can the producer slow down in response to lag?
   What is the impact on the upstream producer's clients?
5. Burst capacity: what is the maximum queue depth the broker can hold
   before data loss risk? How much burst does that provide?

Output:
Design the backpressure strategy specific to the broker technology.
State the consumer lag threshold that triggers each response level:
   alert only → slow producer → load shed → reject.
Enumerate the load shedding criteria: which messages are dropped first?
State the burst capacity calculation: max queue depth ÷ ingestion rate
= time before data loss risk at zero consumer throughput.
Explicitly state that Kafka does not implement native backpressure and
the alternatives used for this pipeline.
