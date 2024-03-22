---
title: Change Data Capture
weight: 116
---


Change data capture describes the process of recording the change of data in a database. Typically, this means tracking when records are inserted, updated, and deleted along with the data itself.

## Change Data Capture Advantages
- Better use of bandwidth
- Can keep historical data changes

## Change Data Capture Disadvantages
- More complex to set up than [[Full Load|full loads]] or [[Delta Load|delta loads]]
- Usually requires higher permissions to access the database transaction log.

## When to use change data capture
Change data capture is typically used to replicate data that is overwritten to another database. For example, replicating data from an operational database to a data warehouse. While the operational database may not need to store historical changes, it might be useful for analysis.

A few situations where you might use change data capture:

- Replicate changes into a [[Data Warehouse|data warehouse]] or [[Data Lake|data lake]]
- Replicate changes into [[Apache Kafka|Kafka]] (or other streaming tool) in a microservices architecture
- Upgrade a database to a higher version with minimal downtime
- Migrate data from database X to database Y with minimal downtime

## Popular Change Data Capture Tools

- [[Debezium]]
- Confluent
- [[Amazon DMS]]
- Qlik
- Striim
- Matillion Data Loader

