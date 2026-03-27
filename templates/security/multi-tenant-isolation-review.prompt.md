Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: Multi-tenant system description]
[REQUIRED: Tenancy model — shared schema, schema-per-tenant, or database-per-tenant]
[REQUIRED: Current isolation mechanism]

Task:
Evaluate the multi-tenant isolation for data leakage and privilege escalation risk.

Assess isolation at each layer:

1. Application layer:
   - Is tenant context verified on every request?
   - Can a request from Tenant A access Tenant B's data through any code path?
   - Is tenant context established from a verified token, not from a request parameter?

2. Data layer:
   - For shared schema: is row-level security enforced at the database layer?
   - For schema-per-tenant: is cross-schema access prevented?
   - Can a privileged application user access all tenants' data
     when their role only requires access to one?

3. API layer:
   - Does every API endpoint verify that the requested resource belongs
     to the authenticated tenant?
   - Are tenant IDs validated against the authenticated token, not taken from the URL?

4. Infrastructure layer:
   - Are tenant workloads isolated in separate namespaces or compute?
   - Can a compromised tenant's workload access another tenant's resources?

5. Audit and monitoring:
   - Is cross-tenant access logged and alerted?
   - Can a tenant enumeration attack reveal other tenants' existence?

Output:
For each isolation layer: state the current mechanism, the leakage risk,
and the recommended improvement.
Enumerate the data access code paths that bypass tenant isolation checks —
these are critical security vulnerabilities.
Identify the tenant isolation failure scenario with the highest business impact:
a data breach that exposes one tenant's data to another is a compliance event.
Define the cross-tenant access monitoring requirement.
Do not accept "it is an internal service so cross-tenant access is not a risk" —
insider threats and compromised service accounts are in scope.
