Act as a Staff Performance Engineer.

System context:
[REQUIRED: Service with latency problems at high percentiles]
[REQUIRED: Latency measurements — p50, p95, p99, p999 if available]
[REQUIRED: Architecture — synchronous call chains, external dependencies]

Task:
Analyze the sources of tail latency and design mitigations.

Diagnose the tail latency contributors:

1. Synchronous fan-out: if the request makes N parallel calls, the latency
   is determined by the slowest call. How many parallel calls are made?
   At p99 latency of each, what is the expected response time for N calls?
   (P(all N under threshold) = P(one under threshold)^N)

2. GC pauses (JVM): if the service is JVM-based, stop-the-world GC pauses
   appear as latency spikes at high percentiles.

3. Lock contention: under high concurrency, contention on shared resources
   produces tail latency spikes for the requests waiting for the lock.

4. Connection pool exhaustion: when the pool is full, requests queue —
   tail latency = queue wait time + processing time.

5. Downstream tail latency: each external call has its own tail latency.
   Hedged requests (issuing the same request to two backends, taking the
   faster response) can reduce tail latency from dependencies.

Output:
For each identified tail latency source: quantify its contribution using
the stated latency measurements and state the mitigation.
Calculate the expected p99 latency improvement from each mitigation.
For synchronous fan-out: state whether hedged requests are applicable
and the cost (doubled requests to the dependency).
Enumerate the tail latency sources that require architectural changes
vs. those addressable through configuration or code changes.
Do not claim to eliminate tail latency — state the achievable reduction
with specific mitigations.
