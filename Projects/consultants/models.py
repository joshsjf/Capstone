from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class ConsultantListing(models.Model):
    def __str__(self):
        return self.consultantName

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    image = models.ImageField(default='default.jpg', upload_to='consultant_pics')

    consultantName = models.CharField(max_length = 20)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 20)
    website = models.CharField(max_length = 20)
    industry = models.CharField(max_length = 20)
    specialistArea = models.CharField(max_length = 20)

    receive_newsletter = models.BooleanField()
    description = models.TextField()
    tscs = models.BooleanField()

    def get_absolute_url(self):
        return reverse('cons-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
