Act as a Staff Event-Driven Architecture Expert.

System context:
[REQUIRED: Pipeline description — current or proposed]

Task:
Decompose this event processing pipeline into logical stages.

For each stage:
1. Name the stage and its single responsibility
2. State the input event type and schema requirements
3. State the output event type and schema
4. Identify the processing guarantee required at this stage:
   at-least-once, exactly-once, or at-most-once
5. State whether the stage is stateless or stateful
6. Identify the scaling unit — what determines how many instances are needed

Output:
Enumerate each stage with all six properties.
Identify stages where the processing guarantee conflicts with the
implementation approach — these are correctness risks.
Identify stateful stages — these constrain horizontal scaling and require
a state management strategy.
Enumerate the event schemas at each stage boundary — these are the
inter-stage contracts that must be versioned and evolved carefully.
Flag any stage that combines multiple responsibilities — these should
be split for independent scalability and fault isolation.
