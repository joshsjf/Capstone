from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class JobListing(models.Model):
    def __str__(self):
        return self.title

    #All the fields Jobs will have
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    pay_Rate = models.IntegerField()
    reference_Number = models.CharField(max_length = 200)
    summary = models.TextField()
    description = models.TextField()
    phone_Number = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    instructions = models.CharField(max_length = 500)
    is_Expired = models.BooleanField(default=False)
    terms_And_Conditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
