Act as a Senior Java Engineer performing a code review.
Apply Spring Boot 3.x conventions and Java 17+ idioms.

Code under review:
[REQUIRED: Java code]

Task:
Review this Java/Spring Boot code for correctness, idiom adherence, and
production quality.

Evaluate specifically:

Spring Boot patterns:
- Is dependency injection correct? Constructor injection preferred over field injection.
- Are transaction boundaries correct? @Transactional placed at the service layer,
  not the repository layer.
- Are Spring beans correctly scoped? Stateful data should not be stored in
  singleton beans.
- Is exception handling using @ExceptionHandler or @ControllerAdvice at the
  correct level?

Java idioms:
- Are Optional types used correctly? Optional.get() without isPresent() check
  is a NullPointerException waiting to happen.
- Are streams used correctly? Avoid side effects in stream operations.
- Are records used for immutable data transfer objects?
- Is var used appropriately — only where type is obvious from the right side?

Resource management:
- Are all AutoCloseable resources used in try-with-resources blocks?
- Are database connections always returned to the pool?
- Are thread pool executors shut down?

Null safety:
- Are all method parameters that must be non-null annotated with @NonNull?
- Are all API response fields that may be null explicitly typed as Optional
  or annotated with @Nullable?

Output:
Format each comment as:
[BLOCKING | SUGGESTION | NITPICK]: [ClassName.methodName:line] — [Issue] — [Recommendation]

Enumerate blocking issues first.
Provide the corrected code snippet for each BLOCKING comment.
Do not comment on imports, formatting, or JavaDoc unless they indicate
a logical error.
Do not recommend Lombok unless it is already in use in the codebase.
