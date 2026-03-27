# /architecture-review Command

## Description
Executes a multi-perspective architectural review on a provided system context. It strings together three distinct architect personas to evaluate the same system blueprint.

## Invocation
`/architecture-review [system-context.md]`

## Agent Persona
This command delegates execution sequentially to the `APOS Reviewer`, `Security Reviewer`, and then explicitly asks the model to act as a `Staff Distributed Systems Architect`.

## Execution Flow
1.  Read the `[system-context.md]` System Brief.
2.  Route first to the `APOS Reviewer` simply to verify the Context Level is at least Level 2. If it is Level 1, reject the request and ask for a detailed configuration and load description.
3.  Execute Pass 1: "Evaluate this architecture for scalability, consistency, and failure modes."
4.  Execute Pass 2 (via `Security Reviewer`): "Evaluate this architecture for threat models and privilege escalation."
5.  Synthesize: "Act as a Principal Architect. Combine these findings into a unified risk register, ordered by severity."
