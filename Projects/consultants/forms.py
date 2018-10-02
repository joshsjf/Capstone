from django import forms
from .models import ConsultantListing

class ConsultantCreateView(forms.ModelForm):
    tscs = forms.BooleanField(required=True)

    class Meta:
        model = ConsultantListing
        fields = ['consultantName', 'image', 'email', 'phoneNumber', 'website',
    				'industry', 'specialistArea', 'receive_newsletter', 'description', 'tscs']

class ConsultantUpdateForm(forms.ModelForm):
    pk = ''
    id = ''
    class Meta:
        model = ConsultantListing
        fields = ['consultantName', 'image', 'email', 'phoneNumber', 'website',
    				'industry', 'specialistArea', 'receive_newsletter', 'description', 'tscs']
