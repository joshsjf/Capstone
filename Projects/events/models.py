from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class EventListing(models.Model):
    def __str__(self):
        return self.title
