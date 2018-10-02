from django.urls import path
from . views import  CompanyPageView, CompanyDetailView, CompanyCreateView, CompanyDeleteView, UserCompanyPageView, ConsultantDetailView, ConsultantPageView, ConsultantDeleteView
from . import views as company_views

urlpatterns = [
    path('', CompanyPageView.as_view(), name='companies-home'),
    path('consultants/', ConsultantPageView.as_view(), name='consultants-home'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('consultant/<int:pk>/', ConsultantDetailView.as_view(), name='consultant-detail'),
    path('new/', company_views.companyCreate, name='company-create'),
    path('<str:username>/companies', UserCompanyPageView.as_view(), name='user-company'),
    path('<int:pk>/update/',company_views.companyUpdateView, name='company-update'),
    path('<int:pk>/company/delete/', CompanyDeleteView.as_view(), name='company-delete'),
    path('<int:pk>/consultant/delete/', ConsultantDeleteView.as_view(), name='consultant-delete'),
]
