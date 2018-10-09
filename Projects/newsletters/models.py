from django.db import models

class NewsletterUser(models.Model):
    def __str__(self):
        return self.email

    email= models.EmailField()
    date_Added = models.DateTimeField(auto_now_add=True)
