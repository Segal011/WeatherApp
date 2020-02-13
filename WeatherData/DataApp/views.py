import logging
from datetime import datetime

import requests
# from requests import Response
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from DataApp.models import City, Country
from DataApp.serializers import CitySerializer, CountrySerializer

logging.basicConfig(level=logging.DEBUG)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('-search_time')
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@csrf_exempt
def get_city_by_name(request, *callback_args, **callback_kwargs):

    country, instance_country = Country.objects.get_or_create(code=callback_kwargs.get('code'))
    city, instance_city = City.objects.get_or_create(name=callback_kwargs.get('city'), country=country)

    if not instance_city:
        city.search_time = datetime.now()
        city.save()
        logging.debug('updated',)
    else:
        logging.debug('created')

    city = model_to_dict(city)
    return JsonResponse(city)



