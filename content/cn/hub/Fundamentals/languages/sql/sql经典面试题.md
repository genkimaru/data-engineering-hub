---
title: mysql的高阶技巧
---

## 6个SQL查询小技巧
1、行列转换

create table if not exists tb1(
name varchar(255),
age int,
gender varchar(255)
)

insert tb1 value("Jone",10,"male");
insert tb1 value("kate",20,"female");
insert tb1 value("mike",30,"male");

select 
col1 
from (
select case when rowid = 1 then col1 else null end as col1 ,
case when rowid = 2 then col1 else null end as col2 ,
case when rowid = 3 then col1 else null end as col3 
from (
select name as col1 , row_number() over (order by name) as rowid from tb1
union all
select age as col1,row_number() over (order by name)  as rowid from tb1
union all
select gender as col1, row_number() over (order by name) as rowid  from tb1
) as temp 
) as temp2 where col1 is not null


select * from tmp;
