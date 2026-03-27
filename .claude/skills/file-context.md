# File-Based Context Skill

## Description
This skill enforces the rules for providing file-based context to the model, ensuring that injected data is structurally demarcated and optimized for the context window (Chapter 7 §7.8).

## Operational Rules

1.  **Mandatory Block Formatting**: Never paste raw code or text inline. All external file context must be strictly enclosed within XML-style `<document>` tags or standard markdown code fences (```) with the filename explicitly declared.
    *   *Example:* `<document index="1" path="src/auth.ts">\n[content]\n</document>`
2.  **Explicit Citation**: When referencing context provided in a document block, you must explicitly cite the filename or document index to maintain the evidentiary chain.
3.  **Context Minimization**: When pulling context via MCP or tools, extract and inject only the relevant functions, classes, or configuration blocks rather than the entire file, to preserve the context budget.
4.  **Files API Awareness**: If operating in an environment that supports a native Files API (e.g., Anthropic's Prompt Caching), structure the context such that static system prompts and large files are grouped at the top of the context window to maximize cache hit rates.

## Agent Behavior
*   When a user pastes raw code without formatting, the agent should internally restructure it into a bounded block before analyzing it.
*   The agent must explicitly reject ambiguous instructions that rely on "the code above" if multiple files are provided without clear demarcation.
