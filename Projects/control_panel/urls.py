from django.urls import path

from newsletters.views import control_newsletter, control_newsletter_list, control_newsletter_detail, control_newsletter_edit, control_newsletter_delete

urlpatterns = [
    path('newsletter/', control_newsletter, name='control_newsletter'),
    path('newsletter-list/', control_newsletter_list, name='control_newsletter_list'),
    path('newsletter-detail/<int:pk>/', control_newsletter_detail, name='control_newsletter_detail'),
    path('newsletter-edit/<int:pk>/', control_newsletter_edit, name='control_newsletter_edit'),
    path('newsletter-delete/<int:pk>/', control_newsletter_delete, name='control_newsletter_delete'),
]
