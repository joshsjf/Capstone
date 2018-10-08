from django.urls import path
from . views import  EventPageView, EventDetailView, EventDeleteView, UserEventPageView
from . import views as event_views

urlpatterns = [
    path('', EventPageView.as_view(), name='sites-events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('new/', event_views.eventCreate, name='event-create'),
    path('<str:username>/events', UserEventPageView.as_view(), name='user-event'),
    path('<int:pk>/update/',event_views.eventUpdateView, name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete')
]
