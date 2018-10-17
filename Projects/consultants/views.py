from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ConsultantListing
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from consultants.forms import ConsultantCreateView, ConsultantUpdateForm
from django.urls import reverse


def consultantCreate(request, **kwargs):
	if request.method == 'POST':
		form = ConsultantCreateView(request.POST, request.FILES,)
		if form.is_valid():
			form.instance.author = request.user
			comp = form.save()
			messages.success(request, "Consultant profile has been created!")
			return redirect(reverse('consultant-detail', kwargs={'pk': comp.pk}))
	else:
		form = ConsultantCreateView()
	return render(request, 'consultants/consultantlisting_form.html', {'form': form})


def consultantUpdateView(request, pk):
	instance = get_object_or_404(ConsultantListing, id=pk)
	form = ConsultantUpdateForm(request.POST or None, request.FILES, instance=instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Consultant profile has been updated!")
		return redirect(reverse('consultant-detail', kwargs={'pk': pk}))
	else:
		c_form = ConsultantUpdateForm(instance = ConsultantListing.objects.get(pk=pk))
	return render(request, 'consultants/consultantupdate_form.html', {'c_form': c_form})


class ConsultantPageView(ListView):
	model = ConsultantListing
	template_name = 'consultants/consultant.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class UserConsultantPageView(ListView):
	model = ConsultantListing
	template_name = 'consultants/user_consultant.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return ConsultantListing.objects.filter(author=user).order_by('-date_posted')


class ConsultantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = ConsultantListing
	template_name = 'consultants/consultantlisting_confirm_delete.html'
	success_url = '/consultants'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author



class ConsultantDetailView(DetailView):
	model = ConsultantListing
	template_name = 'consultants/consultantlisting_detail.html'
