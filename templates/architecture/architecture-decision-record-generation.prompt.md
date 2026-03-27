Act as a Staff Architect documenting an architectural decision.

Decision context:
[REQUIRED: What decision was made]
[REQUIRED: What alternatives were considered]
[REQUIRED: What constraints drove the decision]
[REQUIRED: What trade-offs were accepted]
[OPTIONAL: When the decision was made and by whom]

Task:
Produce a complete Architecture Decision Record for this decision.

Output:
Format the ADR with these sections:

# ADR-[XXXX]: [Decision title — specific and searchable]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]

## Context
[2–3 paragraphs: the situation that necessitated a decision,
the constraints in play, and why the decision could not be deferred]

## Decision
[1–2 paragraphs: the specific decision made, with enough detail
that an engineer unfamiliar with the context can implement it correctly]

## Consequences
[Positive consequences: what the decision enables]
[Negative consequences: what the decision constrains or costs]
[Risks: what could go wrong if the decision proves incorrect]

## Alternatives considered
[For each alternative: name, brief description, reason rejected]

## Review trigger
[The condition under which this decision should be revisited:
specific metric threshold, team size, technology milestone, or date]

Write in present tense for the decision section.
Use past tense for the context (what was happening).
The review trigger must be a specific, observable condition —
not "when the situation changes."
