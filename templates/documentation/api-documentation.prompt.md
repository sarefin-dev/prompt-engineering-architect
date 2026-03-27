Act as a Senior Software Engineer writing API documentation.

API context:
[REQUIRED: API name and purpose]
[REQUIRED: Authentication method]
[REQUIRED: Base URL and versioning strategy]
[REQUIRED: List of endpoints with their purpose]

Audience:
[REQUIRED: External developers integrating against this API, or internal consumers?]

Task:
Write complete API documentation for the stated API.

For each endpoint, document:

## [HTTP Method] [Path]
**Summary:** [One sentence — what this endpoint does]
**Authentication:** [Required / not required / optional]

**Request**
Headers:
  [Header name]: [Description and whether required]

Path parameters:
  [Parameter]: [Type, description, constraints]

Query parameters:
  [Parameter]: [Type, description, default, constraints]

Request body (if applicable):
  [JSON schema or field table: field, type, required/optional, description]

**Response**
Success (HTTP [code]):
  [Response body schema]

Error responses:
  [HTTP code]: [When this occurs] — [Response body]
  [HTTP code]: [When this occurs] — [Response body]

**Example**
Request:
  [Complete curl example]
Response:
  [Complete example response body]

**Notes**
[Rate limits, idempotency behavior, retry guidance, side effects]

Output:
Document every endpoint in the structure above.
Every error response must be documented — undocumented errors are
discovered only by integration failures.
The Example section must use realistic values — not "string" and "123".
Idempotency behavior must be stated for all POST, PUT, and PATCH endpoints.
Rate limits must be stated if they exist.
Do not document only the happy path — document the constraints and
error conditions that integrators will encounter.
