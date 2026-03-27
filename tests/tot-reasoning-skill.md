# ToT Reasoning Skill — Skill Test

## Input Prompt
The user asks: "We need to scale our database layer to handle 10x traffic. What caching strategy should we use?"

*Context injected: `.claude/skills/tot-reasoning.md`*

## Expected Agent Behavior (With Skill)
The agent intercepts the request and refuses to provide a single answer. It explicitly states it is generating three distinct branches:
1.  **Branch 1 (Cache-Aside Redis)**: High probability, standard implementation.
2.  **Branch 2 (Read-Through/Write-Behind)**: Stronger consistency mechanism.
3.  **Branch 3 (Materialized Views/No Cache)**: Database-native optimization avoiding distributed cache complexity.

The agent explicitly scores these three approaches against the operational overhead and consistency requirements, safely pruning the weaker branches before stating a final recommendation.

## Conclusion
The skill successfully interrupts the model's instinct to produce an immediate optimal answer, forcing divergent thinking.
