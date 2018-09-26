from django import forms
from django.contrib.auth.models import Companies
from django.contrib.auth.forms import UserCreationForm

class MyForm(forms.Form):
    check = forms.BooleanField(required = True)
