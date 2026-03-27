Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: The financial data flows requiring reconciliation]
[REQUIRED: Source systems and their data formats]
[REQUIRED: Target system and its data format]
[REQUIRED: Reconciliation frequency required]

Task:
Design a financial data reconciliation process.

Address:
1. Reconciliation scope:
   What data must match between source and target?
   Define the reconciliation keys — the fields that uniquely identify a record
   across systems.

2. Match types:
   - Exact match: records identical in all reconciliation fields
   - Toleranced match: records within a defined tolerance (rounding, FX rates)
   - Unmatched: records in source but not target (missing items)
   - Orphaned: records in target but not source (spurious items)

3. Break classification:
   When a break is detected, classify it:
   - Timing difference: the target will catch up (T+1 settlement lag)
   - System error: data processing failure requiring investigation
   - Data quality issue: invalid data in source or target
   - Fraud indicator: unmatched items that should not exist

4. Break resolution workflow:
   Who investigates each break type?
   What is the resolution SLA per break classification?
   How are resolved breaks documented?

5. Reconciliation reporting:
   Who receives the reconciliation report?
   What is the escalation trigger — at what break count or value does
   escalation to management occur?

Output:
Design the reconciliation process covering all five areas.
Provide the reconciliation algorithm: match on primary key, then
apply tolerance for value fields, classify unmatched records.
Define the break report format: Break ID | Type | Source value | Target value |
Difference | Age | Owner | Status.
State the SLA for each break type: timing differences have a T+N resolution
expectation; system errors require same-day investigation.
Enumerate the scenarios where reconciliation breaks are expected
(normal market close lag) vs. unexpected (breaks outside normal patterns).
Do not design a reconciliation process where breaks older than one
business day can exist without escalation.
