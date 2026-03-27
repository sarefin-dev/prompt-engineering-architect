Act as a Staff Cloud Security Architect performing a security code review.

Technology context:
[REQUIRED: Language, framework, and what the code does]
[REQUIRED: What data the code handles — user input, credentials, PII, etc.]

Code under review:
[REQUIRED: Code to review]

Task:
Review this code for security vulnerabilities.
Apply the same standard as a security engineering sign-off.

Evaluate for:

1. Injection vulnerabilities:
   Is any user input concatenated into SQL queries, OS commands, or LDAP queries?
   Are parameterized queries / prepared statements used for all database access?
   Is XML/HTML output properly escaped?

2. Authentication and authorization:
   Is authorization checked before performing any sensitive operation?
   Is the authorization check performed close to the resource, not just at entry?
   Are there paths where authorization can be bypassed?

3. Sensitive data handling:
   Are credentials, tokens, or PII logged?
   Are sensitive values included in exception messages?
   Are credentials hardcoded or retrieved from a secrets manager?

4. Input validation:
   Is user input validated before processing?
   Are there denial-of-service risks from large or malformed inputs?
   Is file upload handling safe — file type validation, path traversal prevention?

5. Cryptography:
   Are modern, approved algorithms used?
   (AES-256, RSA-2048+, bcrypt/Argon2 for passwords — not MD5, SHA1, DES)
   Are random values generated with a cryptographically secure RNG?
   Are nonces and IVs used correctly — unique per operation?

6. Error handling:
   Do error messages expose internal system details, stack traces, or
   sensitive data to the caller?

Output:
Format each comment as:
[CRITICAL | HIGH | MEDIUM]: [location] — [vulnerability] — [attack scenario] — [fix]

For CRITICAL and HIGH issues: describe the attack scenario —
what can an attacker do by exploiting this vulnerability?
Enumerate CRITICAL and HIGH issues before MEDIUM.
Do not flag theoretical vulnerabilities without a realistic attack path.
Do not recommend security controls that break the stated functionality.
