Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Full architecture including data stores and their replication state]

Business requirements:
RPO (Recovery Point Objective): [REQUIRED — maximum acceptable data loss]
RTO (Recovery Time Objective): [REQUIRED — maximum acceptable downtime]
Scope of recovery: [REQUIRED — full system, single region, single service]

Task:
Design a disaster recovery strategy that satisfies the stated RPO and RTO.
Address:
1. Backup strategy: what is backed up, how often, and where stored
2. Recovery procedure: step-by-step for each failure scenario
3. Failover automation: which steps can be automated vs. must be manual
4. Data validation: how is the integrity of recovered data verified
5. Testing strategy: how is the DR plan exercised without impacting production

Output:
Provide the DR design covering all five areas.
State the actual RPO and RTO achievable with the recommended design —
if the stated requirements cannot be met with the current architecture,
state what architectural changes are required to meet them.
Enumerate the recovery procedures as runbook steps — specific enough
that an on-call engineer unfamiliar with the system can execute them.
Explicitly state the failure scenarios the DR plan does NOT cover.
Define the DR test frequency and the criteria for declaring a DR test successful.
Do not design a DR plan that has never been tested — include a
first-exercise procedure as part of the plan.
