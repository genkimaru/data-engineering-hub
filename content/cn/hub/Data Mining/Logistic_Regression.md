---
title: 逻辑回归案例
weight: 1
---


我们可以使用一个开源的数据集来实现垃圾评论过滤。以下是一个示例，我们将使用 **YouTube 评论数据集** 来训练一个逻辑回归模型来识别垃圾评论。

1. **数据集**：
    - 我们将使用 **YouTube 评论数据集**，其中包含了一些标记为垃圾（1）或非垃圾（0）的评论。这个数据集相对较小，大约有2000个样本¹²。
    - 你可以从这个网站下载数据集：[YouTube Spam Collection](http://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection)。

2. **步骤**：
    - 读取数据集并准备特征和目标变量。
    - 使用 **TF-IDF** 向量化文本特征。
    - 将数据分为训练集和测试集。
    - 初始化 **Logistic Regression** 模型并在训练数据上进行训练。
    - 在测试数据上进行预测并计算准确率。

3. **示例代码**：
    ```python
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report

    # 读取垃圾评论数据集（示例数据，你可以替换为实际数据集）
    data = pd.read_csv("YouTube_Spam_Collection.csv")

    # 分割特征和目标变量
    X = data["comment_text"]
    y = data["is_spam"]

    # 使用 TF-IDF 向量化文本特征
    vectorizer = TfidfVectorizer(max_features=1000)
    X_tfidf = vectorizer.fit_transform(X)

    # 将数据分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    # 初始化 Logistic Regression 模型
    model = LogisticRegression()

    # 在训练数据上训练模型
    model.fit(X_train, y_train)

    # 在测试数据上进行预测
    y_pred = model.predict(X_test)

    # 计算准确率和其他评估指标
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"准确率：{accuracy:.2f}")
    print("分类报告：")
    print(report)
    ```
 
运行结果 
``` plain
分类报告：
              precision    recall  f1-score   support

           0       0.96      0.96      0.96        27
           1       0.98      0.98      0.98        43

    accuracy                           0.97        70
   macro avg       0.97      0.97      0.97        70
weighted avg       0.97      0.97      0.97        70
```

结果解释
```plain
这是一个**二分类模型**的分类报告，用于评估模型的性能。让我们来解释一下报告中的各项指标：

- **Precision（精确率）**：表示模型预测为正类的样本中，实际为正类的比例。对于类别 0，精确率为 0.96，对于类别 1，精确率为 0.98。这意味着模型在预测为正类时，有很高的准确性。

- **Recall（召回率）**：表示实际为正类的样本中，被模型正确预测为正类的比例。对于类别 0，召回率为 0.96，对于类别 1，召回率为 0.98。这意味着模型能够有效地捕捉到正类样本。

- **F1-score（F1 分数）**：综合考虑了精确率和召回率，是一个综合性能指标。对于类别 0，F1 分数为 0.96，对于类别 1，F1 分数为 0.98。这个指标越接近 1，说明模型的性能越好。

- **Accuracy（准确率）**：表示模型预测正确的样本占总样本数的比例。整体准确率为 0.97，说明模型在整体上表现良好。

- **Macro avg 和 weighted avg**：分别是宏平均和加权平均。宏平均计算了每个类别的指标的平均值，而加权平均考虑了每个类别的样本数量。在这里，宏平均和加权平均的值都接近 0.97，说明模型在两个类别上都有很好的表现。

总之，这个模型在分类任务上表现出色，具有很高的准确性、召回率和 F1 分数。如果你有其他问题或需要更详细的解释，请随时告知！🌟
```
 