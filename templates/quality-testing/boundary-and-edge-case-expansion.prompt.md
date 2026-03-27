Act as a Staff QA Engineer auditing a test suite for production readiness.

Technology context:
[REQUIRED: Language and test framework]
[REQUIRED: The production code under test]
[REQUIRED: The existing test suite]

Task:
Scrutinize the existing test suite for coverage gaps that represent production
failure risk. Reason through the failure modes before identifying missing tests.

Diagnose coverage gaps in this order:

1. Boundary conditions not tested:
   For each input parameter: is the boundary between valid and invalid tested?
   A boundary test that only tests valid=5 but not invalid=0 or invalid=6
   provides false confidence.

2. Error propagation not tested:
   When a dependency throws an exception: does the code handle it correctly
   or does it propagate unexpectedly? Each dependency that can fail needs
   a test for the failure path.

3. State-dependent behavior not tested:
   If the behavior differs based on prior state, each relevant state
   combination needs a test. Enumerate the state space before writing tests.

4. Concurrent access not tested:
   If the code is called from multiple threads or async contexts:
   is thread safety verified?
   An untested assumption of thread safety is a latent production defect.

5. Integration points assumed to succeed:
   Any test that stubs a dependency with a success response only is
   incomplete. Each stubbed dependency also needs a failure test.

Output:
Enumerate the coverage gaps found, ordered by production failure probability.
For each gap:
  - State what scenario is not covered
  - State what the production failure mode would be if it is not covered
  - Provide the missing test
Do not re-explain tests that already exist — only identify and fill gaps.
Quantify the coverage improvement: how many new failure modes are now covered?
