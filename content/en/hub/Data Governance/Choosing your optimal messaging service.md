---
title: Choosing your optimal messaging service
weight: 3
---

## Overview

A short guide on choosing which messaging service(s) to use.

## AWS

```mermaid
%%{init: { "flowchart": { "useMaxWidth": true } } }%%
graph TD

A((Start)) --> B{Fan-out}

B -->|Yes| C{Rate limit}
C -->|Yes| D[SNS + SQS]
C -->|No| E[SNS]

B -->|No| F{Rate limit}
F -->|Yes| G[SQS]
F -->|No| H[Lambda Direct Invoke]

class B internal-link;
```

Source: [AWS re:Invent 2020: Scalable serverless event-driven architectures with SNS, SQS & Lambda](https://www.youtube.com/watch?v=8zysQqxgj0I&t=1887s)

## Azure

#placeholder/description 

## GCP

#placeholder/description 

