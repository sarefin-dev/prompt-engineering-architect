Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Consumer service description]
[REQUIRED: Broker technology, topic/queue, consumer group configuration]
[REQUIRED: Current processing logic — what the consumer does with each message]
[REQUIRED: Retry strategy, DLQ configuration, idempotency approach]

Task:
Evaluate the consumer design for reliability, idempotency, and scalability.

Assess:
1. Idempotency: is the consumer safe to run multiple times with the same message?
   What is the deduplication strategy?
2. Offset/acknowledgement management: when is the message acknowledged?
   Before or after processing? What is the risk of each?
3. Error handling: what happens on processing failure? Retry? DLQ? Both?
4. Scalability: what constrains the number of consumer instances?
   Is there shared mutable state that prevents scaling?
5. Ordering: if ordering is required, how is it preserved across consumer instances?
6. Poison message handling: what happens when a message always fails processing?

Output:
For each dimension: state the current design, the failure mode it introduces,
and the recommended improvement.
Explicitly state whether the consumer is currently idempotent and the
evidence for that assessment.
Enumerate the message processing states: received, processing, processed,
failed, dead-lettered — and verify all transitions are handled.
Identify the conditions under which a message could be processed twice
in the current design — these are the duplicate processing risks.
