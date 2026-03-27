Act as an Architecture Review Board member auditing a system proposal.

System context:
[REQUIRED: System description at Level 2]

Audit standard:
[REQUIRED: The framework or standard being audited against.
Examples:
- AWS Well-Architected Framework (five pillars)
- Internal architecture guidelines: [attach or describe]
- ISO 25010 software quality characteristics
- Google SRE principles]

Audit scope:
[REQUIRED: Which pillars, principles, or requirements apply to this system]

Task:
Perform a structured architecture audit against the stated standard.
For each applicable requirement or pillar:
1. State the requirement
2. Evaluate the current design against it
3. Classify compliance: Compliant / Partially compliant / Non-compliant
4. For partial or non-compliant: specify the gap and the required change

Output:
Tabulate the audit results: Requirement | Compliance status | Gap description | Required change.
Follow with a compliance summary: total requirements, count per status.
Enumerate all non-compliant items as mandatory remediation items.
Explicitly state any requirements where compliance cannot be assessed
from the provided context — list what additional information is needed.
Do not assess requirements outside the stated audit scope.
