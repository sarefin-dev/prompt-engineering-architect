Act as a Senior Software Engineer doing test-driven development.

[REQUIRED: Paste the proposed Polling Publisher Spring Boot component snippet]

Task: We need to write unit tests for the polling publisher before deploying.

Reason through the behavior space before writing the tests:
1. Happy path: Poller finds records, publishes them, and marks them as published.
2. Boundaries: What happens if it finds exactly `batch_size` records? What if it finds 0?
3. Error: What happens if Kafka is down and the publish throws an exception? Does it roll back the transaction so the record is picked up next time?

Output:
Write the test suite using JUnit 5 and Mockito. Name each test using the `[unit]_[condition]_[expected_outcome]` convention.
Do not write tests that require the real PostgreSQL database; mock the JPA repository and KafkaTemplate.
Avoid generic setup methods. Only set up the mocks required for the specific test assertion.
