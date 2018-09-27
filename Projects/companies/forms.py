from django import forms
from .models import CompanyListing

class CompanyCreateView(forms.ModelForm):
    tscs = forms.BooleanField(required=True)

    class Meta:
        model = CompanyListing
        fields = ['companyName', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
    				'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']
