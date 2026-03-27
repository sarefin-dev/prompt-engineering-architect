# MCP Placeholder Audit Skill

## Description
This skill enforces protocol-aware prompt design principles. It ensures that prompts destined for execution in MCP-enabled environments (like Claude Code) correctly separate live data retrieval from human intent.

## Operational Rules

When preparing a prompt template for execution, you MUST audit its `[REQUIRED: ...]` context placeholders and classify them into one of three categories:

### Class 1: Live System State
*   **Definition**: Data that exists in a system, changes over time, and can be retrieved via an API or query. (e.g., table schemas, row counts, consumer lag, current configuration values).
*   **Action**: These placeholders MUST NOT be filled manually by the user. If an MCP tool is available to retrieve this data, replace the manual placeholder with an explicit instruction to use the tool.
*   **Example**: Change `[REQUIRED: Paste the current schema for the users table]` to `Use the database MCP to retrieve the schema and index definitions for the users table.`

### Class 2: Design Intent & Business Constraints
*   **Definition**: Knowledge that exists only in human minds or decision records. (e.g., target SLOs, regulatory requirements, reasons *why* a technology was chosen).
*   **Action**: These placeholders MUST remain as questions for the human user. No tool can answer them. 
*   **Example**: `[REQUIRED: State the maximum allowable P99 latency for this service]` remains unchanged.

### Class 3: Architecture Description
*   **Definition**: The topology and structural relationships of the system.
*   **Action**: If a tool exists to read the infrastructure state (e.g., an AWS or Kubernetes MCP), instruct the model to retrieve it. If not, this remains a human-provided placeholder.

## Enforcement
Before a prompt is executed, review the Context block. If you see a Class 1 placeholder (live data) being requested from the human user, and an appropriate MCP tool is active in the environment, you must rewrite the prompt to use the tool instead. Do not ask humans for data that machines can retrieve.
