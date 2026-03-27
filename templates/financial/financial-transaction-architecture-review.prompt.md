Act as a Staff Distributed Systems Architect specializing in financial systems.

System context:
[REQUIRED: Financial system description — what financial operations it performs]
[REQUIRED: Transaction types — payments, ledger entries, trades, settlements]
[REQUIRED: Regulatory framework — PCI-DSS, SOX, MiFID II, GDPR, or domain-specific]
[REQUIRED: Current architecture — services, databases, messaging]

Financial requirements:
[REQUIRED: Consistency model required — state why eventual consistency is or is not acceptable]
[REQUIRED: Auditability requirements — what must be logged and retained]
[REQUIRED: Regulatory reporting requirements — what reports are produced and how often]

Task:
Evaluate this financial system architecture for correctness, compliance, and auditability.

Focus on the dimensions specific to financial systems:

1. Transaction atomicity:
   Are all financial operations — balance updates, ledger entries, event publication —
   performed atomically? What is the failure mode if any component fails mid-transaction?

2. Idempotency:
   Can every financial operation be safely retried without duplication?
   What is the idempotency key strategy for payment and settlement operations?

3. Causal ordering:
   For operations that must occur in causal sequence (debit before credit,
   risk check before trade execution), is causal ordering enforced?

4. Audit trail:
   Scrutinize the audit trail for gaps — every financial operation must have
   a corresponding audit log entry; any mutation without one is a compliance defect.
   Specifically: who, what, when, from what system, with what authorization?
   Is the audit log append-only and tamper-evident?
   Scrutinize whether the audit log write is atomic with the operation it records
   — a write-then-log pattern is an audit gap under process crash.

5. Reconciliation:
   How does the system verify that internal records match external
   systems (bank feeds, exchange confirmations)?
   What is the reconciliation frequency and the resolution procedure for breaks?

6. Regulatory reporting:
   How are regulatory reports generated? From live transaction data or
   from a separate reporting store?

Output:
Provide a structured analysis with one section per focus area.
For each section: state the current design, the compliance gap, and the
required improvement.
Enumerate the scenarios where data loss or duplication would constitute
a financial or regulatory reporting error — these are P0 risks.
State the consistency model applied to each data category and whether
it satisfies the regulatory requirement.
Scrutinize every operation that modifies financial records — explicitly identify
any without a corresponding audit log entry. Any audit gap is a compliance defect,
not a recommendation.
Do not accept eventual consistency for account balance updates or
ledger entries without a specific compliance justification.
