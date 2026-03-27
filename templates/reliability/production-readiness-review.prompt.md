Act as a Staff Site Reliability Engineer performing a production readiness review.

System context:
[REQUIRED: Full Level 3 system context from Chapter 7]

Acceptance criteria:
[REQUIRED: The SLOs the system must meet]
[REQUIRED: Any hard requirements — compliance, data residency, security]

Task:
Perform a production readiness review against the acceptance criteria.

Evaluate all five dimensions:

Dimension 1 — Reliability:
- Single points of failure identified and mitigated (or risk accepted)
- Circuit breakers on all external dependencies
- Graceful degradation for non-critical features
- Disaster recovery procedure documented and tested

Dimension 2 — Performance:
- Load testing completed against the stated SLOs
- Performance acceptable at 2x peak load (headroom)
- No known memory leaks or resource exhaustion under sustained load

Dimension 3 — Observability:
- Golden signals instrumented for all services
- Alerts defined for all P1 and P2 failure scenarios
- On-call runbooks exist for all P1 alerts
- Distributed tracing in place for the critical path

Dimension 4 — Operational readiness:
- Deployment procedure tested and documented
- Rollback procedure tested — time-to-rollback measured
- Database migrations complete and verified
- Runbooks exist for the three most likely incidents

Dimension 5 — Security:
- Authentication and authorization in place
- No hardcoded credentials or secrets in code or configuration
- Sensitive data encrypted at rest and in transit
- Penetration test or security review completed (if required)

Output:
For each dimension: evaluate as Ready / Needs work / Blocking.
Enumerate all Blocking items — these must be resolved before launch.
Enumerate all Needs work items — these must be scheduled before
the first month of production operation.
State the launch recommendation: launch / launch with conditions / do not launch.
For "launch with conditions": state the exact conditions that must
be met within the first 30 days.
Do not recommend launch if any Blocking item is unresolved.
