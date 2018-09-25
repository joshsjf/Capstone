from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CompanyListing
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

class CompanyCreateView(LoginRequiredMixin, CreateView):
	model = CompanyListing
	fields = ['companyName', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
				'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class CompanyPageView(ListView):
	model = CompanyListing
	template_name = 'companies/company.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class UserCompanyPageView(ListView):
	model = CompanyListing
	template_name = 'companies/user_company.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return CompanyListing.objects.filter(author=user).order_by('-date_posted')

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CompanyListing
	fields = ['companyName', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
			'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author		# do we need a conditional true/false here??


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CompanyListing
	success_url = '/'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author


class CompanyDetailView(DetailView):
	model = CompanyListing
