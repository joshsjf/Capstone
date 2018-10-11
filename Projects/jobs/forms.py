from django import forms
from jobs.models import JobListing


class JobCreateForm(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True)
    class Meta:
        model = JobListing
        fields = ['category', 'title', 'location', 'pay_Rate', 'reference_Number',
    			'summary', 'description', 'phone_Number', 'company', 'instructions', 'terms_And_Conditions']

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
