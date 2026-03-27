Act as a Staff Architect specializing in financial risk management systems.

System context:
[REQUIRED: The business activity generating risk — trading, lending, payments]
[REQUIRED: Risk types — market risk, credit risk, operational risk, liquidity risk]
[REQUIRED: Current risk controls, if any]
[REQUIRED: Regulatory risk requirements — Basel III, FRTB, or domain-specific]

Task:
Design a risk control framework for the stated system.

Address the control layers:

1. Pre-trade / pre-transaction controls (preventive):
   What checks must pass before a transaction is executed?
   - Credit limit checks: does the counterparty have available credit?
   - Position limit checks: does this trade exceed position limits?
   - Market risk checks: does this trade exceed VaR or sensitivity limits?
   - Velocity checks: are too many transactions occurring in too short a window?
   How are these checks implemented to minimize latency impact?

2. Real-time monitoring (detective):
   What conditions are monitored in real time after transaction execution?
   How quickly must a breach be detected?

3. Post-transaction controls (corrective):
   What happens when a limit is breached?
   - Automatic halt: block further transactions until limit is remediated
   - Alert: notify risk management for manual review
   - Force-close: automatically reduce position to within limits

4. Limit management:
   Who can set and change limits? What authorization is required?
   Are limit changes audited?

5. Exception handling:
   What is the procedure for limit override (emergency trading)?
   How are overrides logged and reported?

Output:
Design the risk control framework covering all five layers.
For each check type: state the data required, the latency budget,
and the failure behavior (fail open vs. fail closed).
Enumerate the scenarios where pre-trade controls could be bypassed —
these are operational risk gaps.
State the limit management authorization model — who can set what limits,
with what approval workflow.
Define the breach reporting obligation: when must a breach be reported
to regulators and by what deadline?
Do not design pre-trade controls that add more than 1ms latency
without explicit business justification — high-frequency trading systems
have strict latency requirements.
