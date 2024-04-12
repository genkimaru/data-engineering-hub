---
title: flink窗口操作
---


## 窗口连接 window join
窗口联结在代码中的实现，首先需要调用 DataStream 的.join()方法来合并两条流，得到一个 JoinedStreams；接着通过.where()和.equalTo()方法指定两条流中联结的 key；然后通过.window()开窗口，并调用.apply()传入联结窗口函数进行处理计算
``` java
stream1.join(stream2)
.where(keySelector1).equalTo(keySeelctor2)
.window(windowAssigner)
.apply(joinFunction)
```
where()的参数是键选择器（KeySelector），用来指定第一条流中的 key；而.equalTo()传入的 KeySelector 则指定了第二条流中的 key。两者相同的元素，如果在同一窗口中，就可以匹配起来

## 间隔连接 interval join

间隔连接使用公共密钥连接两个流（我们现在将其称为 A 和 B）的元素，其中流 B 的元素的时间戳位于流 A 中元素的时间戳的相对时间间隔内。
![interval join](/images/flink%20interval%20join.png)

## cogroup 同组连接
![cogroup window](/images/flink%20cogroup.png)