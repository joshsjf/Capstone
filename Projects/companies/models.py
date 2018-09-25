from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class CompanyListing(models.Model):
    def __str__(self):
        return self.title

    #All the fields Jobs will have
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    #Get user company, name, ph
    companyName = models.CharField(max_length = 20)
    contactName = models.CharField(max_length = 20)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 20)
    website = models.CharField(max_length = 20)
    numEmployees = models.IntegerField()

    industry = models.CharField(max_length = 20)
    specialistArea = models.CharField(max_length = 20)
    typeOfBusiness = models.CharField(max_length = 20)

    receive_newsletter = models.BooleanField()
    description = models.TextField()
    tscs = models.BooleanField()

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})
