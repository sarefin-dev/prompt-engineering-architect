Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: What resource requires distributed locking, why, at what frequency]
[REQUIRED: Infrastructure available: Redis, ZooKeeper, database, etcd]

Requirements:
[REQUIRED: Lock duration, acceptable lock acquisition latency,
 behavior on lock holder failure]

Task:
Design a distributed locking mechanism for the stated use case.
Address:
1. Lock acquisition protocol — how is the lock acquired atomically?
2. Lock release protocol — normal release and failure-case release
3. Lock expiration — TTL design to handle lock holder failure
4. Fencing tokens — how are stale lock holders prevented from corrupting state?
5. Retry strategy — how does a waiting client retry acquisition?
6. Clock skew — how does the design handle clock differences across nodes?

Output:
Provide the complete locking protocol with the specified infrastructure.
Include the fencing token design — this is the mechanism that prevents
correctness violations when a lock expires while its holder is still running.
State the minimum and maximum lock TTL and the rationale for each bound.
Enumerate the failure scenarios where the lock may be held longer than
intended and the impact on system correctness.
Do not recommend a distributed lock without a fencing mechanism if
the protected operation is not idempotent.
