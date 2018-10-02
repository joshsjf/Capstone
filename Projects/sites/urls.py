#sites/urls.py

from django.urls import path
from sites import views
from jobs.views import JobPageView

urlpatterns = [
    path('', JobPageView.as_view(), name='sites-home'),
    path('AboutUs/', views.AboutPageView.as_view(), name='sites-aboutus'),
    path('Education/', views.EducationPageView.as_view(), name='sites-education'),
    path('Events/', views.EventsPageView.as_view(), name='sites-events'),
    path('Groups/', views.GroupsPageView.as_view(), name='sites-groups'),
]
