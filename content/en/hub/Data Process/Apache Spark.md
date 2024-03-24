---
title: Apache Spark
weight: 71
---

![[Assets/apache_spark_logo.png|100]]

[Apache Spark](https://spark.apache.org/) is a data processing engine used in Data Engineering primarily for large scale data processing.

## Official Documentation

https://spark.apache.org/docs/latest/

## Apache Spark Advantages

- High speed data querying, analysis, and transformation with large data sets
- Easy to use APIs
- Support for multiple programming languages

## Apache Spark Disadvantages

- Spark lacks a native storage option
- Wrong usage of RDD partitions on Spark Context can cause negative effects over HDFS and MemoryOverhead driver

## Apache Spark storage

Apache Spark is compatible with Hadoop APIs, like HDFS. Spark also works with other storage services such as NoSQL databases, ElasticSearch and Amazon S3.

## Apache Spark model

Apache Spark's programming model is based on **parallel operators**. This is Spark's main advantage and feature, which let us use a Leader-Follower strategy to tackle data.

Spark describes tasks based on a DAG (**Directed Acyclic Graphs**), it gives programmers the option of developing complex pipelines. To understand what DAG does, we must focus on its name:

- *Directed*: stands for a one way process
- *Acyclic*: means that there are no loops on the tasks
- *Graph*: is a reference on how they can be displayed as an actual graph

A DAG system is also fault-tolerant.

## Apache Spark RDDs

RDDs (**Resilient Distributed Datasets**) are the main Spark abstraction. They consist of element sets that are fault tolerance and able to be parallel processed. RDDs also provide scalability due to being distributed processes as well as being immutable. 

RDDs emit two kind of operations: **transformations** (such as filter, map...) and **actions** (such as reduce, collect...). Spark RDDs tend to perform lazy evaluation, which improves efficiency by executing operations only when they are needed.

## Apache Spark Learning Resources

<iframe class="airtable-embed" src="https://airtable.com/embed/shrTqJieLqrOr9xSv?backgroundColor=blue&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

## [Apache Spark Recent Posts](https://www.reddit.com/r/dataengineering/search/?q=Apache%20Spark&restrict_sr=1&sr_nsfw=)

