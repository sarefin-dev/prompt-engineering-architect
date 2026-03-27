# Pre-Commit Hook

## Trigger Condition
Fires automatically whenever code is about to be committed or submitted for review.

## Description
Enforces the mandatory quality gate. It ensures that code is not committed without corresponding behavioral tests.

## Hook Execution
1.  **Detect Changes**: Identify which production files are being modified.
2.  **Verify Tests**: Check if the corresponding `test_` or `spec_` files are also being modified.
3.  **Halt & Warn**: If production code is changed but no tests are modified, intercept the action.
    *   *Warning*: `[QUALITY GATE] You are modifying production code without providing tests. Please provide a RED phase failing test or a description of the boundary conditions being tested.`
4.  **Enforce**: Do not proceed with the commit/submission until tests are provided or the user explicitly overrides with a justification.
