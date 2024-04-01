---
title: K_Means案例
weight: 10
---


### K均值聚类算法实际案例

假设我们有一个数据集，其中包含300个数据点，这些数据点属于4个不同的类别。我们想要使用K均值算法将这些数据点分成4个簇。以下是实现的步骤：

1. **生成合成数据**：我们首先生成一个合成数据集，其中包含4个簇。这可以通过`make_blobs`函数来实现。

2. **初始化K均值模型**：我们使用`KMeans`类来初始化一个K均值模型，指定簇的数量为4。

3. **拟合模型**：将数据拟合到K均值模型中。

4. **获取簇中心和标签**：我们可以获取每个簇的中心点和数据点的标签。

5. **绘制结果**：最后，我们绘制数据点和簇中心，以查看聚类效果。

以下是Python代码实现：

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 生成合成数据
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# 初始化KMeans模型（指定4个簇）
kmeans = KMeans(n_clusters=4, random_state=42)

# 拟合模型
kmeans.fit(X)

# 获取簇中心和标签
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# 绘制数据点和簇中心
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
plt.title("KMeans Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
```

这段代码将生成一个散点图，其中数据点被分成4个簇，并且红色的“x”表示每个簇的中心点。

