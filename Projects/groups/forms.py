from django import forms
from .models import ConsultantListing

class GroupCreateView(forms.ModelForm):
    termsAndConditions = forms.BooleanField(required=True)

    class Meta:
        model = GroupListing
        fields = ['groupName', 'image', 'description', 'termsAndConditions']

class GroupUpdateForm(forms.ModelForm):
    pk = ''
    id = ''
    class Meta:
        model = GroupListing
        fields = ['groupName', 'image', 'description', 'termsAndConditions']
