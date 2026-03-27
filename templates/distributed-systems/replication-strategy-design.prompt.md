Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Database technology, deployment topology, current replication config]

Requirements:
[REQUIRED: Availability target (e.g., 99.9%), RPO, RTO]
[REQUIRED: Geographic distribution requirements if any]

Task:
Design a replication strategy that satisfies the stated availability
and recovery objectives.
Address:
1. Replication topology: single-leader, multi-leader, or leaderless
2. Synchronous vs. asynchronous replication: trade-off between durability and latency
3. Replica count and placement (availability zone, region)
4. Failover mechanism: automatic or manual, promotion criteria
5. Replication lag monitoring and alerting thresholds
6. Read scaling: whether read replicas are used and how staleness is bounded

Output:
Recommend the replication topology with explicit RPO/RTO justification.
For the recommended topology: state the maximum replication lag
acceptable before the read replica is considered too stale for reads.
Enumerate the failure scenarios and the recovery procedure for each:
- Primary failure with synchronous replica
- Primary failure with asynchronous replica (data loss window)
- Network partition between primary and replica
- Split-brain scenario if multi-leader is used
Explicitly state the data loss window (RPO) for the worst-case failure
scenario in the recommended design.
