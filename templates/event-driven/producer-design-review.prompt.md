Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Producer service description]
[REQUIRED: Broker technology and topic/exchange configuration]
[REQUIRED: Current publication approach — synchronous, async, transactional]

Task:
Evaluate the producer design for reliability and correctness.

Assess:
1. Publication atomicity: is event publication atomic with the database write?
   If not: what is the risk of database-committed-but-event-not-published?
2. Idempotent production: can the producer safely retry without duplicating events?
3. Message ordering: does the producer guarantee ordering where required?
4. Schema management: how are schema changes deployed without breaking consumers?
5. Back-pressure handling: what does the producer do when the broker is slow or full?
6. Error handling: what happens when publication fails after retries?

Output:
For each assessed dimension: state the current design, the risk it introduces,
and the recommended improvement.
Identify whether the transactional outbox pattern is required for this producer.
Justify the recommendation: if dual writes are currently used, explain
the failure scenario that the outbox pattern prevents.
If the outbox pattern is already in use: evaluate its implementation
for the risks described in the outbox design checklist.
Enumerate the failure scenarios where events can be lost or duplicated
in the current design.
