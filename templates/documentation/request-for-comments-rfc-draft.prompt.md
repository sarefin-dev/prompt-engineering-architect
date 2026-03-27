Act as a Staff Engineer drafting an RFC for a significant technical change.

Change context:
[REQUIRED: What change is being proposed]
[REQUIRED: Why it is being proposed — specific problem it solves]
[REQUIRED: Who is affected — teams, systems, users]
[REQUIRED: Rollout approach — gradual, flag-gated, or immediate]

Stakeholders:
[REQUIRED: Who needs to review and approve this RFC]

Task:
Draft an RFC that invites genuine technical feedback while making
a clear recommendation.

Structure the RFC as:

## Summary
[1-2 sentences: what is proposed and the primary benefit]

## Motivation
[The problem in specific, concrete terms — with data where available]
[What happens if nothing changes]

## Detailed design
[The proposed change — technical and complete]
[For API changes: exact before and after]
[For architectural changes: component diagram in text form]
[For process changes: before and after workflow]

## Drawbacks
[Honest assessment of the costs and risks of this proposal]
[Do not minimize — reviewers will find them anyway]

## Alternatives
[What else was considered and why this approach was chosen over the alternatives]
[At least two genuine alternatives — not strawmen]

## Unresolved questions
[What the RFC does not answer and how those questions will be resolved]
[Who needs to answer them before the RFC can be accepted]

## Implementation plan
[Sequence of steps to implement the accepted RFC]
[Rollback procedure if implementation goes wrong]

Output:
Write the complete RFC in the structure above.
The Drawbacks section must be substantive — at least three honest weaknesses.
The Alternatives section must include at least two genuine alternatives
with non-trivial trade-off discussion.
State clearly at the top whether this is a proposal seeking feedback
or a plan seeking approval — these require different reviewer actions.
Do not use RFC process to rubber-stamp a decision already made —
if the decision is already made, document it as an ADR instead.
