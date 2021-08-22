""" Weather API URLs. """

from django.urls import path
from weatherAPI import views


urlpatterns = [
    path(
        route = 'weather', # /weather?city=$City&country=$Country&
        view = views.weather_detail,
    )
]