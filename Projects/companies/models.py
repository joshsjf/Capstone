from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class CompanyListing(models.Model):
    def __str__(self):
        return self.companyName

    #All the fields Companies will have
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    image = models.ImageField(default='default.jpg', upload_to='company_pics')
    
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

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
