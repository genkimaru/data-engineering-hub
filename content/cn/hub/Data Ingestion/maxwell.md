---
title: maxwell
---

This is Maxwell's daemon, a change data capture application that reads MySQL binlogs and writes data changes as JSON to Kafka, Kinesis, and other streaming platforms.
--------
```
  mysql> update `test`.`maxwell` set mycol = 55, daemon = 'Stanislaw Lem';
  maxwell -> kafka: 
  {
    "database": "test",
    "table": "maxwell",
    "type": "insert",
    "ts": 1449786310,
    "data": { "id":1, "daemon": "Stanislaw Lem", "mycol": 55 },
    "old": { "mycol":, 23, "daemon": "what once was" }
  }
```
