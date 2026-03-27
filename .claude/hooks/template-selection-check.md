# Template Selection Check Hook

## Trigger Condition
Fires automatically when a user describes a complex architectural or coding problem without specifying a prompt template from the `templates/` directory.

## Description
Prevents the agent from falling back into generic "helpful assistant" mode when a rigorous, methodology-backed template exists for the problem.

## Hook Execution
1.  **Analyze Intent**: Determine if the user's request maps to one of the 9 functional domains (e.g., Database Schema, Security Threat Model, Event-Driven Topology).
2.  **Intercept**: If the user has not invoked a specific `/select-template` or `/architecture-review` command, pause execution.
3.  **Propose Match**: Use the `domain-template-selector` agent to find the 1-2 most relevant APOS templates.
4.  **Enforce Prompt Engineering**: Prompt the user: "I notice you are asking for an architecture review. To produce the highest quality analysis, I recommend we use the `[Template Name]` template. Please provide the following required context variables so we can proceed: `[List of REQUIRED placeholders]`."
