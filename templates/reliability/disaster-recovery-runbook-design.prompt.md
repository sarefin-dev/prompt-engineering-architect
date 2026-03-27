Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Architecture with data stores, messaging, and external dependencies]
[REQUIRED: RPO and RTO targets]
[REQUIRED: Current backup and replication strategy]

Task:
Design disaster recovery runbooks for the three most likely failure scenarios.

For each scenario, produce a runbook with:
1. Detection: how is this failure detected, and by what monitoring?
2. Impact assessment: what is the user-visible impact during the outage?
3. Recovery procedure: step-by-step actions to restore service
   (specific enough for an on-call engineer unfamiliar with the system)
4. Data loss assessment: what data may be lost, and how is it quantified?
5. Verification: how is recovery confirmed before declaring the incident resolved?
6. Post-recovery actions: what cleanup or follow-up is required after recovery?

Scenarios to cover:
Scenario A: Primary database failure with automatic failover
Scenario B: Complete loss of the primary region (no automatic failover)
Scenario C: Data corruption in the primary database

Output:
Provide the three runbooks as numbered step-by-step procedures.
Each step must include: the action, the expected outcome, and the
escalation trigger (when to proceed vs. when to escalate).
State the estimated recovery time for each scenario and what
drives that estimate.
Identify the steps that require specialized access or permissions —
these must be pre-provisioned before the incident.
State the DR test procedure: how is each runbook exercised without
impacting production?
Do not write runbooks in prose — write them as numbered steps.
