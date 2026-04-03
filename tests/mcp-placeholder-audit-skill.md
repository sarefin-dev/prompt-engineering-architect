# MCP Placeholder Audit Skill — Skill Test

## Input Prompt
The user submits this MCP tool description for review:
```
"Processes a payment. Supports USD and EUR. Maximum amount is $50,000.
Requires the 'payments:write' permission. If the user has admin access,
the limit is waived."
```

*Context injected: `.claude/skills/mcp-placeholder-audit.md`*

## Expected Agent Behavior (With Skill)
The agent identifies four implicit placeholders and classifies each against the P1–P5 taxonomy. It blocks deployment until all four are resolved:

**P1 — Capability enumeration: `USD and EUR`**
This is a hardcoded currency list that varies by tenant and region. A UK tenant with GBP enabled will have a model that incorrectly tells users GBP is not supported. Remediation (Pattern A): replace with `{supported_currencies}`, resolved from config at deploy-time.

**P2 — Limit value: `$50,000`**
This is a per-user limit that varies by account tier. A high-tier user with a $500,000 limit will have the model reject valid large payments. Remediation (Pattern B2): replace with "up to your account's configured payment limit" — relational, not absolute.

**P3 — Permission identifier: `payments:write`**
This permission string is hardcoded but will change during auth system migrations. Remediation (Pattern A): replace with `{payments_write_permission}`, resolved from auth config at deploy-time.

**P5 — Behavioral conditional: `If the user has admin access, the limit is waived`**
This is business logic encoded in natural language. The model will act on it. When the policy changes (e.g., admin limit is capped, not waived), the tool description will not be updated and the model will enforce the old policy. Remediation (Pattern C): remove from description entirely. The waiver logic belongs in the tool implementation, surfaced as a response field (e.g., `limit_waived: true`), not as a natural language instruction.

**Risk level: CRITICAL (4 implicit placeholders). Deployment blocked.**

## Conclusion
The skill surfaces the difference between a description that reads correctly and a description that behaves correctly across all deployments. All four findings would have produced silent wrong behavior in production — none would have raised an error.
