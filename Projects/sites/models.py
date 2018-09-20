from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    Companiescol = models.CharField(max_length=45)

class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #auto_now = True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class JobListing(models.Model):
#     def __str__(self):
#         return self.title
#
#     #All the fields Jobs will have
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #Get user company, name, ph
#     category = models.CharField(max_length = 20)
#     title = models.CharField(max_length = 20)
#     location = models.CharField(max_length = 20)
#
#     payrate = models.IntegerField()
#     referencenumber = models.CharField(max_length = 20)
#
#     summary = models.TextField()
#     description = models.TextField()
#
#     contactname = models.ForeignKey(User, on_delete=models.CASCADE)
#     phonenumber = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     instructions = models.CharField(max_length = 20)
