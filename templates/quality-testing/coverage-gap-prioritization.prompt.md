Act as a Staff QA Engineer prioritizing test coverage gaps for a production service.

Technology context:
[REQUIRED: Language and coverage tool — e.g., Python/coverage.py, Java/JaCoCo,
           TypeScript/Istanbul]
[REQUIRED: Coverage report output — paste the summary and file-level breakdown]
[REQUIRED: Service context — what does this service do in production?
           What is the consequence of an undetected defect?]

Current coverage: [REQUIRED: Overall coverage %, and per-module breakdown]
Coverage target: [REQUIRED: The team's coverage target, or state "no target defined"]

Task:
Diagnose the coverage gaps that represent the highest production failure risk.
Coverage percentage is not the goal — covering the right behaviors is.

Reason through risk before identifying gaps:

1. Map modules to production criticality:
   Which modules handle money, security, data integrity, or user-facing
   correctness? These are HIGH criticality.
   Which modules handle configuration, logging, or internal utilities?
   These are LOW criticality.
   State the criticality of each module before evaluating its coverage.

2. Classify uncovered code by type:
   BUSINESS LOGIC: uncovered calculation, validation, or decision code.
     This is the highest risk — incorrect business logic produces wrong results.
   ERROR HANDLING: uncovered exception handlers or fallback paths.
     This is high risk — unhandled errors cause production incidents.
   INFRASTRUCTURE GLUE: uncovered serialization, configuration, framework boilerplate.
     This is medium risk — usually fails loudly rather than silently.
   DEAD CODE: uncovered code that is unreachable.
     This is not a coverage gap — it is a dead code finding (see Template 9).

3. Prioritize by risk × criticality:
   A HIGH criticality module with 40% coverage in BUSINESS LOGIC is
   more urgent than a LOW criticality module with 10% coverage in INFRASTRUCTURE GLUE.

Output:
State the priority order of coverage gaps — not sorted by percentage, sorted by risk.
For each gap:
  Module: [name and current coverage %]
  Criticality: [HIGH | MEDIUM | LOW]
  Uncovered behavior type: [BUSINESS LOGIC | ERROR HANDLING | INFRASTRUCTURE GLUE | DEAD CODE]
  Production failure mode: [what fails in production if this behavior is wrong
                             and not caught by a test]
  Test required: [description of the specific test that closes this gap —
                  not a test file name, a behavior description]
  Estimated test count: [how many tests to cover this gap adequately]

Do not recommend increasing overall coverage % as an objective.
Recommend covering specific high-risk behaviors.
State explicitly which uncovered code is acceptable to leave uncovered and why.
