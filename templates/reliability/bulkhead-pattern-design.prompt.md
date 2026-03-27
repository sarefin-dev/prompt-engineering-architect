Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Service with multiple downstream dependencies or multiple tenant types]
[REQUIRED: The failure scenario that requires bulkhead isolation]

Task:
Design a bulkhead pattern to isolate failures between workload types.

Evaluate two bulkhead approaches:

1. Thread pool bulkhead: separate thread pools per downstream dependency
   - Each dependency gets a fixed thread pool — exhaustion of one pool
     does not affect others
   - Trade-off: more threads total; idle threads waste memory

2. Semaphore bulkhead: limit concurrent calls per dependency
   - A semaphore limits the number of concurrent calls to one dependency
   - Lighter weight than thread pools; appropriate for non-blocking code

For the stated failure scenario:
1. Which workloads or dependencies require isolation from each other?
2. What is the maximum acceptable concurrency per bulkhead?
3. What happens when the bulkhead limit is reached?
   (Fail fast, queue with timeout, or shed load)
4. How does a bulkhead interact with the circuit breaker on the same dependency?

Output:
Recommend the bulkhead type (thread pool vs. semaphore) with rationale.
Specify the bulkhead configuration: pool size or semaphore count per dependency.
State the interaction with the circuit breaker — bulkhead limits concurrent calls,
circuit breaker stops calls when failure rate is high; both together provide layered protection.
Enumerate the failure scenarios the bulkhead prevents vs. the circuit breaker.
State the monitoring required: bulkhead rejection rate is a leading indicator
of resource pressure before the circuit opens.
