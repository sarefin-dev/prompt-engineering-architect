# /apply-apos Command

## Description
Restructures an unstructured or partially structured prompt into the strict 5-layer APOS format.

## Invocation
`/apply-apos [filename.prompt.md] or [raw text]`

## Agent Persona
This command delegates execution to the `APOS Reviewer` agent.

## Execution Flow
1.  Read the provided file or text.
2.  Route the content to the `apos-reviewer` agent.
3.  The agent will diagnose missing layers, identify required context data, and output a structurally compliant version using Markdown headers.
4.  If a file was provided, ask the user if they want to overwrite the file with the APOS-compliant version.
