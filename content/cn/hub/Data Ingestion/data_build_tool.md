---
title: 'Data Build Tool'
weight: 7
---


data build tool 的特点通常包括：

1. 支持多种数据源：可以连接和处理不同类型的数据源，如数据库、文件、API 等。

2. 可视化操作：提供图形化界面或者类似 SQL 的语法，方便用户进行操作和配置。

3. 支持数据转换：可以进行数据清洗、转换、合并等操作，以满足不同的数据处理需求。

4. 调度和监控：可以设置任务调度，监控任务执行情况，保证数据处理的准确性和及时性。

利用 data build tool 进行 ETL 过程通常包括以下步骤：

1. Extract（提取）：从不同的数据源中提取需要的数据，可以是数据库表、文件、API 接口等。

2. Transform（转换）：对提取的数据进行清洗、转换、合并等操作，使其符合目标数据仓库的要求。

3. Load（加载）：将经过转换的数据加载到目标数据仓库中，可以是数据库表、数据湖等存储介质。


案例：利用dbt 将 本地的mysql数据进行过滤掉一些id为敏感数据的记录，然后导入到云端的gcp的bigquery中，这个例子用dbt该如何实现呢？

要利用 dbt 将本地的 MySQL 数据进行过滤并导入到 GCP 的 BigQuery 中，可以按照以下步骤进行：

1. 创建 dbt 项目：首先在本地初始化一个 dbt 项目，可以使用以下命令：
```
dbt init my_project
```

2. 配置数据源：在 dbt 项目目录下的 `profiles.yml` 文件中配置本地 MySQL 数据源和 GCP BigQuery 数据源的连接信息。

3. 编写模型：在 dbt 项目中创建一个模型（model），用于过滤敏感数据。在 `models` 目录下创建一个 `.sql` 文件，编写 SQL 查询语句，例如：
```sql
-- models/filter_sensitive_data.sql
with filtered_data as (
    select * from {{ ref('source_table') }} where id not in ('sensitive_id_1', 'sensitive_id_2')
)
select * from filtered_data
```

4. 配置模型依赖：在 `schema.yml` 文件中定义模型的依赖关系，指定数据源表和过滤模型之间的关系。

5. 运行 dbt：在终端中运行以下命令，执行 dbt 项目并生成目标数据：
```
dbt run
```

6. 导入到 BigQuery：将生成的数据集导入到 GCP 的 BigQuery 中，可以使用 BigQuery 的 Web 界面或者命令行工具进行导入操作。

通过以上步骤，可以利用 dbt 对本地 MySQL 数据进行过滤处理，并将处理后的数据导入到 GCP 的 BigQuery 中，实现数据迁移和处理的自动化流程。

7. 如果使用dbt cloud，可以无需步骤6 ，在 dbt 中，可以使用 dbt Cloud 或者 dbt Cloud CLI 来直接将生成的数据集导入到 BigQuery 中，而无需手动操作。

