Act as a Staff Cloud Security Architect with expertise in data privacy.

System context:
[REQUIRED: System that handles personally identifiable information]
[REQUIRED: PII types — name, email, address, phone, financial, health, behavioral]
[REQUIRED: Current PII handling approach]
[REQUIRED: Applicable regulations — GDPR, CCPA, etc.]

Task:
Review the PII handling architecture for compliance and security.

Assess PII handling across the data lifecycle:

1. Collection: is only necessary PII collected? (data minimization)
   Is there consent for each category of PII collected?

2. Storage: where is PII stored? Is it encrypted at rest?
   Is PII stored in systems that do not require it (logs, analytics, backups)?

3. Processing: is PII accessed only by processes that require it?
   Are PII processing operations logged for audit?

4. Transmission: is PII encrypted in transit?
   Is PII transmitted to third parties? Are data processing agreements in place?

5. Retention: how long is each PII category retained?
   Is there an automated deletion mechanism when the retention period expires?

6. Deletion: when a data subject requests deletion, is PII deleted from
   all systems — including backups, logs, and third-party processors?

7. Breach response: what is the notification procedure for a PII breach?
   (GDPR: 72-hour notification to supervisory authority)

Output:
For each lifecycle stage: state the current control and the compliance gap.
Enumerate the data flows where PII leaves the primary data store:
  analytics pipelines, logging systems, third-party integrations.
Each flow requires a DPA or equivalent legal basis.
Identify where PII may be present in logs or non-production environments
without appropriate protection.
State the data subject rights implementation: access, deletion, rectification,
portability, objection.
Provide the breach notification procedure as numbered steps.
Do not recommend "anonymization" without specifying the technique —
pseudonymization is reversible; true anonymization is not.
