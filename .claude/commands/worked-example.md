# /worked-example Command

## Description
Deploys a pre-configured multi-step system design workflow (The Payment Service Example). This serves as a tutorial on how to use the methodology in practice.

## Invocation
`/worked-example [payment-service | incident-response]`

## Execution Flow
1.  Verify the requested example exists in the `examples/` directory.
2.  Read the foundational System Brief for that example (e.g., `examples/payment-service/system-context.md`).
3.  Provide the user with a table of contents showing the execution sequence of prompts that demonstrate the APOS framework and progressive refinement in action.
4.  Offer to execute `01-architecture-review.prompt.md` using the provided context.
