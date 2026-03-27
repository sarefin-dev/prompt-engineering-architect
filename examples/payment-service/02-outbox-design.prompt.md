Act as a Staff Distributed Systems Architect specializing in event-driven consistency.

[REQUIRED: Paste the contents of system-context.md here]

Task: Based on the previous review, we are implementing the Transactional Outbox pattern using a polling publisher.

Focus exclusively on the polling publisher implementation details. Ignore the Spring Data JPA repository configuration for the primary entity tables.

Design the Outbox table schema for PostgreSQL and the polling mechanism for Spring Boot. Reason through the polling interval, batch size, lock contention issues across the 3 Kubernetes pods, and the deletion/archival strategy for published events.

Provide the exact PostgreSQL schema for the outbox table. Tabulate the trade-offs of using `SKIP LOCKED` vs. a dedicated leader election for the polling pods. Do not write the Spring Boot implementation code yet.
