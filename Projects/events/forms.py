from django import forms
from events.models import EventListing


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['author', 'date_posted', 'eventName', 'eventWhen', 'eventLocation', 'eventDescription', 'registrationCost', 'eventWebsite']
