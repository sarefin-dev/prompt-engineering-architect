# Context Budget Check Hook

## Trigger Condition
Fires automatically when a user pastes a large block of code, logs, or system context that exceeds 1,500 tokens.

## Description
Enforces Context Compression rules to prevent reasoning degradation caused by over-specification.

## Hook Execution
1.  **Measure**: Calculate the approximate token count of the incoming user prompt or context block.
2.  **Intercept**: If the tokens exceed the defined budget (e.g., >1,500 tokens of raw context), pause execution.
3.  **Audit for Noise**: Evaluate the payload. Is it a raw copy-paste of 10 generic YAML files? Is it a 5,000-line stack trace where only the first 50 lines matter?
4.  **Compress**: Run a silent summarization pass:
    *   Strip generic marketing descriptions.
    *   Truncate log files to the relevant error signature.
    *   Summarize standard boilerplate into concise functional descriptions.
5.  **Proceed**: Execute the core prompt against the *compressed* System Brief rather than the raw, over-specified input.
