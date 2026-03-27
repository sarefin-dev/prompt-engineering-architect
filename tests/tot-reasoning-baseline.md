# ToT Reasoning Skill — Baseline Test

## Input Prompt
The user asks: "We need to scale our database layer to handle 10x traffic. What caching strategy should we use?"

## Expected Agent Behavior (Without Skill)
The agent immediately recommends Redis (the industry standard). It provides a generic implementation guide for a cache-aside pattern without explicitly evaluating other structural options or considering the system's specific constraints regarding consistency vs. availability.

## Conclusion
Without the ToT Reasoning skill, the model acts as a probability engine, defaulting to the most statistically common answer rather than performing rigorous architectural trade-off analysis.
