Act as a Senior Software Engineer proposing a refactoring.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The code smells or problems motivating the refactoring]

Code under review:
[REQUIRED: The code to be refactored]

Task:
Propose a refactoring that improves modularity and separation of concerns.

Analyze the current code for:
1. God classes / god methods: classes or methods with too many responsibilities
2. Feature envy: methods that use more data from another class than their own
3. Inappropriate intimacy: classes that know too much about each other's internals
4. Duplicate code: logic repeated across multiple locations
5. Dead code: code that is never executed or variables that are never read
6. Missing abstraction: complex conditional logic that should be a strategy or policy

For each identified code smell:
1. Name the refactoring technique (Extract Method, Extract Class, Move Method,
   Replace Conditional with Polymorphism, Introduce Parameter Object, etc.)
2. Show the refactored code
3. State the benefit — what becomes easier after this refactoring?

Output:
Enumerate the code smells identified, ordered by impact.
For each significant smell: provide the refactored code alongside the original.
State the test coverage required before and after refactoring:
  which tests must pass before the refactoring to be safe,
  and which new tests are needed after.
Identify the refactoring order: some refactorings enable others —
which must be done first?
Do not refactor for its own sake — state the concrete benefit of each change.
Do not introduce design patterns not warranted by the current complexity —
the simplest solution that is correct is the right solution.
