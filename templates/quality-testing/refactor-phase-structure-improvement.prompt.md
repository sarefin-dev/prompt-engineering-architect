Act as a Staff Software Engineer in the refactoring phase of TDD.
All tests are currently passing. The goal is to improve structure
without changing behavior.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The implementation that made the tests pass — paste the code]
[REQUIRED: The complete test suite — paste all tests]

Task:
Identify refactoring opportunities in the implementation. Apply only
behavior-preserving transformations.

Diagnose refactoring candidates in order of structural impact:

1. Duplication: Is any logic repeated? Extract it.
2. Naming: Do names communicate intent? A method named processData
   is not self-documenting. Rename to express what it processes.
3. Single Responsibility: Does each method do one thing?
   A method that both validates and persists violates SRP — extract.
4. Magic values: Are there unexplained literals? Replace with named constants.
5. Complexity: Is any conditional logic complex enough to extract into
   a named method or a strategy?

For each refactoring:
1. State which structural problem it addresses
2. Show the refactored code
3. Confirm the tests still pass — reason through each assertion

Prohibit: changing behavior — if a test would fail, the change is not
a refactoring, it is an implementation change.
Prohibit: adding features or error handling not covered by existing tests —
that requires a new RED phase.
Prohibit: changing test code to make refactored production code pass —
if refactoring breaks a test, revisit the refactoring.
