Act as a Staff Performance Engineer.

System context:
[REQUIRED: System to be load tested]
[REQUIRED: SLOs — latency targets, throughput targets, error rate limits]
[REQUIRED: Expected load profile — normal, peak, and burst]

Task:
Design a load testing strategy for the stated system.

Address the four load test types:

1. Baseline test: verify normal operation under expected load
   - Duration: 30–60 minutes at normal throughput
   - Success criteria: all SLOs met, no degradation over time

2. Stress test: identify the breaking point
   - Ramp load from 100% to 500% of normal throughput
   - Success criteria: identify the load at which SLOs are first violated

3. Spike test: verify burst handling
   - Apply the stated burst load for the stated burst duration
   - Success criteria: system recovers to normal latency within N minutes

4. Soak test: verify stability under sustained load
   - Run at 80% of the stress test limit for 24 hours
   - Success criteria: no memory leaks, no degradation over time

For each test type:
- Define the workload: what API endpoints, in what ratio, with what data
- Define the success criteria: specific SLO thresholds
- Define the failure investigation procedure: what metrics to examine if criteria fail

Output:
Provide the load test design for all four types.
Specify the load testing tool (k6, Gatling, Locust) with rationale.
Define the monitoring dashboard required during testing:
   which metrics to watch in real time.
Enumerate the components to monitor for saturation during the stress test.
State the data requirements: does the test need production-volume data?
If so, how is it provisioned without using real user data?
Define the environment: can this test run in staging, or must it run in
a production-like environment with production-scale infrastructure?
