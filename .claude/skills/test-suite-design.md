# Test Suite Design Skill

## Description
This skill enforces rules for generating test suites that verify behavior and boundaries, rather than simply maximizing line coverage. 

## Operational Rules

When tasked with generating or reviewing unit or integration tests, you MUST enforce the following constraints:

### 1. Reason Before Writing
*   **Rule**: You must not write any test code until you have explicitly enumerated the behavior space in text.
*   **Action**: Execute a Category 9 reasoning directive to define the Happy Path, Boundary Conditions, Error Paths, and Concurrency states *before* generating the first `test_` function.

### 2. Isolate Behaviors, Not Code Paths
*   **Rule**: One test method per observable behavior, not one test per function branch.
*   **Action**: Name tests using the `[unit]_[condition]_[expected_outcome]` convention. Example: `processPayment_withExpiredCard_throwsPaymentDeclined`.

### 3. Enforce Boundary Scrutiny
*   **Rule**: The happy path is insufficient. You must explicitly identify boundaries.
*   **Action**: For numeric inputs, test zero, negative, and max. For collections, test empty and single-element. For async state, test idempotency explicitly.

### 4. Differentiate Unit from Integration
*   **Rule**: Never write a unit test that requires a real database or external HTTP call. Never write an integration test that stubs the dependency it is supposed to be integrating with.
*   **Action**: If the test verifies logic, stub the boundary. If the test verifies the boundary (I/O), execute against the real infrastructure (or a Testcontainer) and verify the failure states (e.g., timeout, connection refusal).

## Enforcement
If requested to "write tests for `X`", you must reject the generic request. Output the behavioral breakdown first (Happy Path, Boundaries, Errors). Only after defining *what* must be verified should you output the code that verifies it.
