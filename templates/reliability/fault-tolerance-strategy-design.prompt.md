Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Architecture description — services, databases, messaging]
[REQUIRED: Current fault tolerance mechanisms, if any]
[REQUIRED: Availability target — e.g., 99.9% (8.76 hours downtime/year)]

Task:
Design a fault tolerance strategy that achieves the stated availability target.

Work through the fault tolerance dimensions:

1. Redundancy: which components require redundant instances?
   Calculate: at what failure rate does a single instance violate the SLO?

2. Failover: for each redundant component, what is the failover mechanism?
   - Active-active: both instances serve traffic; automatic on failure
   - Active-passive: standby promoted on failure; what is promotion latency?

3. Health checking: how does the load balancer detect that an instance has failed?
   - Liveness probe: is the process alive?
   - Readiness probe: is the process ready to serve traffic?
   Distinguish the two — a liveness failure should restart; a readiness failure
   should stop traffic without restart.

4. Graceful degradation: when a dependency is unavailable, what is the
   degraded-but-functional behavior? (cached response, default, partial result)

5. Bulkhead isolation: which components must be isolated to prevent
   one failure from cascading to others?

Output:
For each component: state the current fault tolerance posture and
the recommended improvement to meet the availability target.
Calculate the required component availability to achieve the system SLO:
   if three components are in series, each must achieve the cube root of the system SLO.
Enumerate the failure scenarios that the recommended design handles and
those it does not — every design has limits.
State the detection latency for each failure type — how long before
the system routes around the failure?
Do not recommend redundancy for components where the MTBF makes
single-instance operation acceptable within the SLO.
