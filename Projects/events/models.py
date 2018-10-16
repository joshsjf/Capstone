from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

class EventListing(models.Model):
    def __str__(self):
        return self.event_Name


    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length = 30)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    event_Name = models.CharField(max_length = 50)
    event_Time_dd_mm_yyyy = models.CharField(max_length = 20)
    event_Location = models.CharField(max_length = 50)
    registration_Cost = models.IntegerField()
    event_Website = models.CharField(max_length = 200)
    event_Description = models.TextField()
    is_Expired = models.BooleanField(default=False)
    terms_And_Conditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
