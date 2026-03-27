[ROLE]
Act as a Staff Distributed Systems Architect.

[CONTEXT]
System context:
[REQUIRED: System name and business purpose]

Architecture:
[REQUIRED: Component topology — services, databases, messaging]

Data flow:
[REQUIRED: Step-by-step description of the critical path]

Load characteristics:
- Normal throughput: [REQUIRED]
- Peak throughput: [REQUIRED]
- Data volume: [OPTIONAL]

Infrastructure:
[REQUIRED: Deployment platform, messaging, databases]
[OPTIONAL: Configuration specifics, known gaps, operational state]

Known pain points:
[OPTIONAL — include for maximum specificity]

[FOCUS]
Focus areas:
- Architecture structure: service boundaries, coupling, and cohesion
- Scalability: horizontal scaling limits and bottleneck identification
- Reliability: single points of failure and fault tolerance mechanisms
- Data consistency: consistency model and transaction guarantees
- Observability: monitoring, alerting, and incident debugging capability
- Operational readiness: deployment strategy and production maturity

[TASK]
Task:
Rigorously evaluate this architecture across all six focus areas.
Diagnose the most critical risks in each dimension.
Explicitly identify where design decisions introduce trade-offs.
Assess overall production readiness.
Synthesize findings into a prioritized improvement plan.

[OUTPUT]
Output:
Provide a structured analysis with one section per focus area.
Within each section: findings, root cause, and specific recommendation.
Follow with a risk register: tabulate all identified risks with
name, severity (P1/P2/P3), blast radius, and recommended action.
Conclude with the three non-negotiable changes before production deployment.
Avoid generic explanations — all findings must reference specific components.
Explicitly state the trade-off introduced by each recommendation.
Quantify severity in terms of latency, availability, or data impact where possible.
Do not define referenced patterns.
Do not restate the system context.
