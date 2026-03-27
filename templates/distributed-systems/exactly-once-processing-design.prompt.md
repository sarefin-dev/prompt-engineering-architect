Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Event processing pipeline — producer, broker, consumer, storage]
[REQUIRED: Current delivery guarantee — at-least-once or at-most-once]

Requirements:
[REQUIRED: Why exactly-once is required — what duplicate processing causes]

Task:
Design an exactly-once processing strategy for the stated pipeline.

Work through the three levels of exactly-once:
Level 1 — Exactly-once within the broker:
[Kafka idempotent producer: enable.idempotence=true, acks=all, retries=MAX_INT.
 Transactional API: transactional.id set, initTransactions() called before produce.
 This prevents duplicate messages from producer retries at the broker level only.]

Level 2 — Exactly-once across broker and consumer:
[Read-process-commit atomicity requires ALL of the following:
 Producer: enable.idempotence=true, transactional.id set
 Consumer: isolation.level=read_committed (default is read_uncommitted — this is
 the most commonly missed configuration; without it, the consumer reads
 uncommitted messages and the atomicity guarantee does not hold)
 Offset commit: sendOffsetsToTransaction() within the producer transaction,
 not commitSync() — commitSync() breaks the atomicity guarantee.
 Note: this provides exactly-once within the Kafka topology only —
 external side effects (database writes, API calls) are NOT covered by this level.]

Level 3 — Exactly-once end-to-end (including external side effects):
[Outbox pattern: atomic write + outbox insert in single database transaction,
 then publish from outbox (polling or CDC-based — see Template 17).
 Idempotency keys: consumer-side deduplication store keyed on message ID.
 Deduplication store TTL must exceed the maximum retry window.
 This is the only level that covers external storage and API side effects.]

For each level: assess whether it is achievable with the current stack
and what configuration or code changes are required.

Output:
State which level of exactly-once is required for the business case.
For the required level: provide the specific implementation design.
Enumerate the failure scenarios that can cause duplicate processing
and how each is detected and prevented.
State the performance impact of the exactly-once implementation
compared to at-least-once delivery.
Explicitly acknowledge that exactly-once end-to-end requires
the external system (database, API) to support idempotent operations —
enumerate which external systems require this and how it is achieved.
