# APOS Structure Skill — Baseline Test

## Input Prompt
The user asks: "Write me a prompt that makes Claude review our microservice architecture and tell me if it's production-ready."

## Expected Agent Behavior (Without Skill)
The agent produces a single-paragraph prompt that mixes the persona, instructions, and expected output into one undifferentiated block. It uses softening language ("please review", "let me know if") and does not define what "production-ready" means. The output format is left open — the model will produce whatever structure it chooses. The result is a prompt that will generate a different response on every run depending on which elements the model happens to attend to first.

## Conclusion
Without the APOS structure skill, the model treats prompt writing as natural language composition. It produces a readable request but not an engineered specification. The prompt has no primacy anchor, no context depth, no task boundary, and no output contract — four simultaneous failure modes.
