Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Full architecture description at Level 2 or 3]

Task:
Scrutinize this architecture for single points of failure — leave no
component's redundancy assumption unchallenged.

For each component, evaluate:
1. Is there redundancy? If not, this is a SPOF.
2. Is there automatic failover? If not, what is the manual recovery procedure?
3. What is the blast radius when this component fails?
4. What is the expected time to detection (MTTD)?
5. What is the expected time to recovery (MTTR)?

Output:
Enumerate all SPOFs. For each:
- Component name
- Failure mode (what specifically fails)
- Blast radius (scope and user impact)
- Current detection mechanism (or "None")
- Current recovery mechanism (or "Manual")
- Recommended mitigation

Distinguish between SPOFs that are: acceptable (redundancy not justified by cost),
addressable (the engineering team must fix before the production release gate), and critical (must be fixed immediately — block release).
Order by blast radius — widest impact first.
Do not omit infrastructure SPOFs: load balancers, DNS, monitoring systems,
deployment pipelines — these are SPOFs too.
