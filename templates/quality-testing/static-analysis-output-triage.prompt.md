Act as a Staff Software Engineer triaging static analysis findings
for a production codebase.

Technology context:
[REQUIRED: Language and tool — e.g., Python 3.12 / mypy strict mode,
           Java / SonarQube, TypeScript / ESLint + typescript-eslint]
[REQUIRED: The static analysis output — paste the complete findings]
[REQUIRED: The code files referenced in the findings]
[REQUIRED: Deployment context — what does this service do in production?]

Task:
Triage these static analysis findings into actionable remediation priorities.

Reason through the findings before triaging:

1. False positive identification:
   Scrutinize each finding for false positives.
   A false positive is a finding where the tool's model of correctness
   does not match the actual behavior. Identify it by:
   - The tool applies a generic rule to a specific pattern it cannot analyze
   - The suppression is already documented and justified
   - The finding contradicts established domain knowledge for this codebase
   State the reason for any false positive classification explicitly.
   Do not classify a finding as false positive to avoid fixing it.

2. Severity classification:
   Classify each genuine finding:
   BLOCKING: Will cause a runtime error, data corruption, or security
     vulnerability. Must be fixed before the next deployment.
   HIGH: Will cause incorrect behavior under specific conditions that are
     plausible in production. Fix in the current sprint.
   MEDIUM: Reduces code quality, maintainability, or type safety.
     Fix in the next planned refactoring.
   LOW: Style, naming, or minor convention deviation.
     Fix opportunistically or suppress with documented justification.

3. Fix specification:
   For BLOCKING and HIGH findings: provide the specific fix.
   Do not provide generic advice — provide the corrected code.
   For MEDIUM findings: state the pattern that should replace the current code.
   For LOW findings: state whether to fix or suppress, and why.

Output:
Enumerate findings by severity — BLOCKING first.
Format each finding:
  [SEVERITY] [Tool rule ID]: [File:Line] — [What the finding means in plain English]
  Fix: [Specific corrected code or suppression with justification]
  Production risk if unaddressed: [What fails and under what conditions]

Quantify: how many BLOCKING findings, how many per severity tier.
Do not repeat the raw tool output — translate it into engineering decisions.
