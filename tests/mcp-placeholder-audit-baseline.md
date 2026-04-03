# MCP Placeholder Audit Skill — Baseline Test

## Input Prompt
The user submits this MCP tool description for review:
```
"Processes a payment. Supports USD and EUR. Maximum amount is $50,000.
Requires the 'payments:write' permission. If the user has admin access,
the limit is waived."
```

## Expected Agent Behavior (Without Skill)
The agent reviews the tool description and approves it as clear and well-written. It notes that the description is specific and provides useful information to the model. It does not identify `USD and EUR` as a deploy-time capability enumeration that will be wrong for GBP-enabled tenants. It does not flag `$50,000` as a per-user limit that will be incorrect for high-tier users. It does not identify `payments:write` as a permission string that will change during auth system migrations. It does not flag "If the user has admin access, the limit is waived" as business logic encoded in natural language that the model will act on — and that will become silently wrong when the policy changes.

The tool ships with four implicit placeholders that will produce wrong model decisions in at least three deployment configurations.

## Conclusion
Without the placeholder audit skill, the model evaluates tool descriptions for readability, not for deployment variance. A clear description is not a correct description. The skill is required to distinguish values that are fixed from values that are implicit variables disguised as facts.
