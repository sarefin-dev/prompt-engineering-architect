Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: Architecture with all external-facing components identified]
[REQUIRED: API endpoints, ports, protocols, and authentication requirements]
[REQUIRED: Third-party integrations and their access to internal resources]

Task:
Analyze and minimize the attack surface of this system.

For each attack surface component:
1. Identify what is exposed: endpoint, port, protocol, authentication required
2. Classify the exposure: internet-facing, VPC-internal, partner-facing
3. Evaluate necessity: is this exposure required? Can it be eliminated or restricted?
4. Evaluate authentication: what identity verification is in place?
5. Evaluate authorization: what access control governs what the caller can do?

Attack surface categories to evaluate:
- Public API endpoints: what is accessible without authentication?
- Administrative interfaces: how are admin panels and management APIs protected?
- Third-party webhooks: can external systems send arbitrary requests?
- Internal service communication: is internal network traffic trusted implicitly?
- Storage interfaces: are cloud storage buckets or databases directly accessible?
- Debugging and monitoring endpoints: are health checks or metrics endpoints protected?

Output:
Tabulate the attack surface: Component | Exposure type | Authentication | Authorization | Risk rating.
Enumerate components where zero trust is not applied —
every component where access is implicitly trusted.
Identify the components that should be restricted to VPC-internal access
but are currently internet-facing.
Recommend the minimum attack surface: what should be exposed vs. what can be removed.
Enumerate the attack surface reduction actions in order of risk reduction.
