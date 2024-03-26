---
title: Data Warehouse
weight: 130
---

A data warehouse is a central repository for data which will be used for reporting and analytics. Data comes into the data warehouse from [[Online Transaction Processing|transactional systems]], relational databases, or [[Data Lake|other sources]] usually on a regular cadence. Business analysts, data engineers, data scientists, and decision makers then access the data through [[Business Intelligence|business intelligence]] tools, [[SQL]] clients, and other analytics applications. Because the primary use cases for a data warehouse revolve around analytics, they typically use an [[Online Analytical Processing|OLAP]] technology for performance.

## Data Warehouse Advantages

- Consolidate data from multiple data sources into one "source of truth"
- Optimized for read access which makes generating reports faster than using a source transaction system for reporting
- Store and analyze large amounts of historical data

## Data Warehouse Disadvantages

- A significant investment of time and resources to properly build
- Not designed for ingesting data in real-time (although they can typically handle near real-time)

## When to use a Data Warehouse

Data warehouses are made for complex queries on large datasets. You should consider a data warehouse if you're looking to keep your historical data separate from current transactions for performance reasons.

## Popular Data Warehouses
- [[Tools/Databases/Amazon Redshift|Amazon Redshift]]
- [[Azure Synapse Analytics]]
- [[Google BigQuery]]
- [[Microsoft SQL Server]]
- [[Snowflake]]

## Data Warehouse Benchmarks
- 1 TB: [2020 - Redshift, Snowflake, Presto and BigQuery](https://fivetran.com/blog/warehouse-benchmark)
- 30 TB: [2019 - Redshift, Azure SQL Data Warehouse, BigQuery, Snowflake](https://gigaom.com/report/cloud-data-warehouse-performance-testing/)

![[Learning Resources#Data Warehousing Learning Resources]]

