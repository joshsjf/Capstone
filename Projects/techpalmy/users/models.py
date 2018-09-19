from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    def __str__(self):
        return "{} Profile".format(self.user.username)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
