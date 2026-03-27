Act as a Staff Performance Engineer and Systems Architect.

System context:
[REQUIRED: Architecture — services, databases, caching, messaging]
[REQUIRED: Current load and resource utilization]

Target scale:
[REQUIRED: Target user count, request rate, or data volume]
[REQUIRED: Timeline — when does the target need to be met?]

Traffic characteristics:
[REQUIRED: Read/write ratio, peak-to-average ratio]
[OPTIONAL: Geographic distribution, seasonality]

Task:
Estimate the infrastructure required to support the target scale.

Work through each tier:

1. API/Service tier:
   - Current RPS per instance
   - Target RPS from scale multiplier
   - Required instance count = target RPS ÷ RPS per instance × headroom factor (1.4)
   - Autoscaling configuration: min, max, scale-out trigger

2. Database tier:
   - Current read and write IOPS
   - Target IOPS from scale multiplier
   - Read scaling: replica count to distribute read load
   - Write scaling: does write IOPS require sharding or a different approach?
   - Storage: current size × growth rate × timeline + 30% buffer

3. Cache tier:
   - Target cache hit rate and its impact on database load
   - Required cache size: working set estimate
   - Cache cluster configuration

4. Message broker:
   - Target message throughput
   - Partition count required for target parallelism
   - Storage required for retention period

Output:
Tabulate infrastructure at each tier: Current | Required at target | Change.
State all assumptions explicitly — the estimate is only as valid as its assumptions.
Identify the tier with the shortest runway before the current configuration saturates.
Provide the cost estimate at target scale (instance type × count × region pricing).
State the architectural change required for any tier where horizontal scaling
alone is insufficient.
Do not provide precise cost estimates without stating the cloud provider,
region, and pricing tier used — costs vary significantly.
