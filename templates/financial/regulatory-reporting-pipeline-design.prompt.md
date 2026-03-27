Act as a Staff Distributed Systems Architect specializing in financial reporting.

System context:
[REQUIRED: The regulatory reporting requirement — what report, to whom, how often]
[REQUIRED: Source data systems — where the data originates]
[REQUIRED: Report format requirements — schema, validation rules]
[REQUIRED: Submission deadline and late submission consequences]

Task:
Design a regulatory reporting pipeline that satisfies the stated requirements.

Address:
1. Data sourcing:
   Where does each data element in the report come from?
   What is the data lineage — from source system to report field?
   Are source systems the authoritative record, or are there intermediate stores?

2. Data quality:
   What validation rules apply to each report field?
   How are validation failures detected and resolved before submission?
   What is the reject-and-fix procedure for invalid records?

3. Report generation:
   Is the report generated from a live system (risky — queries contend with
   production writes) or from a reporting copy (preferred)?
   What is the reporting window (T+0, T+1, T+2)?

4. Reconciliation:
   Before submission, how is the report reconciled with the source systems?
   What are the break tolerances — at what discrepancy level is manual
   review required?

5. Submission and confirmation:
   How is the report submitted to the regulator?
   How is submission confirmation received and stored?
   What is the re-submission procedure if the initial submission is rejected?

6. Auditability of the report itself:
   The report generation process must be auditable — the system must be
   able to reproduce any previously submitted report.
   How is the input data snapshot preserved for reproductibility?

Output:
Design the reporting pipeline covering all six areas.
Provide the data lineage map: for each report field, trace the source
system, transformation logic, and validation rule.
State the reconciliation procedure as a runbook.
Define the pipeline SLA: what is the minimum time required to generate
and validate the report before the submission deadline?
Enumerate the failure scenarios and their recovery procedures:
  source system unavailable, validation failures, submission rejected.
Do not design a pipeline where the report cannot be reproduced
after submission — regulators may request historical report reproduction.
