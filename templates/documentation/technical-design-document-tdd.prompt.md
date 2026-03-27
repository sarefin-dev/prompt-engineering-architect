Act as a Staff Software Architect writing a technical design document.

Document audience:
[REQUIRED: Who will read this — engineers, tech leads, architects, product managers]

Design context:
[REQUIRED: What is being built — feature, system, or component]
[REQUIRED: Why it is being built — business driver or technical need]
[REQUIRED: Constraints — timeline, technology stack, team size]

Technical decisions made:
[REQUIRED: The major architectural and design decisions]

Alternatives considered:
[REQUIRED: What was evaluated and why it was not chosen]

Task:
Write a complete Technical Design Document for the stated design.

Structure the document as follows:

## Overview
[2-3 paragraphs: what this is, why it exists, and what it changes]

## Background and motivation
[The problem being solved — specific enough that a new engineer
 understands why this design exists and what it replaces]

## Goals and non-goals
[Goals: what this design must achieve — measurable where possible]
[Non-goals: what is explicitly out of scope — prevents scope creep]

## Design
[The proposed solution — component structure, data flow, key algorithms]
[Use numbered lists for sequential flows; tables for component responsibilities]
[Data model: schema or data structure definitions]
[API design: endpoint definitions, request/response shapes]

## Alternatives considered
[For each alternative: what it is, why it was evaluated, why it was rejected]

## Implementation plan
[Phased approach: what is built in each phase]
[Dependencies: what must be true before each phase can begin]

## Testing strategy
[Unit tests, integration tests, load tests — one paragraph each]

## Operational considerations
[Deployment approach, monitoring, alerting, rollback procedure]

## Open questions
[Questions that must be answered before implementation begins]

Output:
Write the complete TDD in the structure above.
Use clear, direct prose — no passive voice, no hedging.
Diagrams should be described in text (e.g., "Component A sends event X to Component B")
  rather than placeholder [diagram here] notes.
The Goals section must contain measurable success criteria.
The Open Questions section must be populated — every design has uncertainties.
Do not write marketing language — describe what the system does, not how innovative it is.
Do not leave any section empty — if a section has nothing to say, state why.
