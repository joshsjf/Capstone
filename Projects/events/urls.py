from django.urls import path
from . views import  EventPageView, EventDetailView, EventCreateView, EventDeleteView, UserEventPageView
from . import views as event_views

urlpatterns = [
    path('', EventPageView.as_view(), name='sites-events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail')
]
