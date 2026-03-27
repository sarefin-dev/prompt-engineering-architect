Act as a Senior Software Engineer reducing code complexity.

Code under review:
[REQUIRED: Complex code — deeply nested, long methods, complex conditionals]

Task:
Reduce the complexity of this code while preserving its behavior.

Apply complexity reduction techniques:

1. Guard clauses: replace nested if-else with early returns
   (inverts the structure — happy path at the bottom, edge cases at the top)

2. Extract method: extract complex logic into named methods that
   communicate intent ("isEligibleForDiscount" is clearer than 10 lines of conditions)

3. Replace nested conditionals with a lookup table or strategy pattern:
   complex switch-like structures are often cleaner as maps or polymorphism

4. Decompose complex boolean expressions:
   extract multi-condition boolean expressions into well-named variables
   or methods

5. Replace magic numbers with named constants:
   constants with meaningful names make the intent clear

6. Reduce method parameter count:
   more than 3-4 parameters indicates a parameter object or design problem

For each technique applied: show the before and after code side by side.

Output:
State the cyclomatic complexity reduction from each change, if estimable.
Show the before and after for each refactoring applied.
Verify that the behavior is identical — provide the test cases that
confirm the before and after produce identical results.
State the readability benefit — what becomes easier to understand
after the refactoring?
Do not reduce complexity at the cost of correctness — preserve all
edge cases, even if the original code handled them verbosely.
