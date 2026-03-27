# /tdd-red Command

## Description
Executes the first phase of the TDD Prompt Cycle. It generates a failing test specification for a described behavior before any implementation code is written.

## Invocation
`/tdd-red [description of behavior to implement]`

## Agent Persona
This command delegates execution to the `Code Quality Reviewer` agent.

## Execution Flow
1.  Read the user's description of the desired behavior.
2.  Route the description to the agent with instructions to generate *only* the test code.
3.  The agent must explicitly define the Happy Path, Boundaries, and Error states in text before outputting the test method.
4.  The agent outputs the test and instructs the user: "Run this test and confirm it fails for the correct reason. Do not proceed to `/tdd-green` until failure is confirmed."
