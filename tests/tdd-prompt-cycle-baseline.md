# TDD Prompt Cycle Skill — Baseline Test

## Input Prompt
The user says: "I need a prompt that classifies customer support tickets into categories. Write the prompt for me."

## Expected Agent Behavior (Without Skill)
The agent immediately writes a classification prompt. It chooses categories based on common sense (Billing, Technical, Account, General), writes an instruction-based prompt, and delivers it. No test cases are defined before the prompt is written. No output schema is specified. No RED cases are identified. The categories are the agent's best guess at what the user needs, not a specification the user has approved.

When the prompt is later deployed, it misclassifies edge cases that were never considered — tickets that span two categories, tickets in non-English languages, tickets that are actually spam. These failures surface in production because no adversarial cases were defined before authoring.

## Conclusion
Without the TDD prompt cycle skill, the model authors prompts speculatively. It optimises for producing a plausible-looking output, not for covering the test cases that matter. The result is a prompt calibrated for what seemed reasonable at authoring time, not for what production inputs actually look like.
