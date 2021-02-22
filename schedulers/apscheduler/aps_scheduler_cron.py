import time
from apscheduler.schedulers.blocking import BlockingScheduler


def job(text):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print('{}-----{}'.format(text, t))


scheduler = BlockingScheduler()
# scheduler.add_job(job, 'cron', hour=13, minute="*/1", args=['job1'])
# scheduler.add_job(job, 'cron', hour="*", minute="*", second="*/5", args=['job2'])

scheduler.add_job(job, 'cron', hour="8-17", minute="*/10", args=['job-1'], misfire_grace_time=5*60)
scheduler.start()

# job('test1')