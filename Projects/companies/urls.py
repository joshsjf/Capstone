from django.urls import path
from . views import   CompanyPageView, CompanyDetailView, CompanyCreateView, CompanyDeleteView, UserCompanyPageView, CompanyMapView
from . import views as company_views

urlpatterns = [
    path('', CompanyPageView.as_view(), name='companies-home'),
    path('map/', CompanyMapView.as_view(), name='companies-map'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('new/', company_views.companyCreate, name='company-create'),
    path('<str:username>/companies', UserCompanyPageView.as_view(), name='user-company'),
    path('<int:pk>/update/', company_views.companyUpdateView, name='company-update'),
    path('<int:pk>/company/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
