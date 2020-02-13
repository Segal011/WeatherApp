from .models import Country, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = ['id', 'name', 'search_time', 'country']


# class WeatherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Weather
#         fields = ['city', 'temperature', 'description', 'icon']


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name', 'search_time', 'code']
