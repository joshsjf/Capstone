from django import forms
from jobs.models import JobListing


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['category', 'title', 'location', 'payrate', 'referencenumber',
    			'summary', 'description', 'phonenumber', 'company', 'instructions']

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})    
