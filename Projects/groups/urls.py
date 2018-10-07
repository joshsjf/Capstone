from django.urls import path
from . views import  GroupCreateView, UserGroupPageView, GroupDetailView, GroupPageView, GroupDeleteView
from . import views as group_views

urlpatterns = [
    path('', GroupPageView.as_view(), name='group-home'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('new/', group_views.consultantCreate, name='group-create'),
    path('<str:username>/groups', UserGroupPageView.as_view(), name='user-group'),
    path('<int:pk>/update/',group_views.groupUpdateView, name='group-update'),
    path('<int:pk>/group/delete/', GroupDeleteView.as_view(), name='group-delete'),
]
