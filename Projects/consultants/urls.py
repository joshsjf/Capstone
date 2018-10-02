from django.urls import path
from . views import  ConsultantCreateView, UserConsultantPageView, ConsultantDetailView, ConsultantPageView, ConsultantDeleteView
from . import views as consultant_views

urlpatterns = [
    path('', ConsultantPageView.as_view(), name='cons-home'),
    path('<int:pk>/', ConsultantDetailView.as_view(), name='cons-detail'),
    path('consultant/<int:pk>/', ConsultantDetailView.as_view(), name='cons-detail'),
    path('new/', consultant_views.consultantCreate, name='cons-create'),
    path('<str:username>/consultants', UserConsultantPageView.as_view(), name='user-cons'),
    path('<int:pk>/update/',consultant_views.consultantUpdateView, name='cons-update'),
    path('<int:pk>/consultant/delete/', ConsultantDeleteView.as_view(), name='cons-delete'),
]
