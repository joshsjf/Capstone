from django import forms
from .models import ConsultantListing

class ConsultantCreateView(forms.ModelForm):
    tscs = forms.BooleanField(required=True)

    class Meta:
        model = ConsultantListing
        fields = ['groupName', 'image', 'description', 'term']

class ConsultantUpdateForm(forms.ModelForm):
    pk = ''
    id = ''
    class Meta:
        model = ConsultantListing
        fields = ['groupName', 'image', 'description', 'tscs']
