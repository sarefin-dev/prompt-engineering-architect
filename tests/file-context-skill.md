# File-Based Context — Skill Test

## Input Prompt
The user provides: "Here is my code for `app.py`: `def start(): pass` and here is `tests.py`: `def test_start(): start()`... [150 lines of raw inline code]. Please review it."

*Context injected: `.claude/skills/file-context.md`*

## Expected Agent Behavior (With Skill)
The agent intercepts the unstructured request. Before analyzing the code, it internally re-formats the user's input into:
`<document index="1" path="app.py">...</document>`
`<document index="2" path="tests.py">...</document>`

It then structures its findings with explicit analytical citations (e.g., "In `<document path='app.py'>`, the `start()` function lacks...").

## Conclusion
The skill successfully enforces XML-style boundaries, anchoring the model to the specific file structures even when the user failed to provide them cleanly.
