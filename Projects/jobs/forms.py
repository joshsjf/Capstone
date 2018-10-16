from django import forms
from django.shortcuts import render, reverse, redirect
from jobs.models import JobListing
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe


class JobCreateForm(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True, label = "<a href='/termsandconditions' target='_blank'>Terms and Conditions</a>")

    class Meta:
        model = JobListing
        fields = ['category', 'title', 'location', 'pay_Rate', 'reference_Number',
    			'summary', 'description', 'phone_Number', 'company', 'instructions', 'terms_And_Conditions']

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
