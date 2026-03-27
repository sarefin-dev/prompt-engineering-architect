# File-Based Context — Baseline Test

## Input Prompt
The user provides: "Here is my code for `app.py`: `def start(): pass` and here is `tests.py`: `def test_start(): start()`... [150 lines of raw inline code]. Please review it."

## Expected Agent Behavior (Without Skill)
The model attempts to read the flat text string but conflates the files, occasionally hallucinating variables from `tests.py` into the scope of `app.py` because the boundary between the two contexts is purely whitespace.

## Conclusion
Unstructured inline context reduces the model's ability to isolate functional boundaries, leading to hallucination across file scopes.
