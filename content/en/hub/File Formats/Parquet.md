---
title: Apache Parquet
weight: 30
---

![GitHub Repo stars](https://img.shields.io/github/stars/apache/parquet-mr?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/apache/parquet-mr) ![GitHub](https://img.shields.io/github/license/apache/parquet-mr)

Apache Parquet is an open source data file format that was designed to improve performance when handling [[Column-oriented Database|column-oriented data]] in bulk. Apache Parquet is able to provide efficient compression and encoding schemes with enhanced performance due to its design. This makes it a common interchange format for both batch and interactive workloads, similar to other available columnar-storage file formats in Hadoop like RCFile and ORC.

**Extension:** `.parquet`

## Apache Parquet Official Documentation

https://parquet.apache.org/docs/

## Apache Parquet Advantages

- Reduces IO operations.
- Column-based format makes it more efficient in terms of storage space but also speeds up analytics queries.
- Highly efficient data compression and decompression.
- Support type-specific encoding.
- Supports several data types and nested data structures.

## Apache Parquet Disadvantages

- Not human readable (binary).
- More memory required to read data vs row-based format.
- Can be slower to write than row-based file formats because of the metadata overhead.

