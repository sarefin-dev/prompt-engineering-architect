# Tool Description Quality Skill

## Description
This skill enforces the rules for writing tool (function) descriptions for agentic workflows. It ensures that tool schemas function as effective prompts for the model's tool-selection reasoning.

## Operational Rules

When reviewing, generating, or registering tool schemas (such as MCP resources or custom Claude tools), you MUST evaluate the tool description against the following criteria:

### 1. The Description is a Prompt
*   **Rule**: Do not write tool descriptions like API documentation. Write them as instructions to the model on *when* and *why* to use the tool.
*   **Action**: Replace "Returns user profile data" with "Use this tool to retrieve a user's permissions when evaluating an authorization request."

### 2. Explicit Negative Constraints
*   **Rule**: The model will overuse tools if it is not explicitly told when *not* to use them.
*   **Action**: Every tool description must include a "Do NOT use this tool when..." clause.
*   **Example**: "Do NOT use this tool to retrieve historical logs. Use `get_historical_logs` instead."

### 3. State Requirements for Invocation
*   **Rule**: If a tool requires information that the model must gather first, the description must state that prerequisite strictly.
*   **Action**: Inject Category 4 (Constraint) vocabulary.
*   **Example**: "You MUST retrieve the `environment_id` before calling this tool."

### 4. Schema Precision over Overloading
*   **Rule**: Tool parameters must be typed explicitly. Avoid `string` when an enum or specific format is required.
*   **Action**: Enforce strict enums or provide regex patterns for string formats (e.g., ISO-8601 dates). Do not use a generic `query` parameter if the tool expects a structured SQL query.

## Enforcement
A tool schema without explicit positive ("Use this to...") and negative ("Do NOT use this when...") usage conditions is defective. Review and rewrite tool descriptions to function as behavioral constraints.
