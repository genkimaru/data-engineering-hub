---
title: Amazon DMS
weight: 36
---

[Amazon Database Migration Service](https://aws.amazon.com/dms/) (DMS) is a tool used to replicate data from a source database and a supported destination (e.g. PostgreSQL, S3, Kinesis, etc.). It is marketed as a way to migrate on-prem databases to a database in the cloud but is also often used to perform ongoing [[Change Data Capture|change data capture]].

## Amazon DMS Official Documentation

https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html

## Amazon DMS Advantages

- Simple to use
- Supports several data sources and destinations
- Migrate data with minimal downtime
- Cost effective

## Amazon DMS Disadvantages

- A replication instance can't be scaled up or down
- A replication instance can't be stopped, only deleted
- Each source and destination have their own specific limitations (see docs)

## [Amazon DMS Recent Posts](https://www.reddit.com/r/dataengineering/search/?q=AWS%20DMS&restrict_sr=1&sr_nsfw=)

