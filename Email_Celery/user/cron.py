from django_cron import CronJobBase, Schedule
from datetime import datetime


# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1  # run every 1 minute
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'my_app.my_cron_job'    # a unique code for your cron job

#     def do(self):
#         # define your task here
#         print(f'Task ran at {datetime.now()}')


def my_scheduled_job():
    print("runcron sussecdully")
