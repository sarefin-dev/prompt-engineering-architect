Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: The business transaction that spans multiple services]
[REQUIRED: The services involved and their operations]
[REQUIRED: What must be rolled back if the transaction fails]

Task:
Design a Saga pattern implementation for the stated distributed transaction.

Decision 1: Recovery strategy — reason through this before designing the steps.
A Saga can fail at any step. There are two fundamentally different recovery strategies:

Backward recovery (rollback):
When a step fails, compensate all previously completed steps in reverse order.
The transaction ends in a cancelled state.
Use when: the business cannot tolerate a partial outcome and compensation for
all steps is achievable (no non-compensable steps in the critical path).
Example: flight booking — if hotel fails after flight reserves, cancel the flight.

Forward recovery (retry to completion):
When a step fails, retry that step until it succeeds (with backoff and timeout).
The saga does not compensate completed steps — it drives toward completion.
Use when: the transaction must complete (not just be cancelled), the failing
step is retryable, and partial outcomes are worse than delayed completion.
Example: payment processing — if the settlement step fails after authorization,
retry settlement rather than voiding the authorization.
Not usable when: the failing step is non-retryable (external service is down
indefinitely) or the business accepts cancellation as an outcome.

State which recovery strategy is correct for this transaction and why.
If the transaction has steps requiring different strategies (some forward,
some backward), design the hybrid: state the pivot point — after which step
does the saga commit to forward recovery only.

Decision 2: Orchestration vs. Choreography
Evaluate both approaches for this specific transaction:
- Orchestration: central coordinator directs each step (advantages: visibility,
  central error handling; risks: orchestrator as SPOF)
- Choreography: each service reacts to events and emits completion events
  (advantages: loose coupling; risks: hard to reason about, difficult to debug)
Recommend one approach with explicit rationale. State whether the chosen
recovery strategy (forward vs. backward) influences the architectural choice
— orchestrated sagas handle forward recovery more cleanly; choreographed
sagas make backward compensation harder to reason about.

For the recommended approach:
1. Define the transaction steps in order
2. For each step: state whether it supports forward recovery, backward
   recovery, or neither (non-compensable, non-retryable)
3. Define the compensating transaction for each backward-recovery step
4. Define what triggers compensation (which failure conditions)
5. Define the retry policy for each forward-recovery step (backoff, timeout,
   maximum attempts, circuit breaker threshold)
6. Design the idempotency strategy for each step and compensation
7. Design the monitoring and observability for saga state

Output:
State the recovery strategy (backward / forward / hybrid) with business justification.
Provide the complete saga design for the recommended approach.
For backward-recovery steps: enumerate all compensating transactions —
every step that can fail must have a defined, idempotent compensation.
For forward-recovery steps: state the retry policy and the failure threshold
at which the saga transitions to backward recovery or enters a stuck state.
Identify steps where neither recovery strategy applies (side effects already
taken — e.g., email sent, payment charged to card) — design the explicit
handling for these: manual intervention queue, compensating notification,
or business-level correction procedure.
State the saga state machine: the valid states and transitions for both
the happy path and both recovery paths.
Enumerate the failure scenarios and the recovery sequence triggered by each.
Do not design a saga without explicitly choosing a recovery strategy —
an unspecified recovery strategy is a design debt that becomes a production
incident when the first step fails at 2am.
Do not assume backward recovery is always the right choice for financial
transactions — a payment saga that cancels an authorization because a
downstream step failed may be worse than retrying.
