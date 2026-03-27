Act as a Staff Software Engineer designing integration tests for a service boundary.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The service and the specific boundary under test:
           database layer | HTTP API | message consumer | external API client]
[REQUIRED: The test infrastructure available:
           real database? testcontainer? in-memory substitute? WireMock?]

Integration boundary:
[REQUIRED: Describe what crosses the boundary — data in, data out, state changes]
[REQUIRED: What isolation is available? Can this test run independently
           of other integration tests? Does it need setup/teardown?]

Task:
Design the integration test suite for this specific boundary.

Reason through the test surface before specifying tests:

1. Happy path with real infrastructure:
   The integration test must exercise the actual I/O — not the business logic
   (that is the unit test's responsibility).
   What is the minimal happy-path test that proves the integration works?

2. Infrastructure failure behavior:
   What happens when the real infrastructure returns an error?
   Test the failure path explicitly — not by unit-testing the error handler,
   but by making the integration actually fail.
   For databases: test connection timeout, constraint violation, deadlock retry.
   For HTTP: test 4xx, 5xx, connection timeout, response parsing failure.
   For message brokers: test poison message handling, offset commit failure.

3. Data contract verification:
   Does the data the service writes match what the consumer expects to read?
   State the contract explicitly before writing the test.
   Any change to serialization, field naming, or data type is a contract change —
   test it at the integration level, not only at the unit level.

4. Idempotency at the boundary:
   If the operation is supposed to be idempotent, prove it.
   Call the same operation twice with the same input.
   Assert the second call produces the same result and does not create
   duplicate side effects.

Output:
Enumerate the integration tests, grouped by test category.
For each test:
  Name: [boundary]_[condition]_[expected outcome]
  Category: [Happy path | Infrastructure failure | Contract | Idempotency]
  Infrastructure required: [what must be running for this test to execute]
  Setup: [what state must exist before the test runs]
  Assertion: [the specific observable outcome that proves the behavior is correct]
  Teardown: [what state must be cleaned up after the test]

Do not write tests that test the business logic — that is the unit test suite.
Integration tests test that the integration works, not that the logic is correct.
State explicitly which behaviors are the unit test's responsibility
and which are the integration test's responsibility.
Prohibit: integration tests that share state with other tests —
  each integration test must be independently runnable.
