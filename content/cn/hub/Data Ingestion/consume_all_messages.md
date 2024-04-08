---
title: Consume all messages
weight: 3
---


在 Kafka 中，消费者组中的不同消费者默认会分别消费主题中的不同分区数据。但如果你希望每个消费者都消费全量数据，可以采用以下方法：

- 手动分配分区：在创建消费者时，你可以手动分配分区给每个消费者。这样，每个消费者将负责处理指定的分区，从而确保每个消费者都能消费全量数据。这种方式需要你显式地管理分区分配，但可以精确控制消费者的数据处理.


- 消费者组协调器：Kafka 的消费者组协调器会自动分配分区给消费者。如果你希望每个消费者都消费全量数据，可以将每个消费者订阅的主题分区数设置为与主题的分区总数相等。这样，每个消费者将负责处理所有分区，从而实现全量数据的消费.
``` python
from kafka import KafkaConsumer, TopicPartition

# 配置 Kafka 服务器和主题
bootstrap_servers = 'your_kafka_broker'
topic = 'your_topic'

# 创建消费者
consumer = KafkaConsumer(
    topic,
    group_id='your_consumer_group',
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # 从最早的消息开始消费
    enable_auto_commit=False,  # 禁用自动提交偏移量
)

# 获取主题的分区列表
partitions = consumer.partitions_for_topic(topic)

# 手动分配分区给消费者
for partition in partitions:
    tp = TopicPartition(topic, partition)
    consumer.assign([tp])

# 消费消息
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")

# 关闭消费者
consumer.close()
```