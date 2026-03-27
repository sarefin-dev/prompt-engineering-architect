Act as a Staff Software Engineer auditing a codebase for DRY violations.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The codebase surface to audit — paste the relevant files or modules]
[REQUIRED: The domain — what does this code do?]

Task:
Scrutinize this code for duplication. Identify violations of the
Don't Repeat Yourself principle at three levels of abstraction.

Reason through duplication at each level before reporting findings:

Level 1 — Literal duplication:
Identical or near-identical code blocks appearing in more than one location.
Near-identical means: same logic, different variable names or minor formatting.
For each instance: state both locations, the lines duplicated, and the
extraction opportunity.

Level 2 — Structural duplication:
Code that follows the same pattern with different data.
Example: three methods that each validate a different entity type using
identical validation logic with different field names.
This is a candidate for a generic validator parameterized by the entity type.
For each instance: state the pattern, all locations where it appears,
and the abstraction that would unify them.

Level 3 — Semantic duplication:
Code that solves the same problem in different ways.
Example: two different implementations of pagination, one using offset/limit
and one using cursor-based, both in the same service layer.
This is the hardest duplication to identify and the most expensive to leave.
For each instance: state what problem both solutions solve, which implementation
is the canonical one, and what migration path removes the duplicate.

Output:
Enumerate findings by duplication level and impact.
For each finding:
  Locations: [all files and line ranges containing the duplication]
  Type: [Literal | Structural | Semantic]
  Impact: [tokens of duplicated logic, number of locations, risk if one is
           updated but not the others]
  Extraction: [the proposed abstraction — method, class, utility function,
               or configuration — that eliminates the duplication]
  Test requirement: [what test must exist before the extraction to ensure
                     behavior is preserved]

Prohibit: recommending extraction that introduces a dependency cycle.
Prohibit: recommending extraction if the duplicated code is likely to diverge
  by design — duplication is not always a defect.
For each extraction marked as Structural or Semantic: state explicitly
whether the code will diverge in the future (in which case, leave it)
or converge (in which case, extract it now).
