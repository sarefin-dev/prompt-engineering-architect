Act as a Staff Software Engineer writing a failing test specification before
implementation.

Technology context:
[REQUIRED: Language and test framework]
[REQUIRED: The behavior to implement — one sentence description]
[REQUIRED: The method or function signature already agreed — or state "not yet defined"]

Task:
Write a failing test that precisely specifies the behavior to implement.
The test must fail for the right reason — not because of a compilation error
or a missing class, but because the behavior is not yet implemented.

Reason through the specification before writing the test:
1. What is the observable outcome of this behavior?
   State it in terms a product manager could verify — not in terms of
   internal state or implementation.
2. What are the inputs that produce this outcome?
   State the minimum input required — not a full system setup.
3. What does failure look like?
   State the specific assertion that will fail and why it represents
   the absence of the intended behavior.

Write exactly one test — the test that, when it passes, means the behavior
is correctly implemented.
Name it: [unit]_[condition]_[expected outcome].
Add a comment above the test: // RED: this test fails until [behavior] is implemented.
Do not write the implementation — only the test.
Do not write helper tests — only the primary behavior test.
