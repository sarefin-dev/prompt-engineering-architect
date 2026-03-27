# ReAct Pattern Skill

## Description
This skill enforces the Reason + Act (ReAct) pattern for autonomous agentic workflows, ensuring all tool calls are preceded by explicit, visible reasoning to prevent compounding errors and loops.

## Operational Rules

1.  **Mandatory Thought Prefix**: No tool call may be issued without an explicit, preceding thought block that explains *why* the tool is being called.
2.  **Reasoning Structure**:
    *   **What do I know?** (Summarize current state)
    *   **What is the most important unknown?** (Identify the gap)
    *   **Which tool resolves this?** (Name the tool and parameters)
3.  **Halt on Loops**: If the agent observes that its reasoning or tool calls are repeating the same parameters without producing new information, it must immediately halt the loop, switch approaches, or trigger the stopping condition.
4.  **Explicit Stopping Conditions**: The agent must maintain specific, measurable criteria for when the task is considered successfully completed or hopelessly exhausted.

## Agent Behavior
*   The agent must structure its turns strictly as:
    `THOUGHT: ...`
    `ACTION: [Tool Call]`
    `OBSERVATION: [Tool Result]`
*   The agent must not batch speculative, dependent tool calls in a single turn.
