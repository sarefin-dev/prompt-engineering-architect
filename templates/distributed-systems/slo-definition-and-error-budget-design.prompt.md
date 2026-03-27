Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System description with current reliability characteristics]

User experience requirements:
[REQUIRED: What reliability matters to users of this system]
[REQUIRED: What is the current pain — what breaks, how often, for how long]

Task:
Design the Service Level Objective framework for this system.
For each critical user journey, define:

1. SLI (Service Level Indicator): the specific metric that measures reliability
   for this journey (availability, latency, error rate, data freshness)
2. SLO (Service Level Objective): the target value that defines "reliable"
   for this SLI (e.g., 99.9% of requests complete in < 200ms)
3. Error budget: the allowed failure budget derived from the SLO
   (e.g., 0.1% of requests may exceed 200ms — at 100 req/s, that is
   8.76 hours of full outage per year, or 52.6 minutes per month)
4. Burn rate alerting: at what burn rate should an alert page?
   (e.g., 2% burn rate means the monthly budget exhausted in 2 days)

Output:
Define the SLO framework for each critical user journey.
Tabulate: Journey | SLI | SLO | Monthly error budget | Burn rate alert threshold.
State the monitoring implementation for each SLI — what metrics to collect,
from where, and how to aggregate them.
Identify SLOs where the current system cannot meet the stated target —
these define the minimum reliability improvements required.
Do not set SLO targets without error budget implications — every SLO
implies an error budget and a burn rate alerting strategy.
