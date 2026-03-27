Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Pipeline with processing failures]
[REQUIRED: Current retry configuration or lack thereof]
[REQUIRED: Types of failures: transient vs. permanent]

Task:
Design a dead-letter queue strategy for the pipeline.

Address:
1. Retry policy: how many retries, with what backoff, before routing to DLQ?
2. DLQ routing trigger: which failures go to DLQ immediately (unrecoverable)?
   Which are retried first?
3. DLQ storage: same broker technology as the main queue, or separate store?
4. DLQ monitoring: what alerts are required on DLQ depth and message age?
5. DLQ replay: how are DLQ messages replayed after the root cause is fixed?
   Can replay be triggered per message, per batch, or only full replay?
6. Poison message detection: how are messages that always fail detected
   and quarantined to prevent DLQ loops?

Output:
Provide the complete DLQ design covering all six areas.
Specify the retry policy: attempts, backoff algorithm (exponential with jitter),
minimum and maximum backoff interval.
State the DLQ alert thresholds: depth, message age, and growth rate.
Enumerate the failure types and their routing: retry first vs. DLQ immediately.
Describe the replay procedure as runbook steps.
Explicitly handle the DLQ loop scenario: a message replayed from DLQ
that immediately fails again and returns to DLQ.
Do not design a retry strategy with fixed intervals — always use
exponential backoff with jitter.
