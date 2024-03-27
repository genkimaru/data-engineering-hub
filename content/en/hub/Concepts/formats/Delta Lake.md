---
title: Delta Lake
weight: 31
---

![GitHub Repo stars](https://img.shields.io/github/stars/delta-io/delta?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/delta-io/delta) ![GitHub](https://img.shields.io/github/license/delta-io/delta)

[Delta Lake](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) is an open-source storage framework that enables building a  
[Lakehouse architecture](http://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) with compute engines including Spark, PrestoDB, Flink, Trino, and Hive and APIs for Scala, Java, Rust, Ruby, and Python.

Delta Lake is essentially a metadata layer on top of Parquet.

The file layout looks like:

![[Assets/delta-lake-file-format.png|500]]

Delta Lake Official Documentation

https://docs.delta.io/latest/index.html

## Delta Lake Advantages (over plain [[Apache Parquet|Parquet]])

- ACID transactions with optimistic concurrency control.
- Efficient streaming I/O.
- Caching.
- Time travel.
- Data layout optimization, e.g. Z-ordering.
- Schema enforcement & evolution.
- UPSERT & MERGE statements.
- Audit logging.

## Delta Lake Disadvantages

- Same Parquet disadvantages.
- Maintenance processes _are_ required to maintain its performance, e.g. `OPTIMIZE`.
- There is a learning curve when using advanced features, e.g. `VACUUM`.

