from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

class ConsultantsPageView(TemplateView):
    template_name = "sites/consultants.html"

class CompaniesPageView(TemplateView):
    template_name = "sites/companies.html"

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
