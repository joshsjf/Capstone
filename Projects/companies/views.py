from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CompanyListing
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from companies.forms import CompanyCreateView, CompanyUpdateForm
from django.urls import reverse


def companyCreate(request, **kwargs):
	if request.method == 'POST':
		form = CompanyCreateView(request.POST, request.FILES,)
		if form.is_valid():
			form.instance.author = request.user
			comp = form.save()
			if (comp.isAConsultant == True):
				messages.success(request, "Consultant profile has been created!")
				return redirect(reverse('consultant-detail', kwargs={'pk': comp.pk}))
			messages.success(request, "Your Company has been created!")
			return redirect(reverse('company-detail', kwargs={'pk': comp.pk}))
	else:
		form = CompanyCreateView()
	return render(request, 'companies/companylisting_form.html', {'form': form})

class CompanyPageView(ListView):
	model = CompanyListing
	template_name = 'companies/company.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class ConsultantPageView(ListView):
	model = CompanyListing
	template_name = 'companies/consultant.html'
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


def CompanyUpdateView(request, pk):
	if request.method  == 'POST':
		c_form = CompanyUpdateForm(request.POST, request.FILES)
		if c_form.is_valid():
			c_form.instance.author = request.user
			camp = c_form.save()
			instance = CompanyListing.objects.get(pk=pk)
			if (instance.isAConsultant == True):
				messages.success(request, "Consultant profile has been updated!")
				return redirect(reverse('consultant-detail', kwargs={'pk': camp.pk}))
			messages.success(request, "Your Company has been updated!")
			return redirect(reverse('company-detail', kwargs={'pk': camp.pk}))
	else:
		c_form = CompanyUpdateForm(instance = CompanyListing.objects.get(pk=pk))
	return render(request, 'companies/companyupdate_form.html', {'c_form': c_form})


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CompanyListing
	success_url = '/companies'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author

class ConsultantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CompanyListing
	template_name = 'companies/consultantlisting_confirm_delete.html'
	success_url = '/consultants'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author


class CompanyDetailView(DetailView):
	model = CompanyListing

class ConsultantDetailView(DetailView):
	model = CompanyListing
	template_name = 'companies/consultantlisting_detail.html'
