from django.urls import path
from django.conf.urls import url
from .import views as newsletter_views

urlpatterns = [
    path('sign-up/', newsletter_views.newsletter_signup, name='signup'),
    path('unsubscribe/', newsletter_views.newsletter_unsubscribe, name='unsubscribe'),
]
