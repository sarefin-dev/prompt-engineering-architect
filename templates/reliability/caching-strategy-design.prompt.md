Act as a Staff Performance Engineer.

System context:
[REQUIRED: System with identified read-heavy operations]
[REQUIRED: Data characteristics — read/write ratio, data size, staleness tolerance]
[REQUIRED: Current caching state]

Task:
Design a caching strategy for the stated system.

Address the caching decisions:

1. Cache placement: where does the cache sit in the request path?
   - Client-side: in the calling service's memory
   - Distributed: Redis, Memcached — shared across service instances
   - CDN/edge: for static or semi-static content
   - Database query cache: materialized views or query results

2. Cache-aside vs. write-through vs. write-behind:
   - Cache-aside: application manages cache explicitly (most flexible)
   - Write-through: writes go to cache and database atomically (consistent)
   - Write-behind: writes go to cache, database updated asynchronously (fastest writes)
   Assess which pattern fits the data's write frequency and consistency requirements.

3. Eviction policy: LRU, LFU, or TTL-based?
   - LRU: most recently used items stay; appropriate for temporal access patterns
   - LFU: most frequently accessed items stay; appropriate for stable hot sets
   - TTL: items expire after a fixed duration; appropriate for time-sensitive data

4. Cache invalidation: how is the cache kept consistent with the database?
   - TTL expiry: simple but accepts staleness
   - Event-driven invalidation: subscribe to change events and invalidate on write
   - Write-through: always consistent but adds write latency

5. Cache stampede prevention: what happens when a cached item expires
   and many requests simultaneously hit the database?

Output:
Recommend the caching architecture with specific technology and configuration.
For each cache tier: specify the eviction policy, TTL, maximum size, and
invalidation strategy.
State the expected cache hit rate and its latency impact.
Design the cache stampede prevention: probabilistic early expiration,
mutex/lock-based refresh, or background refresh.
Enumerate the data categories that should NOT be cached:
user-specific data without per-user cache keys, highly volatile data
where staleness is unacceptable, large objects that evict useful small objects.
