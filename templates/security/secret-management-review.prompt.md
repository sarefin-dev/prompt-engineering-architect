Act as a Staff Cloud Security Architect.

System context:
[REQUIRED: System with credentials, API keys, certificates, and secrets]
[REQUIRED: Current secret management approach]
[REQUIRED: Deployment environment — Kubernetes, cloud, on-premise]

Task:
Evaluate the secret management strategy and design improvements.

Assess the current approach against these requirements:

1. No secrets in code or version control:
   Are there any secrets, API keys, or credentials committed to source control?
   Are configuration files with secrets excluded from version control?

2. Secret storage:
   Are secrets stored in a dedicated secrets manager?
   (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
   Are secrets encrypted at rest with envelope encryption?

3. Secret injection:
   How are secrets provided to the application at runtime?
   (Environment variables, mounted files, secrets manager SDK call)
   Are secrets injected at startup or retrieved dynamically?

4. Secret rotation:
   Are secrets rotated regularly? Is rotation automated?
   What is the secret lifetime for each credential type?

5. Access control:
   Who can access each secret? Is access logged and audited?
   Is the principle of least privilege applied to secret access?

6. Certificate management:
   Are TLS certificates managed and rotated automatically?
   What is the certificate validity period and renewal process?

Output:
For each requirement: state the current compliance state and the gap.
Enumerate any secrets that may be exposed: committed to source control,
logged in plain text, or accessible without authentication.
Design the secret lifecycle for the highest-risk credentials:
creation, distribution, rotation, and revocation.
State the secret rotation procedure for the three most critical credentials.
Define the monitoring required: secret access should be logged and
unauthorized access attempts should alert.
Do not recommend storing secrets in environment variables without
noting the risk — environment variables are readable by all processes
on the host and may be logged.
