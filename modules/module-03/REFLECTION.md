# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*Before the gateway, if I wanted to call the user service I had to know it was on port 8001, and for games port 8002, etc. That's fine when it's just me locally, but imagine a frontend app hardcoding 5 different ports and addresses. The moment you move a service or scale it to a different machine, everything breaks.






---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*This one actually made me think. Both validate_user and fetch_game are calls to other services, but they behave completely differently and that's on purpose.

validate_user blocks everything — if the user doesn't exist, we stop immediately and return 404. There's no point saving an activity for a user that doesn't exist, the data would be meaningless.

fetch_game is the opposite if game-service is down, we just set game to null and carry on. The activity still gets saved. We tested this by stopping game-service mid-test and it worked exactly as expected. The risk of blocking on fetch_game would be that a game-service outage kills activity recording for everyone, which makes no sense since the two things are not related.
---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*
In a monolith, calling three functions takes microseconds. Here, each service call is a network request. If user-service takes 1 second and game-service takes 1 second, the user is already waiting 2 seconds just for enrichment. And if one service in the chain goes down completely, you have to handle it or the whole request fails.

We saw this live today four terminals, four services, and keeping track of which one crashed was already annoying. In production with 10+ services this becomes a real problem. That's probably why observability and resilience are the last two modules.

---

*Keep this file. You will refer back to it during the oral presentation.*
