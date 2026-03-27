Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Service topology — services, their communication patterns]
[REQUIRED: Current observability state — what tracing exists, if any]

Requirements:
[REQUIRED: What questions must distributed tracing answer?
 e.g., "Why did this request take 3 seconds?",
 "Which service caused this error?"]

Task:
Design a distributed tracing strategy for the stated system.
Address:
1. Trace context propagation: how trace IDs travel across service boundaries
   (HTTP headers, message headers, async boundaries)
2. Instrumentation approach: automatic (agent-based) vs. manual SDK
3. Sampling strategy: head-based, tail-based, or hybrid
4. Storage and retention: where traces are stored and for how long
5. Async boundary handling: how traces are correlated across Kafka or RabbitMQ
6. Correlation with logs and metrics: how trace IDs link to structured logs

Output:
Provide the tracing design covering all six areas.
Specify the trace context propagation for each communication protocol used
(HTTP, Kafka, RabbitMQ, gRPC).
State the sampling rate rationale — low sampling misses rare errors,
high sampling is expensive. Recommend tail-based sampling where it is
justified.
Enumerate the service boundaries where trace propagation currently breaks —
these are the highest-priority instrumentation gaps.
State the query patterns the tracing system must support and verify
the recommended storage solution supports them.
