## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**: **\*\***\_\_\_**\*\***
**Branch**: `module-01/Kelyan`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

> _Your answer:_

---Looking at it from the developer's side, the monolith was a trap. Touching the game catalogue meant
being in the same codebase as the login system, the activity tracker, and the notification sender.
A single bad line in an unrelated feature could take the whole thing down on deploy. With separate
services, that risk is contained. If something breaks in game-service, it breaks there and nowhere
else. The person working on it can understand the whole thing in one sitting, write tests without
mocking half the system, and ship without waiting for three other teams to sign off.


## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

> _Your answer:_
The boundary I feel strongest about is between activity-service and logging-service.

On the surface it seems redundant — activity-service already knows what happened, so why hand it
off to another service to write down? But these two services exist for completely different reasons
and answer to different people. activity-service is a product concern: it needs to be fast and
always on. logging-service is a legal concern: it answers to the compliance team, it has to check
GDPR consent before touching any personal data, and it needs to be the single audit trail for the
entire platform — not just gameplay, but auth events, admin actions, everything.

Merging them would mean the GDPR consent check sits inside the critical path of every game
session. Changing a data retention rule would mean redeploying the service that handles social
feeds. The product team and the legal team would be blocked on each other for every single release.
The boundary exists so each side can move without stepping on the other.

---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

> _Your answer:_

Debugging. In the monolith, one user action meant one log file and one stack trace. Something went
wrong, you found it in seconds.

In this architecture, that same action touches activity-service, logging-service, notification-service,
and auth has already handled the first half before any of them see the request. Each service has
its own logs, its own database, and its own failure states. Piecing together what actually happened
means jumping between five different outputs and hoping the timestamps line up. That is genuinely
harder, and we haven't solved it yet.

---

_Keep this file. You will refer back to it during the oral presentation._
