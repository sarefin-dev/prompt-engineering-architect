Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Event streaming platform with retention configuration]
[REQUIRED: Use cases for replay — bug fix reprocessing, new consumer bootstrap,
  audit, disaster recovery]

Task:
Design an event replay architecture.

Address:
1. Retention policy: how long are events retained and for what purpose?
2. Replay safety: how are consumers made idempotent for safe replay?
3. Replay scope: full topic replay vs. time-range replay vs. key-based replay
4. Consumer group management: how is replay isolated from live consumers
   (separate consumer group, offset management)
5. Replay rate: what is the replay throughput and how does it affect
   other consumers?
6. Replay monitoring: how is replay progress tracked and how is completion detected?

Output:
Design the replay architecture covering all six areas.
State the retention period recommendation and the justification —
shorter retention reduces storage cost, longer enables broader replay scenarios.
Describe the replay procedure as runbook steps for the most common
replay scenario in this system.
Enumerate the events that cannot be safely replayed (non-idempotent
side effects) and how those are handled.
State the maximum replay throughput and the impact on live consumer latency.
