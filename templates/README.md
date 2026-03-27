# Domain Templates

This directory houses the 200+ domain-specific APOS prompt templates defined in Part V of *Prompt Engineering for Developers & Architects*.

## Structure
- `architecture/` - System design and macro-topologies (Ch. 19)
- `distributed-systems/` - Consistency, latency, and CAP theorems (Ch. 20)
- `event-driven/` - Messaging, streaming, and outbox patterns (Ch. 21)
- `database/` - Schema design, indexing, and data constraints (Ch. 22)
- `reliability/` - Retry policies, circuit breakers, and SLOs (Ch. 23)
- `security/` - Threat modeling and identity boundaries (Ch. 24)
- `code-review/` - PR reviews, refactoring, and static analysis triage (Ch. 25)
- `financial/` - Double-entry accounting, reconciliation, and idempotency (Ch. 28)
- `quality-testing/` - Boundary analysis and test generation (Ch. 35)

## Usage
Use the `/select-template` command to invoke the `domain-template-selector` agent, which will recommend the appropriate template for your engineering task.
