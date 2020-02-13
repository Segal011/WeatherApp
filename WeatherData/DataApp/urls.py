from django.urls import path, include
from rest_framework import routers

from . import views, admin
from .views import CityViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet, basename='Cities')
router.register(r'countries', CountryViewSet, basename='Countries')

urlpatterns = [
    path('', include(router.urls)),
    # path(r'cities/', CityViewSet.as_view({'get': 'list'})),
    # path(r'countries/', CountryViewSet.as_view({'get': 'list'})),
    path('city/<code>/<city>/', views.get_city_by_name, name='get_city'),

    # path(r'cities/get/', CityViewSet.as_view({'get': 'retrieve'})),
    # path('countries/get/', CountryViewSet.as_view({'get': 'retrieve'})),

]