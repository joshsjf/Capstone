from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class EventListing(models.Model):
    def __str__(self):
        return self.title


    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    eventWhen = models.CharField(max_length = 20)
    eventWhere = models.CharField(max_length = 20)

    registrationCost = models.IntegerField()
    eventWebsite = models.CharField(max_length = 200)

    eventDescription = models.TextField()

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
