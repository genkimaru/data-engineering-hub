---
title: Document Database
weight: 128
---

A document database is a type of [[Non-relational Database|NoSQL]] database that is designed to store and query data as JSON-like documents. Document databases make it easier to store an query data in a way that can evolve with an application's needs. The document model works well with use cases such as catalogs, user profiles, and content management systems where each document is unique and evolves over time.

![[document_database_example.png]]
*"Document data stores" by Microsoft.com*

## Popular Document Databases

[[MongoDB]]
[[Couchbase]]
[[Amazon DynamoDB]]
[[RavenDB]]
[Azure Cosmos DB](https://azure.microsoft.com/services/cosmos-db/)

## Document Database Advantages

- Create documents without needing to define their structure upfront.
- Add new fields to the database without changing the fields of existing documents.
- Can scale horizontally very easily.

## Document Database Disadvantages

- Query performance can be less efficient compared to a [[Relational Database]] because the data isn't necessarily structured or organized for queries.
- Generally requires more technical knowledge to query which means usage is typically limited to technical staff vs other non-technical business people.
- Updating data can be a slow process because the data can be distributed between machines and can be duplicated.
- Atomic transactions are not inherently supported.

## When to use a Document Database

- Storing article content, social media posts, sensor data, and other unstructured data.
- You need to develop and iterate rapidly when building a product.

## Document Database Use Cases

- Content management
- Catalogs. For example, in an e-commerce application, storing different products with different attributes.

