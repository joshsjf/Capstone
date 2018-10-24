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
    company_Name = models.CharField(max_length = 200)
    contact_Name = models.CharField(max_length = 100)
    email = models.EmailField()
    takes_On_Summer_Students = models.BooleanField()
    phone_Number = models.CharField(max_length = 20)
    website = models.CharField(max_length = 100)
    number_Of_Employees = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
    industry = models.CharField(max_length = 50)
    specialist_Area = models.CharField(max_length = 50)
    # type_Of_Business = models.CharField(max_length = 50)
    description = models.TextField()
    is_Expired = models.BooleanField(default=False)
    terms_And_Conditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
