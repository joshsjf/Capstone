from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CompanyListing
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from companies.forms import CompanyCreateView
from django.urls import reverse

def companyCreate(request):
	if request.method == 'POST':
		c_form = CompanyCreateView(request.POST)
		if form.is_valid():
			form.instance.author = request.user
			comp = form.save()
			messages.success(request, "Your company has been created!")
			return redirect(reverse('company-detail', kwargs={'pk': comp.pk}))
	else:
		form = CompanyCreateView()
	return render(request, 'companies/companylisting_form.html', {'form': form})

# class CompanyCreateView(LoginRequiredMixin, CreateView):
# 	model = CompanyListing
# 	fields = ['companyName', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
# 				'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']
#
# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

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
