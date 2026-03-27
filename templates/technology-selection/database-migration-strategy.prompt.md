Act as a Staff Database Architect.

Current state:
[REQUIRED: Source database — technology, version, data volume, schema]
[REQUIRED: Why migration is required]

Target state:
[REQUIRED: Target database — technology and version]

Constraints:
[REQUIRED: Downtime tolerance — none, minutes, or hours]
[REQUIRED: Data consistency requirements during migration]
[REQUIRED: Application compatibility — can the application be updated simultaneously?]

Task:
Design a database migration strategy that satisfies the stated constraints.

Address the migration phases:

Phase 1 — Schema migration:
- Map source schema to target schema — identify type incompatibilities
- Design the DDL migration script
- Identify schema changes that can be applied online vs. offline

Phase 2 — Data migration:
- Bulk data migration: pg_dump/restore, AWS DMS, or custom ETL?
- Estimated migration duration at source data volume
- Batching strategy for large tables

Phase 3 — Application cutover:
- Dual-write period: write to both source and target, read from source
- Validation period: verify target data matches source
- Read cutover: switch reads to target while writes continue on both
- Write cutover: stop writing to source
- Decommission source

Phase 4 — Rollback:
- At each phase: what is the rollback procedure?
- After which phase is rollback no longer practical?

Output:
Provide the migration plan as ordered phases with detailed steps.
For each phase: state the entry criteria, exit criteria, duration estimate,
and rollback procedure.
Provide the data validation queries that confirm migration correctness
before each cutover.
State the point of no return explicitly.
Enumerate the application changes required at each phase:
  connection string, query compatibility, data type handling.
Do not skip the dual-write validation period — data loss from an
unchecked migration is unrecoverable.
