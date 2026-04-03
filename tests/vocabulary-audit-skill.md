# Vocabulary Audit Skill — Skill Test

## Input Prompt
The user submits this prompt for review: "Please ensure the analysis is appropriate and try to identify any relevant issues with the system. Make sure to consider all possible factors and provide useful recommendations."

*Context injected: `.claude/skills/vocabulary-audit.md`*

## Expected Agent Behavior (With Skill)
The agent immediately classifies every substantive word against the 9-category taxonomy and produces a structured findings report:

**Weaknesses Found (Category 7 — Softeners detected):**
- `ensure` → probability-reducing hedge. Replacement: `verify` (Cat 4) or `confirm` (Cat 1).
- `try to identify` → conditional framing. Replacement: `identify` (Cat 1) with no conditional.
- `appropriate` → undefined standard. Replacement: specify the standard explicitly (e.g., "compliant with RFC 7807").
- `relevant` → undefined filter. Replacement: name the relevance criterion (e.g., "that affect availability or data integrity").
- `make sure` → redundant hedge identical to `ensure`. Remove entirely.
- `consider all possible factors` → unbounded scope. Replacement: enumerate the specific factors (e.g., "evaluate latency, throughput, and failure isolation").
- `useful recommendations` → undefined utility. Replacement: "actionable recommendations ranked by implementation priority".

**Categories missing:** Cat 3 (Analytical directives — no instruction to reason before concluding), Cat 4 (Constraint vocabulary — no boundaries on scope or output).

**Rewritten Prompt:**
> "Identify all availability and data integrity issues in the system. For each issue: classify the failure mode, assess the blast radius, and rank remediation steps by implementation priority. Reason through each failure mode before concluding. Do not include issues outside the availability and data integrity scope."

**Verdict: FAIL.** Seven Category 7 softeners, two missing categories.

## Conclusion
The skill converts impressionistic feedback into a classified defect list with precise replacements. The rewritten prompt is measurably stronger — every word belongs to a category that increases response probability.
