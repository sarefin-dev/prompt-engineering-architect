Act as a Senior Software Engineer improving code testability.

Technology context:
[REQUIRED: Language, framework, and current test coverage state]

Code under review:
[REQUIRED: The code that is hard to test]

Task:
Refactor this code to make it unit-testable.

Analyze the testability barriers:
1. Hidden dependencies: direct instantiation of dependencies inside methods
   (new DatabaseConnection(), new HttpClient()) — should be injected
2. Static method calls: static utility methods that cannot be mocked
3. Side effects mixed with logic: code that both computes a value
   and performs I/O cannot be tested without I/O
4. Time and randomness: direct calls to System.currentTimeMillis() or
   Math.random() — should be abstracted behind a Clock or Random interface
5. Global state: static fields that retain state between tests
6. Overly broad public API: methods that expose implementation details
   that tests become coupled to

For each barrier:
1. State the specific testability problem
2. Show the refactored code that removes the barrier
3. Show the unit test that the refactored code enables

Output:
Enumerate the testability barriers in the current code.
For each barrier: provide the refactored code and the unit test it enables.
State the test coverage achievable after refactoring:
  which scenarios can now be tested that could not be before?
Ensure the refactored code maintains the same external behavior —
  this is a behavior-preserving refactoring only.
Do not recommend dependency injection frameworks if the code does not
already use one — use constructor injection directly.
