Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Service architecture — what the service does, its dependencies]
[REQUIRED: Current metrics collection stack]

Task:
Define and implement the four golden signals for each service tier.

For each service, define:

1. Latency:
   - What to measure: time from request receipt to response sent
   - Histogram buckets: [10ms, 50ms, 100ms, 200ms, 500ms, 1s, 5s]
   - Distinguish successful requests from failed requests — failed requests
     may be fast (immediate error) and should not lower the latency percentiles
   - Alert on: p99 latency > [SLO threshold] for > 5 minutes

2. Traffic:
   - What to measure: requests per second, events per second
   - Distinguish by endpoint or event type to identify traffic changes
   - Alert on: traffic drops > 50% vs. same hour last week (dead service)
   - Alert on: traffic spikes > 3x normal (potential abuse or bug)

3. Errors:
   - What to measure: error rate as a percentage of total requests
   - Distinguish 5xx from 4xx — 5xx are service errors; 4xx are client errors
   - Alert on: 5xx error rate > [threshold] for > 2 minutes

4. Saturation:
   - What to measure: the resource most likely to constrain the service
     (CPU utilization, memory utilization, connection pool usage, queue depth)
   - Alert on: saturation > 80% sustained — headroom is running out

Output:
Define the four golden signals for each service in the stated system.
Provide the Prometheus metric definitions (metric name, labels, type) for each.
Provide the alert rules (PromQL) for each signal.
Define the dashboard layout: one row per golden signal,
the most important metric prominently displayed.
Identify which signal is most likely to fire first in the common failure scenarios.
