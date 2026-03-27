Act as a Staff Cloud Security Architect with expertise in regulatory compliance.

System context:
[REQUIRED: System description and the data it processes]

Applicable regulations:
[REQUIRED: List the regulations — PCI-DSS, GDPR, SOX, HIPAA, MiFID II,
  Basel III, DORA, or domain-specific]

Task:
Assess the system's compliance controls against the stated regulations.

For each regulation, evaluate the key control requirements:

PCI-DSS v4.0 (if applicable):
- Requirement 3: Protection of stored account data
  (encryption, tokenization, masking of PAN)
- Requirement 6: Secure systems and software development
  (vulnerability management, secure SDLC)
- Requirement 7: Restrict access to system components
  (least privilege, role-based access)
- Requirement 10: Log and monitor all access
  (audit logs, log integrity, retention)
- Requirement 11: Test security regularly
  (penetration testing, vulnerability scanning)

GDPR (if applicable):
- Article 5: Data minimization and purpose limitation
- Article 25: Data protection by design and by default
- Article 32: Security of processing (encryption, pseudonymization)
- Article 33/34: Breach notification procedures
- Chapter 3: Data subject rights implementation

SOX Section 404 (if applicable):
- Internal controls over financial reporting (ICFR)
- Change management controls for financial systems
- Segregation of duties for financial data access

DORA (Digital Operational Resilience Act, if applicable):
- ICT risk management framework
- Digital operational resilience testing
- Third-party ICT risk management

Output:
For each regulation and control requirement:
state whether the system is Compliant, Partially compliant, or Non-compliant.
Tabulate: Regulation | Requirement | Status | Gap | Required remediation.
Enumerate all Non-compliant items — these represent regulatory exposure.
State the evidence required to demonstrate compliance for each Compliant item —
  compliance must be demonstrable, not asserted.
Identify the controls that require continuous monitoring vs. periodic assessment.
Do not claim compliance based on intent — only on implemented and verified controls.
