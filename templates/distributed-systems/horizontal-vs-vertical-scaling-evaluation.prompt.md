Act as a Staff Performance Engineer.

System context:
[REQUIRED: Architecture with current resource utilization per component]

Current scaling bottleneck:
[REQUIRED: Which component is limiting throughput and why]

Task:
Evaluate whether horizontal or vertical scaling is appropriate for
each bottleneck component.

For each bottleneck component, assess:
1. Is the bottleneck CPU-bound, memory-bound, I/O-bound, or network-bound?
2. Does the service maintain shared mutable state that prevents horizontal scaling?
3. What is the cost differential between horizontal and vertical scaling at target?
4. What is the operational complexity differential?
5. What is the ceiling of vertical scaling for this component?

Output:
For each bottleneck: state the constraint type, the preferred scaling direction,
and the rationale.
Identify any components where horizontal scaling requires architectural changes
(session affinity, shared state, distributed caching) — enumerate those changes.
Tabulate: Component | Bottleneck type | Scaling direction | Required changes | Cost direction.
Do not recommend horizontal scaling for inherently stateful components
without explicitly designing the state distribution strategy.
