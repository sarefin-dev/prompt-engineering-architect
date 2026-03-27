Act as a Staff Software Engineer practising test-driven development.

Technology context:
[REQUIRED: Language and test framework — e.g., Java 17 / JUnit 5 + Mockito,
           Python 3.12 / pytest, TypeScript / Jest]
[REQUIRED: The function, method, or class under test — paste the full code]
[REQUIRED: The domain context — what business operation does this code perform?]

Known dependencies:
[REQUIRED: List all collaborators this code calls — which should be stubbed vs real?]

Task:
Generate a complete unit test suite for the code provided.

Reason through the behavior space before writing any test:

1. Happy path: What is the normal input that produces the expected output?
   State it explicitly before writing the test.

2. Boundary conditions: What are the edges of the valid input space?
   For numeric inputs: zero, negative, maximum value, overflow.
   For string inputs: empty, whitespace-only, maximum length, unicode.
   For collections: empty, single element, maximum size.
   For dates/times: epoch, far future, timezone boundaries.
   Enumerate every boundary before writing boundary tests.

3. Error paths: What inputs should produce exceptions or error states?
   State the expected exception type and message for each.
   Distinguish between validation errors (bad input) and system errors
   (infrastructure failure) — they require different test approaches.

4. Concurrency paths (if the code uses shared state or async operations):
   What happens under concurrent access?
   Is idempotency guaranteed? Test it explicitly.

5. Contract verification: What invariants must hold regardless of input?
   State the invariant before writing the test that verifies it.

Output:
Write one test method per behavior — not one test method per code path.
Name each test: [unit]_[condition]_[expected outcome].
  Example: processPayment_withExpiredCard_throwsPaymentDeclinedException
Each test must:
  - Set up only what is required for the specific behavior
  - Assert exactly one behavioral outcome
  - Use descriptive assertion messages — state what failed and why it matters
Enumerate the test cases in a table before writing the code:
  | Behavior | Input condition | Expected outcome | Test name |
After the table, write the complete test class.
Do not write tests that assert implementation details — assert observable behavior.
Do not write tests that require the production infrastructure to run —
  stub all external dependencies.
Mark any behavior that cannot be tested without integration infrastructure as
  [INTEGRATION TEST REQUIRED: reason].
