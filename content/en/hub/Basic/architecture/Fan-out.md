---
title: Fan-out
weight: 109
---


Fan-out is a pattern where a message from a source is spread or copied to one or more destinations. In data engineering, fan-out is commonly used to send data from a microservice (publisher) to multiple subscribers. The fan-out service normally doesn't save the message once it has been sent, so a message queue is also common to see between the fan-out service and the subscriber for catch-up/re-try scenarios.

```mermaid
%%{init: { "flowchart": { "useMaxWidth": true } } }%%
graph LR

A[Publisher] -->|Message 1| B(Fan-out service)
B -->|Message 1| C[Subscriber 1]
B -->|Message 1| D[Subscriber 2]
B -->|Message 1| E[Subscriber 3]
```

## Fan-out Advantages

- Send data from one source to many destinations

## Fan-out Disadvantages

- Usually limited re-try capabilities if a subscriber is unavailable for an extended period

