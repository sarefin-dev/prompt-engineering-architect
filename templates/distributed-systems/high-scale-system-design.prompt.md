Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: System description — purpose, current architecture, current load]

Target scale:
[REQUIRED: Target throughput, e.g., "1M requests per minute" or "100M DAU"]

Constraints:
[REQUIRED: Latency SLO, consistency requirements, budget or operational constraints]

Task:
Design a distributed architecture capable of sustaining the stated target scale.
Work through the following in order:
1. Decompose the system into independently scalable components
2. For each component, specify the horizontal scaling strategy
3. Identify the stateful components — these constrain horizontal scaling
4. Design the data partitioning strategy for stateful components
5. Specify the load balancing approach at each tier
6. Identify the bottleneck that will limit scaling first and how to address it

Output:
Provide a structured analysis following the six steps.
For each component: specify the scaling approach, the scaling ceiling,
and the trigger to scale (metric and threshold).
Enumerate the three architectural changes required before the target
scale is reachable from the current design.
Tabulate: Component | Scaling approach | Ceiling | Scale trigger.
Explicitly state all consistency trade-offs introduced by the scaling design.
Quantify estimates with stated assumptions — do not invent metrics.
