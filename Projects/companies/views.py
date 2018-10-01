from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CompanyListing
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from companies.forms import CompanyCreateView, CompanyUpdateForm
from django.urls import reverse

@login_required
def companyCreate(request):
	if request.method == 'POST':
		form = CompanyCreateView(request.POST)
		if form.is_valid():
			form.instance.author = request.user
			comp = form.save()
			messages.success(request, "Your company has been created!")
			return redirect(reverse('company-detail', kwargs={'pk': comp.pk}))
	else:
		form = CompanyCreateView()
	return render(request, 'companies/companylisting_form.html', {'form': form})

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

@login_required
def CompanyUpdateView(request, pk):
	if request.method  == 'POST':
		c_form = CompanyUpdateForm(request.POST)
		if c_form.is_valid():
			c_form.save()
			messages.success(request, "Your Company has been updated!")
			return redirect(reverse('company-update', kwargs={'pk': c_form.pk}))
	else:
		c_form = CompanyUpdateForm()
	return render(request, 'companies/companylisting_detail.html', {'c_form': c_form})


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CompanyListing
	success_url = '/'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author


class CompanyDetailView(DetailView):
	model = CompanyListing
