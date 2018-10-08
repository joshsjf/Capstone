from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EventListing
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from events.forms import EventCreateView, EventUpdateForm
from django.contrib import messages
from django.urls import reverse

@login_required
def eventCreate(request):
	if request.method == 'POST':
		form = EventCreateView(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form = form.save()
			messages.success(request, "Event created.")
			return redirect(reverse('event-detail', kwargs={'pk': form.pk}))
	else:
		form = EventCreateView()
	return render(request, 'events/eventlisting_form.html', {'form': form})

def eventUpdateView(request, pk):
	if request.method  == 'POST':
		e_form = EventUpdateForm(request.POST, request.FILES)
		if e_form.is_valid():
			e_form.instance.author = request.user
			camp = e_form.save()
			messages.success(request, "Your event has been updated!")
			return redirect(reverse('event-detail', kwargs={'pk': camp.pk}))
	else:
		e_form = EventUpdateForm(instance = EventListing.objects.get(pk=pk))
	return render(request, 'events/eventupdate_form.html', {'e_form': e_form})

# class EventCreateView(LoginRequiredMixin, CreateView):
# 	model = EventListing
# 	fields = [] #models go here
# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

class EventPageView(ListView):
	model = EventListing
	template_name = 'events/events.html'
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
