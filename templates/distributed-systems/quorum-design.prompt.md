Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Replication topology — number of replicas, write path, read path]
[REQUIRED: Consistency requirements — what must be guaranteed]

Task:
Design a quorum strategy for the stated replication topology.
Address:
1. Write quorum (W): how many nodes must acknowledge a write?
2. Read quorum (R): how many nodes must respond to a read?
3. The W + R > N constraint and its implications for this topology
4. What happens when quorum cannot be achieved:
   - Write quorum failure: writes refused or accepted with degraded consistency?
   - Read quorum failure: reads refused or served from available replicas?
5. The behavior under node failure for each quorum configuration
6. The latency implications of the chosen W and R values

Output:
State the recommended W, R, and N values with rationale.
For each quorum configuration evaluated: state the consistency guarantee,
the availability under node failure, and the write/read latency impact.
Enumerate the failure scenarios where the quorum cannot be achieved and
the system behavior in each case.
Explicitly state whether the design provides linearizability or
eventual consistency under the chosen W and R values.
