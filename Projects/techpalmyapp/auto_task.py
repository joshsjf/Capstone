from django_cron import CronJobBase, Schedule
from jobs.models import JobListing
from companies.models import CompanyListing
from consultants.models import ConsultantListing
from events.models import EventListing
from groups.models import GroupListing
from datetime import timedelta
from django.utils import timezone

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "techpamlyapp.MyCronJob"

    def do(self):
        DAY = 7
        #Items older than 7 days
        items = list(JobListing.objects.filter(date_posted__lte=timezone.now()-timedelta(days=DAY)))
        items.extend(list(CompanyListing.objects.filter(date_posted__lte=timezone.now()-timedelta(days=DAY))))
        items.extend(list(GroupListing.objects.filter(date_posted__lte=timezone.now()-timedelta(days=DAY))))
        items.extend(list(ConsultantListing.objects.filter(date_posted__lte=timezone.now()-timedelta(days=DAY))))
        items.extend(list(EventListing.objects.filter(date_posted__lte=timezone.now()-timedelta(days=DAY))))
        for item in items:
            item.is_Expired = True
            item.save()
