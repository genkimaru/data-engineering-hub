---
title: Apache Kafka详解
weight: 1
---

Apache Kafka is an **Event Streaming** platform

Kafka结合了三个关键功能，让您可以使用经过验证的解决方案端对端实现事件流的用例：

- 发布（写入）和订阅（读取）事件流，包括不间断地将数据从其他系统导入/导出。
- 可靠地持久存储事件流，时间长短由您决定。
- 实时或回顾性地处理事件流。


Kafka的重要概念:
- Producer
- Consumer
- Topic
- Partition
- Consumer Group
- Offset
- Kafka Server
- Kafka Client
- Kafka admin
- Kafka Connect
- Kafka Stream

## Kafka为什么设置消费者组
**Kafka** 中的**消费者组**具有重要意义，让我们深入了解一下：
1. **并行处理**：消费者组允许多个消费者协同工作，同时从一个或多个主题（Topic）中消费消息。每个消费者都可以处理不同的分区（Partitions），从而实现并行处理。这对于大规模数据流的实时处理非常有用。

2. **负载均衡**：当一个主题被多个消费者订阅时，Kafka 会自动将分区分配给消费者组中的不同消费者。这确保了每个消费者都能够处理一部分分区，从而实现负载均衡。如果有新的消费者加入或离开消费者组，分区的重新分配也会自动发生。

3. **容错性**：如果某个消费者崩溃或离线，其他消费者仍然可以继续处理消息。Kafka 会将该消费者负责的分区重新分配给其他活动的消费者，从而确保消息不会丢失。

4. **消费者状态管理**：Kafka 维护每个消费者的消费进度。这意味着即使消费者组中的某个消费者离线，它重新加入时也能从上次消费的位置继续处理消息。

总之，消费者组是 Kafka 中实现高吞吐量、容错性和并行处理的关键机制之一。


## Kakfa 如何保证消息不丢失（message durability）
**Kafka** 通过多种机制来保证消息不丢失：

1. **消息复制**：Kafka 使用**副本**来确保消息的持久性。当消息被发布到**主分区（leader partition）**时，它可以配置为在**跟随分区（follower partitions）**之间同步复制。这意味着如果持有主分区的代理（broker）崩溃，副本可以接替主分区的角色，而不会丢失数据²³.

2. **消息确认机制**：生产者可以配置**消息确认（acks）**级别。默认情况下，设置为`acks=all`（或`acks=-1`），这意味着发送请求在数据被写入主副本和**ISR（in-sync replica）**列表中的所有跟随副本之前不会被确认。这确保了消息在多个副本之间的持久性和一致性⁴.

3. **ISR 列表**：Kafka 维护一个**ISR 列表**，其中包含与主分区同步的副本。只有在ISR列表中的副本才能成为主分区的候选副本。这确保了消息在可用的副本之间进行复制，从而提高了消息的可靠性和持久性⁵.

总之，Kafka 的设计和配置使其成为一个可靠的消息传递系统，确保消息不会丢失。

## kafka 可以保证消息是有序消费的吗？ 

**Kafka** 可以通过一些机制来保证消息的有序消费，但需要注意以下几点：

1. **消息有序性**：我们需要从两个方面看待消息的有序性：
    - 首先，**发送端**能否保证发送到服务器的消息是有序的；
    - 其次，**接收端**能否有序地消费服务器中的数据。

2. **发送端消息有序性**：
    - **Kafka** 分布式的单位是 **partition**（分区）。同一个 **partition** 使用一个 **write ahead log** 组织，因此可以保证 **FIFO** 的顺序。
    - 不同 **partition** 之间不能保证顺序。但是绝大多数用户可以通过 **message key** 来定义，因为同一个 **key** 的消息可以保证只发送到同一个 **partition**。例如，使用 **user ID** 或 **table row ID** 作为 **key**，这样同一个用户或记录的消息永远只会发送到同一个 **partition** 上，从而保证了顺序。

3. **客户端消息发送原理**：
    - 在 **Kafka** 中，消息发送是异步的。在新版本的 **Kafka** 中，只有一种异步方式，即批量发送。
    - 在 **producer** 端，存在两个线程：
        - **主线程**：用户端调用 **send** 方法时，数据被缓存到 **RecordAccumulator** 中，**send** 方法立即返回，但此时并不能确定消息是否真正发送到 **broker**。
        - **sender IO 线程**：不断轮询 **RecordAccumulator**，满足一定条件后，进行真正的网络 IO 发送，使用异步非阻塞的 **NIO**。
    - **ProducerRecord** 对象包含以下字段：
        - 如果在发送时指定了 **partition**，消息将保存到指定的 **partition** 队列。
        - 如果没有指定分区，将对 **key** 散列后计算分区，相同 **key** 的消息将被写到同一个分区队列中。

4. **总结**：
    - 通过队列，保证 **partition** 上的数据元素是有序的。
    - 通过设置相同的路由，让多个数据被路由到同一个 **partition** 即可。

## Kafka的读写速度为什么惊人的快？
**Kafka** 之所以具有出色的读写速度，是因为它在设计和实现上采用了一些关键策略和技术。以下是一些原因：

1. **分布式架构**：**Kafka** 是一个分布式系统，它将数据分散到多个 **broker**（服务器）上。这样可以充分利用集群中的计算和存储资源，从而提高整体的读写速度。

2. **分区和副本**：**Kafka** 中的主题被分成多个 **partition**（分区）。每个 **partition** 可以在不同的 **broker** 上有多个副本。这种设计允许多个消费者并行地读取数据，同时保证数据的冗余和可靠性。

3. **顺序写入**：**Kafka** 的写入操作是顺序的。消息首先被追加到 **partition** 的日志文件中，然后再由 **broker** 处理。这种顺序写入的方式对于磁盘性能非常友好，因为它最大程度地减少了磁盘寻道时间。

4. **零拷贝技术**：**Kafka** 使用零拷贝技术来最小化数据在内存和磁盘之间的复制。这样可以减少 CPU 和内存的开销，提高性能。

5. **批量处理**：**Kafka** 支持批量处理，即一次性处理多条消息。这样可以减少网络传输和磁盘写入的次数，提高效率。

6. **异步处理**：**Kafka** 的生产者和消费者是异步的。生产者可以缓冲多条消息，然后一次性发送到 **broker**。消费者也可以异步地拉取数据。这种异步处理方式可以提高吞吐量。

总之，**Kafka** 的高性能和读写速度得益于其分布式架构、顺序写入、零拷贝技术以及其他优化策略。

