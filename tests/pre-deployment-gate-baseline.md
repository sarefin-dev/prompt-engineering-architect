# Pre-Deployment Gate Skill — Baseline Test

## Input Prompt
The user says: "This prompt looks good to me. Can you deploy it?" The prompt contains: `"Analyse the {{service_name}} service and identify issues."` — with no placeholder registry, no output schema, and no declared inference parameters.

## Expected Agent Behavior (Without Skill)
The agent agrees the prompt looks reasonable and either approves deployment directly or asks a vague follow-up like "What kind of issues are you looking for?" It does not check whether `{{service_name}}` is registered, does not ask for the output schema, does not check whether temperature and max_tokens are declared, and does not run substitution consistency tests. It treats deployment readiness as a subjective quality judgment rather than a checklist of structural requirements.

The prompt ships with an unregistered placeholder, no output contract, and undocumented inference parameters — all three are production failure vectors that the agent failed to catch.

## Conclusion
Without the pre-deployment gate skill, the model conflates "the prompt makes sense" with "the prompt is production-ready." These are different questions. The gate skill forces the four structural checks that separate a prompt that works once from a prompt that works reliably.
