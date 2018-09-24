#sites/urls.py

from django.urls import path
from sites import views
from .views import (PostPageView, UserPostPageView,
                    PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView)

urlpatterns = [
    path('', PostPageView.as_view(), name='sites-home'),

    path('user/<str:username>/posts', UserPostPageView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('AboutUs/', views.AboutPageView.as_view(), name='sites-aboutus'),
    path('Consultants/', views.ConsultantsPageView.as_view(), name='sites-consultants'),
    path('Companies/', views.CompaniesPageView.as_view(), name='sites-companies'),
    path('Education/', views.EducationPageView.as_view(), name='sites-education'),
    path('Events/', views.EventsPageView.as_view(), name='sites-events'),
    path('Groups/', views.GroupsPageView.as_view(), name='sites-groups'),

]
