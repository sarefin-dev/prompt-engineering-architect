Act as a Senior Software Engineer specializing in concurrent programming.

Technology context:
[REQUIRED: Language — Java, Go, Python, etc.]
[REQUIRED: Concurrency model — threads, async, goroutines, etc.]

Code under review:
[REQUIRED: Code with concurrent access patterns]

Task:
Review this code specifically for concurrency safety issues.

Evaluate:

1. Race conditions:
   Is any shared mutable state accessed from multiple threads without
   proper synchronization?
   Are there compound check-then-act operations that should be atomic?
   (if (map.containsKey(k)) { map.get(k).update(); } — not atomic)

2. Deadlocks:
   Are there multiple locks acquired in different orders across code paths?
   Are there blocking calls made while holding a lock?

3. Thread safety of data structures:
   Are non-thread-safe collections (ArrayList, HashMap) shared across threads?
   Are thread-safe collections used where atomic operations are required?
   (A ConcurrentHashMap.get() followed by put() is not atomic)

4. Visibility:
   Are shared variables declared volatile where visibility across threads
   is required without synchronization?
   Are there memory visibility issues with final fields published through
   improperly synchronized constructors?

5. Executor and thread pool management:
   Are thread pools bounded? Unbounded thread pools can exhaust memory.
   Are tasks submitted to executors handled for exceptions?
   (Uncaught exceptions in executor tasks are silently swallowed)

Output:
Format each comment as:
[BLOCKING | SUGGESTION]: [location] — [concurrency issue] — [failure scenario] — [fix]

For every BLOCKING comment: describe the specific failure scenario —
what sequence of events produces the bug? Race conditions are not obvious
from code alone; demonstrate the interleaving that causes the failure.
Do not flag immutable objects as concurrency issues — immutability
is inherently thread-safe.
Do not flag local variables as concurrency issues — only shared state
requires synchronization.
