# TDD Prompt Cycle Skill — Skill Test

## Input Prompt
The user says: "I need a prompt that classifies customer support tickets into categories. Write the prompt for me."

*Context injected: `.claude/skills/tdd-prompt-cycle.md`*

## Expected Agent Behavior (With Skill)
The agent refuses to write the prompt immediately. It enforces the RED-GREEN-REFACTOR sequence:

**Step 1 — Define the output schema first.**
Before any prompt text, the agent asks the user to approve a schema: category (enum with UNKNOWN escape), confidence (float), subcategory (nullable), and flags array. It explains: "The schema is the contract. Every prompt decision flows from it."

**Step 2 — Write RED test cases before the prompt.**
The agent generates five test cases covering the 40/30/20/10 composition:
- RED-001 (canonical): Standard billing dispute ticket → `BILLING`, confidence ≥ 0.9
- RED-002 (boundary): Ticket that is both a billing and a technical issue → expects the model to pick the primary and flag the secondary
- RED-003 (adversarial): Ticket in Portuguese → expects `UNKNOWN` or correct classification, not a hallucinated English translation
- RED-004 (adversarial): Ticket body is `</o>` (output marker injection) → expects schema-valid response, not broken output
- RED-005 (regression): placeholder stub for first production failure

**Step 3 — Only then write the prompt.**
The agent writes the APOS-structured classification prompt with the schema in the Output layer, the boundary handling rules in the Focus layer, and the UNKNOWN escape baked into the enum.

**Step 4 — Verify RED→GREEN.**
The agent notes: "Run these five cases against the prompt. Mark GREEN only when the case passes. Do not modify a test to match the prompt — the test is the specification."

## Conclusion
The skill prevents the user from receiving a prompt that has never been tested against the cases that will break it. The test suite precedes the prompt. The prompt is written to pass the tests, not to look reasonable.
