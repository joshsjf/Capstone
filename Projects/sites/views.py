from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from jobs.models import JobListing
from companies.models import CompanyListing
from consultants.models import ConsultantListing
from groups.models import GroupListing
from events.models import EventListing
from django.db.models import Value, CharField, Q
from django.contrib.postgres.search import SearchQuery


def home(request):
	jobs = JobListing.objects.all().order_by('-date_posted').annotate(type=Value('job', CharField()))
	companies = CompanyListing.objects.all().order_by('-date_posted').annotate(type=Value('company', CharField()))
	events = EventListing.objects.all().order_by('-date_posted').annotate(type=Value('event', CharField()))
	groups = GroupListing.objects.all().order_by('-date_posted').annotate(type=Value('group', CharField()))
	consultants = ConsultantListing.objects.all().order_by('-date_posted').annotate(type=Value('consultant', CharField()))

	results = list(jobs) + list(events) + list(companies) + list(groups) + list(consultants)
	results = sorted(results, key=lambda obj: obj.date_posted, reverse=True)

	return render(request, 'sites/index.html', {'all_items_feed': results})


def search(request):
	template = 'sites/search.html'
	queryitem = request.GET.get('q')
	queryset = queryitem.split(' ')
	results = []
	for query in queryset:
		jobs = JobListing.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query)).annotate(type=Value('job', CharField()))
		events = EventListing.objects.filter(Q(event_Name__icontains=query) | Q(event_Description__icontains=query)).annotate(type=Value('event', CharField()))
		companies = CompanyListing.objects.filter(Q(company_Name__icontains=query) | Q(description__icontains=query)).annotate(type=Value('company', CharField()))
		groups = GroupListing.objects.filter(Q(group_Name__icontains=query) | Q(description__icontains=query)).annotate(type=Value('group', CharField()))
		consultants = ConsultantListing.objects.filter(Q(consultant_Name__icontains=query) | Q(description__icontains=query)).annotate(type=Value('consultant', CharField()))

		results.extend(list(jobs) + list(events) + list(companies) + list(groups) + list(consultants))
	results = sorted(results, key=lambda obj: obj.date_posted, reverse=True)
	results = list(set(results))
	context = {'data': results, 'item': query}

	return render(request, template, context)


# class IndexView(ListView):
# 	template_name = 'sites/index.html'
# 	model = JobListing
# 	context_object_name = 'data'
# 	def get_context_data(self, **kwargs):
# 		context = super(IndexView, self).get_context_data(**kwargs)
# 		context.update({
# 			'character_universe_list': JobListing.objects.order_by('-date_posted'),
# 			'more_context': CompanyListing.objects.order_by('-date_posted'),
# 		})
# 		return context
#
# 	def get_queryset(self):
# 		return JobListing.objects.order_by('-date_posted')


class AboutPageView(TemplateView):
	template_name = "sites/about.html"

class ContactPageView(TemplateView):
	template_name = "sites/contact.html"

class TermsAndCondition(TemplateView):
	template_name = "sites/termsandconditions.html"
