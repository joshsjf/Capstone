from django.db import models


class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    Companiescol = models.CharField(max_length=45)
