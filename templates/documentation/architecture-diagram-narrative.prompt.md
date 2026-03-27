Act as a Staff Architect writing a narrative description of an architecture diagram.

Architecture to describe:
[REQUIRED: The components, their relationships, and the data flows]
[REQUIRED: The intended audience for the description]

Purpose:
[REQUIRED: Will this accompany a diagram, replace one, or describe one for documentation?]

Task:
Write a structured narrative that describes the architecture clearly.

Apply these description principles:
- Describe function before structure — what does the system do before how it is built
- Describe data flow as active sequences — not "data is stored" but
  "the Order Service writes the order to PostgreSQL and publishes an order.created event"
- Name every component on first mention with its role in parentheses
  — "the API Gateway (the single entry point for all client requests)"
- Use consistent naming — do not alternate between "the service" and
  "the Order processor" for the same component

Structure:
## System purpose
[What the system does — one paragraph, no jargon]

## Component overview
[Brief description of each major component and its responsibility]

## Request flow (primary path)
[Step-by-step narrative of a typical request through the system]

## Data flow
[Where data originates, where it is stored, and how it moves between components]

## Failure behavior
[What happens when each major component fails — briefly]

Output:
Write the architecture narrative in the structure above.
Every component must be introduced with its role before its implementation.
The Request flow must use numbered steps — not prose.
Avoid passive voice in the data flow — components act on data,
they do not have things happen to them.
Do not include implementation details (library versions, configuration parameters)
unless they are architecturally significant.
