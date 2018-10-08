from django.urls import path
from . views import  ConsultantCreateView, UserConsultantPageView, ConsultantDetailView, ConsultantPageView, ConsultantDeleteView
from . import views as consultant_views

urlpatterns = [
    path('', ConsultantPageView.as_view(), name='consultants-home'),
    path('<int:pk>/', ConsultantDetailView.as_view(), name='consultant-detail'),
    path('consultant/<int:pk>/', ConsultantDetailView.as_view(), name='consultant-detail'),
    path('new/', consultant_views.consultantCreate, name='consultant-create'),
    path('<str:username>/consultants', UserConsultantPageView.as_view(), name='user-consultant'),
    path('<int:pk>/update/',consultant_views.consultantUpdateView, name='consultant-update'),
    path('<int:pk>/consultant/delete/', ConsultantDeleteView.as_view(), name='consultant-delete'),
]
