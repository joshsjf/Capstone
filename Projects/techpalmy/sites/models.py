from django.db import models

class Companies(models.Model):
    # idCompanies = models.IntegerField(max_length=11)
    Companiescol = models.CharField(max_length=45)

# Create your models here.
