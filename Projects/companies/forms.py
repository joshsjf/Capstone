from django import forms
from .models import CompanyListing

class CompanyCreateView(forms.ModelForm):
    tscs = forms.BooleanField(required=True)

    class Meta:
        model = CompanyListing
        fields = ['companyName', 'isAConsultant', 'image', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
    				'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']

class CompanyUpdateForm(forms.ModelForm):
    pk = ''
    id = ''
    class Meta:
        model = CompanyListing
        fields = ['companyName', 'isAConsultant', 'image', 'contactName', 'email', 'phoneNumber', 'website', 'numEmployees',
    				'industry', 'specialistArea', 'typeOfBusiness', 'receive_newsletter', 'description', 'tscs']
