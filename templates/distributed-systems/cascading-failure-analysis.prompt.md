Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Service dependency graph — which services call which]
[REQUIRED: Current circuit breaker and bulkhead configuration, or lack thereof]

Task:
Analyze cascading failure risk in this service topology.
Work through the following:
1. Identify all synchronous call chains — the longer the chain, the higher the risk
2. For each chain: what happens when the deepest dependency fails?
   Trace the failure propagation upstream.
3. Identify missing circuit breakers on critical call chains
4. Assess the thread pool / connection pool exhaustion risk:
   if a downstream service is slow (not down), do upstream services exhaust
   their connection pools waiting?
5. Identify retry amplification: if all callers retry simultaneously,
   what is the load spike on the recovering service?

Output:
For each identified cascading failure path:
- Trigger: which service fails first
- Propagation: which services fail in sequence and why
- User impact: what the user experiences
- Current mitigation: circuit breaker present or not
- Recommended mitigation: specific circuit breaker design or bulkhead pattern

Enumerate the failure chains that can cause a full system outage from a single
service failure — these are the highest-priority mitigations.
Do not conflate a service being slow with a service being down —
slow upstream services are often more dangerous than failed ones.
