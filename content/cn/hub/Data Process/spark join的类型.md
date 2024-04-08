---
title: Spark Join的类型和使用
weight: 10
---

## spark join 的三种类型
在Spark中，有三种常见的连接方式：Shuffle Hash Join、Broadcast Hash Join和Sort Merge Join，它们各有特点，适合不同的场合：

1. Shuffle Hash Join（Shuffle哈希连接）：
   - 原理：Shuffle Hash Join会对两个数据集的连接键进行哈希分区，并将数据重新分布到不同的Executor上，然后进行连接操作。
   - 适合场合：适合用于连接大规模数据集，数据分布较均匀的情况。由于需要进行Shuffle操作，适合用于连接大数据集时。

2. Broadcast Hash Join（广播哈希连接）：
   - 原理：Broadcast Hash Join会将一个数据集小的数据广播到所有Executor上，然后与另一个数据集进行连接操作。
   - 适合场合：适合用于连接一个小数据集和一个大数据集，或者在一个数据集已经被缓存到内存中的情况下。适合用于连接小数据集时。

3. Sort Merge Join（排序合并连接）：
   - 原理：Sort Merge Join会对两个数据集的连接键进行排序，然后按顺序合并这两个有序数据集来进行连接操作。
   - 适合场合：适合用于连接大数据集并且连接键有序的情况。当数据集已经按连接键有序时，Sort Merge Join可以避免Shuffle操作，适合用于连接有序数据集时。

在实际使用中，根据数据集的大小、数据分布情况、连接键的数据倾斜程度等因素来选择合适的连接方式：
- 如果连接的是大规模数据集，且数据分布较均匀，可以考虑使用Shuffle Hash Join。
- 如果连接的是一个小数据集和一个大数据集，或者已经缓存到内存中的数据集，可以考虑使用Broadcast Hash Join。
- 如果连接的数据集已经按连接键有序，可以考虑使用Sort Merge Join。

综合考虑数据规模、数据分布、内存资源等因素，选择合适的连接方式可以提高Spark作业的性能和效率。

## boardcast hash join 的例子
假设有两个DataFrame，一个包含用户ID和用户名，另一个包含用户ID和用户所在城市，我们可以使用Broadcast Hash Join来将这两个DataFrame连接起来。在这个例子中，我们将用户ID作为连接键。

首先，创建两个DataFrame：
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BroadcastHashJoinExample").getOrCreate()

# 创建第一个DataFrame：用户ID和用户名
data1 = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
df1 = spark.createDataFrame(data1, ["user_id", "username"])

# 创建第二个DataFrame：用户ID和用户所在城市
data2 = [(1, "New York"), (2, "San Francisco"), (3, "Los Angeles")]
df2 = spark.createDataFrame(data2, ["user_id", "city"])
```

然后，使用Broadcast Hash Join将这两个DataFrame连接起来：
```python
from pyspark.sql.functions import broadcast

# 使用Broadcast Hash Join连接两个DataFrame
joined_df = df1.join(broadcast(df2), "user_id")

# 显示连接后的DataFrame
joined_df.show()
```

在这个例子中，我们使用`broadcast(df2)`将第二个DataFrame广播到所有Executor上，然后通过`df1.join()`进行Broadcast Hash Join操作。这样可以避免将较小的DataFrame进行Shuffle操作，提高连接操作的性能。

通过使用Broadcast Hash Join，可以有效地处理连接一个小数据集和一个大数据集的情况，提高连接操作的效率。
