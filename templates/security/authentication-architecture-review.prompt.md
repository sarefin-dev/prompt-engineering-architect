Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: Architecture description with all authentication points]
[REQUIRED: User types — human users, service accounts, external APIs]
[REQUIRED: Current authentication mechanisms per component]

Task:
Evaluate the authentication architecture for correctness and security.

Assess authentication at each boundary:

1. User-facing authentication:
   - Is multi-factor authentication (MFA) available and enforced for privileged users?
   - Are credentials stored using a modern password hashing algorithm (bcrypt, Argon2)?
   - Is session management secure: session fixation, session hijacking, session timeout?
   - Is OAuth 2.0 / OIDC used for federated identity where appropriate?

2. Service-to-service authentication:
   - Is mutual TLS (mTLS) used between internal services, or are services implicitly trusted?
   - Are service account credentials rotated regularly?
   - Are service identities tied to workload identity (Kubernetes service accounts, cloud IAM)
     rather than long-lived credentials?

3. API authentication:
   - Is every API endpoint authenticated? Are there accidentally unauthenticated endpoints?
   - Are JWTs validated correctly: signature, expiry, issuer, audience?
   - Are API keys scoped to minimum required permissions?

4. Administrative access:
   - Is privileged access (admin, DBA, infrastructure) protected with MFA?
   - Is privileged access time-limited and audited?

Output:
For each authentication boundary: state the current mechanism, the security gap,
and the recommended improvement.
Enumerate unauthenticated endpoints — every endpoint that accepts requests
without verifying identity.
Enumerate service-to-service calls where implicit trust is applied
(internal network location used as identity) — these should use explicit identity.
Identify the highest-risk authentication gap — the one most likely to be
exploited by an attacker.
Do not recommend password-based authentication without MFA for any
administrative or privileged access.
