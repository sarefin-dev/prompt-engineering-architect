Act as a Staff Distributed Systems Architect specializing in financial and regulated systems.

System context:
[REQUIRED: System description — what operations must be audited]
[REQUIRED: Regulatory audit requirements — what events, what retention, what format]
[REQUIRED: Current audit logging approach, if any]

Task:
Design a complete audit trail for the stated system.

Address the audit trail properties required for regulatory compliance:

1. Completeness:
   What events must be logged? Define the exhaustive list:
   - Authentication events (login, logout, failed login, MFA)
   - Authorization events (access granted, access denied)
   - Data access events (read of sensitive data)
   - Data modification events (create, update, delete)
   - Financial events (all transactions, regardless of outcome)
   - Administrative events (configuration change, user management, role change)
   - System events (startup, shutdown, failure, recovery)

2. Immutability:
   The audit log must be append-only — no modifications or deletions
   after write. How is this enforced?
   - Database: INSERT-only table with no UPDATE/DELETE permissions
   - Event streaming: append-only Kafka topic with retention policy
   - Object storage: write-once S3 bucket with object lock

3. Tamper evidence:
   How is the audit log protected against silent modification?
   - Cryptographic chaining: each log entry includes a hash of the previous entry
   - External verification: periodic export to an independent system

4. Completeness verification:
   How does the system verify that no audit events were dropped?
   - Sequence numbers: monotonically increasing per source
   - Reconciliation: periodic count reconciliation between the source and the audit log

5. Query capability:
   Regulators will query the audit log by: time range, user, resource, event type.
   Design the indexing to support these queries within acceptable latency.

6. Retention:
   What is the required retention period per event type?
   How is data purged at the end of the retention period
   without violating immutability of unretired records?

Output:
Provide the audit trail design covering all six properties.
Provide the audit event schema — the fields that must appear on every event:
  event_id, timestamp (UTC), actor_id, actor_type, action, resource_type,
  resource_id, outcome, source_ip, session_id, correlation_id.
State the storage technology recommendation with tamper-evidence justification.
Define the retention policy per event category.
Enumerate the audit gaps in the current design — operations that are not logged.
Do not design an audit trail that can be modified by any user, including administrators.
An audit trail that can be modified by administrators provides no audit guarantee.
