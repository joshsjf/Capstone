from django import forms
from .models import GroupListing

class GroupCreateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")

    class Meta:
        model = GroupListing
        fields = ['group_Name', 'image', 'location', 'description', 'terms_And_Conditions']

class GroupUpdateForm(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")
    class Meta:
        model = GroupListing
        fields = ['group_Name', 'image', 'location', 'description', 'terms_And_Conditions']
