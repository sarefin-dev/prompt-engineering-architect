Act as a Staff Performance Engineer specializing in high-scale backend systems.

System context:
[REQUIRED: Architecture with performance problem description]
[REQUIRED: Observed symptoms — latency figures, throughput limitations,
  resource utilization metrics]
[REQUIRED: Scale characteristics — current load, growth trend]

Task:
Diagnose the performance bottlenecks in this system.

Work through the bottleneck identification methodology:

1. Trace the critical path: list every synchronous operation from
   the request entry point to the response — each hop, I/O call,
   database query, and external API call.

2. For each hop: estimate the latency contribution at current load
   and at 10x current load.

3. Identify the resource type of each bottleneck:
   - CPU-bound: computation dominates; parallelism helps
   - I/O-bound: disk or network dominates; caching or async helps
   - Memory-bound: GC pressure or buffer pool exhaustion; tuning helps
   - Lock-bound: contention on shared resources; redesign required

4. Identify the first component to saturate at 10x load:
   this is the scaling bottleneck, regardless of current performance.

5. For each identified bottleneck: assess addressability:
   - Configuration (immediate): connection pool size, cache size, thread pool
   - Code optimization (days): algorithm improvement, query optimization
   - Architectural change (weeks): caching layer, async offload, sharding

Output:
Enumerate bottlenecks ordered by impact on the critical path.
For each bottleneck: component, resource type, current contribution to latency,
behavior at 10x load, and addressability classification.
Provide the three highest-impact improvements in order of implementation priority.
State the expected latency improvement for each — do not claim improvements
without a mechanism.
Do not recommend horizontal scaling as a solution for I/O-bound bottlenecks
where the bottleneck is in a shared resource (database, cache) —
horizontal scaling of the application tier does not address shared resource saturation.
