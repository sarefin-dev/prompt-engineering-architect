Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Pipeline with known burst traffic pattern]
[REQUIRED: Normal throughput, burst throughput, burst duration]

Task:
Design a burst traffic handling strategy.

Address:
1. Buffer sizing: how large must the broker queue be to absorb the burst
   without data loss? (burst rate × burst duration − consumer drain rate × burst duration)
2. Consumer scale-out during burst: can consumers scale out fast enough
   to drain the queue before the buffer fills?
3. Message TTL: should messages expire if they wait too long in the queue?
   What is the acceptable maximum age for this pipeline?
4. Priority queuing: if some messages are more urgent, how are they prioritized?
5. Burst detection and alerting: at what lag threshold is an alert required
   so that operators can intervene before data loss?

Output:
Provide the burst handling design with buffer sizing calculations.
State the maximum sustainable burst at the current configuration:
the burst throughput and duration the system can absorb without dropping messages.
Enumerate the responses in order: automatic (consumer scale-out),
semi-automatic (operator-assisted scale), manual (load shed).
State the message TTL recommendation and the business impact of expired messages.
