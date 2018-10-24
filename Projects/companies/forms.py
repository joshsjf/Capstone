from django import forms
from .models import CompanyListing

class CompanyCreateView(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyCreateView, self).__init__(*args, **kwargs)
        self.fields['lat'].required = False
        self.fields['lon'].required = False


    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    takes_On_Summer_Students = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Do you take on Summer Students?",
                                  initial=False, widget=forms.Select(), required=True)
    class Meta:
        model = CompanyListing
        fields = ['company_Name', 'lat', 'lon', 'image', 'contact_Name', 'email', 'phone_Number', 'website', 'number_Of_Employees',
    				'industry', 'specialist_Area', 'description', 'takes_On_Summer_Students', 'terms_And_Conditions']

# 'type_Of_Business'

class CompanyUpdateForm(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    takes_On_Summer_Students = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Do you take on Summer Students?",
                                  initial='', widget=forms.Select(), required=True)
    class Meta:
        model = CompanyListing
        fields = ['company_Name', 'lat', 'lon', 'image', 'contact_Name', 'email', 'phone_Number', 'website', 'number_Of_Employees',
    				'industry', 'specialist_Area', 'description', 'takes_On_Summer_Students', 'terms_And_Conditions']

# 'type_Of_Business'
