# Pre-Deployment Gate Skill — Skill Test

## Input Prompt
The user says: "This prompt looks good to me. Can you deploy it?" The prompt contains: `"Analyse the {{service_name}} service and identify issues."` — with no placeholder registry, no output schema, and no declared inference parameters.

*Context injected: `.claude/skills/pre-deployment-gate.md`*

## Expected Agent Behavior (With Skill)
The agent halts deployment and runs all four gate checks explicitly, reporting each result:

**CHECK 1 — Placeholder completeness: FAIL**
`{{service_name}}` is present in the template but absent from the placeholder registry. Deployment blocked. Required action: add `service_name` to the registry with its type (P1–P5), resolution time (deploy-time or request-time), and source.

**CHECK 2 — Substitution consistency: UNVERIFIABLE**
Cannot test consistency without a registered placeholder value set. Gate cannot be signed off until Check 1 is resolved.

**CHECK 3 — Boundary value handling: UNVERIFIABLE**
Cannot test boundary values (empty string, null, max-length) without resolving Check 1.

**CHECK 4 — Inference parameter documentation: FAIL**
`temperature`, `max_tokens`, and `stop_sequences` are not declared in the prompt version file. Deployment blocked. Required action: add a `VERSION.yml` file declaring these values. If deployment temperature exceeds 0.5, a written justification is required.

**Overall gate result: FAIL (2 hard failures, 2 unverifiable)**

The agent does not approve deployment under any circumstances until all four checks return PASS. It provides the exact remediation steps for each failure.

## Conclusion
The skill transforms a subjective approval question into a four-condition checklist with binary outcomes. The user cannot accidentally deploy a structurally incomplete prompt — the gate requires explicit sign-off on every condition before the prompt is production-eligible.
