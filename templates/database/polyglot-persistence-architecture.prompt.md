Act as a Staff Database Architect specializing in large-scale systems.

System context:
[REQUIRED: System description — services, data categories, access patterns]
[REQUIRED: Current database technology and its limitations]

Requirements:
[REQUIRED: Per-data-category requirements — consistency, latency, query patterns,
  scale, retention]

Task:
Design a polyglot persistence architecture for the stated system.

For each data category, evaluate the fit of each storage technology:

Relational databases (PostgreSQL, MySQL):
Best for: transactional data, complex joins, strong consistency, ACID guarantees.
Not ideal for: high write throughput at scale, flexible schemas, full-text search.

Document stores (MongoDB, DynamoDB):
Best for: flexible schema evolution, nested documents, key-value access patterns.
Not ideal for: complex joins, strong consistency across documents.

Time-series databases (TimescaleDB, InfluxDB):
Best for: high-frequency time-stamped data, time-range queries, metric storage.
Not ideal for: relational data, complex business logic.

Search engines (Elasticsearch, OpenSearch):
Best for: full-text search, faceted filtering, log aggregation.
Not ideal for: transactional writes, strong consistency, complex joins.

Caches (Redis, Memcached):
Best for: read-heavy data, session storage, rate limiting, pub/sub.
Not ideal for: primary storage, complex queries, large datasets.

Column stores (Redshift, BigQuery, ClickHouse):
Best for: analytical queries, aggregations over large datasets, reporting.
Not ideal for: transactional workloads, point lookups, real-time writes.

Output:
For each data category: recommend the storage technology with rationale.
Tabulate: Data category | Recommended store | Justification | Rejected alternatives.
Design the data flow between stores where needed:
  (e.g., PostgreSQL as source of truth → Redis as read cache → Elasticsearch for search)
Enumerate the synchronization mechanisms between stores and their consistency guarantees.
Identify the operational complexity increase from multiple storage technologies
and whether it is justified.
Do not recommend a store for a use case where it has known fundamental limitations —
state the limitation and the design constraint it imposes.
