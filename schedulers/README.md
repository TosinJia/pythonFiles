
### APScheduler
- [Python使用APScheduler实现定时任务](https://www.cnblogs.com/gdjlc/p/11432526.html)
- [官方文档](https://apscheduler.readthedocs.io/en/latest/userguide.html)

#### 实例
##### 触发器cron
- aps_scheduler.py

#### 异常
##### 1. Run time of job "job2 (trigger: cron[hour='7,17', minute='50'], next run at: 2021-02-22 17:50:00 CST)" was missed by 0:00:01.103655
- https://apscheduler.readthedocs.io/en/stable/userguide.html#missed-job-executions-and-coalescing

> 参数 misfire_grace_time 允许容错的时间，单位为：s（解决这个was missed by 这个报错） 