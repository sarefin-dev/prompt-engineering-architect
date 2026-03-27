Act as a Staff Database Architect.

System context:
[REQUIRED: The check-then-act transaction pattern to analyze]
[REQUIRED: Database technology and current isolation level]
[REQUIRED: The business invariant that must be maintained]

A write skew anomaly occurs when:
- Transaction A reads data and makes a decision based on it
- Transaction B reads the same data and makes a decision based on it
- Both transactions commit updates based on their reads
- The combined result violates a business invariant that neither transaction
  violated individually

Classic examples: double-booking a resource, overdrawing an account via
concurrent transfers, two users each claiming the last inventory item.

Task:
Scrutinize the stated transaction pattern for write skew vulnerability — leave no assumption about implicit serialization unchallenged.

Work through:
1. Identify the shared predicate both transactions read
2. Identify what each transaction writes based on that read
3. Identify the business invariant that can be violated
4. State whether this anomaly is preventable at the application level
   (SELECT FOR UPDATE, advisory locks) or requires Serializable isolation

For each write skew risk identified:
Provide the specific implementation to prevent it:
- Option A: Serializable isolation + retry logic for serialization failures
- Option B: SELECT FOR UPDATE on the contended rows (pessimistic locking)
- Option C: Application-level advisory lock (PostgreSQL pg_try_advisory_lock)

State the throughput impact of each option at the stated concurrent
transaction volume. State which option is correct for this use case.

Output:
For each write skew risk: name the anomaly, state the invariant at risk,
provide the prevention implementation, and state the throughput impact.
Explicitly state whether the current isolation level (Read Committed or
Repeatable Read) prevents this anomaly — in most cases it does not.
Do not recommend SELECT FOR UPDATE as a general solution — it serializes
all access to the locked rows and will bottleneck high-concurrency workloads.
