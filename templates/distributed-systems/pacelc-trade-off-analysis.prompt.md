Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Database or distributed system being evaluated]
[REQUIRED: Current replication configuration and consistency settings]
[REQUIRED: Read and write latency SLOs]
[REQUIRED: Consistency requirements — what staleness or anomalies are acceptable]

PACELC model:
If Partition (P): choose between Availability (A) and Consistency (C) — same as CAP.
Else (E), during normal operation: choose between Latency (L) and Consistency (C).

The PACELC classification of common systems:
- DynamoDB: PA / EL (favors availability and low latency by default;
  strong consistency available but increases latency)
- Cassandra: PA / EL (tunable; lower consistency levels = lower latency)
- CockroachDB: PC / EC (favors consistency, higher latency than AP systems)
- Google Spanner: PC / EC (TrueTime provides external consistency at higher latency)
- PostgreSQL single-leader: PC / EC (strong consistency, leader becomes bottleneck)
- MongoDB (replica set): PA / EL by default; PC / EC with majority write concern

Task:
Apply PACELC analysis to the stated system.

Part 1 — Partition behavior (P side):
Same analysis as Template 7 — state CP vs. AP choice and business justification.

Part 2 — Normal operation trade-off (EL vs. EC):
1. What consistency level is the system currently configured at?
   (e.g., DynamoDB eventual vs. strongly consistent reads;
    Cassandra ONE vs. QUORUM vs. ALL;
    MongoDB w:1 vs. w:majority)
2. What is the read latency at the current consistency level?
3. What anomalies are possible at the current consistency level?
   (stale reads, non-monotonic reads, read-your-own-write violations)
4. What is the latency cost of increasing consistency by one level?
5. What is the minimum consistency level required by the business requirements?

For each operation type (read / write / read-modify-write):
State the consistency level required and the latency implication.

Output:
State the PACELC classification of the system under its current configuration.
For each operation type: state the required consistency level, the current
configuration, and whether they match.
Enumerate the operations that are configured at a lower consistency level
than required — these are latent data correctness bugs.
Quantify the latency cost of correcting each misconfigured operation.
Do not accept "we use eventual consistency" as a complete answer — state
which specific operations tolerate eventual consistency and which do not.
Do not conflate CAP partition behavior with PACELC normal-operation behavior —
they are different trade-off decisions with different business implications.
