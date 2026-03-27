# Pre-Deployment Gate Skill

## Description
This skill enforces a Pre-Deployment Quality Gate to guarantee that no prompt is executed—whether by a human or an automated agent—without meeting strict structural and vocabulary criteria.

## Operational Rules

Before submitting any prompt for execution, or when asked to review a prompt, you MUST evaluate it against the following checklist. If the prompt fails *any* of the mandatory checks, you must reject it and rewrite it.

### Mandatory Structural Checks (The APOS Gate)
1.  **[ ] Role Layer Present**: Does the prompt begin with a specific professional role? (e.g., `Act as a Staff Security Architect`). *If missing, the prompt is invalid.*
2.  **[ ] Context Layer Present**: Is there a system context block that describes the specific architecture and constraints? *If missing, the prompt is invalid.*
3.  **[ ] Focus Layer Present**: Are the analytical boundaries explicitly defined? *If missing, the prompt will wander.*
4.  **[ ] Task Layer Present**: Is the required action defined using Category 3 analytical verbs?
5.  **[ ] Output Layer Present**: Is the output structure explicitly defined?
6.  **[ ] Explicit Negative Constraints**: Does the Output layer contain at least one explicit `Avoid` or `Prohibit` instruction? *If missing, the prompt will produce padding.*

### Mandatory Vocabulary Checks (The Weakness Audit)
Scan the prompt for probability-reducing vocabulary. If any of the following are found, rewrite the prompt:
1.  **[ ] No "If possible" / "Try to"**: Remove optionality. State mandates.
2.  **[ ] No "Usually" / "Generally"**: Remove ambiguity. State explicit conditions.
3.  **[ ] No "Best" / "Appropriate"**: Remove subjective terms. State the exact optimization criteria (e.g., "optimize for lowest latency").
4.  **[ ] No "Make sure to"**: Replace with structural tests or confirmation steps.

### MCP / Tool Use Checks (If Applicable)
If the prompt is intended for an agentic workflow that uses tools (like Claude Code):
1.  **[ ] Protocol Awareness**: Are unresolved placeholders (`[REQUIRED: ...]`) clearly delineated from live context?
2.  **[ ] Reasoning Directives**: Are explicit instructions provided on *how* to evaluate the retrieved data before acting? (e.g., "Verify X against Y before concluding Z").

## Enforcement
Do not execute a prompt that fails the Pre-Deployment Gate. Instead, output the failed checklist items and provide a rewritten, compliant version of the prompt.
