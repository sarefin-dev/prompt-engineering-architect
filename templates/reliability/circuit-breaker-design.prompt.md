Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: The service with the circuit breaker requirement]
[REQUIRED: The dependency being protected — name, criticality, typical latency]
[REQUIRED: Failure behavior — what happens when the dependency is slow or unavailable]

Task:
Design a circuit breaker for the stated dependency.

Define the circuit breaker parameters:

1. Failure threshold: what percentage of calls failing over what window
   should open the circuit? (e.g., 50% failure rate over a 10-second window)

2. Minimum request volume: how many requests must occur in the window
   before the threshold is evaluated? (Prevents opening on low traffic)

3. Wait duration in open state: how long should the circuit stay open
   before testing recovery? (Too short: re-opens immediately. Too long: delays recovery.)

4. Half-open probe strategy: how many requests are tested in half-open state?
   What success rate closes the circuit?

5. Fallback behavior: what does the caller do when the circuit is open?
   (Return cached data, return a default, fail fast with a specific error code)

6. Slow call threshold: should slow calls (not just failures) contribute
   to opening the circuit? At what latency threshold?

Output:
Provide the complete circuit breaker configuration with all six parameters.
Justify each threshold with reference to the dependency's normal behavior.
State the fallback behavior and its impact on user experience.
Enumerate the scenarios the circuit breaker does NOT protect against
(e.g., database corruption, not just availability).
Define the monitoring required: circuit state transitions must be logged
and alerted — an open circuit that goes unnoticed is a silent outage.
State the blast radius if the circuit opens and the fallback is insufficient.
