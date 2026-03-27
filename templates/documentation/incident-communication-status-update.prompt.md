Act as a Senior Engineer writing an incident status communication.

Incident details:
[REQUIRED: What is affected — specific service or feature]
[REQUIRED: Current status — investigating, identified, monitoring, resolved]
[REQUIRED: User impact — what users are experiencing]
[REQUIRED: Time of initial detection]
[REQUIRED: Known cause, if identified]
[REQUIRED: Current mitigation or resolution actions in progress]
[REQUIRED: Estimated time to resolution, if known]

Audience:
[REQUIRED: Internal (engineering team) or external (customers, status page)]

Task:
Write a clear, factual incident status update.

For internal audience:
- Include technical detail sufficient for the engineering team to act
- Include the current hypothesis and investigation steps
- Include what help is needed, if any

For external/customer audience:
- Use plain language — no technical jargon
- State what users experience, not what is technically wrong
- State what is being done, not the internal investigation detail
- Do not speculate about root cause
- Do not promise a specific resolution time unless it is certain

Format:
[STATUS]: [Investigating | Identified | Monitoring | Resolved]
[TIME]: [Current time UTC]
[AFFECTED]: [What service or feature]
[IMPACT]: [What users experience]
[UPDATE]: [What is known and what is being done]
[NEXT UPDATE]: [When the next update will be provided]

Output:
Write the status update in the format above.
Be factual — do not speculate about cause or impact beyond what is confirmed.
Be specific about impact — "some users may experience errors" is not
specific enough. "Users attempting to checkout may receive a 500 error" is.
Do not use passive voice to obscure accountability —
"the service is degraded" not "we may have inadvertently caused some issues."
For external updates: do not include internal system names, error codes,
or investigation details that could be exploited.
