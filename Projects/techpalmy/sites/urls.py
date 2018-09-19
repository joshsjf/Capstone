#sites/urls.py

from django.urls import path
from sites import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='sites-home'),
    path('AboutUs/', views.AboutPageView.as_view(), name='sites-aboutus'),
    path('Consultants/', views.ConsultantsPageView.as_view(), name='sites-consultants'),
    path('Companies/', views.CompaniesPageView.as_view(), name='sites-companies'),
    path('Education/', views.EducationPageView.as_view(), name='sites-education'),
    path('Events/', views.EventsPageView.as_view(), name='sites-events'),
    path('Groups/', views.GroupsPageView.as_view(), name='sites-groups'),
    path('Jobs/', views.JobsPageView.as_view(), name='sites-jobs'),
]
