Act as a Senior Engineer writing onboarding documentation for a new team member.

System context:
[REQUIRED: The system the new engineer will work on]
[REQUIRED: The role — frontend, backend, full-stack, SRE, data engineer]
[REQUIRED: The team's tech stack and development workflow]

Onboarding goal:
[REQUIRED: What should the new engineer be able to do independently
  after completing the onboarding? Be specific.]

Task:
Write a structured onboarding guide.

Structure the guide as:

## Day 1: Environment setup
[Step-by-step setup instructions — specific commands, not "install dependencies"]
[What to do if setup fails — common issues and their fixes]
[Verification: how to confirm the setup is working]

## Week 1: System orientation
[Architecture overview — what exists and how it fits together]
[Key concepts the engineer must understand to be productive]
[Where to find things: codebase structure, documentation, runbooks]
[Who to ask for what — not a name, but a role and responsibility]

## Week 2: First contribution
[A defined first task that is realistic and builds familiarity]
[The development workflow: branch, test, review, deploy]
[The code review standards that apply to this team]

## Reference
[Common commands the engineer will use every day]
[Glossary of team-specific terminology and acronyms]
[Links to: architecture documentation, runbooks, alerting, deployment pipeline]

Output:
Write the complete onboarding guide in the structure above.
Every setup step must include the exact command — not "configure your database."
The Day 1 section must include troubleshooting for the two most common
setup failures.
The Reference section must be genuinely useful — the commands an engineer
runs every day, not a link dump.
Do not assume the reader knows the team's specific tools and workflows —
explain them.
Do not write "ask your manager" as a resolution for anything — name the
specific resource, document, or role the question should go to.
