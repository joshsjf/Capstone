from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class ConsultantListing(models.Model):
    def __str__(self):
        return self.consultant_Name

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', upload_to='consultant_pics')
    consultant_Name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_Number = models.CharField(max_length = 200)
    website = models.CharField(max_length = 200)
    industry = models.CharField(max_length = 200)
    specialist_Area = models.CharField(max_length = 200)
    description = models.TextField()
    is_Expired = models.BooleanField(default=False)
    terms_And_Conditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('consultant-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
