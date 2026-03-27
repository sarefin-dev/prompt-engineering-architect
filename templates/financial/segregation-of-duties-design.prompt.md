Act as a Staff Security Architect specializing in financial controls.

System context:
[REQUIRED: The financial system and its operations]
[REQUIRED: User roles and their current access]
[REQUIRED: Regulatory requirement for segregation — SOX, PCI-DSS, or internal policy]

Task:
Design a segregation of duties (SoD) framework for the stated system.

SoD principles:
No single individual should be able to both authorize and execute a
financial transaction. No single individual should be able to both
process and record a transaction. No single individual should be able
to both approve and audit.

For each critical operation in the system:
1. Identify the operation (e.g., "create a payment", "approve a limit",
   "change a system configuration")
2. Identify the roles that currently can perform this operation
3. Identify the SoD conflict: which combinations of operations create risk
   when performed by the same individual?
4. Design the control: approval workflow, dual authorization, or system
   enforcement of role separation

Address these specific SoD requirements:
- Transaction authorization: the person who creates a payment cannot
  be the same person who approves it above a defined threshold
- Limit management: the person who sets a risk limit cannot be the same
  person who benefits from trades within that limit
- System access: production system access cannot be granted by the same
  person who holds that access
- Audit log access: the person who generates audit events cannot
  have administrative access to modify audit logs

Output:
Provide the SoD matrix: Operation | Roles that can perform it | SoD conflicts.
Design the approval workflow for operations with SoD requirements.
Enumerate the current SoD violations — roles that currently hold
conflicting access.
State the system enforcement vs. procedural enforcement for each control:
system-enforced SoD is preferred; procedural SoD requires compensating controls.
Define the compensating controls for any SoD violation that cannot be
immediately remediated.
Do not accept "we trust our employees" as a compensating control — SoD
exists to protect employees as much as the organization.
