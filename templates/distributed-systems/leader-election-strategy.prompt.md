Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: The component requiring leader election — what the leader does,
 how many nodes, failure characteristics]

Requirements:
[REQUIRED: Acceptable leader election time, split-brain tolerance,
 network partition behavior expected]

Task:
Design a leader election strategy for the stated component.
Evaluate the following approaches against the requirements:
1. External coordination service (ZooKeeper, etcd, Consul)
2. Raft-based consensus within the service itself
3. Database-backed leader lease with heartbeat
4. Kubernetes leader election (if running on Kubernetes)

For each approach: assess correctness under network partition, operational
complexity, leader election latency, and failure recovery time.

Output:
Recommend one approach with explicit trade-off justification.
For the recommended approach: specify the lease duration, the heartbeat
interval, the failure detection threshold, and the split-brain prevention mechanism.
Explicitly state what happens to in-flight operations when a leader fails —
how are they recovered or retried by the new leader?
Enumerate the fencing strategy — how are stale leader writes prevented?
Do not recommend an approach that allows two nodes to simultaneously
believe they are leader without a fencing mechanism.
