Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Consumer processing logic and storage layer]
[REQUIRED: Current delivery guarantee — at-least-once (duplicates possible)]

Task:
Design a duplicate message handling strategy.

Address:
1. Idempotency key design: what field uniquely identifies each message?
   Is it a business key, a message ID, or a composite key?
2. Deduplication store: where are processed message IDs stored?
   (Database, Redis, Bloom filter) — assess accuracy vs. cost trade-off.
3. Deduplication window: how long are processed IDs retained?
   What happens to messages older than the retention window?
4. Atomicity: how is the idempotency check and the processing action
   made atomic to prevent TOCTOU race conditions?
5. Performance impact: what is the overhead of the deduplication check
   on processing throughput?

Output:
Provide the complete deduplication design.
Specify the idempotency key — it must be: stable (same key on retry),
unique (different key for different messages), and extractable before processing.
State the deduplication store selection rationale.
Describe the atomic check-and-process pattern to prevent race conditions
between concurrent consumer instances processing the same message.
State the false-positive rate if a probabilistic structure (Bloom filter) is used.
Enumerate the failure scenarios where duplicate processing may occur
despite the deduplication strategy.
