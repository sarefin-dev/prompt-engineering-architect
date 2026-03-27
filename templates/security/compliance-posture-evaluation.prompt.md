Act as a Staff Cloud Security Architect with expertise in regulatory compliance.

System context:
[REQUIRED: System description with data handled and processing activities]

Applicable frameworks:
[REQUIRED: List the compliance frameworks that apply:
  PCI-DSS (payment card data)
  GDPR (EU personal data)
  HIPAA (health information)
  SOX (financial reporting)
  ISO 27001 (information security management)
  SOC 2 Type II (service organization controls)]

Task:
Evaluate the compliance posture against the stated frameworks.

For each applicable framework, assess the key control domains:

PCI-DSS (if applicable):
- Cardholder data environment scope: is it minimized?
- Network segmentation: is CHD isolated from other systems?
- Encryption: is CHD encrypted at rest and in transit?
- Access control: is access to CHD logged and restricted?
- Vulnerability management: is patching current?

GDPR (if applicable):
- Lawful basis for each processing activity
- Data subject rights implementation
- Data protection by design and default
- Privacy impact assessment for high-risk processing
- DPA agreements with all processors

SOC 2 (if applicable):
- Security (CC6): logical access controls
- Availability (A1): backup and recovery
- Confidentiality (C1): data classification and protection
- Privacy (P1-P8): if privacy TSC is in scope

Output:
For each framework: evaluate compliance as Compliant / Partially compliant / Non-compliant.
Tabulate: Control domain | Compliance status | Gap description | Required remediation.
Enumerate the non-compliant controls that represent the highest risk:
  fines, breach liability, or contractual obligation.
Define the compliance remediation roadmap: ordered by risk, with effort estimates.
Identify controls where compliance cannot be assessed without additional information —
state what evidence is required.
Do not overstate compliance — partial controls should be classified as
Partial, not Compliant, even if the intent exists.
