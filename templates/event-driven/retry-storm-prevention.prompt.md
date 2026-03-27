Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Pipeline with retry configuration]
[REQUIRED: Failure scenario — downstream service or database becoming unavailable]

Task:
Analyze retry storm risk and design mitigations.

Diagnose the retry storm scenario:
1. When the downstream dependency fails, how many consumers are retrying simultaneously?
2. With a fixed retry interval, all consumers retry at the same time —
   what is the request spike on the recovering service?
3. Does the retry amplification exceed the recovering service's capacity?
   If so, the service cannot recover.
4. Does the current retry strategy include a circuit breaker?
   If not, consumers continue to attempt connection indefinitely.

Design the retry storm prevention:
1. Exponential backoff with jitter: prevent synchronized retries
2. Circuit breaker on the consumer: stop retrying after N consecutive failures
3. Consumer lag alerting: detect when the pipeline is stalled
4. DLQ routing after max retries: bound the number of retries

Output:
Quantify the retry storm: concurrent retrying consumers × retry rate
= request rate on recovering service.
State whether the current retry configuration produces a retry storm
under dependency failure.
Provide the specific retry configuration: initial delay, multiplier,
jitter range, maximum delay, maximum attempts.
Specify the circuit breaker: failure threshold, wait duration in open state,
half-open probe strategy.
Enumerate the failure and recovery sequence with the mitigations in place.
