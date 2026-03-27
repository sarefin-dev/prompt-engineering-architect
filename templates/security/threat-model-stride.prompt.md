Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: Architecture description — entry points, services, data stores,
  external integrations, trust boundaries]

Data classification:
[REQUIRED: What data does the system process?
  PII, financial data, health data, credentials, intellectual property]

User types:
[REQUIRED: Who uses the system — authenticated users, anonymous users,
  internal services, external APIs, administrators]

Task:
Scrutinize this system using the STRIDE threat model — leave no trust boundary
assumption unchallenged.

For each trust boundary and component, scrutinize all six threat categories:

Spoofing: Can an attacker impersonate a legitimate user or service?
  - Examine every authentication point
  - Examine service-to-service identity verification

Tampering: Can an attacker modify data in transit or at rest?
  - Examine every data transmission path
  - Examine storage integrity controls

Repudiation: Can an actor deny having performed an action?
  - Examine audit logging coverage
  - Examine log integrity controls

Information disclosure: Can sensitive data be accessed by unauthorized parties?
  - Examine every data access path
  - Examine error messages and logs for data leakage

Denial of service: Can an attacker prevent legitimate users from accessing the system?
  - Examine rate limiting and throttling
  - Examine resource exhaustion vectors

Elevation of privilege: Can an attacker gain access beyond their authorization?
  - Examine authorization enforcement points
  - Examine privilege escalation paths

Output:
Enumerate threats by STRIDE category.
For each threat: describe the attack vector, the asset at risk, the current
control (or absence of one), and the recommended mitigation.
Prioritize threats using a risk rating: Likelihood × Impact (High/Medium/Low).
Enumerate the top five highest-priority threats — these define the
security improvement roadmap.
Scrutinize trust boundaries where no authentication or authorization is enforced —
these are the highest-severity gaps.
Do not limit the threat model to external threats — insider threats and
compromised internal service threats are equally in scope.
