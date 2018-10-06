from django_cron import CronJobBase, Schedule
from jobs.models import JobListing
from django.utils.timezone import now
from datetime import datetime, timedelta

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        #Items older than 7 days
        items = JobListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        for item in items:
            item.is_expired = True
            item.save()
