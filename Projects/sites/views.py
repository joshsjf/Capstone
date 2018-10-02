from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from jobs.models import JobListing
from companies.models import CompanyListing
from django.db.models import Value, CharField

def home(request):
    jobs = JobListing.objects.all().order_by('-date_posted').annotate(type=Value('job', CharField()))
    companies = CompanyListing.objects.all().order_by('-date_posted').annotate(type=Value('company', CharField()))

    all_items = list(jobs) + list(companies)
    all_items = sorted(all_items, key=lambda obj: obj.date_posted, reverse=True)

    return render(request, 'sites/index.html', {'all_items_feed': all_items})

class IndexView(ListView):
    template_name = 'sites/index.html'
    model = JobListing
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'character_universe_list': JobListing.objects.order_by('-date_posted'),
            'more_context': CompanyListing.objects.order_by('-date_posted'),
        })
        return context

    def get_queryset(self):
        return JobListing.objects.order_by('-date_posted')

class ConsultantsPageView(TemplateView):
    template_name = "sites/consultants.html"

class EventsPageView(TemplateView):
    template_name = "sites/events.html"

class GroupsPageView(TemplateView):
    template_name = "sites/groups.html"

class EducationPageView(TemplateView):
    template_name = "sites/education.html"

class AboutPageView(TemplateView):
    template_name = "sites/about.html"

class ContactPageView(TemplateView):
    template_name = "sites/contact.html"
