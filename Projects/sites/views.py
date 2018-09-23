from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from sites.models import Companies, Post, JobListing
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

class PostPageView(ListView):
	model = Post
	template_name = 'sites/index.html'
	context_object_name = 'data'
	ordering = ['-date_posted']
	paginate_by = 3

class UserPostPageView(ListView):
	model = Post
	template_name = 'sites/user_posts.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author		# do we need a conditional true/false here??


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author		# do we need a conditional true/false here??


class JobCreateView(LoginRequiredMixin, CreateView):
	model = JobListing
	fields = ['category', 'title', 'location', 'payrate', 'referencenumber',
			'summary', 'description', 'phonenumber', 'company', 'instructions']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class JobPageView(ListView):
	model = JobListing
	template_name = 'sites/jobs.html'
	context_object_name = 'data'
	ordering = ['-date_posted']

class UserJobPageView(ListView):
	model = JobListing
	template_name = 'sites/user_jobs.html'
	context_object_name = 'data'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return JobListing.objects.filter(author=user).order_by('-date_posted')

class JobDetailView(DetailView):
	model = JobListing

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
