# /tdd-green Command

## Description
Executes the second phase of the TDD Prompt Cycle. It generates the minimum necessary production code to make a previously written failing test pass.

## Invocation
`/tdd-green [test file or specific failing test output]`

## Agent Persona
This command delegates execution to the `Code Quality Reviewer` agent.

## Execution Flow
1.  Read the failing test definition and the compilation/assertion error.
2.  Route to the agent with strict constraints: Write *only* what is necessary to pass the test. No logging, no defensive checks (unless tested), no abstractions.
3.  Output the minimal implementation code.
4.  Instruct the user: "Run the test suite. If it is green, you may proceed to `/tdd-refactor`."
