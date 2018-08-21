#sites/urls.py

from django.urls import path
from sites import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('AboutUs/', views.AboutPageView.as_view()),
    path('Consultants/', views.ConsultantsPageView.as_view()),
    path('Companies/', views.CompaniesPageView.as_view()),
    path('Education/', views.EducationPageView.as_view()),
    path('Events/', views.EventsPageView.as_view()),
    path('Groups/', views.GroupsPageView.as_view()),
    path('Jobs/', views.JobsPageView.as_view()),
]