Act as a Staff Software Engineer writing the minimum code to make a failing
test pass.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The failing test — paste the complete test]
[REQUIRED: The current error message when the test runs]

Task:
Write the minimum production code that makes this specific test pass.

Constraints — enforce these strictly:
Mandate: the implementation must make the stated test pass.
Mandate: the implementation must not make any other currently-passing test fail.
Prohibit: writing code that is not required to make this specific test pass.
Prohibit: adding error handling, logging, or optimization — that is REFACTOR phase.
Prohibit: writing more than one class or function unless the test requires it.

Reason through the minimum before writing:
1. What is the test asserting? State it in one sentence.
2. What is the absolute minimum code structure required to satisfy that assertion?
3. Is there a simpler implementation that also satisfies it?
   If yes, use the simpler one.

Write the implementation.
After the implementation: run through the test in your head and confirm it passes.
State explicitly: "This implementation passes [test name] because [reason]."
State explicitly: "No existing behavior is broken because [reason]."
