# MCP Error Handling — Baseline Test

## Input Prompt
The user asks: "Fetch the latest logs for the payment service."
*(The system simulates an MCP server returning a 500 error or `tool_run_error`.)*

## Expected Agent Behavior (Without Skill)
The agent receives the error, gets confused, and either (a) confidently makes up logs that look like payment service logs to satisfy the user request, or (b) retries the exact same failing tool call in an infinite loop until the context window budget is exhausted.

## Conclusion
Without robust exception rules, the objective-driven nature of the models pushes them toward hallucinating data rather than admitting failure.
