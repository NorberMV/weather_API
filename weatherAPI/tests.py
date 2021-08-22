""" Weather API ."""

# Django rest framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from . requestapi import get_weather



# Create your tests here.

# Live test
class WeatherAPITest(APITestCase):
    """ Run test over the weather API to check
        the status."""
    def test_api_url(self):
        
        url = 'http://localhost:8000/weather?city=Bogota&country=co&'  #
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
        
        


class FuncThirdAPITest(APITestCase):
    """ Run test over the test_get_weather() function
        from the requestapi.py module."""

    def test_get_weather(self):
        # Testing variables
        city = 'Medellin'
        country = 'co'

        weather_data = get_weather(city, country)         # Call to the function
        
        self.assertEqual(weather_data['location_name'], 'Medellín, CO') 


