from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)

class ConsultantsPageView(TemplateView):
    template_name = "consultants.html"

class CompaniesPageView(TemplateView):
    template_name = "companies.html"

class EventsPageView(TemplateView):
    template_name = "events.html"

class JobsPageView(TemplateView):
    template_name = "jobs.html"

class GroupsPageView(TemplateView):
    template_name = "groups.html"

class EducationPageView(TemplateView):
    template_name = "education.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
