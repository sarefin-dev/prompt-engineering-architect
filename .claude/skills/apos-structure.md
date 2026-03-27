# APOS Structure Skill

## Description
This skill enforces the canonical APOS (Role, Context, Focus, Task, Output) prompt architecture.

## Operational Rules

When constructing, reviewing, or revising prompts, you MUST enforce the following 5-layer architecture in this exact order:

1.  **Role Layer**: The first sentence. Sets expertise level, domain, and reasoning archetype.
    *   *Format*: `Act as a [Seniority] [Domain] [Role Type].`
    *   *Example*: `Act as a Staff Distributed Systems Architect.`
    *   *Rule*: Never use generic roles (e.g., "helpful assistant"). Always use a specific, technical persona.

2.  **Context Layer**: The system brief. Anchors the model to a specific architecture rather than a statistical average.
    *   *Format*: Clearly delineated section labeled "System context:" or "Architecture:".
    *   *Content*: Must include technology stack, components, communication styles, data flow, and load characteristics.
    *   *Rule*: Demand specific numbers (e.g., "10,000 requests/sec") over generic adjectives (e.g., "high-traffic"). Identify what is *absent* (e.g., "No dead-letter queue configured").

3.  **Focus Layer**: The analytical boundaries.
    *   *Format*: Explicit sentences defining what to analyze and what to ignore.
    *   *Example*: `Focus exclusively on data consistency and partition tolerance. Ignore frontend rendering concerns.`
    *   *Rule*: Always include at least one negative constraint (what to ignore).

4.  **Task Layer**: The specific operation to perform.
    *   *Format*: Action verbs defining the goal.
    *   *Rule*: Use Category 3 (Analytical) and Category 9 (Reasoning) vocabulary. 

5.  **Output Layer**: The format and constraints of the response.
    *   *Format*: Explicit structural instructions.
    *   *Example*: `Enumerate findings by severity. Support each with a code snippet. Do not include introductory text.`
    *   *Rule*: Must define the exact structure (list, table, code block) and include negative behavioral constraints ("Do not summarize...").

## Enforcement
If a prompt lacks any of these 5 layers, it is invalid. You must instruct the user to provide the missing information or rewrite the prompt to explicitly include headings for each missing layer.
