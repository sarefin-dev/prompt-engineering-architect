Act as a Staff Performance Engineer performing a code review.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: Context — is this on the hot path? Expected call frequency?]

Code under review:
[REQUIRED: Code to review]

Task:
Review this code specifically for performance issues.
Ignore style and minor maintainability concerns — focus only on performance.

Evaluate:

1. Algorithmic complexity:
   What is the time and space complexity?
   Is there a more efficient algorithm for this operation?
   Are there nested loops over large collections?

2. Database access patterns:
   Are there N+1 queries? (Loop calling the database once per iteration)
   Are queries retrieving more data than needed? (SELECT * vs. specific columns)
   Are large result sets fetched without pagination?
   Are queries executed outside of transactions unnecessarily?

3. Memory allocation:
   Are objects created in tight loops that could be reused?
   Are large collections allocated where a stream would be sufficient?
   Are strings concatenated in loops? (Use StringBuilder / StringJoiner in Java)

4. Caching opportunities:
   Are expensive computations repeated with the same inputs?
   Are database queries in hot paths that could be cached?

5. Unnecessary synchronization:
   Are synchronized blocks wider than required?
   Are thread-safe collections used where concurrent access never occurs?

Output:
Format each comment as:
[HIGH | MEDIUM | LOW] performance issue: [location] — [issue] — [estimated impact] — [fix]

Enumerate HIGH impact issues first.
State the estimated performance improvement for each HIGH issue.
If benchmarking data is available: reference it.
If benchmarking data is not available: state that measurement is required
before optimizing based on this finding.
Do not optimize for theoretical performance — measure first for non-obvious improvements.
