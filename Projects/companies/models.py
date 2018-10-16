from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class CompanyListing(models.Model):
    def __str__(self):
        return self.company_Name

    #All the fields Companies will have
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', upload_to='company_pics')
    company_Name = models.CharField(max_length = 20)
    contact_Name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone_Number = models.CharField(max_length = 20)
    website = models.CharField(max_length = 35)
    number_Of_Employees = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
    industry = models.CharField(max_length = 20)
    specialist_Area = models.CharField(max_length = 20)
    type_Of_Business = models.CharField(max_length = 20)
    receive_newsletter = models.BooleanField()
    description = models.TextField()
    is_Expired = models.BooleanField(default=False)
    terms_And_Conditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
