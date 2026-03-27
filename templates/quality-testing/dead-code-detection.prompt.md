Act as a Staff Software Engineer identifying dead code in a production codebase.

Technology context:
[REQUIRED: Language and framework]
[REQUIRED: The codebase to audit — paste the relevant modules or files]
[REQUIRED: Entry points — what are the public API surfaces, event handlers,
           and scheduled jobs that trigger execution?]

Task:
Identify dead code — code that cannot be reached from any entry point
under any input.

Reason through reachability before classifying code as dead:

1. Explicit dead code: methods, classes, or variables that are defined
   but never referenced. State the specific unreferenced symbol.

2. Conditionally dead code: branches that can never be entered given
   the current system constraints.
   Example: a branch checking for a feature flag that was permanently
   enabled six months ago.
   Do not classify a branch as dead without evidence — state the
   evidence (the flag state, the constant value, the constraint).

3. Superseded code: code that implements a behavior that has been
   replaced elsewhere but the old implementation was not removed.
   These are the highest-risk dead code findings — the old implementation
   may be called under error conditions that bypass the new path.

Output:
Enumerate dead code by risk level:
HIGH risk: superseded implementations that may still be reachable under
  error conditions or edge cases.
MEDIUM risk: unreferenced public symbols — may be used by external consumers
  not visible in this codebase.
LOW risk: unreferenced private symbols with no external exposure.

For each finding:
  Symbol: [name and location]
  Type: [Explicit | Conditionally dead | Superseded]
  Evidence: [why it is dead — not reachable from entry point X because Y]
  Removal safety: [safe to delete | verify with callers | requires deprecation period]

Do not classify code as dead if it is invoked reflectively, via dependency
injection, or by an external framework — state these as uncertain findings
requiring manual verification.
