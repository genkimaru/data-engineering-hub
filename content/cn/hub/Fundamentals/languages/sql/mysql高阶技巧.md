---
title: mysql的高阶技巧
---

MySQL 中有许多常用的高阶 SQL 写法，以下列举了一些常见的高级 SQL 技巧和语法：

1. **窗口函数（Window Functions）**：使用 `OVER` 子句来执行聚合、排序等操作，如 `ROW_NUMBER()`, `RANK()`, `LEAD()`, `LAG()` 等。

2. **公共表表达式（Common Table Expressions，CTE）**：使用 `WITH` 关键字创建临时结果集，可以提高查询的可读性和可维护性。

3. **联结（Join）**：除了常见的 `INNER JOIN`、`LEFT JOIN`、`RIGHT JOIN` 外，还可以使用 `CROSS JOIN`、`SELF JOIN` 等。

4. **子查询（Subquery）**：在 `SELECT`、`FROM`、`WHERE` 等子句中嵌套查询，用于实现复杂的逻辑。

5. **条件聚合（Conditional Aggregation）**：使用 `CASE` 表达式在聚合函数中进行条件判断，如 `SUM(CASE WHEN condition THEN column END)`。

6. **动态SQL（Dynamic SQL）**：使用 MySQL 变量和字符串拼接等技巧动态生成 SQL 语句，实现灵活的查询逻辑。

7. **分析函数（Analytic Functions）**：类似于窗口函数，但可以在结果集中进行更复杂的分析，如 `RANK() OVER (PARTITION BY column ORDER BY column)`。

8. **递归查询（Recursive Query）**：使用 `WITH RECURSIVE` 关键字实现递归查询，处理具有递归结构的数据。

9. **数据透视表（Pivot Table）**：使用 `CASE` 表达式和聚合函数将行数据转换为列数据，实现数据透视的效果。

10. **多表更新（Multi-table Update）**：使用 `UPDATE` 语句联结多个表进行更新操作，可以一次性更新多个表中的数据。


