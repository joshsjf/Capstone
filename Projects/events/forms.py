from django import forms
from events.models import EventListing

class EventCreateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True)
    class Meta:
        model = EventListing
        fields = ['event_Name', 'event_Time_dd_mm_yyyy', 'event_Location', 'event_Description', 'registration_Cost', 'event_Website']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = EventListing
        fields = ['event_Name', 'event_Time_dd_mm_yyyy', 'event_Location', 'event_Description', 'registration_Cost', 'event_Website']

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = EventListing
        fields = ['event_Name', 'event_Time_dd_mm_yyyy', 'event_Location', 'event_Description', 'registration_Cost', 'event_Website']
