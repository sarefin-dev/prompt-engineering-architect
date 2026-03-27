# ReAct Pattern — Baseline Test

## Input Prompt
The user asks: "Figure out why the `auth.ts` file isn't authorizing the JWT."

## Expected Agent Behavior (Without Skill)
The agent immediately issues a `read_file` tool call for `auth.ts`, followed by another tool call for `jwt.ts`, optionally printing a block of code, before concluding the JWT secret is missing without ever explaining its investigative strategy or identifying what it learned from each call. The user is blind to its reasoning until the final output.

## Conclusion
The agent operates as a black box, making it impossible to audit its logic or detect compounding errors during execution.
