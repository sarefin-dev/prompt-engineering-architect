Act as a Senior Software Engineer reviewing design pattern usage.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The design pattern claimed to be used, or the pattern the reviewer suspects is needed]

Code under review:
[REQUIRED: Code implementing or needing a design pattern]

Task:
Evaluate whether the design pattern is correctly applied, or whether the
stated pattern is warranted, and propose the correct implementation.

If evaluating an existing pattern implementation:
1. Identify what pattern is being attempted
2. Evaluate whether the implementation is correct
3. Identify deviations from the canonical pattern and their consequences
4. State whether the pattern is warranted for this problem, or whether
   a simpler solution would be more appropriate

If proposing a pattern for untested code:
1. Identify the code smell or problem the pattern would address
2. State which pattern addresses it and why
3. Provide the pattern implementation for this specific code
4. State the trade-offs: what complexity does the pattern introduce?
   Is it justified by the benefit?

Patterns most commonly misapplied in production code:
- Singleton: often applied without considering thread safety or testability impact
- Factory: often applied where simple constructors would be clearer
- Observer: often applied without considering event ordering and memory leak risk
- Strategy: correctly applied produces clean extensibility;
  misapplied produces indirection without benefit

Output:
State whether the pattern is correctly applied or warranted.
If incorrectly applied: show the correct implementation alongside the current one.
If not warranted: show the simpler alternative.
State the specific benefit the pattern provides for this code —
  not the general benefit of the pattern in the abstract.
Do not recommend a design pattern where a function or a simple conditional
would be clearer.
Do not recommend the Gang of Four pattern name without showing the
concrete implementation for the specific code under review.
