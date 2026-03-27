Act as a Staff Engineer translating technical analysis for executive stakeholders.

Technical content:
[REQUIRED: The technical findings, design, or decision to communicate]

Audience:
[REQUIRED: CTO, VP Engineering, CFO, or board — adjust to specific audience]

Business context:
[REQUIRED: Why this matters to the business — what decision does this inform?]

Task:
Write an executive summary of the technical content.

Apply these translation principles:
- Replace technical vocabulary with business vocabulary
  (not "p99 latency" — "9 out of 10 transactions complete in under 200ms,
   but the slowest 1% take over 2 seconds")
- State business impact in terms of users, revenue, or risk — not technical metrics
- Quantify where possible — "40% of users experienced errors" not "error rate was high"
- Lead with the conclusion — executives read the first paragraph
  and skim the rest; the recommendation must be in paragraph one

Structure the summary as:

## Situation (1 paragraph)
[What is the business context and what decision is required]

## Finding (2-3 paragraphs)
[What was assessed or discovered — in business terms]
[What it means for the business — not the technical system]

## Recommendation (1 paragraph)
[What should be done — specific, not vague]
[What it will cost — time, money, or resource commitment]
[What the risk is if nothing is done]

## Options considered (if relevant)
[2-3 alternative approaches and why the recommended option was chosen]

Output:
Write the executive summary in the structure above.
Maximum length: one page (400-500 words).
No technical jargon without a parenthetical plain-English explanation.
The Recommendation must include a specific ask — what is the executive
being asked to approve, fund, or decide?
Do not pad the summary with background context the audience already knows.
Do not soften the risk of inaction — state it clearly.
