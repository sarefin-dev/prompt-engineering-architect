# Post-Generate Hook

## Trigger Condition
Fires automatically immediately after the system generates new code, documentation, or architecture proposals.

## Description
Enforces self-correction and validation. It prevents the model from blindly assuming its generated output is correct without secondary verification.

## Hook Execution
1.  **Intercept**: Pause before returning the final output to the user.
2.  **Verify Syntax**: If the output is code, automatically run a syntax check (if tooling is available, e.g., `npm run lint` or `python -m py_compile`).
3.  **Verify Intent**: If the output is an analysis, cross-reference the output against the `Focus` and negative constraints defined in the original prompt. Did it include something it was asked to avoid?
4.  **Correct**: If a violation or syntax error is found, explicitly state the error and run a silent secondary pass to fix it before presenting to the user.
