# /vocab-check Command

## Description
Scans a prompt for probability-reducing language (softeners, generic verbs) and injects Category 1, 3, and 4 high-leverage terminology.

## Invocation
`/vocab-check [filename.prompt.md] or [raw text]`

## Agent Persona
This command delegates execution to the `Vocabulary Auditor` agent.

## Execution Flow
1.  Read the provided file or text.
2.  Route the content to the `vocabulary-auditor` agent, ensuring it has access to the `vocabulary/` directory YAML definitions.
3.  The agent will output a list of detected weaknesses and a revised version of the text.
4.  Present the revised text to the user.
