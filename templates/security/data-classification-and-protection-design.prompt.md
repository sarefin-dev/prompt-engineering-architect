Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: System with sensitive data — describe the data types handled]
[REQUIRED: Applicable regulations — GDPR, PCI-DSS, HIPAA, SOX, etc.]
[REQUIRED: Current data protection controls]

Task:
Design a data classification and protection framework.

Phase 1 — Classification:
Classify all data categories by sensitivity:

Public: No protection required beyond integrity
Internal: Accessible to authenticated employees
Confidential: Restricted to authorized roles; business-sensitive
Restricted: Highest sensitivity — PII, financial, health, credentials

For each data category in the system: assign a classification.

Phase 2 — Protection controls per classification:
For Confidential and Restricted data, define:
1. Encryption at rest: algorithm, key management, key rotation frequency
2. Encryption in transit: TLS version, certificate validation
3. Access control: who can read, who can write, who can delete
4. Audit logging: what access events are logged
5. Retention and deletion: how long retained, how securely deleted
6. Masking and tokenization: where sensitive values must be masked
   in logs, APIs, and UI displays

Output:
Provide the data classification for each data category.
Design the protection controls for each classification level.
Enumerate the data flows where Restricted data crosses trust boundaries —
each crossing requires explicit protection review.
Identify where Restricted data may currently be logged, cached, or
transmitted without appropriate protection.
State the data subject rights implementation for GDPR-scope data:
right to access, right to deletion, right to rectification.
Do not recommend encryption without specifying key management —
encrypting with a key stored next to the data provides no security.
