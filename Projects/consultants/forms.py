from django import forms
from .models import ConsultantListing

class ConsultantCreateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")

    class Meta:
        model = ConsultantListing
        fields = ['consultant_Name', 'image', 'email', 'phone_Number', 'website',
    				'industry', 'specialist_Area', 'receive_Newsletter', 'description', 'terms_And_Conditions']

class ConsultantUpdateForm(forms.ModelForm):
    class Meta:
        model = ConsultantListing
        fields = ['consultant_Name', 'image', 'email', 'phone_Number', 'website',
    				'industry', 'specialist_Area', 'receive_Newsletter', 'description', 'terms_And_Conditions']
