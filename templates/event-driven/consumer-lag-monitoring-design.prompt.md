Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Kafka/RabbitMQ pipeline with consumer groups]
[REQUIRED: Throughput profile — normal and peak]
[REQUIRED: Current monitoring approach for consumer lag]

Task:
Design a consumer lag monitoring strategy.

Address:
1. Lag metric definition: consumer lag in messages vs. consumer lag in time —
   which is appropriate for this pipeline?
2. Per-partition vs. aggregate lag: when is per-partition monitoring required?
3. Alert thresholds: at what lag level does the situation require:
   a. Warning alert (team notified)
   b. Page alert (on-call woken)
   c. Escalation alert (incident declared)
4. Lag trend: how is lag growth rate monitored? A growing lag at 50,000 messages
   is more urgent than a stable lag at 200,000 messages.
5. Dead consumer detection: if consumer lag grows because no consumer is running,
   how is this detected differently from a slow consumer?

Output:
Define the lag metric and thresholds for each alert level.
Specify the monitoring implementation: what tool, what query, what interval.
Distinguish the alert for a slow consumer (lag growing slowly) from
a dead consumer (lag growing at the production rate).
Provide the on-call runbook for each alert level — what to check first,
what to try first, when to escalate.
State the acceptable lag at peak load — lag is expected to grow during
peak and should not page if it recovers within the acceptable window.
