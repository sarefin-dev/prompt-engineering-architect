# /audit-prompt Command

## Description
Executes the Pre-Deployment Gate on a specified prompt file. It evaluates structural completeness, vocabulary discipline, and logical flow.

## Invocation
`/audit-prompt [filename.prompt.md]`

## Agent Persona
This command delegates execution to the `Prompt Critiquer` agent.

## Execution Flow
1.  Read the content of `[filename.prompt.md]`.
2.  Route the content to the `prompt-critiquer` agent.
3.  The agent will output a Pass/Fail score, a list of defects, and a rewritten version of the prompt.
4.  If the user confirms, overwrite `[filename.prompt.md]` with the rewritten version.
