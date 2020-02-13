from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'weather', views.WeatherViewSet, basename='Weather')

urlpatterns = [
    path('weather/', views.get_weather, name='weather'),
    path('city/<city>/', views.find_city, name='find city'),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]