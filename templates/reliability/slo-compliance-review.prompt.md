Act as a Staff Site Reliability Engineer.

System context:
[REQUIRED: System SLO definitions]
[REQUIRED: Current error budget consumption — this month, last month]
[REQUIRED: Recent incidents and their impact on error budget]

Task:
Perform an SLO compliance review.

Address:
1. Current compliance: is the system within its error budget?
   How many minutes of allowed downtime remain this period?

2. Burn rate analysis: at the current burn rate, will the error budget be
   exhausted before the end of the period? When?

3. Error budget allocation: which incidents consumed the most error budget?
   Are the same root causes recurring?

4. Reliability investment decision: given the error budget consumption,
   should the team pause feature development to invest in reliability?
   (Google SRE principle: if error budget is exhausted, halt features
   until reliability is restored)

5. SLO calibration: are the SLOs set correctly?
   An SLO that is never at risk may be too lenient.
   An SLO that is always nearly exhausted may be too strict.

Output:
State the current error budget status: consumed, remaining, projected exhaustion date.
Enumerate the incidents ordered by error budget impact.
Identify recurring root causes — these indicate systemic reliability gaps.
Recommend the reliability investment priority based on the error budget analysis.
State whether any SLO recalibration is warranted — and in which direction.
Do not recommend tightening an SLO without evidence that the current SLO
is too lenient for the user impact it is intended to measure.
