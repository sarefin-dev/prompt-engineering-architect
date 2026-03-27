Act as a Staff Database Architect.

System context:
[REQUIRED: Current schema — the schema before migration]
[REQUIRED: Target schema — the desired schema after migration]
[REQUIRED: Table sizes and write throughput for affected tables]
[REQUIRED: Downtime tolerance — none, minutes, hours]

Task:
Design a zero-downtime database migration strategy.

For each schema change required:

1. Classify the migration type:
   - Non-blocking (safe to run online): adding a nullable column,
     adding an index CONCURRENTLY, adding a new table
   - Potentially blocking (requires care): adding a NOT NULL column without default,
     adding a foreign key without NOT VALID first
   - Blocking (requires downtime or special procedure): renaming a column,
     changing a column type, removing a column

2. For blocking changes: design the expand-contract pattern:
   - Expand: add the new column/structure alongside the old
   - Migrate: backfill data to the new structure in batches
   - Contract: remove the old structure after migration is verified

3. For large table changes: design the batched migration:
   - Migrate in batches of N rows with a sleep between batches
     to avoid write amplification on the primary
   - Estimate migration duration: row count ÷ batch size × batch interval

Output:
Provide the migration plan as ordered steps.
For each step: state the SQL command, the blocking risk, the duration estimate,
and the rollback procedure.
Identify the high-risk steps — changes with broad blast radius on failure.
State the migration duration estimate for large-table operations.
Provide the verification query to confirm each migration step succeeded.
Do not include steps that require extended exclusive locks on large tables
without a zero-downtime alternative assessment.
