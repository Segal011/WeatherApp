import json

from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import logging
from rest_framework import viewsets

from .models import Weather
from .serializers import WeatherSerializer

logging.basicConfig(level=logging.INFO)

key: str = '&APPID=b17c3faacc3f8b8a0772acc097443e6f'
weather_url: str = 'http://api.openweathermap.org/data/2.5/weather?q='


def get_city_weather(city: str):
    return  requests.get(weather_url + city + key).json()


def get_city_info(city: str):
    try:
        city_weather = get_city_weather(city)
        weather = {
            'city': city + ', ' + city_weather['sys']['country'],
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        return weather
    except KeyError as e:
        logging.warning(e)
        return None


def get_cities(cities):
    weather_data = []
    for city in cities:
        weather = get_city_info(city['name'])
        if weather is not None:
            weather_data.append(weather)
    # weather_data = json.dumps(weather_data)
    return weather_data


@csrf_exempt
def get_weather(request, *callback_args, **callback_kwargs):
    cities = requests.get('http://127.0.0.1:8001/cities/').json()
    return JsonResponse(get_cities(cities), safe=False)


@csrf_exempt
def find_city(request, *callback_args, **callback_kwargs):
    try:
        city_info = get_city_weather(callback_kwargs.get('city'))

        url = "http://localhost:8001/city/" + city_info['sys']['country'] + '/' + callback_kwargs.get('city') + '/'
        payload = {'code': city_info['sys']['country'],
                   'city': callback_kwargs.get('city')}
        city = requests.get(url, data=payload).json()
        weather = get_city_info(city['name'])
        return JsonResponse(weather)

    except KeyError as e:
        logging.warning(e)
        return JsonResponse({})
