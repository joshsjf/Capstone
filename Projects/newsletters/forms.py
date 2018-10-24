from django import forms
from .models import NewsletterUser, Newsletter


class NewsletterUserSignUpForm(forms.ModelForm):

    class Meta:
        model = NewsletterUser
        ordering = ['-id']
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get()
            return email

class NewsletterCreationForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        ordering = ['-id']
        fields = ['subject', 'email', 'status']
