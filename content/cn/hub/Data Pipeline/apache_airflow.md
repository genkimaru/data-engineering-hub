+++
title = 'Apache_airflow'
date = 2024-04-01T09:02:28+08:00
weight = 100
+++

Apache Airflow™ 是一个开源平台，用于开发、调度和监控面向批处理的工作流。Airflow 的可扩展 Python 框架使您能够构建工作流与几乎任何技术连接。Web 界面有助于管理工作流的状态。Airflow 可以通过多种方式进行部署，从笔记本电脑上的单个进程到分布式设置，甚至支持最大的工作流程。

Airflow 的理念是将工作流定义为代码, Workflows as code

Airflow 工作流的主要特征是所有工作流都是在 Python 代码中定义的。“工作流即代码”有多种用途：

- Dynamic: Airflow pipelines are configured as Python code, allowing for dynamic pipeline generation.
- Extensible: The Airflow™ framework contains operators to connect with numerous technologies. All Airflow components are extensible to easily adjust to your environment.
- Flexible: Workflow parameterization is built-in leveraging the Jinja templating engine.

动态：Airflow 管道配置为 Python 代码，允许动态生成管道。

可扩展：Airflow™ 框架包含可连接多种技术的操作符。所有 Airflow 组件都具有可扩展性，可轻松适应您的环境。

灵活：利用 Jinja 模板引擎，内置工作流程参数化功能。

``` python
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
```

如果你喜欢编码而不是点击，那么 Airflow 就是你的理想工具。工作流被定义为 Python 代码，这意味着

- 工作流程可存储在版本控制中，以便回滚到以前的版本

- 多人可同时开发工作流程

- 可编写测试来验证功能

- 组件具有可扩展性，您可以在大量现有组件的基础上进行构建


