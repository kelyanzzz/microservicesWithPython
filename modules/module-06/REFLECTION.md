# Module 6 — Reflection

Team name: kelyan
Branch: module-06/kelyan
Submitted: before Module 7 lesson

1. The "why"

Putting authentication only in the gateway means there's one front door for the whole system. The client sends its token once, the gateway checks it, and anything invalid gets stopped before it ever reaches a service. None of the services have to repeat that same check themselves.

If each service had to validate tokens on its own, we'd be duplicating the same security logic everywhere. Every new service would need that logic written again, and rotating the secret key would mean updating it in every single service instead of just one place. One door is just easier to guard than five.

2. Your choice

We didn't get to fully wire up the M2M flow, but the reasoning behind it makes sense: activity-service calling user-service internally isn't the same as a user making a request, so it shouldn't carry the user's token. A separate M2M token identifies the caller as the service itself, with its own role, rather than borrowing someone else's identity.

If services just passed user tokens around to each other instead, that token would travel further than it should, and you'd lose the ability to tell whether an action came from the user directly or from a service acting on the user's behalf internally. That distinction matters for both security and debugging, even if we didn't implement the M2M token itself this time.

3. The tradeoff

Sharing the SECRET_KEY between the gateway and auth-service is convenient, but it's also a single point of failure. Any service holding that key can verify (and theoretically forge) tokens. If it ever leaked, someone could mint a valid token claiming to be any user, including an admin.

The alternative is having the gateway call auth-service on every single request to check the token instead of verifying it locally. That removes the shared-secret risk but adds a network hop to every request, and now auth-service has to be up and fast for literally anything to work. We traded a security risk for a reliability risk.