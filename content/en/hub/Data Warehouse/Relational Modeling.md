---
title: Relational Modeling
weight: 122
---


Relational modeling revolves around using tables, columns, and rows to represent data. Each table denotes entities or subjects, while every row signifies individual records or instances belonging to that entity. These tables are connected via unique identifiers called foreign keys. Essentially, a foreign key is a column in a table that refers to the primary key of another table. A key component for relational modeling is [[Normalization|normalization]] (reduces data redundancy).

## Relational Modeling Advantages

- Great for transactional/operational workloads where data is constantly inserted, updated, or deleted.
- Supports complex queries and joins.
- Useful when accuracy and reliability are the most important requirements.

## Relational Modeling Disadvantages

- Analytical queries become slow at larger data scales.

