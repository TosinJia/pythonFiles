
### APScheduler
- [花10分钟让你彻底学会Python定时任务框架apscheduler](https://blog.csdn.net/somezz/article/details/83104368)
- [Python使用APScheduler实现定时任务](https://www.cnblogs.com/gdjlc/p/11432526.html)
- [官方文档](https://apscheduler.readthedocs.io/en/latest/userguide.html)


#### 实例
##### 触发器cron
- aps_scheduler.py

#### 异常
##### 1. Run time of job "job2 (trigger: cron[hour='7,17', minute='50'], next run at: 2021-02-22 17:50:00 CST)" was missed by 0:00:01.103655
- https://apscheduler.readthedocs.io/en/stable/userguide.html#missed-job-executions-and-coalescing

参数 | 描述
---|---
misfire_grace_time | 允许容错的时间，单位为：s（解决这个was missed by 这个报错）
coalesce | 如果系统因某些原因没有执行任务，导致任务累计，为True则只运行最后一次，为False 则累计的任务全部跑一遍
