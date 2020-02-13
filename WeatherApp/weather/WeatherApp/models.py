from datetime import datetime
from django.db import models


class Weather:

    class Meta:
        fields = ['city', 'temperature', 'description', 'icon']

    def __init__(self):
        self.city: str
        self.description: str
        self.icon: str
        self.icon: float


