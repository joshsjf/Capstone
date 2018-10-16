from django import forms
from .models import CompanyListing

class CompanyCreateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True)

    class Meta:
        model = CompanyListing
        fields = ['company_Name', 'image', 'contact_Name', 'email', 'phone_Number', 'website', 'number_Of_Employees',
    				'industry', 'specialist_Area', 'type_Of_Business', 'receive_newsletter', 'description', 'terms_And_Conditions']

class CompanyUpdateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True)

    class Meta:
        model = CompanyListing
        fields = ['company_Name', 'image', 'contact_Name', 'email', 'phone_Number', 'website', 'number_Of_Employees',
    				'industry', 'specialist_Area', 'type_Of_Business', 'receive_newsletter', 'description', 'terms_And_Conditions']
