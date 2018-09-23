from sites.models import JobListing

class JobCreateForm(forms.ModelForm):

    class Meta:
    	model = JobListing
    	fields = ['category', 'title', 'location', 'payrate', 'referencenumber',
    			'summary', 'description', 'phonenumber', 'company', 'instructions']
