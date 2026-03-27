Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: System description with consistency and availability requirements]

Business requirements:
[REQUIRED: What user-visible behavior is acceptable under network partition?]
[REQUIRED: What data loss or staleness is acceptable?]

Task:
Scrutinize the CAP theorem trade-off for this system.
Work through the following:
1. What does partition tolerance mean specifically for this system?
   (Can writes be refused during partition? Can reads serve stale data?)
2. What is the user-visible behavior under each partition scenario:
   - CP choice: writes refused, reads guaranteed consistent
   - AP choice: writes accepted, reads may return stale or conflicting data
3. For the business requirements stated: which choice is correct?
4. What specific consistency mechanism implements the chosen behavior?
   (Quorum reads/writes, single-leader replication, consensus protocol)
5. What is the behavior of each API endpoint under the chosen partition strategy?

Output:
State the CP vs. AP choice explicitly and the business justification.
For each API endpoint: state the behavior during partition under the chosen strategy.
Enumerate any endpoints where the partition behavior differs from the default —
these require special handling in the client.
Scrutinize the consistency guarantee: strong / linearizable /
eventual / read-your-writes / causal — leave no assumption about implicit
consistency unchallenged before committing to a classification.
Do not provide a vague "it depends" answer — commit to a specific
choice for the stated requirements and justify it.
