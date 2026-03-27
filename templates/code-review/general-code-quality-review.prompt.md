Act as a Senior Software Engineer performing a code review.

Technology context:
[REQUIRED: Language and framework — e.g., Java 17 / Spring Boot 3.x]
[REQUIRED: Code purpose — what does this code do?]
[REQUIRED: Review standards — style guide, architectural patterns in use]

Code under review:
[REQUIRED: Paste the code to review]

Review priority:
[REQUIRED: Correctness | Performance | Maintainability | All three, in that order]

Task:
Review the code against the stated priority.
Apply the same standard as a blocking code review comment.

Evaluate in priority order:

1. Correctness (defensive, exception-safe, thread-safe):
   - Logic errors that produce incorrect results
   - Missing null checks, boundary conditions, or error cases — is input validation defensive?
   - Incorrect assumptions about thread safety — is shared state thread-safe?
   - Resource leaks — are all resources exception-safe? connections, streams, file handles
   - Incorrect assumptions about mutability — should these objects be immutable?

2. Performance:
   - Unnecessary object creation in hot paths
   - N+1 query patterns in data access code
   - Missing pagination on potentially large result sets
   - Synchronous calls that could be async

3. Maintainability (maintainable, readable, self-documenting, observable):
   - Methods doing more than one thing (SRP violations)
   - Missing abstraction — business logic in the wrong layer
   - Non-self-documenting names — does intent require a comment to explain?
   - Magic numbers and unexplained constants
   - Complex conditional logic that should be extracted
   - Missing instrumentation on integration points — is this code observable in production?

Output:
Format each comment as:
[BLOCKING | SUGGESTION | NITPICK]: [File:Line if applicable] — [Issue] — [Recommendation]

BLOCKING: Must be fixed before merge — correctness, security, or data integrity risk.
SUGGESTION: Should be fixed — significant quality or performance improvement.
NITPICK: Optional improvement — style, naming, minor refactoring.

Enumerate BLOCKING comments first.
Do not produce more than ten comments total — prioritize ruthlessly.
Do not comment on formatting — assume a linter handles that.
Do not suggest improvements that require rewriting the surrounding architecture.
Justify every BLOCKING comment — state what goes wrong if it is not fixed.
