# Plan-and-Execute Skill

## Description
This skill enforces the Plan-and-Execute pattern, separating task decomposition from execution to improve reliability on long-horizon, multi-step engineering tasks.

## Operational Rules

1.  **Phase 1: Planning**: Before attempting any modification or tool execution for a complex task, the agent must generate a strictly numbered execution plan.
    *   The plan must assign one specific action or tool per step.
    *   The plan must state the success criteria for proceeding to the next step.
2.  **Explicit Hold**: The agent must output the plan and await external/user confirmation or internally commit to the plan before proceeding to execution.
3.  **Phase 2: Execution**: The agent must execute exactly one step at a time.
    *   It must declare `Executing Step [N]: [Description]`.
    *   It must not anticipate, synthesize, or execute subsequent steps in the same turn.
4.  **Adaptation**: If a step fails, the agent must halt execution, explain the failure, and propose an amendment to the execution plan rather than creatively working around the constraint blindly.

## Agent Behavior
*   The agent must maintain the state of the plan explicitly, checking off steps as they are mapped to `OBSERVATION` results.
