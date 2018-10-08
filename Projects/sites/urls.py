#sites/urls.py

from django.urls import path
from sites import views

urlpatterns = [
    path('', views.home, name='sites-home'),
    path('search/', views.search, name='search'),
    path('AboutUs/', views.AboutPageView.as_view(), name='sites-about'),
    path('Contact/', views.ContactPageView.as_view(), name='sites-contact'),
]
