# /tdd-refactor Command

## Description
Executes the final phase of the TDD Prompt Cycle. It reviews newly written, test-passing code for structural duplication and naming issues, proposing behavior-preserving improvements.

## Invocation
`/tdd-refactor [source file]`

## Agent Persona
This command delegates execution to the `Code Quality Reviewer` agent.

## Execution Flow
1.  Read the target source file (which must already have passing tests).
2.  Route to the agent to scan for DRY violations (Literal, Structural, Semantic) and SRP violations.
3.  Output refactoring proposals with Before/After code blocks.
4.  Instruct the user: "Apply these changes and rerun the test suite to ensure behavior is preserved."
