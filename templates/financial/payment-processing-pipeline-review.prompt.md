Act as a Staff Distributed Systems Architect specializing in payment systems.

System context:
[REQUIRED: Payment flow — from initiation to settlement]
[REQUIRED: Payment providers and their APIs]
[REQUIRED: Current idempotency strategy]
[REQUIRED: Failure handling — what happens when the payment provider is unavailable]

Regulatory context:
[REQUIRED: Applicable standards — PCI-DSS, PSD2, regional payment regulations]

Task:
Evaluate the payment processing pipeline for correctness, idempotency,
and regulatory compliance.

Assess the critical payment pipeline properties:

1. Exactly-once payment execution:
   Can a payment be charged twice due to retry logic?
   Is the idempotency key stable across retries — does it survive
   process crashes and restarts?
   Does the payment provider support idempotency keys natively?

2. Payment state machine:
   Is there an explicit state machine for payment lifecycle?
   (Initiated → Authorized → Captured → Settled | Failed | Refunded | Disputed)
   Are all state transitions logged?
   Can a payment transition to an invalid state?

3. Timeout and partial failure:
   If the payment provider times out, is the payment status known
   or unknown? What is the query-and-reconcile procedure?

4. Cardholder data handling (PCI-DSS):
   Is cardholder data (PAN, CVV, expiry) handled in the minimum possible scope?
   Is the Cardholder Data Environment (CDE) minimized and segmented?

5. Strong Customer Authentication (if PSD2 applies):
   Is SCA implemented correctly for applicable transactions?
   Are SCA exemptions applied correctly?

Output:
For each property: state the current implementation, the risk, and the
required improvement.
Enumerate the scenarios where a payment could be charged twice —
these are P0 defects requiring immediate remediation.
Enumerate the scenarios where payment status is unknown after a timeout —
these require a reconciliation procedure.
State the PCI-DSS scope — which components are in-scope for PCI-DSS
and what controls are required for each.
Do not accept a retry strategy without idempotency keys for any operation
that charges a customer.
