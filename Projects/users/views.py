from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, ProfileRegistrationForm

# ATTEMPT TO GET USER LISTINGS IN PROFILE
# imports from sites/view.py
from django.shortcuts import render, get_object_or_404, redirect
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


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileRegistrationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to login.")
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileRegistrationForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def profile(request):
    if request.method  == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})


# ATTEMPT TO GET USER LISTINGS IN PROFILE
# from sites/views.py
def home(request):
	jobs = JobListing.objects.all().order_by('-date_posted').annotate(type=Value('job', CharField()))
	companies = CompanyListing.objects.all().order_by('-date_posted').annotate(type=Value('company', CharField()))
	events = EventListing.objects.all().order_by('-date_posted').annotate(type=Value('event', CharField()))
	groups = GroupListing.objects.all().order_by('-date_posted').annotate(type=Value('group', CharField()))
	consultants = ConsultantListing.objects.all().order_by('-date_posted').annotate(type=Value('consultant', CharField()))

	results = list(jobs) + list(events) + list(companies) + list(groups) + list(consultants)
	results = sorted(results, key=lambda obj: obj.date_posted, reverse=True)

	return render(request, 'sites/index.html', {'all_items_feed': results})
