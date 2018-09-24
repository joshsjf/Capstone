from django.urls import path
from . views import CompanyPageView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView, UserCompanyPageView
from . import views

urlpatterns = [
    path('companies/', CompanyPageView.as_view(), name='sites-company'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/new/', CompanyCreateView.as_view(), name='company-create'),
    path('user/<str:username>/company', UserCompanyPageView.as_view(), name='user-company'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
