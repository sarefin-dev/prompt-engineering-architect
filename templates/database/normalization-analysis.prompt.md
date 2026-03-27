Act as a Staff Database Architect.

Schema:
[REQUIRED: Table definitions with columns and their data types]

Business rules:
[REQUIRED: The functional dependencies and business rules the schema must enforce]

Task:
Analyze the schema for normalization issues.

For each table, identify:

First Normal Form (1NF) violations:
- Repeating groups (multiple columns for the same attribute: address1, address2, address3)
- Non-atomic values (comma-separated lists in a single column)
- Rows without a unique identifier

Second Normal Form (2NF) violations (only relevant for composite primary keys):
- Partial functional dependency: a non-key column depends on only part
  of the composite primary key

Third Normal Form (3NF) violations:
- Transitive functional dependency: column A → column B → column C,
  where B is not a key (B should be in its own table)

Boyce-Codd Normal Form (BCNF) violations:
- Functional dependency where the determinant is not a superkey

Output:
For each violation: state the table, the affected columns, the normal form
violated, the anomaly it produces (update anomaly, insertion anomaly, deletion anomaly),
and the remediation.
Where denormalization is recommended for performance: state the query it serves,
the update overhead it introduces, and the consistency risk.
Provide the normalized schema DDL for each table with violations.
Do not recommend normalization beyond 3NF without explicit performance evidence
that BCNF causes a problem for this system.
