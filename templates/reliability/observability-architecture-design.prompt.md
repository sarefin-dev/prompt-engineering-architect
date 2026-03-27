Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System architecture — services, databases, messaging]
[REQUIRED: Current observability state — what monitoring exists today]
[REQUIRED: Failure scenarios that are currently invisible]

Task:
Design a complete observability architecture covering all three pillars.

Pillar 1 — Metrics:
- What metrics must be collected per service tier?
  (Apply the four golden signals: latency, traffic, errors, saturation)
- What is the collection mechanism? (Prometheus scrape, StatsD push, OTel)
- What is the retention period and resolution?
- Define the dashboards: one per service, one for the system as a whole

Pillar 2 — Distributed tracing:
- What is the trace context propagation strategy across service boundaries?
- What is the sampling rate? (Head-based, tail-based, or adaptive)
- What is the trace storage system and retention?
- What is the correlation strategy between traces, logs, and metrics?
  (trace_id in every log line; trace_id as a metric label)

Pillar 3 — Structured logging:
- What fields must appear in every log entry?
  (trace_id, span_id, service_name, environment, severity, timestamp, message)
- What is the log aggregation system?
- What is the retention period?
- What log-based alerts are required?

Output:
Design the observability architecture covering all three pillars.
Define the instrumentation requirements per service:
what the service must emit vs. what the infrastructure provides.
Enumerate the alerts with thresholds, notification channels, and on-call routing.
Define the incident debugging workflow: from alert to root cause,
what is the exact sequence of queries across metrics, traces, and logs?
Enumerate the failure scenarios that remain invisible after this
observability design — every design has blind spots.
