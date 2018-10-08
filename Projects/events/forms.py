from django import forms
from events.models import EventListing


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['author', 'date_posted', 'event_Name', 'event_When', 'event_Location', 'event_Description', 'registration_Cost', 'event_Website']
