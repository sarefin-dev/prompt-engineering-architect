Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System with current alerting gaps]
[REQUIRED: On-call structure — who is on call, what hours, what escalation path]

Task:
Design an alerting strategy that is actionable, non-noisy, and complete.

Address the alerting design principles:

1. Alert on symptoms, not causes: page on "users cannot complete checkout"
   not "database CPU is high." The former always requires action.
   The latter may resolve automatically.

2. Severity tiers:
   - P1 (page immediately): user-impacting, cannot wait until business hours
   - P2 (page during business hours): degraded but functional, growing risk
   - P3 (ticket): no current impact, monitoring trend

3. Alert fatigue prevention: an alert that fires and resolves automatically
   should not page. Define a minimum sustained duration for each alert.

4. Actionability: every P1 alert must have a runbook entry. If there is no
   documented response, the alert should not page.

5. Coverage gaps: what failure scenarios would currently produce zero alerts?

Output:
Design the alert definitions for the system.
Tabulate: Alert name | Signal | Threshold | Duration | Severity | Runbook link.
Enumerate the failure scenarios currently not covered by alerting —
the conditions that would only be detected by user reports.
Define the alert noise reduction configuration: evaluation intervals,
resolution delays, and inhibition rules (suppress low-severity alerts
when a higher-severity alert is firing for the same component).
State the on-call runbook requirement: all P1 alerts must have a runbook
before deployment to production.
Do not design alerts that fire at 100% utilization — that is too late.
Alert at 80% to provide time for remediation.
