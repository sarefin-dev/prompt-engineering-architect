Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System architecture with observability stack]
[REQUIRED: A specific incident type to design the debugging workflow for]
Example incident types:
- "p99 API latency has spiked from 200ms to 3 seconds"
- "Error rate on the order service has increased from 0.1% to 5%"
- "Kafka consumer lag is growing — pipeline is falling behind"

Task:
Design the incident debugging workflow for the stated incident type.

Structure the workflow as a decision tree:

Step 1 — Triage (first 5 minutes):
What is the user impact? How many users are affected? Is it growing or stable?

Step 2 — Scope identification (minutes 5–15):
Is this a single service or multiple? Is it all requests or a subset?
What changed recently — deployments, configuration, traffic?

Step 3 — Root cause hypothesis generation (minutes 15–30):
Given the symptoms, what are the top three most likely causes?
What metric or trace would confirm or rule out each hypothesis?

Step 4 — Confirmation and mitigation (minutes 30–60):
For each hypothesis: what is the mitigation while root cause is confirmed?
How is the mitigation applied without making things worse?

Step 5 — Resolution and recovery:
How is the system restored to full health?
What monitoring confirms resolution?

Output:
Provide the debugging workflow as a numbered decision tree.
For each step: list the specific queries to run in each observability tool,
the metrics to examine, and the decision criteria.
State the escalation triggers: when does the incident commander escalate,
and to whom?
Enumerate the common false leads for this incident type —
the symptoms that look like one cause but are actually another.
Define the post-incident documentation requirement: what must be captured
during the incident for the post-mortem.
