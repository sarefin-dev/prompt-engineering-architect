# TDD Prompt Cycle Skill

## Description
This skill enforces a Test-Driven Development (TDD) multi-prompt workflow. It ensures that code generation is handled as a sequential, verification-driven process rather than a single-shot request.

## Operational Rules

When tasked with writing both tests and implementation code, or when acting as a Staff Software Engineer in a TDD workflow, you MUST separate the work into three distinct, sequential phases. Do not attempt to write the test and the implementation in the same response.

### Phase 1: RED (Failing Test Specification)
*   **Goal**: Specify the behavior explicitly before writing any production code.
*   **Action**: Generate *only* the unit test. 
*   **Constraint**: The test must fail for the right reason (because the behavior is not yet implemented), not due to compilation errors or missing dependencies.
*   **Verification**: Ask the user to run the test and confirm it fails. Do not proceed until failure is confirmed.

### Phase 2: GREEN (Minimum Implementation)
*   **Goal**: Write the absolute minimum code required to make the failing test pass.
*   **Action**: Generate *only* the production code necessary to satisfy the assertion in the RED phase test.
*   **Constraint**: Do not add error handling, logging, optimizations, or generalize the code beyond what is strictly required to pass the specific test. (That is the REFACTOR phase).
*   **Verification**: Ask the user to run the test suite and confirm all tests pass.

### Phase 3: REFACTOR (Structural Improvement)
*   **Goal**: Improve the internal structure of the code without changing its observable behavior.
*   **Action**: Identify duplication, poor naming, or complexity. Provide refactored code.
*   **Constraint**: The refactoring MUST NOT change behavior. If a test would fail because of the change, it is an implementation change, not a refactoring.
*   **Verification**: Ask the user to run the test suite to confirm it is still green.

## Enforcement
If a user requests "write tests and implement feature X", you must refuse the single-shot execution. Explain the TDD Prompt Cycle. Output the RED phase test first, and explicitly wait for confirmation of failure before outputting the GREEN phase implementation.
