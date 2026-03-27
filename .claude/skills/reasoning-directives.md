# Reasoning Directives Skill

## Description
This skill enforces Category 9 analytical reasoning directives to close degrees of freedom and prevent the model from arriving at premature or contradictory conclusions.

## Operational Rules

When evaluating reasoning chains or constructing complex analytical prompts, you MUST enforce the following structural logic gates:

### 1. Single-Context Directives
These directives control how the model reasons about static context before concluding.
*   **"Reason Through" / "Work Through"**: Require explicit decomposition of logic. (e.g., `Reason through the execution path before concluding.`)
*   **"Identify Before Recommending"**: Demand explicit problem framing before solution generation. (e.g., `Identify the bottleneck before recommending a caching strategy.`)
*   **"Do Not Substitute Assumptions"**: Enforce strict reliance on provided context. (e.g., `Do not substitute assumptions for missing configuration details. Specify what is missing.`)

### 2. Multi-Context / MCP Directives
These directives govern how the model reasons across multiple tool calls or interleaved data retrievals.
*   **"Verify Against Retrieved Data"**: Require reconciliation. (e.g., `Verify your assessment against retrieved statistics before proceeding.`)
*   **"State Confirmations & Denials"**: Make the evidentiary chain explicit. (e.g., `State what each tool call confirmed or denied before issuing the next tool call.`)
*   **"Do Not Proceed with Contradiction"**: Enforce contradiction resolution over silent assumption. (e.g., `If retrieved data contradicts a key assumption in your prior assessment: stop, state the contradiction explicitly, and revise the assessment before proceeding. Do not proceed while holding an unresolved contradiction.`)

## Enforcement
A prompt designed for complex analysis or tool use is defective if it lacks explicit reasoning directives. Inject Category 9 reasoning directives into the Task layer of the APOS structure to control the sequence and quality of the model's analytical process.
