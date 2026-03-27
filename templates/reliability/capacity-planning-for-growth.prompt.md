Act as a Staff Performance Engineer.

System context:
[REQUIRED: Current infrastructure configuration and utilization]
[REQUIRED: Current load metrics — RPS, DAU, data volume]
[REQUIRED: Growth projections — 6 months, 12 months, 24 months]

Task:
Perform capacity planning for the stated growth projections.

For each major component (API tier, service tier, database, cache, messaging):

1. Current utilization: what percentage of capacity is currently used?

2. Growth multiplier: at the stated growth rate, what is the load multiplier
   at 6, 12, and 24 months?

3. Capacity ceiling: at what load does the current configuration saturate?
   (state the headroom — time before saturation at current growth rate)

4. Scaling action: what action is required before saturation?
   When should it be triggered? (At 70% utilization, not at 100%)

5. Cost projection: what is the estimated infrastructure cost increase
   at each growth milestone?

Output:
Tabulate: Component | Current utilization | 6-month projection |
12-month projection | Saturation point | Required action | When to act.
Identify the component with the shortest runway before saturation —
this is the highest-priority scaling action.
State the cost projection at each milestone.
Enumerate the architectural changes that cannot be addressed by scaling alone —
components that require redesign before the 24-month target is reachable.
Base all projections on stated assumptions — list each assumption explicitly.
