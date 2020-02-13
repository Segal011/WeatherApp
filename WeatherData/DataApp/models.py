from datetime import datetime
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25, default=None, blank=True, null=True, unique=True)
    search_time = models.DateTimeField(default=datetime.now, blank=True)
    code = models.CharField(max_length=2, unique=True)


class City(models.Model):
    name = models.CharField(max_length=25, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    search_time = models.DateTimeField(default=datetime.now, blank=True)


class City2(models.Model):
    name = models.CharField(max_length=25, unique=True)



