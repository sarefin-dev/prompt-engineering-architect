System Context: Payment Service (Level 2)

Architecture:
External Gateway → API Layer (Spring Boot) → Payment Service (Spring Boot)

Responsibilities:
The Payment Service receives authorization requests, talks to the external Stripe API, and records the outcome in our local database. It then publishes a `PaymentCompleted` message to Kafka so the Order Service can proceed.

Communication:
- Sync REST from API Layer to Payment Service
- Sync REST from Payment Service to Stripe API
- Async Kafka from Payment Service to Order Service

Data:
- PostgreSQL 15, single primary node.
- Schema not yet defined.
- We must guarantee we don't lose the record of a payment if Kafka is down, and we must guarantee we don't double-charge a customer if our service crashes mid-request.

Infrastructure:
Kubernetes. 3 Pod replicas default.
