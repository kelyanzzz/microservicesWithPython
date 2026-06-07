# Module 4 — Reflection

**Team name**: _______________
**Branch**: `module-04/<team-name>`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

> *Your answer:*activity-service gains the ability to move on immediately after saving the activity it doesn't sit waiting for notification-service to respond. Under load, this means activity-service can handle many requests without being slowed down by notification delivery. If notification-service is temporarily down, the activity still gets saved and the message just waits in the queue until it comes back up. Nothing is lost.

notification-service gains the ability to process at its own pace. Instead of receiving a flood of simultaneous HTTP calls it wasn't ready for, it picks up messages one by one from the queue. The two services are completely decoupled in time.

---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

> *Your answer:*A direct HTTP call would couple activity-service to notification-service at runtime. If notification-service is slow, activity-service waits and the user feels it. If it crashes mid-request, the message is gone no retry, no recovery. We would have to build all of that ourselves.

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent  but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

> *Your answer:*With a synchronous call you know immediately if the notification was delivered you get a 200 or an error. With async, you only know the message reached the broker. Whether notification-service actually processed it, stored it, or failed silently activity-service has no idea.

A user would never know their notification was missed unless they noticed its absence. As a developer, you would have to actively check — looking at notification-service logs, checking the RabbitMQ dead-letter queue, or building a separate monitoring system. What you lose going async is visibility by default. Errors become silent unless you build something specifically to surface them.

---

*Keep this file. You will refer back to it during the oral presentation.*