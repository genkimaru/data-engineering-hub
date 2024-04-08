---
title: Flink案例
weight: 21
---

给定一个流数据，输入的数据结构是一个Transaction对象，里面包含
``` plain
txid string,
amount int,
name string
``` 
三个字段，需要用flink对该transaction的流数据进行实时检测。
检测规则如下，如果对于某一个name，连续有三次的amount超过100，则进行报警，报警信息在控制台显示出来，如果是不是连续的三次，则无需报警。
这样的一个程序请用java代码来实现

{{<tabs "flink" >}}
{{<tab "Java" >}}
```Java
import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.util.Collector;

public class TransactionDetection {

    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<Transaction> transactions = ... // 从数据源获取Transaction流数据

        transactions
            .keyBy(Transaction::getName)
            .flatMap(new TransactionAlertFunction())
            .print();

        env.execute("Transaction Detection Job");
    }

    public static class TransactionAlertFunction implements FlatMapFunction<Transaction, String> {

        private static final int THRESHOLD = 100;
        private static final int CONSECUTIVE_COUNT = 3;

        @Override
        public void flatMap(Transaction transaction, Collector<String> out) {
            if (transaction.getAmount() > THRESHOLD) {
                // 检测到金额超过阈值
                TransactionState state = TransactionState.getOrDefault(transaction.getName());
                state.incrementCount();

                if (state.getCount() >= CONSECUTIVE_COUNT) {
                    out.collect("ALERT: Detected 3 consecutive transactions exceeding 100 for " + transaction.getName());
                    state.resetCount();
                }
            } else {
                // 金额未超过阈值，重置计数
                TransactionState.resetCount(transaction.getName());
            }
        }
    }

    public static class TransactionState {
        private String name;
        private int count;

        private static final Map<String, TransactionState> stateMap = new HashMap<>();

        public static TransactionState getOrDefault(String name) {
            return stateMap.computeIfAbsent(name, k -> new TransactionState(name, 0));
        }

        public static void resetCount(String name) {
            TransactionState state = stateMap.get(name);
            if (state != null) {
                state.count = 0;
            }
        }

        public void incrementCount() {
            count++;
        }

        public int getCount() {
            return count;
        }

        private TransactionState(String name, int count) {
            this.name = name;
            this.count = count;
        }
    }

}
```

{{</tab >}}
{{<tab "Java" >}}

```java
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;

public class FlinkRealTimeAlert {

    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<Transaction> transactionStream = ... // 从数据源获取Transaction流数据

        DataStream<Tuple2<String, Integer>> alertStream = transactionStream
            .keyBy(Transaction::getName)
            .process(new AlertProcessFunction());

        alertStream.print();

        env.execute("Flink Real-time Alert Job");
    }

    public static class AlertProcessFunction extends KeyedProcessFunction<String,
    Transaction, Tuple2<String, Integer>> {
        private static final int THRESHOLD = 100;
        private static final int ALERT_COUNT = 3;

        private ValueState<Integer> countState;

        @Override
        public void open(Configuration parameters) throws Exception {
            ValueStateDescriptor<Integer> countDescriptor = 
            new ValueStateDescriptor<>("countState", Integer.class);
            countState = getRuntimeContext().getState(countDescriptor);
        }

            @Override
            public void processElement(Transaction transaction, Context context, 
            Collector<Tuple2<String, Integer>> out) throws Exception {
                Integer count = countState.value();
                if (count == null) {
                    count = 0;
                }

                if (transaction.getAmount() > THRESHOLD) {
                    count++;
                    countState.update(count);
                } else {
                    // do nothing, keep count as it is
                }

                if (count >= ALERT_COUNT) {
                    out.collect(new Tuple2<>(transaction.getName(), transaction.getAmount()));
                }
            }

    }

    public static class Transaction {
        private String txid;
        private int amount;
        private String name;

        public Transaction(String txid, int amount, String name) {
            this.txid = txid;
            this.amount = amount;
            this.name = name;
        }

        public String getTxid() {
            return txid;
        }

        public int getAmount() {
            return amount;
        }

        public String getName() {
            return name;
        }
    }
}
```


{{</tab  >}}
{{</tabs >}}

