Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Network topology — nodes, regions, availability zones]
[REQUIRED: Current partition tolerance behavior — CP or AP design]

Task:
Analyze system behavior under the following partition scenarios.
For each scenario, state what each component does and what the user experiences:

Scenario 1: Partition between availability zones within one region
Scenario 2: Partition between regions (if multi-region)
Scenario 3: Partition isolating a single node from the rest of the cluster
Scenario 4: Partition causing a split-brain (two subsets each believe they are primary)

For each scenario:
1. Which components can still serve requests?
2. Which components refuse requests (consistent behavior)?
3. Which components serve potentially stale data (available behavior)?
4. What data loss or corruption risk exists?
5. How long can the system operate in this degraded state?
6. What is the recovery procedure when the partition heals?

Output:
Structure the analysis by scenario.
For each scenario: provide the per-component behavior, user impact,
data risk, and recovery procedure.
Identify scenarios where the stated CP/AP design is violated
by the actual implementation — these are correctness bugs.
Enumerate the monitoring required to detect each partition scenario
within the target detection window.
