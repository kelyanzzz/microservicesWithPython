Module 5 — Reflection

Team name: kelyan
Branch: module-05/kelyan
Submitted: before Module 6 lesson

1. The "why"

SQLite holds the full, accurate game record — it's the write model. Redis only holds a stripped-down summary built for fast lookups — it's the read model. Keeping both means each one gets used for what it's actually good at: SQLite for correctness, Redis for high-traffic reads.

If every read had to go through SQLite, that load would only get worse as traffic grows. Pulling a small cached version from Redis instead is faster and takes pressure off the database.

2. Your choice

The consent check means our logs will never be complete on purpose. A user's activity can exist fine in activity-service, but if they haven't opted in, logging-service has to refuse to store it.

I'd put that check inside logging-service itself, not the gateway or activity-service. logging-service owns the consent data and the log storage, so it should be the one deciding what gets recorded. If that decision lived anywhere else, some other producer down the line could bypass it entirely and consent would stop meaning anything.

3. The tradeoff

The drift between SQLite and Redis only becomes a problem when the stale data changes what the user actually believes or decides.

It's fine when the data isn't critical and a short delay doesn't hurt anyone. But there are systems where that's never acceptable — banking, payments, medical records, anything tied to legal consent — because being wrong there isn't just a minor inconvenience.