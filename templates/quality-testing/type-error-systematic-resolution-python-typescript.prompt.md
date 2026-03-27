Act as a Staff Software Engineer resolving type system errors.

Technology context:
[REQUIRED: Language and type checker — Python/mypy or TypeScript/tsc]
[REQUIRED: The type error output in full]
[REQUIRED: The code producing the errors]

Task:
Resolve the type errors systematically, working from root causes outward.

Type errors are frequently cascading — one incorrect type annotation produces
ten downstream errors. Diagnose the root cause before fixing downstream symptoms.

Reason through the error chain:
1. Identify which error is the root cause vs. which are downstream effects.
   Fix the root cause first. State which errors you expect to disappear
   as a result.

2. For each remaining error after root cause resolution:
   - State what the type system is asserting
   - State what the code is doing
   - State whether the type system is correct or the code is correct
     (not every type error means the code is wrong — sometimes the type
     annotation is wrong)

3. Do not use Any or type: ignore to suppress an error unless:
   - The suppression is accompanied by a comment explaining why the
     type system cannot model this correctly
   - The suppression is localized to the specific line causing the issue

Output:
State the root cause error first.
For each fix: show the before and after.
State explicitly whether each fix changes runtime behavior or only
improves type annotation accuracy.
After all fixes: state how many errors should remain and why.
