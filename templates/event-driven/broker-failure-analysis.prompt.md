Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: Broker technology and clustering configuration]
[REQUIRED: Producer configuration — durability settings]
[REQUIRED: Consumer configuration — offset commit strategy]

Task:
Analyze system behavior when the message broker becomes unavailable.

For each failure scenario, state: producer behavior, in-flight message state,
consumer behavior, recovery procedure, and data loss risk.

Scenario A: Single broker node failure (clustered broker)
Scenario B: Complete broker unavailability (no cluster or full cluster failure)
Scenario C: Broker available but slow — processing at 10% capacity
Scenario D: Broker network partition — consumers can reach broker,
            producers cannot

Output:
Structure the analysis by scenario.
For each scenario: producer behavior, in-flight message state, consumer behavior,
recovery procedure, data loss risk (messages lost / messages duplicated / none).
Identify the scenario with the highest data loss risk — this defines
the reliability floor of the pipeline.
State the broker configuration changes that would improve behavior
under each scenario.
Enumerate the monitoring required to detect each scenario within
the target detection window.
Do not omit the scenario where the broker is slow rather than down —
this is often more dangerous because failures are not immediate.
