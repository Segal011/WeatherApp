from .models import Weather
from rest_framework import serializers


class WeatherSerializer():
    class Meta:
        fields = ['city', 'temperature', 'description', 'icon']

