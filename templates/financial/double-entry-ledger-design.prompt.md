Act as a Staff Database Architect specializing in financial systems.

System context:
[REQUIRED: The financial domain — banking, trading, e-commerce, payroll]
[REQUIRED: The accounts and transaction types that the ledger must support]
[REQUIRED: Scale — transactions per second, total accounts, data retention period]

Task:
Design a double-entry ledger system.

Address the core ledger design principles:

1. Double-entry structure:
   Every financial transaction must have equal debits and credits.
   Design the schema that enforces this invariant at the database level.

2. Immutability:
   Ledger entries must never be modified after commit.
   Corrections are new entries (reversal + correcting entry), not updates.
   Design the schema to prevent UPDATE and DELETE on committed entries.

3. Account balance computation:
   Should account balances be computed on-read (sum of ledger entries)
   or maintained as a running balance? Analyze the trade-off for this system's
   read/write ratio.

4. Transaction isolation:
   What isolation level is required for ledger writes?
   SERIALIZABLE isolation prevents phantom reads but limits throughput.
   REPEATABLE READ may be acceptable for most operations.

5. Temporal queries:
   The ledger must support: balance at any point in time,
   transaction history for any account, and reconciliation reports.
   Design the schema and indexing to support these queries efficiently.

6. Multi-currency:
   If the system handles multiple currencies, how are exchange rates
   applied and stored? Exchange rate at time of transaction must be preserved.

Output:
Provide the ledger schema DDL with all constraints.
The schema must enforce: debit/credit balance at the database level,
immutability via INSERT-only constraints (mandate this — UPDATE and DELETE on
committed financial records are not optional constraints, they are regulatory
requirements), foreign key integrity on all account and transaction references.
State the balance computation strategy with trade-off justification.
Enumerate the temporal query patterns and the indexes required to support them.
Identify any operation that would require modifying a committed ledger entry
and design the correcting entry procedure instead.
Do not design a ledger that allows UPDATE on committed entries under any circumstance —
corrections must go through the audit trail.
