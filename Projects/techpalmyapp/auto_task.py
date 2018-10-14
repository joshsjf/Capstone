from django_cron import CronJobBase, Schedule
from jobs.models import JobListing
from companies.models import CompanyListing
from consultants.models import ConsultantListing
from events.models import EventListing
from groups.models import GroupListing
from django.utils.timezone import now
from datetime import datetime, timedelta

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        #Items older than 7 days
        items = JobListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        items += CompanyListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        items += GroupListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        items += ConsultantListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        items += EventListing.objects.filter(date_posted__gte=datetime.now()-timedelta(days=7))
        for item in items:
            item.is_Expired = True
            item.save()     // where does this save to??
