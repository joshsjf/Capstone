from django.urls import path
from . views import  CompanyUpdateView, CompanyPageView, CompanyDetailView, CompanyCreateView, CompanyDeleteView, UserCompanyPageView
from . import views as company_views

urlpatterns = [
    path('', CompanyPageView.as_view(), name='companies-home'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('new/', company_views.companyCreate, name='company-create'),
    path('<str:username>/companies', UserCompanyPageView.as_view(), name='user-company'),
    path('<int:pk>/update/',CompanyUpdateView.as_view(), name='company-update'),
    path('<int:pk>/company/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
