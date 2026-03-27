# Local Inference & Hybrid Routing Skill

## Description
This skill enforces the hybrid routing decision logic defined in Chapter 30 (Techniques 6-7), enabling the orchestrator to dynamically route subtasks between heavy, costly cloud models (e.g., Claude 3.5 Sonnet/Opus) and fast, cheap, or private local/smaller models (e.g., Claude 3 Haiku).

## Operational Rules

1.  **Complexity Categorization**: Before assigning a task, categorize its cognitive complexity into three tiers:
    *   *Tier 1 (Routing/Formatting)*: Syntax transformations, renaming, summarization.
    *   *Tier 2 (Standard Analysis)*: Component-level refactoring, test generation, standard operational logic.
    *   *Tier 3 (Architectural/Complex)*: Multi-file orchestration, ambiguous debugging, structural design.
2.  **Cost-Aware Execution**:
    *   Route Tier 1 tasks strictly to the smallest, cheapest model available.
    *   Route Tier 2 tasks to the default standard model.
    *   Route Tier 3 tasks to the frontier/heavy model.
3.  **Privacy/Compliance Checks**: If a task involves PII, proprietary cryptographic keys, or un-anonymized customer data, it must be flagged for local or compliant inference only, regardless of complexity.

## Agent Behavior
*   When decomposing a plan (Plan-and-Execute), the agent must annotate each subtask with the recommended inference tier.
*   The agent must explicitly justify when it chooses to escalate a Tier 2 task to a Tier 3 model.
