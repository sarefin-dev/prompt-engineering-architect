# Vocabulary Audit Skill

## Description
This skill enforces prompt engineering vocabulary discipline, eliminating probability-reducing language and injecting high-leverage terminology.

## Operational Rules

When reviewing, generating, or executing prompts, you MUST audit the language against the following rules:

### 1. Eliminate Weakening Vocabulary (Probability Reducers)
You must aggressively remove or replace the following terms:
*   **"If possible" / "Try to"**: Revert to `Must` or `Mandate`. (Removes optionality).
*   **"Usually" / "Generally" / "Sometimes"**: Revert to explicit conditional rules (e.g., `If X, then Y`).
*   **"Appropriate" / "Suitable" / "Best"**: Revert to explicit criteria (e.g., `Optimized for lowest tail latency`).
*   **"Make sure" / "Ensure"**: Replace with structural constraints or tests (e.g., `Verify X by checking Y`).
*   **"Think about" / "Consider"**: Replace with Category 3 analytical directives (e.g., `Analyze`, `Evaluate`, `Diagnose`).

### 2. Inject Strengthening Vocabulary (Precision & Constraint)
Elevate the prompt by injecting Category 1 (Precision) and Category 4 (Constraint) words where applicable:
*   Use `Explicitly` to eliminate hidden assumptions.
*   Use `Rigorously` or `Scrutinize` to activate deep, adversarial analysis.
*   Use `Avoid` or `Prohibit` to set strict boundaries on the output.
*   Use `Exactly` or `Verbatim` for strict matching requirements.

### 3. Elevate the Output Format
Replace weak output requests with Category 9 (Format) directives:
*   Instead of "list", use `Enumerate` (implies ordered/prioritized).
*   Instead of "compare", use `Tabulate` (forces a matrix comparison).
*   Instead of "explain", use `Diagnose` (forces root-cause analysis) or `Demonstrate` (forces code generation).
*   Instead of "write", use `Synthesize` (implies combining findings).

### 4. Activate Staff-Level Constructs
When the context is architectural (system design, distributed systems), inject Category 6/7/8 terms (e.g., `idempotent`, `blast radius`, `backpressure`, `tail latency`, `golden signals`). 

## Enforcement
If a prompt contains weakening vocabulary, you must edit the prompt to remove the weakness *before* executing the task. Treat weakening vocabulary as a structural defect.
