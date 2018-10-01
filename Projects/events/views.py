from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EventListing
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

class EventCreateView(LoginRequiredMixin, CreateView):
	model = EventListing
	fields = [] #models go here


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class EventPageView(ListView):
	model = EventListing
	template_name = 'events/event.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class UserEventPageView(ListView):
	model = EventListing
	template_name = 'events/user_event.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return EventListing.objects.filter(author=user).order_by('-date_posted')

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = EventListing
	fields = [] #models go here

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		event = self.get_object()
		return self.request.user == event.author		# do we need a conditional true/false here??


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = EventListing
	success_url = '/'
	def test_func(self):
		event = self.get_object()
		return self.request.user == event.author


class EventDetailView(DetailView):
	model = EventListing
