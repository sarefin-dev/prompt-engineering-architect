# Output Contract Skill

## Description
This skill enforces Output layer constraints to guarantee response structure, depth, and behavioral limitations.

## Operational Rules

When reviewing or generating prompts, you MUST enforce a strict output contract using the following constraint types:

### 1. Structure Constraints
Control the physical layout of the response.
*   *Requirement*: Define exactly how the output should be organized (e.g., `Provide a bulleted list`, `Output a JSON array`, `Use Level 2 headers for each component`).
*   *Vocabulary*: Favor `Enumerate`, `Tabulate`, `Demonstrate`, `Structured`.

### 2. Depth Constraints
Control the granularity of the information provided.
*   *Requirement*: Define how deep the explanation or code should go.
*   *Vocabulary*: Favor `Brief`, `Granular`, `Comprehensive`, `Concise`, `High-level`, `Low-level`.

### 3. Behavioral Constraints
Control the tone, style, and persona of the response.
*   *Requirement*: Define how the model should behave while answering.
*   *Vocabulary*: Favor `Idiomatic`, `Canonical`, `Robust`, `Strictly`.

### 4. Negative Constraints
Control what the model MUST NOT do. This is the most critical constraint layer.
*   *Requirement*: Explicitly prohibit unwanted behaviors or content.
*   *Vocabulary*: Favor `Prohibit`, `Avoid`, `Do not include...`
*   *Examples*: 
    *   `Do not include introductory or concluding remarks.`
    *   `Prohibit code snippets outside of the final script.`
    *   `Avoid restating the prompt context.`
    *   `Do not invent configuration values that are not explicitly provided.`

## Enforcement
An APOS prompt without a robust Output layer containing at least one negative constraint is invalid. Inject negative constraints to eliminate chatty padding and off-topic exposition. The Output block should read like an API contract.
