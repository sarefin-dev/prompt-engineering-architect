Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System with dependencies whose failure should not cause full outage]
[REQUIRED: The critical path — what must work for the system to be useful]
[REQUIRED: Non-critical features that can degrade]

Task:
Design a graceful degradation strategy.

For each non-critical dependency:
1. Identify the feature that depends on it
2. Define the degraded behavior: what does the user experience when
   this dependency is unavailable?
3. Define the degradation trigger: how does the system detect that
   degradation is needed? (Circuit open, timeout, health check failure)
4. Define the degradation exit: how does the system restore full functionality
   when the dependency recovers?

For the critical path:
1. What is the minimum set of dependencies that must be available
   for the system to provide core value?
2. What is the user-visible behavior when a critical path dependency fails?

Output:
Enumerate the degradation tiers from full functionality to minimum viable.
For each tier: state the trigger condition, the degraded behavior,
and the user experience impact.
Define the monitoring required to detect when the system is operating
in each degraded tier — degraded operation should not be silent.
Enumerate the features that cannot be degraded gracefully —
their failure causes full unavailability — and assess whether this is acceptable.
State the recovery sequence: in what order are features restored as
dependencies recover?
