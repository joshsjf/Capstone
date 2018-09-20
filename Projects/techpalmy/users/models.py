from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator

class Profile(models.Model):
    def __str__(self):
        return "{} Profile".format(self.user.username)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    company = models.CharField(max_length=20, default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, default="") # validators should be a list


    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
