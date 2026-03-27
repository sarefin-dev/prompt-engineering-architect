Act as a Staff Distributed Systems Architect.

System context:
[REQUIRED: Level 2 system description]

Observed symptoms:
[REQUIRED: Production problems, performance issues, operational pain]
Examples:
- "Service B fails whenever Service A deploys"
- "Database writes slow to 30s under load every Monday morning"
- "We cannot change Service C without affecting Services D, E, and F"

Task:
Identify the architectural anti-patterns producing the stated symptoms.
For each symptom:
1. Name the anti-pattern (using standard terminology where applicable)
2. Explain the causal relationship between the anti-pattern and the symptom
3. Identify where in the architecture the anti-pattern is instantiated
4. Propose the canonical refactoring to resolve it

Output:
Structure the analysis by symptom.
For each symptom: anti-pattern name, causal explanation, location in
architecture, canonical resolution.
Tabulate: Symptom | Anti-pattern | Location | Resolution approach.
Identify any anti-patterns that contribute to multiple symptoms —
these are the highest-leverage improvements.
Use standard anti-pattern names: distributed monolith, shared database,
chatty services, God service, synchronous chains, missing circuit breaker, etc.
Do not invent anti-pattern names — use established terminology.
