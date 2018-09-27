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
    date_posted = models.DateTimeField(default = timezone.now)
    #Get user company, name, ph
    category = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)

    payrate = models.IntegerField()
    referencenumber = models.CharField(max_length = 20)

    summary = models.TextField()
    description = models.TextField()

    phonenumber = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)

    instructions = models.CharField(max_length = 20)
