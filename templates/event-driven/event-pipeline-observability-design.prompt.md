Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Pipeline description with current monitoring state]

Task:
Design the observability strategy for this event pipeline.

Cover all three pillars:

Metrics:
- Consumer lag per consumer group and topic/partition
- Message throughput: produced per second, consumed per second
- Processing time per message: p50, p95, p99
- Error rate: processing failures per second, DLQ depth
- Broker health: disk utilization, network throughput, partition leader distribution

Distributed tracing:
- Trace correlation: how does a trace ID propagate from producer to consumer?
- Async boundary: how are traces linked across the broker?
  (Trace context in message headers)
- Sampling: what percentage of messages carry trace context?

Structured logging:
- What fields must appear in every log entry:
  trace_id, message_id, topic, partition, offset, consumer_group,
  processing_status, latency_ms
- Where are logs aggregated and retained?

Output:
Provide the observability design covering all three pillars.
Enumerate the alert conditions with thresholds:
- Consumer lag > [N] messages for > [T] minutes: page
- DLQ depth > [N]: page
- Processing error rate > [X]%: page
- No messages consumed for > [T] minutes: page (dead consumer)
Define the incident debugging workflow: starting from an alert,
what are the exact steps to identify root cause using metrics, traces, and logs?
Identify the current observability gaps — the conditions that would
currently be invisible until user-reported.
