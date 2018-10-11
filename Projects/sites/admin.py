from django.contrib import admin
from users.models import Profile
from jobs.models import JobListing
from groups.models import GroupListing
from events.models import EventListing
from consultants.models import ConsultantListing
from companies.models import CompanyListing


admin.site.register(Profile)
admin.site.register(JobListing)
admin.site.register(GroupListing)
admin.site.register(EventListing)
admin.site.register(ConsultantListing)
admin.site.register(CompanyListing)
admin.site.site_header = "Techpalmy Administration"
