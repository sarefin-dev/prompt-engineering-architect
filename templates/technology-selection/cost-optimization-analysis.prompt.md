Act as a Staff Performance Engineer and Cloud Architect.

System context:
[REQUIRED: Current infrastructure configuration and monthly cost]
[REQUIRED: Utilization data — CPU, memory, storage, network per component]
[REQUIRED: Traffic patterns — peak, average, and trough utilization]

Task:
Identify infrastructure cost optimization opportunities.

Analyze each cost category:

1. Right-sizing:
   Which instances are consistently underutilized?
   (< 20% CPU utilization on average is a right-sizing opportunity)
   What is the cost saving from downsizing to the next instance tier?

2. Reserved vs. on-demand pricing:
   Which instances run at > 80% utilization continuously?
   These are candidates for reserved instance pricing (40–60% discount).
   Which instances have variable load? On-demand or spot instances appropriate.

3. Storage optimization:
   Is data tiered by access frequency?
   Old data in hot storage that belongs in cold storage.
   Uncompressed data that could be compressed without impact.

4. Idle resources:
   Development and staging environments running 24/7 when used only during
   business hours — schedule them to stop overnight and on weekends.

5. Data transfer costs:
   Egress costs between regions or availability zones.
   Can frequently-transferred data be cached at the destination?

6. Managed service vs. self-managed:
   Are there self-managed databases or middleware that could be replaced
   by managed services at lower total cost (including operational overhead)?

Output:
Tabulate optimization opportunities: Category | Current cost | Optimized cost | Saving | Risk.
Prioritize by saving potential — highest first.
State the implementation risk for each optimization:
  right-sizing is low risk; architecture changes are higher risk.
Estimate the total monthly saving from all recommended changes.
State the one-time implementation cost for each change.
Do not recommend optimizations that reduce reliability below the stated SLO.
