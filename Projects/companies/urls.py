from django.urls import path
from . views import  CompanyPageView, CompanyDetailView, CompanyCreateView, CompanyDeleteView, UserCompanyPageView
from . import views as company_views

urlpatterns = [
    path('', CompanyPageView.as_view(), name='sites-companies'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('new/', company_views.companyCreate, name='company-create'),
    path('<str:username>/companies', UserCompanyPageView.as_view(), name='user-company'),
    path('<int:pk>/update/',company_views.CompanyUpdateView, name='company-update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
