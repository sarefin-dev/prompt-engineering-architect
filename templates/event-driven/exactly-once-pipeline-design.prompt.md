Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Full pipeline description — producer, broker, consumer, storage]
[REQUIRED: Current delivery guarantee]
[REQUIRED: Business case for exactly-once — what duplication costs]

Task:
Design an exactly-once processing pipeline.

Work through the three boundaries where duplication can occur:

Boundary 1: Producer to broker
   - Idempotent producer: prevents broker-side duplication on producer retry
   - Transactional producer: atomically publishes to multiple topics

Boundary 2: Broker to consumer
   - Transactional consumer: atomically reads, processes, and commits offset
   - Deduplication: consumer-side deduplication using idempotency keys

Boundary 3: Consumer to storage (external side effect)
   - Idempotent storage writes: primary key constraints, upsert semantics
   - Outbox pattern: atomic write + event in single transaction

For each boundary: assess whether exactly-once is achievable with
the current technology stack.

Output:
State which boundary currently allows duplication in the pipeline.
Provide the specific implementation for exactly-once at each boundary
using the available technology.
State the performance impact: throughput reduction and latency increase
from the exactly-once implementation.
Enumerate the failure scenarios that can still produce duplicates
despite the exactly-once implementation — at-least-once is the
fallback for scenarios where exactly-once cannot be guaranteed.
Do not claim exactly-once end-to-end if the storage layer does not
support idempotent writes — state the residual duplication risk.
