from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    Companiescol = models.CharField(max_length=45)

class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 100)
    content = models.TextField()
    dated_posted = models.DateTimeField(default = timezone.now) #auto_now = True
    author = models.ForeignKey(User, on_delete=models.CASCADE)
