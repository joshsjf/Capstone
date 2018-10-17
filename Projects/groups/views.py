from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GroupListing
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from groups.forms import GroupCreateView, GroupUpdateForm
from django.urls import reverse


def groupCreate(request, **kwargs):
	if request.method == 'POST':
		form = GroupCreateView(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			comp = form.save()
			messages.success(request, "Group profile has been created!")
			return redirect(reverse('group-detail', kwargs={'pk': comp.pk}))
	else:
		form = GroupCreateView()
	return render(request, 'groups/grouplisting_form.html', {'form': form})


def groupUpdateView(request, pk):
	instance = get_object_or_404(GroupListing, id=pk)
	form = GroupUpdateForm(request.POST or None, request.FILES, instance=instance)
	if form.is_valid():
		form.save()
		return redirect(reverse('group-detail', kwargs={'pk': pk}))
	else:
		g_form = GroupUpdateForm(instance = GroupListing.objects.get(pk=pk))
	return render(request, 'groups/groupupdate_form.html', {'g_form': g_form})


class GroupPageView(ListView):
	model = GroupListing
	template_name = 'groups/group.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class UserGroupPageView(ListView):
	model = GroupListing
	template_name = 'groups/user_groups.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return GroupListing.objects.filter(author=user).order_by('-date_posted')


class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = GroupListing
	template_name = 'groups/grouplisting_confirm_delete.html'
	success_url = '/groups'
	def test_func(self):
		company = self.get_object()
		return self.request.user == company.author



class GroupDetailView(DetailView):
	model = GroupListing
	template_name = 'groups/grouplisting_detail.html'
