Act as a Staff Software Architect familiar with the C4 model.

Architecture description:
[REQUIRED: Prose or structured description of the system]

Review level:
[REQUIRED: Context | Container | Component | Code — specify which level(s)]

Task:
Evaluate the [stated level(s)] of the architecture using C4 model principles.

For the Context level:
- Identify all external users and systems
- Evaluate whether all system interactions are captured
- Identify missing actors or external dependencies

For the Container level:
- Evaluate container (service/database/browser) boundary definitions
- Assess communication protocols between containers
- Identify container responsibilities that overlap or are missing

For the Component level:
- Evaluate component cohesion within each container
- Assess component dependencies for circular dependency risks
- Identify components that should be extracted or merged

Output:
Structure the review by C4 level.
For each element at the reviewed level: name, responsibility assessment,
and any identified issue.
Enumerate missing elements — actors, containers, components, or
relationships not captured in the description.
Identify the three most significant gaps for the stated level.
Do not review levels not specified in the review scope.
