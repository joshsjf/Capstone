#sites/urls.py

from django.urls import path
from sites import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('AboutUs/', views.AboutPageView.as_view(), name='aboutus'),
    path('Consultants/', views.ConsultantsPageView.as_view(), name='consultants'),
    path('Companies/', views.CompaniesPageView.as_view(), name='companies'),
    path('Education/', views.EducationPageView.as_view(), name='education'),
    path('Events/', views.EventsPageView.as_view(), name='events'),
    path('Groups/', views.GroupsPageView.as_view(), name='groups'),
    path('Jobs/', views.JobsPageView.as_view(), name='jobs'),
]
