# Tree of Thought (ToT) Reasoning Skill

## Description
This skill enforces the Tree of Thought (ToT) structural reasoning pattern for complex architectural decisions, preventing premature anchoring to suboptimal solutions.

## Operational Rules

1.  **Mandatory Parallel Generation**: When faced with a complex architectural problem, do not immediately pursue a single solution. Generate exactly three distinct, structurally different hypotheses or solution branches first.
2.  **Branch Independence**: Each branch must represent a genuinely different mechanism or pattern (e.g., synchronous orchestration vs. asynchronous choreography), not just minor variations of the same approach.
3.  **Evaluate and Prune**: Before generating any code or final recommendations, explicitly evaluate all three branches against the provided constraints and evidence. Score or rank them.
4.  **Synthesis**: Adopt the highest-scoring branch for the remainder of the analysis. State the primary trade-off accepted by choosing this path.

## Agent Behavior
*   When executing a task that requires this skill, the agent must output a designated `[ToT: Branch Generation]` section before any conclusions.
*   The agent must output a `[ToT: Pruning]` section explaining why the discarded branches were eliminated.
