# /review-tool Command

## Description
Audits an MCP tool description (or custom Claude tool schema) against protocol-aware instruction principles.

## Invocation
`/review-tool [json/yaml schema file]`

## Agent Persona
This command delegates execution to the `MCP Tool Reviewer` agent.

## Execution Flow
1.  Read the target schema file.
2.  Route the JSON/YAML to the `mcp-tool-reviewer` agent.
3.  The agent will evaluate if the tool description functions as a behavioral prompt (positive and negative usage constraints, strict typing).
4.  Display the identified usage gaps.
5.  If confirmed by the user, overwrite the tool schema file with the rewritten, constraint-heavy version.
