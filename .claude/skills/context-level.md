# Context Level Skill

## Description
This skill enforces context delivery rules, ensuring that prompts anchor the model to a defined system reality rather than statistical averages.

## Operational Rules

When writing or reviewing an APOS prompt, evaluate the depth of the Context layer based on the complexity of the Task. Apply the appropriate Context Level block:

### Level 1 — Minimal Context (30-80 Tokens)
*   **Use Case**: Quick factual questions, single-concern technical questions.
*   **Content Required**: Technology stack, primary components, communication pattern (sync vs async), database type.
*   **Constraint**: Limit descriptions. Avoid failure modes or operational states.

### Level 2 — Architectural Context (100-250 Tokens)
*   **Use Case**: Design review, component interaction analysis, technology selection.
*   **Content Required**: Complete Service list with responsibilities, full data flow map (`Client -> Gateway -> Service -> DB`), communication patterns per boundary, specific infrastructure deployment.
*   **Constraint**: Include what is *absent* (e.g., "No dead-letter queue").

### Level 3 — Deep System Brief (250-600 Tokens)
*   **Use Case**: Architecture review, post-mortem, scaling and capacity limits analysis, pre-launch checklist.
*   **Content Required**: Everything in Level 2 PLUS load characteristics (normal vs. peak throughput), specific operational state (e.g., "No consumer lag monitoring"), and explicitly stated *known pain points*.
*   **Constraint**: Replace all generic capacity terms ("high scale") with specific numbers ("10,000 requests/sec").

## Enforcement
Never accept a prompt for a complex task (like an architecture review or debugging an incident) with only Level 1 context. Demand Level 2 or Level 3 context. Identify generic context terms ("uses a message queue") and mandate specific replacements ("RabbitMQ single node, fanout exchange, no clustering").
