Act as a Principal Microservices Architect specializing in financial transaction flows.

[REQUIRED: Paste the contents of system-context.md here]

Focus exclusively on the transaction boundary between the PostgreSQL database commit and the Kafka message publish. Ignore the API layer routing and the Stripe integration details for this pass.

Evaluate this architecture for the dual-write problem. Reason through the failure modes where the database commit succeeds but the Kafka publish fails, and vice versa.

Enumerate the risks in this flow. Proscribe a specific architectural pattern to guarantee at-least-once delivery to Kafka without risking double-charges. Prohibit generalized advice; be specific to Spring Boot, PostgreSQL, and Kafka.
