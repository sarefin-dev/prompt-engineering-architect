Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: System description with user roles and permission requirements]
[REQUIRED: Resource types that require access control]
[REQUIRED: Current authorization approach, if any]

Task:
Design an authorization model that enforces least privilege.

Evaluate authorization models for this system:

1. Role-Based Access Control (RBAC):
   - Assign permissions to roles; assign roles to users
   - Appropriate when: permissions are stable, users fit well-defined roles
   - Risk: role explosion when roles are created to handle every permission edge case

2. Attribute-Based Access Control (ABAC):
   - Permissions based on attributes of the user, resource, and environment
   - Appropriate when: fine-grained dynamic permission decisions are required
   - Risk: policy complexity makes it hard to reason about effective permissions

3. Relationship-Based Access Control (ReBAC):
   - Permissions derived from relationships between entities
   - Appropriate when: sharing and delegation between users is a core feature
   - Example: Google Zanzibar model

For the recommended model:
1. Define the permission taxonomy: what actions exist, on what resource types?
2. Define the roles or policies: who gets what permissions by default?
3. Define the enforcement point: where in the architecture are permissions checked?
4. Define the audit logging: what authorization decisions are logged?

Output:
Recommend the authorization model with explicit rationale for this system.
Define the permission taxonomy: Action × Resource type matrix.
Identify every enforcement point — authorization must be enforced close
to the resource, not just at the API gateway.
Enumerate the privilege escalation paths: ways an attacker with low-privilege
access could gain higher-privilege access.
Define the "deny by default" rule: any resource access not explicitly
permitted must be denied, not permitted.
Do not recommend a model where adding a new resource type requires
manual permission grants for all existing users — this creates permission gaps.
