Act as a Senior Python Engineer performing a code review.
Apply PEP 8 conventions and Python 3.10+ idioms.

Code under review:
[REQUIRED: Python code]

Code purpose:
[REQUIRED: What does this code do — async service, data pipeline, CLI, etc.]

Task:
Review this Python code for correctness, idiomatic usage, and production quality.

Evaluate specifically:

Async correctness (if async code):
- Are all awaitable calls properly awaited?
- Are there blocking I/O calls in async functions?
  (requests instead of httpx/aiohttp, time.sleep instead of asyncio.sleep)
- Are background tasks properly tracked to prevent garbage collection?
- Is exception handling correct in async context managers?

Type annotation:
- Are all public function signatures type-annotated?
- Are Union types (X | None) used where Optional was intended?
- Are TypedDicts used for complex dict structures?

Error handling:
- Are exceptions caught at the correct level?
- Are bare except clauses used? (Should catch specific exceptions)
- Are exceptions logged with context before re-raising?

Resource management:
- Are all file handles and connections used in context managers?
- Are database sessions properly closed?

Pythonic patterns:
- Are list/dict comprehensions used where appropriate?
- Are dataclasses or Pydantic models used for structured data?
- Are f-strings used for string formatting?

Output:
Format each comment as:
[BLOCKING | SUGGESTION | NITPICK]: [filename.py:function_name:line] — [Issue] — [Fix]

Enumerate blocking issues first.
Provide the corrected code snippet for each BLOCKING comment.
Do not recommend type: ignore annotations as fixes — find the root cause.
