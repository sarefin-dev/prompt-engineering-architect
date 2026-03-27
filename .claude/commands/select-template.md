# /select-template Command

## Description
Searches the `templates/` directory (containing 200+ domain-specific APOS templates) and recommends the single best template for the user's stated goal.

## Invocation
`/select-template [description of engineering task]`

## Agent Persona
This command delegates execution to the `Domain Template Selector` agent.

## Execution Flow
1.  Route the user's description to the `domain-template-selector` agent.
2.  The agent will pattern-match against the template library categorizations.
3.  Display the recommended template filepath, the justification, and the required inputs (the `[REQUIRED: ...]` placeholders from that template).
4.  Optionally, offer to read that template into context for immediate use.
