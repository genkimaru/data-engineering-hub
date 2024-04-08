---
title: Flink CDC 
weight: 5
---


### 什么是CDC
广义概念上，能够捕获数据变更的技术统称为 CDC（Change Data Capture）。通常我们说的 CDC 主要面向数据库的变更，是一种用于捕获数据库中数据变化的技术。


### CDC的用途
CDC 的主要应用有三个方面：

- 数据同步，通过 CDC 将数据同步到其他存储位置来进行异地灾备或备份。
- 数据分发，通过 CDC 将数据从一个数据源抽取出来后分发给下游各个业务方做数据处理和变换。
- 数据采集，使用 CDC 将源端数据库中的数据读取出来后，经过 ETL 写入数据仓库或数据湖。

### CDC的实现途径
按照实现机制，CDC 可以分为两种类型：
- 基于查询和基于日志的 CDC。基于查询的 CDC 通过定时调度离线任务的方式实现，一般为批处理模式，无法保证数据的实时性，数据一致性也会受到影响。
- 基于日志的 CDC 通过实时消费数据库里的日志变化实现，如通过连接器直接读取 MySQL 的 binlog 捕获变更。这种流处理模式可以做到低延迟，因此更好地保障了数据的实时性和一致性。


### Flink CDC和其他常见CDC技术的比较
![Flink cdc](/images/flink_cdc.avif)

在上图中，我们比较了几种常见的 CDC 方案。相比于其他方案，Flink CDC 在功能上集成了许多优势：

在实现机制方面，Flink CDC 通过直接读取数据库日志捕获数据变更，保障了数据实时性和一致性。
在同步能力方面，Flink CDC 支持全量和增量两种读取模式，并且可以做到无缝切换。
在数据连续性方面，Flink CDC 充分利用了 Apache Flink 的 checkpoint 机制，提供了断点续传功能，当作业出现故障重启后可以从中断的位置直接启动恢复。
在架构方面，Flink CDC 的分布式设计使得用户可以启动多个并发来消费源库中的数据。
在数据变换方面，Flink CDC 将从数据库中读取出来后，可以通过 DataStream、SQL 等进行各种复杂计算和数据处理。
在生态方面，Flink CDC 依托于强大的 Flink 生态和众多的 connector 种类，可以将实时数据对接至多种外部系统。


### Flink CDC 示例
``` yaml
################################################################################
# Description: Sync MySQL all tables to Doris
################################################################################
source:
  type: mysql
  hostname: localhost
  port: 3306
  username: root
  password: 123456
  tables: app_db.\.*
  server-id: 5400-5404
  server-time-zone: UTC

sink:
  type: doris
  fenodes: 127.0.0.1:8030
  username: root
  password: ""
  table.create.properties.light_schema_change: true
  table.create.properties.replication_num: 1

pipeline:
  name: Sync MySQL Database to Doris
  parallelism: 2
  ```


运行
  ```bash
   bin/flink-cdc.sh mysql-to-doris.yaml
   ```