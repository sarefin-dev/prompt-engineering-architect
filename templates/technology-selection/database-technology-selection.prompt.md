Act as a Staff Database Architect specializing in large-scale systems.

System context:
[REQUIRED: What data the database will store and how it will be accessed]

Requirements:
[REQUIRED: Consistency model required — ACID / eventual]
[REQUIRED: Query patterns — transactional, analytical, time-series, search, graph]
[REQUIRED: Scale — writes/second, data volume, growth rate]
[REQUIRED: Operational constraints — team expertise, managed vs. self-hosted, cloud]
[REQUIRED: Compliance — data residency, encryption at rest requirements]

Options to evaluate:
[REQUIRED: 2-4 database technologies appropriate for the use case]

Task:
Evaluate the database options against the stated requirements.

For each option:
1. Data model fit: does the data model match the database's strengths?
2. Consistency: what consistency model does it provide by default?
   Can stronger consistency be configured, and at what cost?
3. Query capability: does it support the stated query patterns efficiently?
4. Scalability path: what is the scaling approach at 10x current data volume?
5. Operational maturity: what expertise is required to operate it reliably?
6. Ecosystem: drivers, ORMs, monitoring integrations, backup tooling

Output:
Tabulate the evaluation per option across all six dimensions.
Eliminate options that cannot satisfy the consistency or compliance requirements.
Provide the recommendation with the specific configuration required
to meet the consistency and durability requirements.
State the indexing strategy required to support the stated query patterns
for the recommended option.
Explicitly state the scaling ceiling of the recommended option and
the architectural change required when it is reached.
Do not recommend a NoSQL database for use cases where ACID transactions
are required without a detailed justification.
