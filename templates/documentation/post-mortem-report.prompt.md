Act as a Staff Site Reliability Engineer writing a post-mortem report.

Incident context:
[REQUIRED: What failed — system, service, or process]
[REQUIRED: When it started, when it was detected, when it was resolved]
[REQUIRED: User impact — what users experienced and for how long]
[REQUIRED: Timeline of events during the incident]
[REQUIRED: Root cause or contributing factors as currently understood]
[REQUIRED: Actions taken during the incident]

Task:
Write a blameless post-mortem report.

Structure the report as:

## Incident summary
[3-4 sentences: what happened, when, user impact, duration]

## Timeline
[Chronological events — detection, investigation steps, actions taken, resolution]
[Use the format: [HH:MM UTC] — [Event or action]]

## Root cause analysis
[The sequence of conditions that led to the incident]
[Use the "five whys" structure: Why did X fail? Because Y. Why did Y happen? Because Z...]
[Stop when the root cause is something the team can act on]

## Contributing factors
[Conditions that made the incident worse or harder to detect —
 these are not the root cause but are addressable]

## Detection
[How was the incident detected? Was this via monitoring, user reports, or internal discovery?]
[Was the detection time acceptable? If not, what was the detection gap?]

## Resolution
[What actions resolved the incident?]
[Could resolution have been faster? What delayed it?]

## Action items
[Specific, assigned, time-bound improvements that prevent recurrence]
[Format: [Action] — [Owner] — [Due date]]

## Lessons learned
[What went well during the incident response?]
[What should be improved?]

Output:
Write the complete post-mortem in the structure above.
The report must be blameless — individuals are never named as causes.
System and process failures are named; people are not.
The Root cause analysis must go beyond the proximate cause
(the service failed) to the systemic cause (the monitoring gap that
allowed the failure to be invisible).
Every action item must have an owner and a due date — unowned action
items are never completed.
The Timeline must be specific — "approximately 14:30" is not acceptable
if the exact time is available in logs.
Do not include speculation about what caused the incident in the
Root cause section — only state what is confirmed.
