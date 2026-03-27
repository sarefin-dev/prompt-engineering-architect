# ReAct Pattern — Skill Test

## Input Prompt
The user asks: "Figure out why the `auth.ts` file isn't authorizing the JWT."

*Context injected: `.claude/skills/react-pattern.md`*

## Expected Agent Behavior (With Skill)
The agent prefixes every action it takes with explicit syntax:
`THOUGHT: I need to see how the JWT is being validated. I will read auth.ts.`
`ACTION: call read_file(auth.ts)`
`OBSERVATION: [file loaded]`
`THOUGHT: The file relies on an environment variable process.env.JWT_SECRET. I need to check if this is defined in the local .env file.`
`ACTION: call local_bash('cat .env')`

## Conclusion
The skill forces the agent into an auditable, step-by-step reasoning cycle. The agent's decision-making is surfaced before the tools execute, stopping hallucination loops.
