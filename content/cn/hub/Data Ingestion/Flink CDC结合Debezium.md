---
title: Flink CDC结合Debezium
weight: 6
---

[Debezium](https://debezium.io/) is an open-source log-based **change data capture** tool used for streaming changes from your database. It works by reading the Transaction Log of your database to capture INSERT/UPDATE/DELETE events and propagates those events to a consumer (most commonly **Apache Kafka**).

### Debezium Advantages

- Captures changes in a way that has minimal impact on the source
- Changes can be captured with very low latency

### 一个利用Flink CDC结合Debezium 监控mysql变更操作，并将变更数据发送kafka的例子

要实现利用Flink CDC动态监控MySQL的test表的变更操作，并将变更数据发送到Kafka中，可以按照以下步骤进行：

1. 部署Apache Flink集群：确保已经搭建好Apache Flink集群，并准备好运行Flink Job。

2. 部署Debezium MySQL Connector：将Debezium MySQL Connector部署到Flink集群中，配置连接MySQL数据库的信息。

3. 编写Flink Job：编写一个Flink应用程序，通过Debezium Connector监听MySQL的test表的变更数据，并将变更数据发送到Kafka中。以下是一个简单的Flink Job示例：

```java
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;

public class MySQLChangeDataCaptureJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 添加MySQL CDC Source
        DataStream<String> mysqlDataStream = env.addSource(new MySQLDebeziumSourceFunction("mysql-connector-properties"));

        // 将变更数据发送到Kafka Sink
        mysqlDataStream.addSink(new FlinkKafkaProducer<>("kafka-topic", new SimpleStringSchema(), kafkaProperties));

        env.execute("MySQL Change Data Capture Job");
    }
}
```

4. 提交Flink Job：将编写好的Flink Job提交到Flink集群中运行，监控MySQL的test表的变更操作，并将变更数据实时发送到Kafka中。

5. 监控和验证：监控Flink Job的运行状态，确保CDC任务正常工作。可以通过Kafka Consumer验证数据是否正常发送到Kafka中。

通过以上步骤，您可以成功利用Flink CDC实现动态监控MySQL的test表的变更操作，并将变更数据发送到Kafka中。请根据实际情况调整配置和代码，以满足您的需求。


