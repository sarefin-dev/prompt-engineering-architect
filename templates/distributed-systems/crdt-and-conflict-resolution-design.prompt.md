Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: The data that may have concurrent conflicting updates]
[REQUIRED: The merge semantics — what does "correct" mean when conflicts occur?]

Task:
Design a conflict resolution strategy for concurrent updates to the
stated data under eventual consistency.

Evaluate the following approaches:
1. Last-write-wins (LWW) with timestamps — when is it safe?
2. Multi-value register (keep all conflicting versions) — when is it appropriate?
3. Operational transformation — for ordered, text-like data
4. CRDT (Conflict-free Replicated Data Type) — identify which CRDT
   matches the data semantics (G-Counter, PN-Counter, OR-Set, LWW-Map, etc.)
5. Application-level merge — custom merge function for domain-specific semantics

For each approach: assess whether it produces correct results
for the stated merge semantics.

Output:
Recommend the conflict resolution approach with domain-specific justification.
For the recommended approach: describe the merge function precisely
in terms of the data model.
Enumerate the cases where the chosen approach may produce a result
that is technically correct but business-semantically wrong —
these require additional application-level validation.
Do not recommend LWW without explicit assessment of clock skew risk.
