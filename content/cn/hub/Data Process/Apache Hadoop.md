---
title: Apache Hadoop
weight: 70
---

![[Assets/hadoop_logo.jpg|100]]

[Apache Hadoop](https://hadoop.apache.org/) is a data processing framework designed to batch process big amounts of data.

# Official Documentation

https://hadoop.apache.org/docs/current/

# Apache Hadoop Advantages

- **MapReduce** function
- *Divide and Conquer* strategy to deal with data
- HDFS system to store data

# Apache Hadoop Disadvantages

- Hadoop works on disk, which makes it slower than memory
- Low efficiency on small files
- High latency

# HDFS

**HDFS** or Hadoop Distributed File System is a native tool on Hadoop that let us store structured and non-structured data on a local cluster. Although HDFS is the main option and is the one Apache Spark uses as well, Hadoop offers other tools such as HFTP, HSFTP, WebHDFS, and Amazon S3.


# How does Hadoop work?

Apache Hadoop is settled upon a **Leader-Follower** system. A Leader node, also known as *NameNode* in HDFS, will be responsible for creating tasks and sending information to Follower nodes through the information nodes, known as *DataNodes*. 

Once the *name node* and the *data nodes* are configured, the Leader will set a **job-tracker**. This job-tracker will have control over the tasks using **task-trackers** on the Follower nodes. This is done to prevent Followers from trying to complete every task, that is, job-trackers **indicate exactly** which tasks must be done on each follower node as well as which information every follower node needs to fetch from the data nodes.

This way of working, the *Divide and Conquer* system, is also what defines MapReduce on Hadoop. Tasks get divided to every follower node, which improves data processing speed on real large datasets. MapReduce consists of two functions:

- Map: Map will read important information in the HDFS environment, analyzing key-value pairs and sending them to the datanodes.
- Reduce: Reduce will retrieve all pairs and group them by its key to produce the final pairs. Once this finishes, the data will be stored in a datanode.

When the MapReduce function is finished, the leader will be informed.

![[Assets/mapreduce.png]]

# When to use Hadoop?

|                        **_Use it if..._**                       |                   **_Don't use it if..._**                  |
|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| **You are working with tasks that can be divided on side jobs** | **You are working with serial tasks or  low latency tasks** |

