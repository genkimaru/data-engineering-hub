---
title: spark structured streaming案例
weight: 20
---

假如有三个数据源，分别是提供温度，湿度，紫外线强度三个数据的接口，这三个接口都是通过gPRC来提供Json数据格式。  
其返回的数据给是分别是这样的
``` JSON
{
    "datetime":"2024-01-01 12:00:00",
    "temparature":"30",
    "location":"F1D1",
}
{
    "datetime":"2024-01-01 12:00:00",
    "humidity":"30",
    "location":"F1D1",
}
{
    "datetime":"2024-01-01 12:00:00",
    "ultraviolet":"30",
    "location":"F1D1",
}
```

这些数据接口每隔1秒钟就会更新一次数据
现在需要设计一个流处理引擎，实时处理这些数据，需求如下，以十秒钟的数据为一个时间窗口，如果这个时间窗口的数据中，某个地点的温度，以及湿度，以及紫外线强度的值 都超过某一个设定的阈值，并且连续超过一分钟，则记录一个状态值为true，则进行报警，把报警信息打印出来，如果这三个指标只要有一个没有达到阈值，则重置这个状态值为false。
使用spark structured streaming框架，分别用python和java实现之
   
   
{{< tabs "sss" >}}
{{< tab "Python" >}}

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("RealTimeDataProcessing").getOrCreate()

# Define the schema for temperature data
temperature_schema = StructType([
    StructField("datetime", StringType(), True),
    StructField("temperature", IntegerType(), True),
    StructField("location", StringType(), True)
])

# Define the schema for humidity data
humidity_schema = StructType([
    StructField("datetime", StringType(), True),
    StructField("humidity", IntegerType(), True),
    StructField("location", StringType(), True)
])

# Define the schema for ultraviolet data
ultraviolet_schema = StructType([
    StructField("datetime", StringType(), True),
    StructField("ultraviolet", IntegerType(), True),
    StructField("location", StringType(), True)
])

# Read data from gRPC sources
temperature_df = spark.readStream.format("grpc").option("host", "temperature_server").load()
humidity_df = spark.readStream.format("grpc").option("host", "humidity_server").load()
ultraviolet_df = spark.readStream.format("grpc").option("host", "ultraviolet_server").load()

# Define threshold values
temperature_threshold = 30
humidity_threshold = 80
ultraviolet_threshold = 8

# Join the dataframes on 'location' and 'datetime' columns
joined_df = temperature_df.join(humidity_df, ["location", "datetime"]).join(ultraviolet_df, ["location", "datetime"])

# Define the condition for triggering an alert
alert_condition = (col("temperature") >= temperature_threshold) & (col("humidity") >= humidity_threshold) & (col("ultraviolet") >= ultraviolet_threshold)

# Define the window duration and slide duration
windowed_df = joined_df.withWatermark("datetime", "10 seconds").groupBy(window("datetime", "10 seconds")).agg(collect_list("location").alias("locations"), max(when(alert_condition, 1).otherwise(0)).alias("alert"))

# Filter the windowed dataframe to find consecutive alerts for a minute
consecutive_alerts_df = windowed_df.filter((col("alert") == 1)).groupBy("window").agg(count("alert").alias("consecutive_alerts")).filter(col("consecutive_alerts") >= 6)

# Start the streaming query to monitor consecutive alerts
query = consecutive_alerts_df.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()




```

{{< /tab >}}
{{< tab "Java" >}}

```java
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQuery;
import static org.apache.spark.sql.functions.*;

public class RealTimeDataProcessing {

    public static void main(String[] args) throws Exception {
        SparkSession spark = SparkSession.builder()
                .appName("RealTimeDataProcessing")
                .getOrCreate();

        // Read data from gRPC sources
        Dataset<Row> temperatureDF = spark
                .readStream()
                .format("grpc")
                .option("host", "temperature_server")
                .load();

        Dataset<Row> humidityDF = spark
                .readStream()
                .format("grpc")
                .option("host", "humidity_server")
                .load();

        Dataset<Row> ultravioletDF = spark
                .readStream()
                .format("grpc")
                .option("host", "ultraviolet_server")
                .load();

        // Define threshold values
        int temperatureThreshold = 30;
        int humidityThreshold = 80;
        int ultravioletThreshold = 8;

        // Join the dataframes on 'location' and 'datetime' columns
        Dataset<Row> joinedDF = temperatureDF.join(humidityDF, "location")
                .join(ultravioletDF, "location");

        // Define the condition for triggering an alert
        Column alertCondition = col("temperature").geq(temperatureThreshold)
                .and(col("humidity").geq(humidityThreshold))
                .and(col("ultraviolet").geq(ultravioletThreshold));

        // Define the window duration and slide duration
        Dataset<Row> windowedDF = joinedDF.withWatermark("datetime", "10 seconds")
                .groupBy(window("datetime", "10 seconds"))
                .agg(collect_list("location").as("locations"),
                        max(when(alertCondition, 1)).otherwise(0).as("alert"));

        // Filter the windowed dataframe to find consecutive alerts for a minute
        Dataset<Row> consecutiveAlertsDF = windowedDF.filter(col("alert").equalTo(1))
                .groupBy("window")
                .agg(count("alert").as("consecutive_alerts"))
                .filter(col("consecutive_alerts").geq(6));

        // Start the streaming query to monitor consecutive alerts
        StreamingQuery query = consecutiveAlertsDF.writeStream()
                .outputMode("complete")
                .format("console")
                .start();

        query.awaitTermination();
    }
}



```

{{< /tab >}}
{{< /tabs >}}

