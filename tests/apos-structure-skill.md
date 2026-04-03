# APOS Structure Skill — Skill Test

## Input Prompt
The user asks: "Write me a prompt that makes Claude review our microservice architecture and tell me if it's production-ready."

*Context injected: `.claude/skills/apos-structure.md`*

## Expected Agent Behavior (With Skill)
The agent refuses to produce a single-paragraph prompt. Instead, it constructs a five-layer APOS specification and asks the user for the missing Context before proceeding:

1. **Role layer** (primacy): Defines the persona as a Principal Architect with explicit competencies in distributed systems and production readiness assessment. Placed first.
2. **Context layer** (early anchor): Flags that the Layer 2 system context is missing — the agent explicitly asks: "You must provide: the service count, the deployment environment, the team size, and the primary quality attribute concern."
3. **Task layer** (content-completion anchor): Frames the evaluation as a structured assessment against named quality attributes, not an open-ended review.
4. **Focus layer** (recency): Adds constraints — distinguish blocking issues from advisory items; do not recommend patterns the team cannot operationally support.
5. **Output layer** (recency): Specifies a JSON schema with `overall_rating`, `blocking_issues`, `advisory_items`, and `quality_attribute_scores` — not free-form prose.

The agent withholds the final prompt until the user supplies the missing context.

## Conclusion
The skill enforces mechanical layer construction and surfaces the context dependency before any prompt text is produced. The user cannot receive a weak prompt by accident — the skill requires them to specify what it needs.
