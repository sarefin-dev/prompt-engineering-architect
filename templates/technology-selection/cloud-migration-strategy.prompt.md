Act as a Principal Architect designing a cloud migration.

Current state:
[REQUIRED: On-premise or current cloud infrastructure description]
[REQUIRED: Applications, data volumes, and dependencies]

Target:
[REQUIRED: Target cloud provider and deployment model — IaaS, PaaS, SaaS]
[REQUIRED: Migration goals — cost reduction, scalability, operational efficiency]

Constraints:
[REQUIRED: Compliance and data residency requirements]
[REQUIRED: Downtime tolerance per application]
[REQUIRED: Timeline and budget]

Task:
Design the cloud migration strategy.

Apply the 6R migration framework to each application:

1. Rehost (lift and shift): move as-is to cloud IaaS
   - Fast, low risk, minimal cloud benefit
   - Suitable for: applications with no near-term modernization plans

2. Replatform (lift, tinker, and shift): make targeted optimizations
   - Move to managed services (RDS instead of self-managed MySQL)
   - Suitable for: applications that benefit from managed services without redesign

3. Repurchase (drop and shop): replace with SaaS
   - Suitable for: commodity capabilities (CRM, ERP, email)

4. Refactor/Re-architect: redesign for cloud-native
   - Highest benefit, highest effort
   - Suitable for: applications that require scalability or agility unavailable on-premise

5. Retire: decommission
   - Suitable for: applications with no users or overlapping capability

6. Retain: keep on-premise
   - Suitable for: applications with compliance constraints or recent investment

Output:
Classify each application by 6R category.
Sequence the migration: applications with dependencies must migrate in order.
Identify the applications that should migrate first (quick wins —
low complexity, high savings) vs. last (high risk, high complexity).
State the data migration strategy for each database:
  snapshot and restore, continuous replication, or cutover.
Define the rollback procedure for each application during migration.
Enumerate the compliance and data residency requirements that constrain
which cloud regions each application can use.
