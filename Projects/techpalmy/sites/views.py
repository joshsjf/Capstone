from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from sites.models import Companies
from sites.models import Post


class HomePageView(ListView):
	def get(self, request, **kwargs):
		data = Post.objects.all()
		args = {'data': data}
		return render(request, 'index.html', args)

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
