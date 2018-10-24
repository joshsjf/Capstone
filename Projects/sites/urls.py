#sites/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='sites-home'),
    path('search/', views.search, name='search'),
    path('AboutUs/', views.AboutPageView.as_view(), name='sites-about'),
    path('ContactUs/', views.contactUs, name='sites-contact'),
    path('termsandconditions/', views.TermsAndCondition.as_view(), name='tc'),
]
